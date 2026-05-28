#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lightweight repository validation for CI and local pre-push checks.
Does not require a running Odoo server or database.
"""
from __future__ import annotations

import ast
import re
import sys
from pathlib import Path

MODULE_ROOT = Path(__file__).resolve().parents[1]
SKIP_COMPILE_DIRS = {'.git', '__pycache__', '.venv', 'venv'}
SECRET_PATTERNS = [
    re.compile(r'api[_-]?key\s*=\s*["\'][^"\']{8,}["\']', re.I),
    re.compile(r'access_token\s*=\s*["\'][^"\']{8,}["\']', re.I),
    re.compile(r'BEGIN (RSA |OPENSSH )?PRIVATE KEY'),
]


def load_manifest() -> dict:
    manifest_path = MODULE_ROOT / '__manifest__.py'
    text = manifest_path.read_text(encoding='utf-8')
    match = re.search(r'\{', text, re.DOTALL)
    if not match:
        raise ValueError('Could not parse __manifest__.py')
    manifest = ast.literal_eval(text[match.start():])
    if not isinstance(manifest, dict):
        raise ValueError('Manifest is not a dict')
    return manifest


def validate_manifest(manifest: dict) -> list[str]:
    errors = []
    required = ('name', 'version', 'depends', 'data', 'installable', 'license')
    for key in required:
        if key not in manifest:
            errors.append('manifest missing key: %s' % key)
    version = manifest.get('version', '')
    if not re.match(r'^19\.0\.\d+\.\d+\.\d+$', version):
        errors.append('manifest version should match 19.0.x.y.z (got %r)' % version)
    if manifest.get('installable') is not True:
        errors.append('manifest installable must be True')
    for rel in manifest.get('data', []):
        if not (MODULE_ROOT / rel).is_file():
            errors.append('manifest data file missing: %s' % rel)
    return errors


def validate_changelog_version(manifest: dict) -> list[str]:
    errors = []
    changelog = (MODULE_ROOT / 'CHANGELOG.md').read_text(encoding='utf-8')
    version = manifest['version']
    if '[%s]' % version not in changelog:
        errors.append('CHANGELOG.md has no section for version %s' % version)
    return errors


def compile_python() -> list[str]:
    errors = []
    for path in MODULE_ROOT.rglob('*.py'):
        if any(part in SKIP_COMPILE_DIRS for part in path.parts):
            continue
        try:
            compile(path.read_text(encoding='utf-8'), str(path), 'exec')
        except SyntaxError as exc:
            errors.append('syntax error %s: %s' % (path.relative_to(MODULE_ROOT), exc))
    return errors


def scan_secrets() -> list[str]:
    warnings = []
    for path in MODULE_ROOT.rglob('*'):
        if not path.is_file() or path.suffix in ('.png', '.gif', '.jpg'):
            continue
        if '.git' in path.parts:
            continue
        try:
            content = path.read_text(encoding='utf-8', errors='ignore')
        except OSError:
            continue
        for pattern in SECRET_PATTERNS:
            if pattern.search(content):
                warnings.append('possible secret in %s' % path.relative_to(MODULE_ROOT))
    return warnings


def main() -> int:
    errors: list[str] = []
    print('Validating whatsapp_simple at', MODULE_ROOT)
    manifest = load_manifest()
    print('  version:', manifest.get('version'))
    errors.extend(validate_manifest(manifest))
    errors.extend(validate_changelog_version(manifest))
    errors.extend(compile_python())
    secret_hits = scan_secrets()
    if secret_hits:
        print('WARN: secret pattern scan:')
        for hit in secret_hits:
            print(' ', hit)
    if errors:
        print('FAILED:')
        for err in errors:
            print(' ', err)
        return 1
    print('OK: manifest, changelog, python syntax')
    return 0


if __name__ == '__main__':
    sys.exit(main())

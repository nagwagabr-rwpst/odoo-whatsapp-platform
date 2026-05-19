# -*- coding: utf-8 -*-
"""Registry verification for whatsapp.bulk.send.wizard (run via odoo-bin shell)."""
import inspect

from odoo.addons.whatsapp_simple.wizard.whatsapp_bulk_send_wizard import WhatsAppBulkSendWizard


def verify(env):
    model = env['whatsapp.bulk.send.wizard']
    print('model:', model)
    print('_name:', model._name)
    print('attachment_count in _fields:', 'attachment_count' in model._fields)
    print('multi_attachment_count in _fields:', 'multi_attachment_count' in model._fields)
    print('source file:', inspect.getfile(WhatsAppBulkSendWizard))
    print('class attachment_count attr:', getattr(WhatsAppBulkSendWizard, 'attachment_count', None))
    print('field keys:', sorted(model._fields.keys()))

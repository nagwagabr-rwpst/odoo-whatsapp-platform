# -*- coding: utf-8 -*-
"""
Module-level constants for whatsapp_simple.

Kept free of Odoo model/service imports so models can load without
pulling in the full provider stack at registry init time.
"""

PROVIDER_SELECTION_LABELS = [
    ('green_api', 'Green API'),
    ('mock_provider', 'Mock Provider (Test Mode)'),
    ('meta_cloud', 'Meta WhatsApp Cloud API'),
    ('evolution', 'Evolution API'),
    ('ultramsg', 'UltraMsg'),
    ('twilio', 'Twilio WhatsApp'),
    ('gupshup', 'Gupshup'),
    ('custom', 'Custom Internal API'),
]

PROVIDER_STATUS_SELECTION = [
    ('healthy', 'Healthy'),
    ('degraded', 'Degraded'),
    ('disconnected', 'Disconnected'),
]

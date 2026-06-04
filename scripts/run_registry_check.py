# -*- coding: utf-8 -*-
import inspect

from odoo.addons.relayruntime.wizard.whatsapp_bulk_send_wizard import WhatsAppBulkSendWizard

model = env['whatsapp.bulk.send.wizard']
print('model:', model)
print('_name:', model._name)
print('multi_attachment_count in _fields:', 'multi_attachment_count' in model._fields)
print('attachment_count in _fields:', 'attachment_count' in model._fields)
print('source:', inspect.getfile(WhatsAppBulkSendWizard))
print('class has multi_attachment_count:', hasattr(WhatsAppBulkSendWizard, 'multi_attachment_count'))
print('keys:', sorted(model._fields.keys()))

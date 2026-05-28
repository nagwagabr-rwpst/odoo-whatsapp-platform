# -*- coding: utf-8 -*-
# RelayRuntime — Odoo application layer (ERP integration + orchestration entrypoint).
# Runtime engine extraction target: repository /runtime/ (see docs/architecture/runtime-boundaries.md).

{

    'name': 'RelayRuntime',

    'version': '19.0.6.0.0',

    'category': 'Productivity',

    'summary': 'Replay-safe campaign execution runtime for Odoo',

    'description': """
RelayRuntime
============

RelayRuntime is a production-oriented WhatsApp campaign execution runtime for Odoo.

Features include:

* replay-safe recovery
* resilient batch execution
* lease-safe worker orchestration
* runtime observability
* retry lineage tracking
* attachment orchestration
* operational diagnostics

Designed as a platform-oriented runtime architecture initially delivered as an Odoo application.

Technical note: this addon was previously distributed as ``whatsapp_simple``.
See MIGRATION.md at the repository root for upgrade guidance.
    """,

    'author': 'RelayRuntime Contributors',
    'website': 'https://github.com/YOUR_ORG/relayruntime',
    'license': 'LGPL-3',

    'depends': [
        'base',
        'sale',
        'mail',
        'product',
    ],

    'data': [
        'security/whatsapp_security.xml',
        'security/ir.model.access.csv',
        'views/whatsapp_config_views.xml',
        'views/whatsapp_message_log_views.xml',
        'views/whatsapp_delivery_dashboard_views.xml',
        'views/whatsapp_bulk_campaign_views.xml',
        'views/whatsapp_campaign_monitor_views.xml',
        'views/whatsapp_menu.xml',
        'views/res_partner_views.xml',
        'views/sale_order_views.xml',
        'wizard/whatsapp_send_wizard_views.xml',
        'wizard/whatsapp_bulk_send_wizard_views.xml',
        'wizard/whatsapp_product_selection_wizard_views.xml',
    ],

    'assets': {
        'web.assets_backend': [
            'relayruntime/static/src/js/campaign_monitor_kanban.js',
        ],
    },

    'post_init_hook': 'post_init_hook',

    'installable': True,

    'application': True,

}

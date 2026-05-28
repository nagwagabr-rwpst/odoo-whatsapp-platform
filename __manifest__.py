# -*- coding: utf-8 -*-

{

    'name': 'WhatsApp Simple',

    'version': '19.0.5.5.0',

    'category': 'Marketing',

    'summary': 'Runtime-aware WhatsApp bulk campaigns with execution attempts for Odoo 19',

    'description': """
WhatsApp Simple — campaign execution for Odoo 19 Community
==========================================================

Outbound WhatsApp bulk and single sends with execution-attempt tracking,
lease/heartbeat runtime coordination, retry lineage, delivery logs, and
provider adapters (Green API and Mock Provider are send-capable).

See the module README.md and docs/ for architecture, limitations, and operations.
    """,

    'author': 'WhatsApp Simple Contributors',
    'website': 'https://github.com/YOUR_ORG/whatsapp_simple',
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

            'whatsapp_simple/static/src/js/campaign_monitor_kanban.js',

        ],

    },

    'post_init_hook': 'post_init_hook',

    'installable': True,

    'application': True,

}



# -*- coding: utf-8 -*-

{

    'name': 'WhatsApp Simple',

    'version': '19.0.5.4.2',

    'category': 'Marketing',

    'summary': 'Provider-agnostic WhatsApp sales workflow for Odoo 19 Community',

    'description': """

WhatsApp integration with interchangeable provider adapters (Green API, Meta Cloud,

Evolution, UltraMsg, Twilio, Gupshup, custom). Bulk sending, delivery tracking,

campaign monitor, and product workflows are provider-independent.

    """,

    'author': 'Custom',

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



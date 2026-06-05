# -*- coding: utf-8 -*-



{

    'name': 'RWPST RelayRuntime',

    'version': '19.0.5.4.277',

    'category': 'Marketing',

    'summary': 'Operational Messaging Runtime for Odoo',

    'description': """

RWPST RelayRuntime — operational messaging runtime for Odoo Community.



Provider-agnostic WhatsApp adapters (Green API, Meta Cloud, Evolution, UltraMsg, and more).



Includes an Enterprise-style app launcher (Command Center), bulk campaigns, delivery tracking,

live monitor, and product workflows.

    """,

    'author': 'Custom',

    'license': 'LGPL-3',

    'icon': '/relayruntime/static/description/icon.png',

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

        'views/whatsapp_app_dashboard_views.xml',

        'views/whatsapp_bulk_campaign_views.xml',

        'views/whatsapp_campaign_monitor_views.xml',

        'views/res_partner_views.xml',

        'views/sale_order_views.xml',

        'wizard/whatsapp_send_wizard_views.xml',

        'wizard/whatsapp_bulk_send_wizard_views.xml',

        'views/whatsapp_menu.xml',

        'wizard/whatsapp_product_selection_wizard_views.xml',

    ],

    'assets': {

        'web._assets_primary_variables': [
            ('before', 'web/static/src/scss/primary_variables.scss', 'relayruntime/static/src/scss/_rwpst_brand_tokens.scss'),
            ('before', 'web/static/src/scss/primary_variables.scss', 'relayruntime/static/src/scss/rwpst_brand_primary_variables.scss'),
            ('after', 'web/static/src/scss/primary_variables.scss', 'relayruntime/static/src/scss/rwpst_brand_derived_variables.scss'),
            ('after', 'web/static/src/webclient/burger_menu/burger_menu.variables.scss', 'relayruntime/static/src/scss/rwpst_brand_component_variables.scss'),
        ],

        'web.assets_backend': [

            'relayruntime/static/src/scss/_rwpst_brand_tokens.scss',

            'relayruntime/static/src/scss/rwpst_variables.scss',

            'relayruntime/static/src/scss/rwpst_mixins.scss',

            'relayruntime/static/src/scss/rwpst_theme.scss',

            'relayruntime/static/src/scss/rwpst_dashboard.scss',

            'relayruntime/static/src/scss/rwpst_tiles.scss',

            'relayruntime/static/src/scss/rwpst_global_brand.scss',

            'relayruntime/static/src/js/campaign_monitor_kanban.js',

        ],

        'web.assets_frontend': [
            'relayruntime/static/src/scss/_rwpst_brand_tokens.scss',
            'relayruntime/static/src/scss/rwpst_global_brand.scss',
        ],

    },

    'post_init_hook': 'post_init_hook',

    'installable': True,

    'application': True,

}


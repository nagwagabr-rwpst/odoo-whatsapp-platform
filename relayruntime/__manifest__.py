# -*- coding: utf-8 -*-
# RelayRuntime — Odoo application layer (ERP integration + orchestration entrypoint).
# Runtime engine extraction target: repository /runtime/ (see docs/architecture/runtime-boundaries.md).
# Reconstruction: Lineage B foundation + Lineage A enterprise UI (MERGE-003).

{

    'name': 'RelayRuntime – Enterprise WhatsApp Messaging for Odoo Community',

    'version': '19.0.6.1.0',

    'category': 'Marketing',

    'summary': (
        'Enterprise WhatsApp Messaging platform for Odoo Community with campaigns, '
        'bulk messaging, delivery tracking and multi-provider support.'
    ),

    'description': """
RelayRuntime – Enterprise WhatsApp Messaging for Odoo Community
===============================================================

RelayRuntime is an Enterprise WhatsApp Messaging platform for Odoo Community.
Run WhatsApp Messaging operations with Bulk Messaging, Campaign Management,
a Delivery Dashboard, Message Queue control, Retry for failed deliveries,
message Templates, Notifications, and Multi Provider support including
Meta Cloud API, Evolution API, and Green API.

Key capabilities:

* WhatsApp Bulk Messaging
* WhatsApp Campaign Management
* Scheduled Messages
* Delivery Dashboard and Delivery Tracking
* Retry Failed Messages
* Queue Management
* Multi WhatsApp Providers (Meta Cloud API, Evolution API, Green API)
* Message Templates and Notifications
* Campaign Analytics
* Enterprise Messaging Runtime for Odoo Community

Experience:

* Command Center (KPIs, alerts, workspaces)
* Enterprise navigation (Operations / Analytics / Configuration)
* Delivery Dashboard and Live Monitor
* RWPST branding

Note: this addon was previously distributed as ``whatsapp_simple``.
    """,

    'author': 'RelayRuntime Contributors',
    'website': 'https://relayruntime.rwpst.com',
    'license': 'LGPL-3',
    'price': 49.0,
    'currency': 'USD',
    'icon': '/relayruntime/static/description/icon.png',
    'images': [
        'static/description/banner_1.png',
        'static/description/AppIcon.png',
        'static/description/screenshots/01_command_center.png',
        'static/description/screenshots/02_settings.png',
        'static/description/screenshots/03_bulk_wizard.png',
        'static/description/screenshots/06_delivery_dashboard.png',
    ],

    'depends': [
        'base',
        'sale',
        'mail',
        'product',
    ],

    # Menus last: whatsapp_menu.xml owns all menuitem XML IDs (incl. menu_whatsapp_root)
    # and must load after every action/view file those menus reference.
    'data': [
        'security/whatsapp_security.xml',
        'security/ir.model.access.csv',
        'views/whatsapp_config_views.xml',
        'views/whatsapp_message_log_views.xml',
        'views/whatsapp_bulk_campaign_views.xml',
        'views/whatsapp_campaign_monitor_views.xml',
        'views/whatsapp_app_dashboard_views.xml',
        'views/whatsapp_delivery_dashboard_views.xml',
        'views/res_partner_views.xml',
        'views/sale_order_views.xml',
        'wizard/whatsapp_send_wizard_views.xml',
        'wizard/whatsapp_bulk_send_wizard_views.xml',
        'wizard/whatsapp_product_selection_wizard_views.xml',
        'views/whatsapp_menu.xml',
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

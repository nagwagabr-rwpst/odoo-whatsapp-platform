# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError

from odoo.addons.whatsapp_simple.services.logger import campaign_logger

CAMPAIGN_STATE_SELECTION = [
    ('draft', 'Draft'),
    ('running', 'Running'),
    ('completed', 'Completed'),
    ('completed_with_errors', 'Completed with Errors'),
    ('stopped', 'Stopped'),
    ('failed', 'Failed'),
]

# Legacy processing_state values mapped for backward-compatible views/code
_PROCESSING_STATE_MAP = {
    'draft': 'draft',
    'running': 'running',
    'completed': 'done',
    'completed_with_errors': 'done',
    'stopped': 'cancelled',
    'failed': 'cancelled',
}


class WhatsAppBulkCampaign(models.Model):
    _name = 'whatsapp.bulk.campaign'
    _description = 'WhatsApp Bulk Campaign'
    _order = 'create_date desc, id desc'

    name = fields.Char(string='Reference', required=True, index=True)
    message = fields.Text(string='Message')
    attachment_info = fields.Text(string='Attachments')
    attachment_ids = fields.Many2many(
        'ir.attachment',
        'whatsapp_campaign_attachment_rel',
        'campaign_id',
        'attachment_id',
        string='Free Attachments',
        readonly=True,
        bypass_search_access=True,
        help='User-uploaded files for this campaign (not product catalog images).',
    )
    attachment_count = fields.Integer(
        string='Attachment Count',
        compute='_compute_attachment_count',
        store=True,
    )
    product_ids = fields.Many2many(
        'product.template',
        'whatsapp_campaign_product_rel',
        'campaign_id',
        'product_id',
        string='Products',
        readonly=True,
    )
    partner_ids = fields.Many2many(
        'res.partner',
        'whatsapp_campaign_partner_rel',
        'campaign_id',
        'partner_id',
        string='Recipients',
        readonly=True,
    )
    use_product_images = fields.Boolean(string='Used Product Images', readonly=True)
    include_product_description = fields.Boolean(string='Included Descriptions', readonly=True)

    total_count = fields.Integer(string='Total Recipients', readonly=True)
    total_recipients = fields.Integer(string='Recipients', related='total_count', store=True)
    sent_count = fields.Integer(string='Sent', readonly=True)
    total_success = fields.Integer(string='Success', related='sent_count', store=True)
    failed_count = fields.Integer(string='Failed', readonly=True)
    total_failures = fields.Integer(string='Failures', related='failed_count', store=True)
    skipped_count = fields.Integer(string='Skipped', readonly=True)
    total_skipped = fields.Integer(string='Total Skipped', related='skipped_count', store=True)
    cooldown_count = fields.Integer(string='Cooldowns', readonly=True)
    total_attachments_sent = fields.Integer(string='Attachments Sent', readonly=True)
    total_attachments = fields.Integer(
        string='Total Attachments',
        related='total_attachments_sent',
        store=True,
    )

    success_rate = fields.Float(
        string='Success Rate %',
        compute='_compute_success_rate',
        store=True,
        digits=(16, 2),
    )

    started_at = fields.Datetime(string='Started At', readonly=True, index=True)
    finished_at = fields.Datetime(string='Finished At', readonly=True)
    execution_started_at = fields.Datetime(
        string='Execution Started',
        readonly=True,
        index=True,
        help='When the bulk sender started processing recipients.',
    )
    execution_finished_at = fields.Datetime(
        string='Execution Finished',
        readonly=True,
        help='When the bulk sender finished or was interrupted.',
    )
    duration_seconds = fields.Float(
        string='Duration (seconds)',
        compute='_compute_duration',
        store=True,
        digits=(16, 2),
    )
    running_duration_seconds = fields.Float(
        string='Running Duration (s)',
        compute='_compute_running_duration',
        digits=(16, 2),
    )

    progress_percent = fields.Float(string='Progress %', readonly=True, digits=(16, 2))
    progress_percentage = fields.Float(
        string='Progress',
        related='progress_percent',
        readonly=True,
    )
    processed_count = fields.Integer(string='Processed', readonly=True)
    remaining_count = fields.Integer(string='Remaining', readonly=True)
    current_step = fields.Char(string='Current Step', readonly=True)

    state = fields.Selection(
        selection=CAMPAIGN_STATE_SELECTION,
        string='State',
        default='draft',
        readonly=True,
        index=True,
    )
    processing_state = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('running', 'Running'),
            ('done', 'Done'),
            ('cancelled', 'Cancelled'),
        ],
        string='Processing State',
        compute='_compute_processing_state',
        store=True,
        readonly=True,
    )

    current_partner_id = fields.Many2one(
        'res.partner',
        string='Current Contact',
        readonly=True,
        help='Deprecated alias; use current_recipient_id.',
    )
    current_recipient_id = fields.Many2one(
        'res.partner',
        string='Current Recipient',
        readonly=True,
    )
    current_recipient_number = fields.Char(string='Current Number', readonly=True)
    current_product_id = fields.Many2one('product.template', string='Current Product', readonly=True)
    last_activity_at = fields.Datetime(string='Last Activity', readonly=True, index=True)

    parent_campaign_id = fields.Many2one(
        'whatsapp.bulk.campaign',
        string='Parent Campaign',
        readonly=True,
        ondelete='set null',
    )
    retry_campaign_ids = fields.One2many(
        'whatsapp.bulk.campaign',
        'parent_campaign_id',
        string='Retry Campaigns',
        readonly=True,
    )
    retry_count = fields.Integer(compute='_compute_retry_count')

    user_id = fields.Many2one(
        'res.users',
        string='Sent By',
        default=lambda self: self.env.user,
        readonly=True,
    )
    company_id = fields.Many2one(
        'res.company',
        string='Company',
        default=lambda self: self.env.company,
        readonly=True,
        index=True,
    )
    log_ids = fields.One2many(
        'whatsapp.message.log',
        'campaign_id',
        string='Message Logs',
        readonly=True,
    )
    sale_order_ids = fields.One2many(
        'sale.order',
        'whatsapp_campaign_id',
        string='Sales Orders',
        readonly=True,
    )
    sale_order_count = fields.Integer(compute='_compute_sale_order_count')

    @api.depends('attachment_ids')
    def _compute_attachment_count(self):
        for campaign in self:
            campaign.attachment_count = len(campaign.attachment_ids)

    @api.depends('sent_count', 'failed_count', 'skipped_count')
    def _compute_success_rate(self):
        for campaign in self:
            total = campaign.sent_count + campaign.failed_count + campaign.skipped_count
            campaign.success_rate = (campaign.sent_count / total * 100.0) if total else 0.0

    @api.depends('started_at', 'finished_at', 'execution_started_at', 'execution_finished_at')
    def _compute_duration(self):
        for campaign in self:
            start = campaign.execution_started_at or campaign.started_at
            end = campaign.execution_finished_at or campaign.finished_at
            if start and end:
                campaign.duration_seconds = (end - start).total_seconds()
            else:
                campaign.duration_seconds = 0.0

    @api.depends('state', 'execution_started_at', 'last_activity_at', 'execution_finished_at')
    def _compute_running_duration(self):
        now = fields.Datetime.now()
        for campaign in self:
            start = campaign.execution_started_at or campaign.started_at
            if not start:
                campaign.running_duration_seconds = 0.0
                continue
            if campaign.state == 'running':
                anchor = campaign.last_activity_at or now
                campaign.running_duration_seconds = (anchor - start).total_seconds()
            elif campaign.execution_finished_at:
                campaign.running_duration_seconds = (
                    campaign.execution_finished_at - start
                ).total_seconds()
            elif campaign.finished_at:
                campaign.running_duration_seconds = (campaign.finished_at - start).total_seconds()
            else:
                campaign.running_duration_seconds = 0.0

    @api.depends('state')
    def _compute_processing_state(self):
        for campaign in self:
            campaign.processing_state = _PROCESSING_STATE_MAP.get(campaign.state, 'draft')

    def _compute_sale_order_count(self):
        for campaign in self:
            campaign.sale_order_count = len(campaign.sale_order_ids)

    def _compute_retry_count(self):
        for campaign in self:
            campaign.retry_count = len(campaign.retry_campaign_ids)

    def action_open_logs(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': _('Message Logs'),
            'res_model': 'whatsapp.message.log',
            'view_mode': 'list,form,graph,pivot',
            'domain': [('campaign_id', '=', self.id)],
        }

    def action_open_sale_orders(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': _('Sales Orders'),
            'res_model': 'sale.order',
            'view_mode': 'list,form',
            'domain': [('whatsapp_campaign_id', '=', self.id)],
        }

    def action_create_product_selection(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': _('Create Sale Order from Selection'),
            'res_model': 'whatsapp.product.selection.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_campaign_id': self.id,
                'default_product_ids': [(6, 0, self.product_ids.ids)],
            },
        }

    def action_retry_failed_recipients(self):
        """Create a linked retry campaign and resend failed/skipped recipients only."""
        self.ensure_one()
        if self.state == 'running':
            raise UserError(_('Cannot retry while the campaign is still running.'))

        failed_logs = self.log_ids.filtered(
            lambda log: log.delivery_state in ('failed', 'skipped') and log.partner_id
        )
        partners = failed_logs.mapped('partner_id')
        if not partners:
            raise UserError(_('No failed or skipped recipients to retry for this campaign.'))

        config = self.env['whatsapp.config'].get_active_config(self.company_id)
        retry_campaign = self.create({
            'name': _('Retry: %s') % self.name,
            'message': self.message,
            'attachment_info': self.attachment_info,
            'attachment_ids': [(6, 0, self.attachment_ids.ids)],
            'product_ids': [(6, 0, self.product_ids.ids)],
            'partner_ids': [(6, 0, partners.ids)],
            'use_product_images': self.use_product_images,
            'include_product_description': self.include_product_description,
            'user_id': self.env.uid,
            'company_id': self.company_id.id,
            'parent_campaign_id': self.id,
            'state': 'draft',
        })

        from odoo.addons.whatsapp_simple.services.whatsapp_bulk_service import WhatsAppBulkSender

        campaign_logger.info(
            'Retry campaign %s created from parent %s (%s recipients)',
            retry_campaign.id,
            self.id,
            len(partners),
        )

        sender = WhatsAppBulkSender(self.env, config, retry_campaign)
        sender.send_to_partners(
            partners,
            self.message,
            self.attachment_ids,
            products=self.product_ids,
            use_product_images=self.use_product_images,
            include_product_description=self.include_product_description,
        )

        return {
            'type': 'ir.actions.act_window',
            'name': _('Retry Campaign'),
            'res_model': 'whatsapp.bulk.campaign',
            'res_id': retry_campaign.id,
            'view_mode': 'form',
            'target': 'current',
        }

    def action_open_monitor(self):
        self.ensure_one()
        return self.env.ref('whatsapp_simple.action_whatsapp_campaign_monitor').read()[0]

    def _update_execution_progress(
        self,
        processed,
        total,
        partner=None,
        product=None,
        phone=None,
        step=None,
        commit=False,
    ):
        """Update live execution fields for UI and monitor views."""
        now = fields.Datetime.now()
        remaining = max(total - processed, 0)
        percent = (processed / total * 100.0) if total else 0.0
        vals = {
            'progress_percent': percent,
            'processed_count': processed,
            'remaining_count': remaining,
            'current_recipient_id': partner.id if partner else False,
            'current_partner_id': partner.id if partner else False,
            'current_recipient_number': phone or '',
            'current_product_id': product.id if product else False,
            'current_step': step or '',
            'last_activity_at': now,
        }
        self.write(vals)
        campaign_logger.debug(
            'Campaign %s: %.1f%% (%s/%s) step=%s recipient=%s product=%s',
            self.id,
            percent,
            processed,
            total,
            step or '-',
            partner.display_name if partner else '-',
            product.display_name if product else '-',
        )
        if commit:
            self.env.cr.commit()

    def _mark_running(self, total):
        now = fields.Datetime.now()
        self.write({
            'state': 'running',
            'started_at': now,
            'execution_started_at': now,
            'total_count': total,
            'processed_count': 0,
            'remaining_count': total,
            'progress_percent': 0.0,
            'current_step': _('Starting campaign'),
            'last_activity_at': now,
        })

    def _mark_finished(self, stats, stopped=False, failed=False):
        now = fields.Datetime.now()
        sent = stats.get('sent', 0)
        failed_count = stats.get('failed', 0)
        skipped = stats.get('skipped', 0)

        if failed:
            state = 'failed'
        elif stopped:
            state = 'stopped'
        elif failed_count:
            state = 'completed_with_errors'
        else:
            state = 'completed'

        self.write({
            'total_count': stats.get('total', self.total_count),
            'sent_count': sent,
            'failed_count': failed_count,
            'skipped_count': skipped,
            'cooldown_count': stats.get('cooldown_count', 0),
            'total_attachments_sent': stats.get('total_attachments_sent', 0),
            'finished_at': now,
            'execution_finished_at': now,
            'progress_percent': 100.0,
            'processed_count': stats.get('total', self.total_count),
            'remaining_count': 0,
            'state': state,
            'current_recipient_id': False,
            'current_partner_id': False,
            'current_recipient_number': False,
            'current_product_id': False,
            'current_step': _('Finished'),
            'last_activity_at': now,
        })
        campaign_logger.info(
            'Campaign %s finished: state=%s sent=%s failed=%s skipped=%s',
            self.id,
            state,
            sent,
            failed_count,
            skipped,
        )

    # Backward-compatible alias used by bulk sender
    def _update_progress(self, index, total, partner=None, product=None, state='running'):
        phone = partner._whatsapp_find_phone_number() if partner else ''
        self._update_execution_progress(
            index,
            total,
            partner=partner,
            product=product,
            phone=phone,
            step=_('Sending to recipient'),
        )

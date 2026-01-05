# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class TPOPaymentApplication(models.Model):
    _name = 'tpo.payment.application'
    _inherit = ['mail.thread']
    _description = 'Payment Application / Invoice'
    _order = 'application_date desc'

    name = fields.Char(string='Application Number', required=True, tracking=True)
    project_id = fields.Many2one('tpo.project', string='Project', required=True, tracking=True)
    
    # Dates
    application_date = fields.Date(string='Application Date', default=fields.Date.today, required=True, tracking=True)
    period_start_date = fields.Date(string='Period Start Date', tracking=True)
    period_end_date = fields.Date(string='Period End Date', tracking=True)
    
    # Status
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('under_review', 'Under Review'),
        ('approved', 'Approved'),
        ('paid', 'Paid'),
        ('rejected', 'Rejected'),
    ], string='Status', default='draft', tracking=True)
    
    # Responsible
    technical_office_engineer_id = fields.Many2one('res.users', string='Technical Office Engineer', tracking=True)
    accountant_id = fields.Many2one('res.users', string='Accountant', tracking=True)
    
    # Financial Details
    total_amount = fields.Monetary(string='Total Amount', compute='_compute_total_amount', store=True)
    currency_id = fields.Many2one('res.currency', string='Currency', related='project_id.partner_id.currency_id', store=True)
    
    # Lines
    line_ids = fields.One2many('tpo.payment.application.line', 'application_id', string='Application Lines')
    
    # Site Verification
    site_verified = fields.Boolean(string='Site Verified', default=False, tracking=True)
    site_verification_date = fields.Date(string='Site Verification Date', tracking=True)
    site_verification_notes = fields.Text(string='Site Verification Notes', tracking=True)
    
    # Documents
    document_ids = fields.Many2many('ir.attachment', 'tpo_payment_application_document_rel',
                                   'payment_id', 'attachment_id', string='Documents')
    
    # Related Invoice
    invoice_id = fields.Many2one('account.move', string='Related Invoice', tracking=True)
    
    active = fields.Boolean(string='Active', default=True)
    
    @api.depends('line_ids.amount')
    def _compute_total_amount(self):
        for record in self:
            record.total_amount = sum(record.line_ids.mapped('amount'))
    
    def action_submit(self):
        self.write({'state': 'submitted'})
    
    def action_approve(self):
        self.write({'state': 'approved'})
    
    def action_pay(self):
        self.write({'state': 'paid'})
    
    def action_reject(self):
        self.write({'state': 'rejected'})
    
    def action_verify_site(self):
        self.write({
            'site_verified': True,
            'site_verification_date': fields.Date.today(),
        })


class TPOPaymentApplicationLine(models.Model):
    _name = 'tpo.payment.application.line'
    _description = 'Payment Application Line'
    _order = 'sequence, id'

    application_id = fields.Many2one('tpo.payment.application', string='Payment Application', required=True, ondelete='cascade')
    sequence = fields.Integer(string='Sequence', default=10)
    
    item_code = fields.Char(string='Item Code')
    description = fields.Text(string='Description', required=True)
    unit = fields.Char(string='Unit')
    quantity = fields.Float(string='Quantity', default=1.0)
    unit_price = fields.Monetary(string='Unit Price')
    amount = fields.Monetary(string='Amount', compute='_compute_amount', store=True)
    currency_id = fields.Many2one('res.currency', string='Currency', related='application_id.currency_id', store=True)
    
    # Progress
    planned_quantity = fields.Float(string='Planned Quantity', default=0.0)
    completed_quantity = fields.Float(string='Completed Quantity', default=0.0)
    progress_percentage = fields.Float(string='Progress (%)', compute='_compute_progress', store=True)
    
    @api.depends('quantity', 'unit_price')
    def _compute_amount(self):
        for line in self:
            line.amount = line.quantity * line.unit_price
    
    @api.depends('planned_quantity', 'completed_quantity')
    def _compute_progress(self):
        for line in self:
            if line.planned_quantity > 0:
                line.progress_percentage = (line.completed_quantity / line.planned_quantity) * 100
            else:
                line.progress_percentage = 0.0


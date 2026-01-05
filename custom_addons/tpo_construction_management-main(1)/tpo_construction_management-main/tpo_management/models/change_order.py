# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class TPOChangeOrder(models.Model):
    _name = 'tpo.change.order'
    _inherit = ['mail.thread']
    _description = 'Change Order / Variation Order (VO)'
    _order = 'date desc'

    name = fields.Char(string='VO Number', required=True, tracking=True)
    project_id = fields.Many2one('tpo.project', string='Project', required=True, tracking=True)
    
    # Dates
    date = fields.Date(string='Date', default=fields.Date.today, required=True, tracking=True)
    approval_date = fields.Date(string='Approval Date', tracking=True)
    
    # Status
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('under_review', 'Under Review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], string='Status', default='draft', tracking=True)
    
    # Responsible
    project_manager_id = fields.Many2one('res.users', string='Project Manager', tracking=True)
    technical_office_engineer_id = fields.Many2one('res.users', string='Technical Office Engineer', tracking=True)
    site_engineer_id = fields.Many2one('res.users', string='Site Engineer', tracking=True)
    
    # Change Order Details
    change_type = fields.Selection([
        ('scope', 'Scope Change'),
        ('quantity', 'Quantity Change'),
        ('specification', 'Specification Change'),
        ('time', 'Time Extension'),
        ('cost', 'Cost Change'),
        ('other', 'Other'),
    ], string='Change Type', required=True, tracking=True)
    
    subject = fields.Char(string='Subject', required=True, tracking=True)
    description = fields.Text(string='Description', required=True, tracking=True)
    reason = fields.Text(string='Reason for Change', tracking=True)
    location = fields.Char(string='Location', tracking=True, help='Specific site location affected by the change')
    
    # Financial Impact
    original_amount = fields.Monetary(string='Original Amount', tracking=True)
    revised_amount = fields.Monetary(string='Revised Amount', tracking=True)
    change_amount = fields.Monetary(string='Change Amount', compute='_compute_change_amount', store=True)
    currency_id = fields.Many2one('res.currency', string='Currency', related='project_id.partner_id.currency_id', store=True)
    
    # Time Impact
    original_duration = fields.Float(string='Original Duration (Days)', tracking=True)
    revised_duration = fields.Float(string='Revised Duration (Days)', tracking=True)
    duration_change = fields.Float(string='Duration Change (Days)', compute='_compute_duration_change', store=True)
    
    # Site Visit
    site_visit_required = fields.Boolean(string='Site Visit Required', default=False, tracking=True)
    site_visit_date = fields.Date(string='Site Visit Date', tracking=True)
    site_visit_notes = fields.Text(string='Site Visit Notes', tracking=True)
    site_visit_participants = fields.Many2many('res.users', string='Site Visit Participants')
    
    # Lines
    line_ids = fields.One2many('tpo.change.order.line', 'change_order_id', string='Change Order Lines')
    
    # Documents
    document_ids = fields.Many2many('ir.attachment', 'tpo_change_order_document_rel',
                                   'change_order_id', 'attachment_id', string='Documents')
    
    # Related Documents
    related_shop_drawing_ids = fields.Many2many('tpo.shop.drawing', string='Related Shop Drawings')
    related_rfi_ids = fields.Many2many('tpo.rfi', string='Related RFIs')
    
    active = fields.Boolean(string='Active', default=True)
    
    @api.depends('original_amount', 'revised_amount')
    def _compute_change_amount(self):
        for record in self:
            record.change_amount = record.revised_amount - record.original_amount
    
    @api.depends('original_duration', 'revised_duration')
    def _compute_duration_change(self):
        for record in self:
            record.duration_change = record.revised_duration - record.original_duration
    
    def action_submit(self):
        self.write({'state': 'submitted'})
    
    def action_approve(self):
        self.write({
            'state': 'approved',
            'approval_date': fields.Date.today(),
        })
    
    def action_reject(self):
        self.write({'state': 'rejected'})
    
    def action_schedule_site_visit(self):
        self.write({'site_visit_required': True})


class TPOChangeOrderLine(models.Model):
    _name = 'tpo.change.order.line'
    _description = 'Change Order Line'
    _order = 'sequence, id'

    change_order_id = fields.Many2one('tpo.change.order', string='Change Order', required=True, ondelete='cascade')
    sequence = fields.Integer(string='Sequence', default=10)
    
    item_code = fields.Char(string='Item Code')
    description = fields.Text(string='Description', required=True)
    unit = fields.Char(string='Unit')
    original_quantity = fields.Float(string='Original Quantity', default=0.0)
    revised_quantity = fields.Float(string='Revised Quantity', default=0.0)
    quantity_change = fields.Float(string='Quantity Change', compute='_compute_quantity_change', store=True)
    unit_price = fields.Monetary(string='Unit Price')
    amount = fields.Monetary(string='Amount', compute='_compute_amount', store=True)
    currency_id = fields.Many2one('res.currency', string='Currency', related='change_order_id.currency_id', store=True)
    
    @api.depends('original_quantity', 'revised_quantity')
    def _compute_quantity_change(self):
        for line in self:
            line.quantity_change = line.revised_quantity - line.original_quantity
    
    @api.depends('quantity_change', 'unit_price')
    def _compute_amount(self):
        for line in self:
            line.amount = line.quantity_change * line.unit_price


# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class TPOBOQ(models.Model):
    _name = 'tpo.boq'
    _inherit = ['mail.thread']
    _description = 'Bill of Quantities (BOQ)'
    _order = 'date desc'

    name = fields.Char(string='BOQ Reference', required=True, tracking=True)
    project_id = fields.Many2one('tpo.project', string='Project', required=True, tracking=True)
    date = fields.Date(string='Date', default=fields.Date.today, required=True, tracking=True)
    
    # Status
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], string='Status', default='draft', tracking=True)
    
    # Responsible
    technical_office_engineer_id = fields.Many2one('res.users', string='Technical Office Engineer', tracking=True)
    estimator_id = fields.Many2one('res.users', string='Estimator', tracking=True)
    
    # Content
    description = fields.Text(string='Description', tracking=True)
    total_amount = fields.Monetary(string='Total Amount', compute='_compute_total_amount', store=True)
    currency_id = fields.Many2one('res.currency', string='Currency', related='project_id.partner_id.currency_id', store=True)
    
    # Lines
    line_ids = fields.One2many('tpo.boq.line', 'boq_id', string='BOQ Lines')
    
    # Documents
    document_ids = fields.Many2many('ir.attachment', 'tpo_boq_document_rel',
                                   'boq_id', 'attachment_id', string='Documents')
    
    active = fields.Boolean(string='Active', default=True)
    
    @api.depends('line_ids.amount')
    def _compute_total_amount(self):
        for record in self:
            record.total_amount = sum(record.line_ids.mapped('amount'))
    
    def action_submit(self):
        self.write({'state': 'submitted'})
    
    def action_approve(self):
        self.write({'state': 'approved'})
    
    def action_reject(self):
        self.write({'state': 'rejected'})


class TPOBOQLine(models.Model):
    _name = 'tpo.boq.line'
    _description = 'BOQ Line'
    _order = 'sequence, id'

    boq_id = fields.Many2one('tpo.boq', string='BOQ', required=True, ondelete='cascade')
    sequence = fields.Integer(string='Sequence', default=10)
    
    item_code = fields.Char(string='Item Code')
    description = fields.Text(string='Description', required=True)
    unit = fields.Char(string='Unit')
    quantity = fields.Float(string='Quantity', default=1.0)
    unit_price = fields.Monetary(string='Unit Price')
    amount = fields.Monetary(string='Amount', compute='_compute_amount', store=True)
    currency_id = fields.Many2one('res.currency', string='Currency', related='boq_id.currency_id', store=True)
    
    @api.depends('quantity', 'unit_price')
    def _compute_amount(self):
        for line in self:
            line.amount = line.quantity * line.unit_price


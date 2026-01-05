# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class TPOTechnicalOffer(models.Model):
    _name = 'tpo.technical.offer'
    _inherit = ['mail.thread']
    _description = 'Technical & Financial Offer'
    _order = 'date desc'

    name = fields.Char(string='Offer Reference', required=True, tracking=True)
    project_id = fields.Many2one('tpo.project', string='Project', required=True, tracking=True)
    date = fields.Date(string='Date', default=fields.Date.today, required=True, tracking=True)
    
    # Status
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('under_review', 'Under Review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('won', 'Won'),
        ('lost', 'Lost'),
    ], string='Status', default='draft', tracking=True)
    
    # Responsible
    estimating_department_id = fields.Many2one('res.users', string='Estimating Department', tracking=True)
    
    # Offer Details
    offer_type = fields.Selection([
        ('technical', 'Technical Only'),
        ('financial', 'Financial Only'),
        ('both', 'Technical & Financial'),
    ], string='Offer Type', default='both', required=True, tracking=True)
    
    description = fields.Text(string='Description', tracking=True)
    
    # Financial
    total_amount = fields.Monetary(string='Total Amount', compute='_compute_total_amount', store=True)
    currency_id = fields.Many2one('res.currency', string='Currency', related='project_id.partner_id.currency_id', store=True)
    validity_date = fields.Date(string='Validity Date', tracking=True)
    
    # Lines
    offer_item_ids = fields.One2many('tpo.technical.offer.line', 'offer_id', string='Offer Items')
    
    # Documents
    document_ids = fields.Many2many('ir.attachment', 'tpo_technical_offer_document_rel',
                                   'offer_id', 'attachment_id', string='Documents')
    
    active = fields.Boolean(string='Active', default=True)
    
    @api.depends('offer_item_ids.amount')
    def _compute_total_amount(self):
        for record in self:
            record.total_amount = sum(record.offer_item_ids.mapped('amount'))
    
    def action_submit(self):
        self.write({'state': 'submitted'})
    
    def action_approve(self):
        self.write({'state': 'approved'})
    
    def action_reject(self):
        self.write({'state': 'rejected'})


class TPOTechnicalOfferLine(models.Model):
    _name = 'tpo.technical.offer.line'
    _description = 'Technical Offer Line'
    _order = 'sequence, id'

    offer_id = fields.Many2one('tpo.technical.offer', string='Offer', required=True, ondelete='cascade')
    sequence = fields.Integer(string='Sequence', default=10)
    
    item_code = fields.Char(string='Item Code')
    description = fields.Text(string='Description', required=True)
    unit = fields.Char(string='Unit')
    quantity = fields.Float(string='Quantity', default=1.0)
    unit_price = fields.Monetary(string='Unit Price')
    amount = fields.Monetary(string='Amount', compute='_compute_amount', store=True)
    currency_id = fields.Many2one('res.currency', string='Currency', related='offer_id.currency_id', store=True)
    
    @api.depends('quantity', 'unit_price')
    def _compute_amount(self):
        for line in self:
            line.amount = line.quantity * line.unit_price


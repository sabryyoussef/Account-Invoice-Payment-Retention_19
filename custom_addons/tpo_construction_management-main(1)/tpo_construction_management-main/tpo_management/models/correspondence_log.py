# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class TPOCorrespondenceLog(models.Model):
    _name = 'tpo.correspondence.log'
    _inherit = ['mail.thread']
    _description = 'Correspondence Log'
    _order = 'date desc'

    name = fields.Char(string='Reference', required=True, tracking=True)
    project_id = fields.Many2one('tpo.project', string='Project', required=True, tracking=True)
    
    # Dates
    date = fields.Date(string='Date', default=fields.Date.today, required=True, tracking=True)
    received_date = fields.Date(string='Received Date', tracking=True)
    
    # Status
    state = fields.Selection([
        ('draft', 'Draft'),
        ('sent', 'Sent'),
        ('received', 'Received'),
        ('acknowledged', 'Acknowledged'),
    ], string='Status', default='draft', tracking=True)
    
    # Responsible
    document_controller_id = fields.Many2one('res.users', string='Document Controller', tracking=True)
    
    # Correspondence Details
    correspondence_type = fields.Selection([
        ('letter', 'Letter'),
        ('email', 'Email'),
        ('fax', 'Fax'),
        ('memo', 'Memo'),
        ('other', 'Other'),
    ], string='Correspondence Type', required=True, tracking=True)
    
    direction = fields.Selection([
        ('outgoing', 'Outgoing'),
        ('incoming', 'Incoming'),
    ], string='Direction', required=True, tracking=True)
    
    subject = fields.Char(string='Subject', required=True, tracking=True)
    description = fields.Text(string='Description', tracking=True)
    
    # Parties
    from_partner_id = fields.Many2one('res.partner', string='From', tracking=True)
    to_partner_id = fields.Many2one('res.partner', string='To', tracking=True)
    
    # Priority
    priority = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent'),
    ], string='Priority', default='medium', tracking=True)
    
    # Response
    requires_response = fields.Boolean(string='Requires Response', default=False, tracking=True)
    response_date = fields.Date(string='Response Date', tracking=True)
    response_reference = fields.Char(string='Response Reference', tracking=True)
    
    # Documents
    document_ids = fields.Many2many('ir.attachment', 'tpo_correspondence_log_document_rel',
                                   'correspondence_id', 'attachment_id', string='Documents')
    
    # Related Documents
    related_shop_drawing_ids = fields.Many2many('tpo.shop.drawing', string='Related Shop Drawings')
    related_rfi_ids = fields.Many2many('tpo.rfi', string='Related RFIs')
    related_change_order_ids = fields.Many2many('tpo.change.order', string='Related Change Orders')
    
    active = fields.Boolean(string='Active', default=True)
    
    def action_send(self):
        self.write({
            'state': 'sent',
            'date': fields.Date.today(),
        })
    
    def action_receive(self):
        self.write({
            'state': 'received',
            'received_date': fields.Date.today(),
        })
    
    def action_acknowledge(self):
        self.write({'state': 'acknowledged'})


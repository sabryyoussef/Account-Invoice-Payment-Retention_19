# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class TPORFI(models.Model):
    _name = 'tpo.rfi'
    _inherit = ['mail.thread']
    _description = 'Request for Information (RFI)'
    _order = 'date desc'

    name = fields.Char(string='RFI Number', required=True, tracking=True)
    project_id = fields.Many2one('tpo.project', string='Project', required=True, tracking=True)
    
    # Dates
    date = fields.Date(string='Date', default=fields.Date.today, required=True, tracking=True)
    response_date = fields.Date(string='Response Date', tracking=True)
    due_date = fields.Date(string='Due Date', tracking=True)
    
    # Status
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('answered', 'Answered'),
        ('closed', 'Closed'),
    ], string='Status', default='draft', tracking=True)
    
    # Responsible
    site_engineer_id = fields.Many2one('res.users', string='Site Engineer', tracking=True)
    technical_office_engineer_id = fields.Many2one('res.users', string='Technical Office Engineer', tracking=True)
    
    # RFI Details
    subject = fields.Char(string='Subject', required=True, tracking=True)
    description = fields.Text(string='Description', required=True, tracking=True)
    location = fields.Char(string='Location', tracking=True, help='Specific site location where the issue was identified')
    
    # Issue Type
    issue_type = fields.Selection([
        ('discrepancy', 'Design Discrepancy'),
        ('omission', 'Omission'),
        ('error', 'Error'),
        ('clarification', 'Clarification Needed'),
        ('unforeseen', 'Unforeseen Condition'),
        ('other', 'Other'),
    ], string='Issue Type', required=True, tracking=True)
    
    # Priority
    priority = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent'),
    ], string='Priority', default='medium', tracking=True)
    
    # Response
    response = fields.Text(string='Response', tracking=True)
    responded_by_id = fields.Many2one('res.users', string='Responded By', tracking=True)
    
    # Site Visit
    site_visit_required = fields.Boolean(string='Site Visit Required', default=False, tracking=True)
    site_visit_date = fields.Date(string='Site Visit Date', tracking=True)
    site_visit_notes = fields.Text(string='Site Visit Notes', tracking=True)
    
    # Documents
    document_ids = fields.Many2many('ir.attachment', 'tpo_rfi_document_rel',
                                   'rfi_id', 'attachment_id', string='Documents')
    
    # Related Documents
    related_shop_drawing_ids = fields.Many2many('tpo.shop.drawing', string='Related Shop Drawings')
    related_itr_ids = fields.Many2many('tpo.itr', string='Related ITRs')
    
    active = fields.Boolean(string='Active', default=True)
    
    def action_submit(self):
        self.write({'state': 'submitted'})
    
    def action_answer(self):
        self.write({
            'state': 'answered',
            'response_date': fields.Date.today(),
        })
    
    def action_close(self):
        self.write({'state': 'closed'})
    
    def action_schedule_site_visit(self):
        self.write({'site_visit_required': True})


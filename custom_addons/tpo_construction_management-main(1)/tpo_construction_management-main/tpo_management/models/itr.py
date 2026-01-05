# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class TPOITR(models.Model):
    _name = 'tpo.itr'
    _inherit = ['mail.thread']
    _description = 'Inspection & Test Request (ITR)'
    _order = 'request_date desc'

    name = fields.Char(string='ITR Number', required=True, tracking=True)
    project_id = fields.Many2one('tpo.project', string='Project', required=True, tracking=True)
    
    # Dates
    request_date = fields.Date(string='Request Date', default=fields.Date.today, required=True, tracking=True)
    inspection_date = fields.Date(string='Inspection Date', tracking=True)
    response_date = fields.Date(string='Response Date', tracking=True)
    
    # Status
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('scheduled', 'Scheduled'),
        ('inspected', 'Inspected'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('resubmitted', 'Resubmitted'),
    ], string='Status', default='draft', tracking=True)
    
    # Responsible
    site_engineer_id = fields.Many2one('res.users', string='Site Engineer', tracking=True)
    technical_office_engineer_id = fields.Many2one('res.users', string='Technical Office Engineer', tracking=True)
    
    # ITR Details
    inspection_type = fields.Selection([
        ('rebar', 'Rebar Inspection'),
        ('concrete_pour', 'Pre-Concrete Pour'),
        ('formwork', 'Formwork Inspection'),
        ('mep', 'MEP Inspection'),
        ('finishes', 'Finishes Inspection'),
        ('final', 'Final Inspection'),
        ('other', 'Other'),
    ], string='Inspection Type', required=True, tracking=True)
    
    description = fields.Text(string='Description', required=True, tracking=True)
    location = fields.Char(string='Location', tracking=True, help='Specific site location for inspection')
    
    # Priority
    priority = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent'),
    ], string='Priority', default='medium', tracking=True)
    
    # Inspection Results
    inspection_result = fields.Selection([
        ('approved', 'Approved'),
        ('approved_as_noted', 'Approved as Noted'),
        ('rejected', 'Rejected'),
        ('conditional', 'Conditional Approval'),
    ], string='Inspection Result', tracking=True)
    
    inspection_notes = fields.Text(string='Inspection Notes', tracking=True)
    inspector_name = fields.Char(string='Inspector Name', tracking=True)
    
    # Quality Participation
    technical_office_participated = fields.Boolean(string='Technical Office Participated', default=False, tracking=True)
    participation_notes = fields.Text(string='Participation Notes', tracking=True)
    
    # Documents
    document_ids = fields.Many2many('ir.attachment', 'tpo_itr_document_rel',
                                   'itr_id', 'attachment_id', string='Documents')
    
    # Related Documents
    related_shop_drawing_ids = fields.Many2many('tpo.shop.drawing', string='Related Shop Drawings')
    related_rfi_ids = fields.Many2many('tpo.rfi', string='Related RFIs')
    
    active = fields.Boolean(string='Active', default=True)
    
    def action_submit(self):
        self.write({'state': 'submitted'})
    
    def action_schedule(self):
        self.write({'state': 'scheduled'})
    
    def action_inspect(self):
        self.write({
            'state': 'inspected',
            'inspection_date': fields.Date.today(),
        })
    
    def action_approve(self):
        self.write({
            'state': 'approved',
            'response_date': fields.Date.today(),
        })
    
    def action_reject(self):
        self.write({
            'state': 'rejected',
            'response_date': fields.Date.today(),
        })
    
    def action_resubmit(self):
        self.write({
            'state': 'resubmitted',
            'request_date': fields.Date.today(),
        })


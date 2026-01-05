# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class TPOAsBuiltDrawing(models.Model):
    _name = 'tpo.as.built.drawing'
    _inherit = ['mail.thread']
    _description = 'As-Built Drawing'
    _order = 'completion_date desc'

    name = fields.Char(string='Drawing Reference', required=True, tracking=True)
    project_id = fields.Many2one('tpo.project', string='Project', required=True, tracking=True)
    
    # Dates
    completion_date = fields.Date(string='Completion Date', tracking=True)
    submission_date = fields.Date(string='Submission Date', default=fields.Date.today, tracking=True)
    
    # Status
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
    ], string='Status', default='draft', tracking=True)
    
    # Responsible
    technical_office_engineer_id = fields.Many2one('res.users', string='Technical Office Engineer', tracking=True)
    surveyor_id = fields.Many2one('res.users', string='Surveyor', tracking=True)
    
    # Drawing Details
    discipline = fields.Selection([
        ('architectural', 'Architectural'),
        ('structural', 'Structural'),
        ('mep', 'MEP'),
        ('civil', 'Civil'),
        ('other', 'Other'),
    ], string='Discipline', required=True, tracking=True)
    
    description = fields.Text(string='Description', tracking=True)
    drawing_number = fields.Char(string='Drawing Number', tracking=True)
    revision_number = fields.Integer(string='Revision Number', default=0, tracking=True)
    
    # Site Measurement
    site_measured = fields.Boolean(string='Site Measured', default=False, tracking=True)
    site_measurement_date = fields.Date(string='Site Measurement Date', tracking=True)
    site_measurement_notes = fields.Text(string='Site Measurement Notes', tracking=True)
    
    # Changes from Original
    changes_description = fields.Text(string='Changes Description', tracking=True, 
                                      help='Description of changes from original design')
    
    # Documents
    document_ids = fields.Many2many('ir.attachment', 'tpo_as_built_drawing_document_rel',
                                   'as_built_drawing_id', 'attachment_id', string='Drawings')
    
    # Related Documents
    related_shop_drawing_ids = fields.Many2many('tpo.shop.drawing', string='Related Shop Drawings')
    
    active = fields.Boolean(string='Active', default=True)
    
    def action_start(self):
        self.write({'state': 'in_progress'})
    
    def action_complete(self):
        self.write({
            'state': 'completed',
            'completion_date': fields.Date.today(),
        })
    
    def action_submit(self):
        self.write({
            'state': 'submitted',
            'submission_date': fields.Date.today(),
        })
    
    def action_approve(self):
        self.write({'state': 'approved'})
    
    def action_measure_site(self):
        self.write({
            'site_measured': True,
            'site_measurement_date': fields.Date.today(),
        })


# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class TPOMaterialSubmittal(models.Model):
    _name = 'tpo.material.submittal'
    _inherit = ['mail.thread']
    _description = 'Material Submittal'
    _order = 'submittal_date desc'

    name = fields.Char(string='Submittal Reference', required=True, tracking=True)
    project_id = fields.Many2one('tpo.project', string='Project', required=True, tracking=True)
    
    # Dates
    submittal_date = fields.Date(string='Submittal Date', default=fields.Date.today, required=True, tracking=True)
    response_date = fields.Date(string='Response Date', tracking=True)
    
    # Status
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('approved_as_noted', 'Approved as Noted'),
        ('rejected', 'Rejected'),
        ('resubmitted', 'Resubmitted'),
    ], string='Status', default='draft', tracking=True)
    
    # Responsible
    technical_office_engineer_id = fields.Many2one('res.users', string='Technical Office Engineer', tracking=True)
    
    # Material Details
    material_description = fields.Text(string='Material Description', required=True, tracking=True)
    specification = fields.Text(string='Specification', tracking=True)
    manufacturer = fields.Char(string='Manufacturer', tracking=True)
    model = fields.Char(string='Model', tracking=True)
    
    # Submission Log
    revision_number = fields.Integer(string='Revision Number', default=0, tracking=True)
    submission_log_ids = fields.One2many('tpo.material.submittal.log', 'submittal_id', string='Submission Log')
    
    # Documents
    document_ids = fields.Many2many('ir.attachment', 'tpo_material_submittal_document_rel', 
                                   'submittal_id', 'attachment_id', string='Documents')
    sample_ids = fields.Many2many('ir.attachment', 'tpo_material_submittal_sample_rel',
                                 'submittal_id', 'attachment_id', string='Samples', 
                                 domain=[('res_model', '=', 'tpo.material.submittal')])
    
    # Comments
    consultant_comments = fields.Text(string='Consultant Comments', tracking=True)
    client_comments = fields.Text(string='Client Comments', tracking=True)
    
    active = fields.Boolean(string='Active', default=True)
    
    def action_submit(self):
        self.write({'state': 'submitted'})
        # Create submission log entry
        self.env['tpo.material.submittal.log'].create({
            'submittal_id': self.id,
            'submission_date': fields.Date.today(),
            'revision_number': self.revision_number,
            'status': 'submitted',
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
        self.revision_number += 1
        self.write({
            'state': 'resubmitted',
            'submittal_date': fields.Date.today(),
        })
        # Create submission log entry
        self.env['tpo.material.submittal.log'].create({
            'submittal_id': self.id,
            'submission_date': fields.Date.today(),
            'revision_number': self.revision_number,
            'status': 'resubmitted',
        })


class TPOMaterialSubmittalLog(models.Model):
    _name = 'tpo.material.submittal.log'
    _description = 'Material Submittal Log Entry'
    _order = 'submission_date desc'

    submittal_id = fields.Many2one('tpo.material.submittal', string='Submittal', required=True, ondelete='cascade')
    submission_date = fields.Date(string='Submission Date', required=True)
    revision_number = fields.Integer(string='Revision Number', required=True)
    status = fields.Selection([
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('approved_as_noted', 'Approved as Noted'),
        ('rejected', 'Rejected'),
        ('resubmitted', 'Resubmitted'),
    ], string='Status', required=True)
    response_date = fields.Date(string='Response Date')
    comments = fields.Text(string='Comments')


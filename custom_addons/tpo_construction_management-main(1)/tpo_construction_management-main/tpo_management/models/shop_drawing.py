# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class TPOShopDrawing(models.Model):
    _name = 'tpo.shop.drawing'
    _inherit = ['mail.thread']
    _description = 'Shop Drawing'
    _order = 'submission_date desc'

    name = fields.Char(string='Drawing Reference', required=True, tracking=True)
    project_id = fields.Many2one('tpo.project', string='Project', required=True, tracking=True)
    
    # Dates
    submission_date = fields.Date(string='Submission Date', default=fields.Date.today, required=True, tracking=True)
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
    
    # Submission Log
    submission_log_ids = fields.One2many('tpo.shop.drawing.log', 'drawing_id', string='Submission Log')
    
    # Documents
    document_ids = fields.Many2many('ir.attachment', 'tpo_shop_drawing_document_rel',
                                   'shop_drawing_id', 'attachment_id', string='Drawings')
    
    # Comments
    consultant_comments = fields.Text(string='Consultant Comments', tracking=True)
    client_comments = fields.Text(string='Client Comments', tracking=True)
    
    # Site Verification
    site_verified = fields.Boolean(string='Site Verified', default=False, tracking=True)
    site_verification_date = fields.Date(string='Site Verification Date', tracking=True)
    site_verification_notes = fields.Text(string='Site Verification Notes', tracking=True)
    
    active = fields.Boolean(string='Active', default=True)
    
    def action_submit(self):
        self.write({'state': 'submitted'})
        # Create submission log entry
        self.env['tpo.shop.drawing.log'].create({
            'drawing_id': self.id,
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
            'submission_date': fields.Date.today(),
        })
        # Create submission log entry
        self.env['tpo.shop.drawing.log'].create({
            'drawing_id': self.id,
            'submission_date': fields.Date.today(),
            'revision_number': self.revision_number,
            'status': 'resubmitted',
        })
    
    def action_verify_site(self):
        self.write({
            'site_verified': True,
            'site_verification_date': fields.Date.today(),
        })


class TPOShopDrawingLog(models.Model):
    _name = 'tpo.shop.drawing.log'
    _description = 'Shop Drawing Log Entry'
    _order = 'submission_date desc'

    drawing_id = fields.Many2one('tpo.shop.drawing', string='Shop Drawing', required=True, ondelete='cascade')
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


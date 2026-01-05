# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class TPOVisit(models.Model):
    _name = 'tpo.visit'
    _inherit = ['mail.thread']
    _description = 'TPO Visit Task'
    _order = 'visit_date desc'

    name = fields.Char(string='Visit Reference', required=True, tracking=True)
    project_id = fields.Many2one('tpo.project', string='Project', required=True, tracking=True)
    
    # Dates
    visit_date = fields.Date(string='Visit Date', default=fields.Date.today, required=True, tracking=True)
    visit_time = fields.Float(string='Visit Time', tracking=True)
    
    # Status
    state = fields.Selection([
        ('planned', 'Planned'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='planned', tracking=True)
    
    # Participants
    technical_office_engineer_id = fields.Many2one('res.users', string='Technical Office Engineer', tracking=True)
    site_engineer_id = fields.Many2one('res.users', string='Site Engineer', tracking=True)
    surveyor_id = fields.Many2one('res.users', string='Surveyor', tracking=True)
    project_manager_id = fields.Many2one('res.users', string='Project Manager', tracking=True)
    other_participants_ids = fields.Many2many('res.users', string='Other Participants')
    
    # Visit Type
    visit_type = fields.Selection([
        ('site_measurement', 'Site Measurement & Verification'),
        ('rfi_clarification', 'RFI Clarification/Investigation'),
        ('shop_drawing_check', 'Shop Drawing Implementation Check'),
        ('change_order_scoping', 'Change Order Scoping & Validation'),
        ('quality_inspection', 'Quality Inspection Participation'),
        ('other', 'Other'),
    ], string='Visit Type', required=True, tracking=True)
    
    # Visit Details
    location = fields.Char(string='Location', required=True, tracking=True, help='Specific site location')
    purpose = fields.Text(string='Purpose', required=True, tracking=True)
    findings = fields.Text(string='Findings', tracking=True)
    recommendations = fields.Text(string='Recommendations', tracking=True)
    
    # Duration
    duration_hours = fields.Float(string='Duration (Hours)', tracking=True)
    
    # Documents
    document_ids = fields.Many2many('ir.attachment', 'tpo_visit_document_rel',
                                   'visit_id', 'attachment_id', string='Documents')
    photos_ids = fields.Many2many('ir.attachment', 'tpo_visit_photo_rel',
                                 'visit_id', 'attachment_id', string='Photos',
                                 domain=[('res_model', '=', 'tpo.visit')])
    
    # Related Documents
    related_shop_drawing_ids = fields.Many2many('tpo.shop.drawing', string='Related Shop Drawings')
    related_rfi_ids = fields.Many2many('tpo.rfi', string='Related RFIs')
    related_itr_ids = fields.Many2many('tpo.itr', string='Related ITRs')
    related_change_order_ids = fields.Many2many('tpo.change.order', string='Related Change Orders')
    related_as_built_drawing_ids = fields.Many2many('tpo.as.built.drawing', string='Related As-Built Drawings')
    related_payment_application_ids = fields.Many2many('tpo.payment.application', string='Related Payment Applications')
    
    active = fields.Boolean(string='Active', default=True)
    
    def action_start(self):
        self.write({'state': 'in_progress'})
    
    def action_complete(self):
        self.write({
            'state': 'completed',
            'visit_date': fields.Date.today(),
        })
    
    def action_cancel(self):
        self.write({'state': 'cancelled'})


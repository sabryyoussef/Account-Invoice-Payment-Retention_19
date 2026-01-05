# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class TPOProjectHandover(models.Model):
    _name = 'tpo.project.handover'
    _inherit = ['mail.thread']
    _description = 'Project Handover Certificate'
    _order = 'handover_date desc'

    name = fields.Char(string='Certificate Number', required=True, tracking=True)
    project_id = fields.Many2one('tpo.project', string='Project', required=True, tracking=True)
    
    # Dates
    handover_date = fields.Date(string='Handover Date', default=fields.Date.today, required=True, tracking=True)
    completion_date = fields.Date(string='Completion Date', tracking=True)
    
    # Status
    state = fields.Selection([
        ('draft', 'Draft'),
        ('prepared', 'Prepared'),
        ('submitted', 'Submitted'),
        ('signed', 'Signed'),
        ('completed', 'Completed'),
    ], string='Status', default='draft', tracking=True)
    
    # Responsible
    project_manager_id = fields.Many2one('res.users', string='Project Manager', tracking=True)
    administration_id = fields.Many2one('res.users', string='Administration', tracking=True)
    
    # Handover Details
    description = fields.Text(string='Description', tracking=True)
    handover_type = fields.Selection([
        ('partial', 'Partial Handover'),
        ('final', 'Final Handover'),
    ], string='Handover Type', default='final', required=True, tracking=True)
    
    # Signatures
    contractor_signature = fields.Binary(string='Contractor Signature', tracking=True)
    contractor_signed_by = fields.Many2one('res.users', string='Contractor Signed By', tracking=True)
    contractor_signed_date = fields.Date(string='Contractor Signed Date', tracking=True)
    
    client_signature = fields.Binary(string='Client Signature', tracking=True)
    client_signed_by = fields.Many2one('res.partner', string='Client Signed By', tracking=True)
    client_signed_date = fields.Date(string='Client Signed Date', tracking=True)
    
    # Checklist
    checklist_ids = fields.One2many('tpo.project.handover.checklist', 'handover_id', string='Handover Checklist')
    all_items_completed = fields.Boolean(string='All Items Completed', compute='_compute_all_items_completed', store=True)
    
    # Documents
    document_ids = fields.Many2many('ir.attachment', 'tpo_project_handover_document_rel',
                                   'handover_id', 'attachment_id', string='Documents')
    
    # Related Documents
    related_as_built_drawing_ids = fields.Many2many('tpo.as.built.drawing', string='Related As-Built Drawings')
    
    active = fields.Boolean(string='Active', default=True)
    
    @api.depends('checklist_ids.completed')
    def _compute_all_items_completed(self):
        for record in self:
            if record.checklist_ids:
                record.all_items_completed = all(record.checklist_ids.mapped('completed'))
            else:
                record.all_items_completed = False
    
    def action_prepare(self):
        self.write({'state': 'prepared'})
    
    def action_submit(self):
        self.write({'state': 'submitted'})
    
    def action_sign(self):
        self.write({
            'state': 'signed',
            'contractor_signed_date': fields.Date.today(),
        })
    
    def action_complete(self):
        self.write({
            'state': 'completed',
            'client_signed_date': fields.Date.today(),
        })


class TPOProjectHandoverChecklist(models.Model):
    _name = 'tpo.project.handover.checklist'
    _description = 'Project Handover Checklist Item'
    _order = 'sequence, id'

    handover_id = fields.Many2one('tpo.project.handover', string='Handover', required=True, ondelete='cascade')
    sequence = fields.Integer(string='Sequence', default=10)
    
    name = fields.Char(string='Item', required=True)
    description = fields.Text(string='Description')
    completed = fields.Boolean(string='Completed', default=False)
    completed_date = fields.Date(string='Completed Date')
    completed_by = fields.Many2one('res.users', string='Completed By')
    notes = fields.Text(string='Notes')


# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TPOReportWizard(models.TransientModel):
    _name = 'tpo.report.wizard'
    _description = 'TPO Report Wizard'

    report_type = fields.Selection([
        ('boq', 'BOQ Report'),
        ('shop_drawing', 'Shop Drawing Status Report'),
        ('rfi', 'RFI Tracking Report'),
        ('itr', 'ITR Status Report'),
        ('change_order', 'Change Order Report'),
        ('payment_application', 'Payment Application Report'),
        ('document_status', 'Document Status Dashboard'),
        ('submission_log', 'Submission Log Report'),
        ('project_progress', 'Project Progress Report'),
    ], string='Report Type', required=True)
    
    project_id = fields.Many2one('tpo.project', string='Project')
    project_ids = fields.Many2many('tpo.project', string='Projects')
    
    date_from = fields.Date(string='Date From')
    date_to = fields.Date(string='Date To')
    
    state_filter = fields.Selection([
        ('all', 'All States'),
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], string='State Filter', default='all')
    
    include_details = fields.Boolean(string='Include Details', default=True)
    include_summary = fields.Boolean(string='Include Summary', default=True)
    
    def action_generate_report(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Generate Report',
            'res_model': 'tpo.report.wizard',
            'view_mode': 'form',
            'target': 'new',
            'res_id': self.id,
            'context': self.env.context,
        }


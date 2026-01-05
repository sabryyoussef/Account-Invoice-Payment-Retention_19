# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class TPOProjectSchedule(models.Model):
    _name = 'tpo.project.schedule'
    _inherit = ['mail.thread']
    _description = 'Project Schedule (Gantt Chart)'
    _order = 'date desc'

    name = fields.Char(string='Schedule Name', required=True, tracking=True)
    project_id = fields.Many2one('tpo.project', string='Project', required=True, tracking=True)
    date = fields.Date(string='Date', default=fields.Date.today, required=True, tracking=True)
    
    # Status
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], string='Status', default='draft', tracking=True)
    
    # Responsible
    project_manager_id = fields.Many2one('res.users', string='Project Manager', tracking=True)
    planner_id = fields.Many2one('res.users', string='Planner', tracking=True)
    
    # Schedule Details
    description = fields.Text(string='Description', tracking=True)
    baseline_date = fields.Date(string='Baseline Date', tracking=True)
    planned_start_date = fields.Date(string='Planned Start Date', tracking=True)
    planned_end_date = fields.Date(string='Planned End Date', tracking=True)
    
    # Activities
    activity_ids = fields.One2many('tpo.project.schedule.activity', 'schedule_id', string='Activities')
    
    # Documents
    document_ids = fields.Many2many('ir.attachment', 'tpo_project_schedule_document_rel',
                                   'schedule_id', 'attachment_id', string='Documents')
    
    active = fields.Boolean(string='Active', default=True)
    
    def action_submit(self):
        self.write({'state': 'submitted'})
    
    def action_approve(self):
        self.write({'state': 'approved'})
    
    def action_reject(self):
        self.write({'state': 'rejected'})


class TPOProjectScheduleActivity(models.Model):
    _name = 'tpo.project.schedule.activity'
    _description = 'Project Schedule Activity'
    _order = 'sequence, id'

    schedule_id = fields.Many2one('tpo.project.schedule', string='Schedule', required=True, ondelete='cascade')
    sequence = fields.Integer(string='Sequence', default=10)
    
    name = fields.Char(string='Activity Name', required=True)
    description = fields.Text(string='Description')
    
    planned_start_date = fields.Date(string='Planned Start Date')
    planned_end_date = fields.Date(string='Planned End Date')
    actual_start_date = fields.Date(string='Actual Start Date')
    actual_end_date = fields.Date(string='Actual End Date')
    
    duration = fields.Float(string='Duration (Days)', compute='_compute_duration', store=True)
    progress = fields.Float(string='Progress (%)', default=0.0)
    
    predecessor_ids = fields.Many2many('tpo.project.schedule.activity', 
                                       'schedule_activity_predecessor_rel',
                                       'activity_id', 'predecessor_id',
                                       string='Predecessors')
    
    is_critical = fields.Boolean(string='Critical Path', default=False)
    
    @api.depends('planned_start_date', 'planned_end_date')
    def _compute_duration(self):
        for record in self:
            if record.planned_start_date and record.planned_end_date:
                delta = record.planned_end_date - record.planned_start_date
                record.duration = delta.days + 1
            else:
                record.duration = 0.0


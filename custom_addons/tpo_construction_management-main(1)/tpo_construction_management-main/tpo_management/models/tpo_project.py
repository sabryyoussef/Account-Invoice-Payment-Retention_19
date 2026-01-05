# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class TPOProject(models.Model):
    _name = 'tpo.project'
    _inherit = ['mail.thread']
    _description = 'TPO Project'
    _order = 'name'

    name = fields.Char(string='Project Name', required=True, tracking=True)
    code = fields.Char(string='Project Code', required=True, tracking=True, copy=False)
    partner_id = fields.Many2one('res.partner', string='Client', required=True, tracking=True)
    project_id = fields.Many2one('project.project', string='Related Project', tracking=True)
    
    # Document counts
    boq_count = fields.Integer(string='BOQ Count', compute='_compute_document_counts')
    shop_drawing_count = fields.Integer(string='Shop Drawings Count', compute='_compute_document_counts')
    rfi_count = fields.Integer(string='RFI Count', compute='_compute_document_counts')
    itr_count = fields.Integer(string='ITR Count', compute='_compute_document_counts')
    change_order_count = fields.Integer(string='Change Orders Count', compute='_compute_document_counts')
    payment_application_count = fields.Integer(string='Payment Applications Count', compute='_compute_document_counts')
    
    # Project phases
    phase = fields.Selection([
        ('pre_execution', 'Pre-Execution & Planning'),
        ('execution', 'Execution & Monitoring'),
        ('financial', 'Financial & Closure'),
        ('closed', 'Closed'),
    ], string='Current Phase', default='pre_execution', tracking=True)
    
    # Dates
    start_date = fields.Date(string='Start Date', tracking=True)
    end_date = fields.Date(string='End Date', tracking=True)
    handover_date = fields.Date(string='Handover Date', tracking=True)
    
    # Team
    project_manager_id = fields.Many2one('res.users', string='Project Manager', tracking=True)
    technical_office_engineer_id = fields.Many2one('res.users', string='Technical Office Engineer', tracking=True)
    site_engineer_id = fields.Many2one('res.users', string='Site Engineer', tracking=True)
    document_controller_id = fields.Many2one('res.users', string='Document Controller', tracking=True)
    
    # Document Control
    document_control_code = fields.Char(string='Document Control Code', help='Standard naming convention prefix')
    
    active = fields.Boolean(string='Active', default=True)
    
    @api.depends('boq_ids', 'shop_drawing_ids', 'rfi_ids', 'itr_ids', 'change_order_ids', 'payment_application_ids')
    def _compute_document_counts(self):
        for record in self:
            record.boq_count = len(record.boq_ids)
            record.shop_drawing_count = len(record.shop_drawing_ids)
            record.rfi_count = len(record.rfi_ids)
            record.itr_count = len(record.itr_ids)
            record.change_order_count = len(record.change_order_ids)
            record.payment_application_count = len(record.payment_application_ids)
    
    # Relations
    boq_ids = fields.One2many('tpo.boq', 'project_id', string='BOQs')
    shop_drawing_ids = fields.One2many('tpo.shop.drawing', 'project_id', string='Shop Drawings')
    rfi_ids = fields.One2many('tpo.rfi', 'project_id', string='RFIs')
    itr_ids = fields.One2many('tpo.itr', 'project_id', string='ITRs')
    change_order_ids = fields.One2many('tpo.change.order', 'project_id', string='Change Orders')
    payment_application_ids = fields.One2many('tpo.payment.application', 'project_id', string='Payment Applications')
    
    @api.model
    def create(self, vals):
        if not vals.get('code'):
            # Create sequence if not exists
            sequence = self.env['ir.sequence'].search([('code', '=', 'tpo.project')], limit=1)
            if not sequence:
                sequence = self.env['ir.sequence'].create({
                    'name': 'TPO Project Sequence',
                    'code': 'tpo.project',
                    'prefix': 'TPO-',
                    'padding': 4,
                    'number_increment': 1,
                    'number_next': 1,
                })
            vals['code'] = sequence.next_by_id() or _('New')
        return super(TPOProject, self).create(vals)
    
    def name_get(self):
        result = []
        for record in self:
            name = f"[{record.code}] {record.name}"
            result.append((record.id, name))
        return result


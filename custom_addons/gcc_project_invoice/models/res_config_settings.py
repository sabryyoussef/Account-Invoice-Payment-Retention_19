# -*- coding: utf-8 -*-

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    advance_received_account_id = fields.Many2one(
        "account.account",
        related="company_id.advance_received_account_id",
        readonly=False,
        string="Advance Received From Customers",
    )
    retention_receivable_account_id = fields.Many2one(
        "account.account",
        related="company_id.retention_receivable_account_id",
        readonly=False,
        string="Retention Receivable (10%)",
    )
    performance_bond_receivable_account_id = fields.Many2one(
        "account.account",
        related="company_id.performance_bond_receivable_account_id",
        readonly=False,
        string="Performance Bonds Receivable",
    )
    deduction_account_id = fields.Many2one(
        "account.account",
        related="company_id.deduction_account_id",
        readonly=False,
        string="Deduction Against Invoice",
    )

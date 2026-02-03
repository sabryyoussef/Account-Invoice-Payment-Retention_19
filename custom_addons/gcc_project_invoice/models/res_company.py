# -*- coding: utf-8 -*-

from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    advance_received_account_id = fields.Many2one(
        "account.account",
        string="Advance Received From Customers",
        domain="[('company_id', '=', id)]",
        help="Liability account for customer advances. Debited when applying advance deduction on invoice.",
    )
    retention_receivable_account_id = fields.Many2one(
        "account.account",
        string="Retention Receivable (e.g. 10%)",
        domain="[('company_id', '=', id)]",
        help="Asset account for retention amounts (collected later).",
    )
    performance_bond_receivable_account_id = fields.Many2one(
        "account.account",
        string="Performance Bonds Receivable",
        domain="[('company_id', '=', id)]",
        help="Asset account for performance bond amounts.",
    )
    deduction_account_id = fields.Many2one(
        "account.account",
        string="Deduction Against Invoice (Penalties)",
        domain="[('company_id', '=', id)]",
        help="Expense or contra-revenue account for penalties & deductions.",
    )

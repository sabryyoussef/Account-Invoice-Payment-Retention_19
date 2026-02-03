# -*- coding: utf-8 -*-

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class AccountMove(models.Model):
    _inherit = "account.move"

    # --- References ---
    contract_ref = fields.Char(string="Contract No")
    po_ref = fields.Char(string="PO No")
    invoice_ref = fields.Char(string="Inv Ref")
    covered_period = fields.Char(string="Covered Period")

    # --- Deduction inputs (monetary, company currency for storage; use currency_id for display) ---
    advance_payment_deduction = fields.Monetary(
        string="Advance Payment Deduction",
        currency_field="company_currency_id",
        default=0.0,
    )
    penalties_deductions = fields.Monetary(
        string="Penalties & Deductions",
        currency_field="company_currency_id",
        default=0.0,
    )
    performance_bond_amount = fields.Monetary(
        string="Performance Bond",
        currency_field="company_currency_id",
        default=0.0,
    )
    retention_percent = fields.Float(
        string="Retention %",
        default=0.0,
    )
    retention_amount = fields.Monetary(
        string="Retention Amount",
        currency_field="company_currency_id",
        compute="_compute_retention_amount",
        store=True,
        readonly=False,
    )

    # --- Computed (for display and journal logic) ---
    gross_untaxed = fields.Monetary(
        string="Gross (Untaxed)",
        currency_field="company_currency_id",
        compute="_compute_deduction_totals",
        store=True,
    )
    deductions_total = fields.Monetary(
        string="Total Deductions (Advance+Penalties+Bond)",
        currency_field="company_currency_id",
        compute="_compute_deduction_totals",
        store=True,
    )
    tax_base_after_deductions = fields.Monetary(
        string="Tax Base After Deductions",
        currency_field="company_currency_id",
        compute="_compute_deduction_totals",
        store=True,
    )
    net_collect_now = fields.Monetary(
        string="Net Collect Now",
        currency_field="company_currency_id",
        compute="_compute_deduction_totals",
        store=True,
    )

    @api.depends(
        "invoice_line_ids",
        "invoice_line_ids.price_subtotal",
        "advance_payment_deduction",
        "penalties_deductions",
        "performance_bond_amount",
        "retention_percent",
        "retention_amount",
        "amount_total",
    )
    def _compute_deduction_totals(self):
        for move in self:
            if move.move_type != "out_invoice":
                move.gross_untaxed = 0
                move.deductions_total = 0
                move.tax_base_after_deductions = 0
                move.net_collect_now = move.amount_total or 0
                continue
            gross = move.amount_untaxed_signed or 0
            adv = move.advance_payment_deduction or 0
            pen = move.penalties_deductions or 0
            bond = move.performance_bond_amount or 0
            deductions_total = adv + pen + bond
            tax_base = gross - deductions_total
            retention = move.retention_amount or 0
            move.gross_untaxed = gross
            move.deductions_total = deductions_total
            move.tax_base_after_deductions = tax_base
            # Net collect = total - retention - advance - penalties - bond (what customer pays now)
            move.net_collect_now = (move.amount_total_signed or 0) - retention - adv - pen - bond

    @api.depends("tax_base_after_deductions", "retention_percent")
    def _compute_retention_amount(self):
        for move in self:
            if move.move_type != "out_invoice":
                move.retention_amount = 0
                continue
            if not move.retention_percent:
                move.retention_amount = 0
                continue
            base = move.tax_base_after_deductions or 0
            move.retention_amount = move.currency_id.round(base * (move.retention_percent / 100.0))

    @api.constrains("advance_payment_deduction", "penalties_deductions", "performance_bond_amount", "retention_amount")
    def _check_deductions_non_negative(self):
        for move in self:
            if move.move_type != "out_invoice":
                continue
            if (move.advance_payment_deduction or 0) < 0:
                raise ValidationError("Advance Payment Deduction cannot be negative.")
            if (move.penalties_deductions or 0) < 0:
                raise ValidationError("Penalties & Deductions cannot be negative.")
            if (move.performance_bond_amount or 0) < 0:
                raise ValidationError("Performance Bond cannot be negative.")
            if (move.retention_amount or 0) < 0:
                raise ValidationError("Retention Amount cannot be negative.")

    @api.constrains("advance_payment_deduction", "penalties_deductions", "performance_bond_amount", "retention_amount", "amount_total")
    def _check_deductions_not_exceed_total(self):
        for move in self:
            if move.move_type != "out_invoice" or not move.amount_total:
                continue
            total = abs(move.amount_total_signed or 0)
            reduce_total = (move.advance_payment_deduction or 0) + (move.penalties_deductions or 0) + (move.performance_bond_amount or 0) + (move.retention_amount or 0)
            if reduce_total > total:
                raise ValidationError(
                    "Sum of deductions (advance + penalties + performance bond + retention) cannot exceed invoice total."
                )

    def _get_deduction_amounts(self):
        """Return amounts in company currency for journal lines. Only for out_invoice with deductions."""
        self.ensure_one()
        if self.move_type != "out_invoice":
            return None
        adv = self.advance_payment_deduction or 0
        pen = self.penalties_deductions or 0
        bond = self.performance_bond_amount or 0
        ret = self.retention_amount or 0
        if adv == 0 and pen == 0 and bond == 0 and ret == 0:
            return None
        # Convert to company currency if invoice is in other currency
        company_currency = self.company_id.currency_id
        if self.currency_id != company_currency:
            date = self.invoice_date or self.date
            adv = self.currency_id._convert(adv, company_currency, self.company_id, date)
            pen = self.currency_id._convert(pen, company_currency, self.company_id, date)
            bond = self.currency_id._convert(bond, company_currency, self.company_id, date)
            ret = self.currency_id._convert(ret, company_currency, self.company_id, date)
        return {"advance": adv, "penalties": pen, "performance_bond": bond, "retention": ret}

    def _validate_deduction_accounts(self):
        """Block posting if any deduction amount > 0 but corresponding account not set."""
        self.ensure_one()
        amounts = self._get_deduction_amounts()
        if not amounts:
            return
        company = self.company_id
        if amounts["advance"] > 0 and not company.advance_received_account_id:
            raise ValidationError(
                "Advance Payment Deduction is set but company has no 'Advance Received From Customers' account. "
                "Configure it in Accounting Settings."
            )
        if amounts["penalties"] > 0 and not company.deduction_account_id:
            raise ValidationError(
                "Penalties & Deductions is set but company has no 'Deduction Against Invoice' account. "
                "Configure it in Accounting Settings."
            )
        if amounts["performance_bond"] > 0 and not company.performance_bond_receivable_account_id:
            raise ValidationError(
                "Performance Bond is set but company has no 'Performance Bonds Receivable' account. "
                "Configure it in Accounting Settings."
            )
        if amounts["retention"] > 0 and not company.retention_receivable_account_id:
            raise ValidationError(
                "Retention is set but company has no 'Retention Receivable' account. "
                "Configure it in Accounting Settings."
            )

    def _create_deduction_move_lines(self):
        """
        After Odoo has created standard lines (A/R debit, revenue+VAT credit), add adjustment lines:
        - Debit Retention receivable / Credit A/R
        - Debit Performance bond receivable / Credit A/R
        - Debit Advance received / Credit A/R
        - Debit Deduction (expense) / Credit A/R
        So final A/R = amount_total - retention - bond - advance - penalties = net_collect_now.
        """
        for move in self:
            if move.move_type != "out_invoice" or move.state != "posted":
                continue
            amounts = move._get_deduction_amounts()
            if not amounts:
                continue

            company = move.company_id
            partner = move.partner_id
            company_currency = company.currency_id

            # Find the receivable line (the one with receivable account, same partner)
            receivable_line = None
            for line in move.line_ids:
                # Odoo 16+: account_type; older: user_type_id.type
                atype = getattr(line.account_id, "account_type", None)
                if not atype and hasattr(line.account_id, "user_type_id"):
                    atype = getattr(line.account_id.user_type_id, "type", None)
                if atype in ("asset_receivable", "receivable") and line.partner_id == partner:
                    receivable_line = line
                    break
            if not receivable_line:
                continue

            receivable_account = receivable_line.account_id
            date = move.date
            ref = move.ref or move.name or ""

            lines_vals = []

            # 1. Retention: Dr Retention receivable, Cr A/R
            if amounts["retention"] > 0:
                lines_vals.append({
                    "name": _("Retention (%.2f%%)") % (move.retention_percent or 0),
                    "account_id": company.retention_receivable_account_id.id,
                    "partner_id": partner.id,
                    "debit": amounts["retention"],
                    "credit": 0,
                    "move_id": move.id,
                    "date": date,
                    "ref": ref,
                })
                lines_vals.append({
                    "name": _("Retention (%.2f%%)") % (move.retention_percent or 0),
                    "account_id": receivable_account.id,
                    "partner_id": partner.id,
                    "debit": 0,
                    "credit": amounts["retention"],
                    "move_id": move.id,
                    "date": date,
                    "ref": ref,
                })

            # 2. Performance bond: Dr Performance bond receivable, Cr A/R
            if amounts["performance_bond"] > 0:
                lines_vals.append({
                    "name": _("Performance Bond"),
                    "account_id": company.performance_bond_receivable_account_id.id,
                    "partner_id": partner.id,
                    "debit": amounts["performance_bond"],
                    "credit": 0,
                    "move_id": move.id,
                    "date": date,
                    "ref": ref,
                })
                lines_vals.append({
                    "name": _("Performance Bond"),
                    "account_id": receivable_account.id,
                    "partner_id": partner.id,
                    "debit": 0,
                    "credit": amounts["performance_bond"],
                    "move_id": move.id,
                    "date": date,
                    "ref": ref,
                })

            # 3. Advance deduction: Dr Advance received (reduce liability), Cr A/R
            if amounts["advance"] > 0:
                lines_vals.append({
                    "name": _("Advance Payment Deduction"),
                    "account_id": company.advance_received_account_id.id,
                    "partner_id": partner.id,
                    "debit": amounts["advance"],
                    "credit": 0,
                    "move_id": move.id,
                    "date": date,
                    "ref": ref,
                })
                lines_vals.append({
                    "name": _("Advance Payment Deduction"),
                    "account_id": receivable_account.id,
                    "partner_id": partner.id,
                    "debit": 0,
                    "credit": amounts["advance"],
                    "move_id": move.id,
                    "date": date,
                    "ref": ref,
                })

            # 4. Penalties: Dr Deduction account, Cr A/R
            if amounts["penalties"] > 0:
                lines_vals.append({
                    "name": _("Penalties & Deductions"),
                    "account_id": company.deduction_account_id.id,
                    "partner_id": partner.id,
                    "debit": amounts["penalties"],
                    "credit": 0,
                    "move_id": move.id,
                    "date": date,
                    "ref": ref,
                })
                lines_vals.append({
                    "name": _("Penalties & Deductions"),
                    "account_id": receivable_account.id,
                    "partner_id": partner.id,
                    "debit": 0,
                    "credit": amounts["penalties"],
                    "move_id": move.id,
                    "date": date,
                    "ref": ref,
                })

            if lines_vals:
                self.env["account.move.line"].create(lines_vals)

    def _post(self, soft=True):
        # Validate accounts before posting
        for move in self:
            if move.move_type == "out_invoice":
                move._validate_deduction_accounts()
        res = super()._post(soft=soft)
        # After standard lines exist, add deduction lines
        self._create_deduction_move_lines()
        return res

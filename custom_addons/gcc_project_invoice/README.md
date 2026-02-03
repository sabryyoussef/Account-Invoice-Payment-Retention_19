# GCC Project Invoice (Odoo 19)

Module for project invoicing with **advance payment deduction**, **retention**, **performance bond**, and **penalties & deductions**. Implements the "receivable split" pattern: one customer invoice produces one journal entry with extra lines that move part of receivable into retention receivable, performance bond receivable, advance (liability reduction), and deduction (expense).

## Features

- **Contract/PO/Inv ref** on customer invoices
- **Advance Payment Deduction** — reduces receivable and debits "Advance Received From Customers"
- **Penalties & Deductions** — debits deduction (expense) account, credits A/R
- **Performance Bond** — debits performance bond receivable, credits A/R
- **Retention %** — computed retention amount; debits retention receivable, credits A/R
- **Company settings** for the four deduction accounts (Accounting → Settings)

## Installation

1. Copy `gcc_project_invoice` into your Odoo 19 addons path.
2. Restart Odoo, then Apps → Update Apps List.
3. Install "GCC Project Invoice (Advance, Retention, Deductions)".

## Configuration

1. Go to **Accounting → Configuration → Settings**.
2. In **GCC Project Invoice**, set:
   - **Advance Received From Customers** (liability account)
   - **Retention Receivable** (asset)
   - **Performance Bonds Receivable** (asset)
   - **Deduction Against Invoice** (expense)
3. Create these accounts in your Chart of Accounts if they don't exist.

## Usage

1. Create a **Customer Invoice** (out_invoice).
2. Fill lines and totals as usual.
3. In **Project / Deductions**:
   - Optionally set Contract No, PO No, Inv Ref.
   - Set **Advance Payment Deduction**, **Penalties & Deductions**, **Performance Bond** as needed.
   - Set **Retention %**; **Retention Amount** is computed from (Gross − deductions).
4. **Confirm** and **Post** the invoice.
5. The module adds extra move lines after Odoo's standard lines so that:
   - Final A/R = amount customer pays now (total − retention − advance − penalties − bond).
   - Retention, bond, advance, and penalties are posted to the configured accounts.

## Testing (from advanced_plan.md)

**Test A:** Invoice untaxed 10,000, VAT 15% = 1,500, Total 11,500. Advance 2,000, Penalties 100, Retention 10% of (10,000 − 2,000 − 100) = 790. After post: A/R = 8,610; retention account debit 790; advance liability reduced 2,000.

**Test B (EXPLAINED flow):** Record advance 100,000 (manual entry: Dr Bank, Cr Advance Received). Invoice 1 deduct 50,000, Invoice 2 deduct 50,000. Advance liability becomes 0 after second invoice.

## Plan

Implementation follows `docs/plan/advanced_plan.md` (Steps 1–5). Report and advance wizard are deferred (Steps 7–8).

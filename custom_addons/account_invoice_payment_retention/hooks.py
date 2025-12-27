# Copyright 2020 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

_logger = logging.getLogger(__name__)


def post_init_hook(env):
    """Load demo data after module installation"""
    _logger.info("Loading Payment Retention demo data...")
    _load_demo_data(env)


def _load_demo_data(env):
    """Create demo retention accounts, configure company, and create demo partners"""
    
    company = env.company
    
    # Check if retention accounts already exist
    retention_payable = env['account.account'].search([
        ('code', '=', '241000'),
    ], limit=1)
    
    retention_receivable = env['account.account'].search([
        ('code', '=', '141000'),
    ], limit=1)
    
    # Create Retention Payable Account if not exists
    if not retention_payable:
        retention_payable = env['account.account'].create({
            'code': '241000',
            'name': 'Retention Payable',
            'account_type': 'liability_current',
            'reconcile': True,
        })
        _logger.info("Created Retention Payable Account: %s", retention_payable.code)
    
    # Create Retention Receivable Account if not exists
    if not retention_receivable:
        retention_receivable = env['account.account'].create({
            'code': '141000',
            'name': 'Retention Receivable',
            'account_type': 'asset_current',
            'reconcile': True,
        })
        _logger.info("Created Retention Receivable Account: %s", retention_receivable.code)
    
    # Configure company with retention accounts
    company.write({
        'retention_account_id': retention_payable.id,
        'retention_receivable_account_id': retention_receivable.id,
        'retention_method': 'untax',
    })
    _logger.info("Configured company retention settings")
    
    # Add admin user to retention group
    retention_group = env.ref('account_invoice_payment_retention.group_payment_retention', raise_if_not_found=False)
    if retention_group:
        admin_user = env.ref('base.user_admin', raise_if_not_found=False)
        if admin_user and retention_group not in admin_user.groups_id:
            admin_user.write({'groups_id': [(4, retention_group.id)]})
            _logger.info("Added admin user to retention group")
    
    # Create demo partners if they don't exist
    _create_demo_partners(env)
    
    # Create demo invoices
    _create_demo_invoices(env, retention_payable, retention_receivable)
    
    _logger.info("Payment Retention demo data loaded successfully!")


def _create_demo_partners(env):
    """Create demo partners for retention scenarios"""
    
    partners_data = [
        {
            'name': 'ABC Construction Ltd',
            'email': 'abc.construction@example.com',
            'phone': '+1 555-0101',
            'company_type': 'company',
        },
        {
            'name': 'XYZ Engineering Corp',
            'email': 'xyz.engineering@example.com',
            'phone': '+1 555-0102',
            'company_type': 'company',
        },
        {
            'name': 'Global Materials Supplier',
            'email': 'global.materials@example.com',
            'phone': '+1 555-0201',
            'company_type': 'company',
        },
        {
            'name': 'Professional Services Inc',
            'email': 'pro.services@example.com',
            'phone': '+1 555-0202',
            'company_type': 'company',
        },
    ]
    
    for partner_data in partners_data:
        existing = env['res.partner'].search([('email', '=', partner_data['email'])], limit=1)
        if not existing:
            env['res.partner'].create(partner_data)
            _logger.info("Created demo partner: %s", partner_data['name'])


def _create_demo_invoices(env, retention_payable, retention_receivable):
    """Create demo invoices and bills with various retention scenarios"""
    
    # Get demo partners
    customer1 = env['res.partner'].search([('email', '=', 'abc.construction@example.com')], limit=1)
    customer2 = env['res.partner'].search([('email', '=', 'xyz.engineering@example.com')], limit=1)
    vendor1 = env['res.partner'].search([('email', '=', 'global.materials@example.com')], limit=1)
    vendor2 = env['res.partner'].search([('email', '=', 'pro.services@example.com')], limit=1)
    
    if not all([customer1, customer2, vendor1, vendor2]):
        _logger.warning("Demo partners not found, skipping invoice creation")
        return
    
    # Get default accounts
    income_account = env['account.account'].search([
        ('account_type', '=', 'income'),
    ], limit=1)
    
    expense_account = env['account.account'].search([
        ('account_type', '=', 'expense'),
    ], limit=1)
    
    if not income_account or not expense_account:
        _logger.warning("Income/Expense accounts not found, skipping invoice creation")
        return
    
    # Customer Invoice Scenarios
    invoices_data = [
        # Scenario 1: Customer Invoice - 10% Retention (Percent, Untaxed)
        {
            'move_type': 'out_invoice',
            'partner_id': customer1.id,
            'payment_retention': 'percent',
            'retention_method': 'untax',
            'amount_retention': 10.0,
            'invoice_line_ids': [(0, 0, {
                'name': 'Construction Project Phase 1 - 10% Retention',
                'quantity': 1,
                'price_unit': 10000.00,
                'account_id': income_account.id,
            })],
        },
        # Scenario 2: Customer Invoice - 5% Retention (Percent, Total)
        {
            'move_type': 'out_invoice',
            'partner_id': customer2.id,
            'payment_retention': 'percent',
            'retention_method': 'total',
            'amount_retention': 5.0,
            'invoice_line_ids': [(0, 0, {
                'name': 'Engineering Design Services - 5% Retention (Total)',
                'quantity': 4,
                'price_unit': 2500.00,
                'account_id': income_account.id,
            })],
        },
        # Scenario 3: Customer Invoice - Fixed $500 Retention
        {
            'move_type': 'out_invoice',
            'partner_id': customer1.id,
            'payment_retention': 'amount',
            'amount_retention': 500.0,
            'invoice_line_ids': [(0, 0, {
                'name': 'Construction Project Phase 2 - Fixed $500 Retention',
                'quantity': 1,
                'price_unit': 5000.00,
                'account_id': income_account.id,
            })],
        },
        # Scenario 4: Customer Invoice - No Retention
        {
            'move_type': 'out_invoice',
            'partner_id': customer2.id,
            'invoice_line_ids': [(0, 0, {
                'name': 'Quick Consulting Service - No Retention',
                'quantity': 2,
                'price_unit': 800.00,
                'account_id': income_account.id,
            })],
        },
        # Scenario 5: Vendor Bill - 10% Retention (Percent, Untaxed)
        {
            'move_type': 'in_invoice',
            'partner_id': vendor1.id,
            'payment_retention': 'percent',
            'retention_method': 'untax',
            'amount_retention': 10.0,
            'invoice_line_ids': [(0, 0, {
                'name': 'Bulk Building Materials - 10% Retention',
                'quantity': 20,
                'price_unit': 1500.00,
                'account_id': expense_account.id,
            })],
        },
        # Scenario 6: Vendor Bill - Fixed $1000 Retention
        {
            'move_type': 'in_invoice',
            'partner_id': vendor2.id,
            'payment_retention': 'amount',
            'amount_retention': 1000.0,
            'invoice_line_ids': [(0, 0, {
                'name': 'Professional Consulting Contract - Fixed $1000 Retention',
                'quantity': 1,
                'price_unit': 15000.00,
                'account_id': expense_account.id,
            })],
        },
        # Scenario 7: Vendor Bill - 8% Retention (Multi-line)
        {
            'move_type': 'in_invoice',
            'partner_id': vendor1.id,
            'payment_retention': 'percent',
            'retention_method': 'untax',
            'amount_retention': 8.0,
            'invoice_line_ids': [
                (0, 0, {
                    'name': 'IT Infrastructure Setup - 8% Retention',
                    'quantity': 5,
                    'price_unit': 2000.00,
                    'account_id': expense_account.id,
                }),
                (0, 0, {
                    'name': 'Annual Maintenance Contract',
                    'quantity': 1,
                    'price_unit': 5000.00,
                    'account_id': expense_account.id,
                }),
            ],
        },
        # Scenario 8: Vendor Bill - No Retention
        {
            'move_type': 'in_invoice',
            'partner_id': vendor2.id,
            'invoice_line_ids': [(0, 0, {
                'name': 'Office Supplies - No Retention',
                'quantity': 10,
                'price_unit': 100.00,
                'account_id': expense_account.id,
            })],
        },
    ]
    
    for invoice_data in invoices_data:
        try:
            invoice = env['account.move'].create(invoice_data)
            _logger.info("Created demo %s: %s (Retention: %s)", 
                        'Invoice' if invoice_data['move_type'] == 'out_invoice' else 'Bill',
                        invoice.name or 'Draft',
                        invoice_data.get('payment_retention', 'None'))
        except Exception as e:
            _logger.warning("Failed to create demo invoice: %s", str(e))

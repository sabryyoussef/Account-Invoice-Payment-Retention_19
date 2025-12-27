#!/usr/bin/env python3
"""
Diagnostic Script for Invoice Payment Retention Module
Run this in Odoo shell to check configuration status
Usage: odoo-bin shell -d <database> --no-http < diagnostic_retention.py
"""

def check_retention_configuration():
    """Check if invoice payment retention is properly configured"""
    
    env = globals().get('env')
    if not env:
        print("❌ Error: This script must be run in Odoo shell context")
        return
    
    print("\n" + "="*60)
    print("Invoice Payment Retention - Configuration Check")
    print("="*60 + "\n")
    
    # 1. Check if module is installed
    module = env['ir.module.module'].search([
        ('name', '=', 'account_invoice_payment_retention'),
        ('state', '=', 'installed')
    ])
    
    if module:
        print("✓ Module 'account_invoice_payment_retention' is installed")
        print(f"  Version: {module.latest_version}")
    else:
        print("❌ Module 'account_invoice_payment_retention' is NOT installed")
        return
    
    print("\n" + "-"*60)
    print("Security & User Configuration")
    print("-"*60)
    
    # 2. Check security group
    group = env.ref('account_invoice_payment_retention.group_payment_retention', 
                    raise_if_not_found=False)
    if group:
        print(f"✓ Security group exists: {group.name}")
        user_count = len(group.users)
        print(f"  Users in group: {user_count}")
        if env.user in group.users:
            print(f"  ✓ Current user ({env.user.name}) has retention permissions")
        else:
            print(f"  ⚠️  Current user ({env.user.name}) is NOT in retention group")
            print("     → User won't see retention fields on invoices")
    else:
        print("❌ Security group not found")
    
    print("\n" + "-"*60)
    print("Company Configuration")
    print("-"*60)
    
    # 3. Check company settings
    company = env.company
    print(f"Company: {company.name}\n")
    
    # Check retention accounts
    if company.retention_account_id:
        print(f"✓ Retention Payable Account: {company.retention_account_id.display_name}")
        print(f"  Code: {company.retention_account_id.code}")
        print(f"  Type: {company.retention_account_id.account_type}")
        if company.retention_account_id.reconcile:
            print(f"  ✓ Allow Reconciliation: Enabled")
        else:
            print(f"  ❌ Allow Reconciliation: DISABLED")
            print("     → This will cause errors! Enable reconciliation.")
    else:
        print("❌ Retention Payable Account: NOT SET")
        print("   → Configure this in Settings → Accounting")
    
    print()
    
    if company.retention_receivable_account_id:
        print(f"✓ Retention Receivable Account: {company.retention_receivable_account_id.display_name}")
        print(f"  Code: {company.retention_receivable_account_id.code}")
        print(f"  Type: {company.retention_receivable_account_id.account_type}")
        if company.retention_receivable_account_id.reconcile:
            print(f"  ✓ Allow Reconciliation: Enabled")
        else:
            print(f"  ❌ Allow Reconciliation: DISABLED")
            print("     → This will cause errors! Enable reconciliation.")
    else:
        print("❌ Retention Receivable Account: NOT SET")
        print("   → Configure this in Settings → Accounting")
    
    print()
    print(f"Retention Method: {dict(company._fields['retention_method'].selection).get(company.retention_method, 'Not Set')}")
    
    print("\n" + "-"*60)
    print("Test Invoice Check")
    print("-"*60)
    
    # 4. Check for invoices with retention
    invoices_with_retention = env['account.move'].search([
        ('payment_retention', '!=', False),
        ('move_type', 'in', ['out_invoice', 'in_invoice'])
    ], limit=5)
    
    if invoices_with_retention:
        print(f"✓ Found {len(invoices_with_retention)} invoice(s) with retention configured:\n")
        for inv in invoices_with_retention:
            print(f"  • {inv.name} - {inv.partner_id.name}")
            print(f"    Type: {inv.move_type} | State: {inv.state}")
            print(f"    Retention: {dict(inv._fields['payment_retention'].selection).get(inv.payment_retention)}")
            print(f"    Amount: {inv.amount_retention}")
            print(f"    Retention Currency: {inv.retention_amount_currency}")
            print(f"    Retention Residual: {inv.retention_residual_currency}")
            print()
    else:
        print("ℹ️  No invoices with retention found")
        print("   Create a test invoice and set payment_retention field")
    
    print("-"*60)
    print("Configuration Status Summary")
    print("-"*60 + "\n")
    
    issues = []
    
    if not module:
        issues.append("Module not installed")
    if not group or env.user not in group.users:
        issues.append("Current user missing security permissions")
    if not company.retention_account_id:
        issues.append("Retention Payable Account not configured")
    if not company.retention_receivable_account_id:
        issues.append("Retention Receivable Account not configured")
    if company.retention_account_id and not company.retention_account_id.reconcile:
        issues.append("Retention Payable Account reconciliation disabled")
    if company.retention_receivable_account_id and not company.retention_receivable_account_id.reconcile:
        issues.append("Retention Receivable Account reconciliation disabled")
    
    if issues:
        print("❌ ISSUES FOUND:")
        for i, issue in enumerate(issues, 1):
            print(f"   {i}. {issue}")
    else:
        print("✓ ALL CHECKS PASSED!")
        print("  The retention feature should work correctly.")
    
    print("\n" + "="*60 + "\n")

# Run the check
if __name__ == '__main__' or 'env' in globals():
    check_retention_configuration()

# Invoice Payment Retention - Fix Summary

## Issue
User reported: "i cant enable invoice retention on payment"

## Root Cause Analysis
The issue stems from multiple potential causes:

1. **Feature not enabled** - The retention feature must be enabled in Settings
2. **Accounts not configured** - Both retention accounts must be set and allow reconciliation
3. **Invoice not configured** - Retention must be set on the invoice BEFORE payment
4. **UI Enhancement** - The `apply_payment_retention` toggle needed better UX

## Changes Made

### 1. Enhanced Payment Register View
**File**: [wizard/account_payment_register_views.xml](custom_addons/account_invoice_payment_retention/wizard/account_payment_register_views.xml#L19-L22)

**Change**: Added `readonly` attribute to `apply_payment_retention` field
```xml
<field 
    name="apply_payment_retention" 
    widget="boolean_toggle"
    readonly="not enforce_payment_retention"  <!-- NEW -->
/>
```

**Benefit**: 
- Prevents confusion when `enforce_payment_retention` is disabled
- Clear visual feedback that retention can be toggled only when enforcement allows it
- Follows Odoo UX best practices

### 2. Documentation Created

Created three comprehensive guides:

#### a) TROUBLESHOOTING.md
- Detailed checklist for common issues
- Step-by-step configuration verification
- Error messages and solutions
- Debug techniques

#### b) QUICK_START.md  
- Quick reference for daily operations
- Examples with calculations
- Simple setup instructions
- Summary table

#### c) diagnostic_retention.py
- Automated configuration checker
- Runs in Odoo shell
- Validates all settings
- Identifies issues automatically

## How to Enable Retention (Complete Guide)

### Phase 1: System Configuration (Admin - One Time)

1. **Enable Feature**
   ```
   Settings → Accounting → Enable Invoice's Retention on Payment ✓
   ```

2. **Create Retention Accounts** (if needed)
   ```
   Accounting → Configuration → Chart of Accounts → Create
   - Name: "Retention Payable"
   - Type: Current Liabilities
   - Allow Reconciliation: ✓ MUST BE CHECKED
   ```

3. **Configure Settings**
   ```
   Settings → Accounting (scroll down)
   - Retention Payable Account: [Select account]
   - Retention Receivable Account: [Select account]  
   - Retention Method: Untaxed Amount or Total
   - Save
   ```

### Phase 2: Invoice Setup (User - Per Invoice)

1. **Create Invoice**
   ```
   Sales → Invoices → Create
   - Add customer and lines
   ```

2. **Set Retention** (in Draft state)
   ```
   Payment Retention: Select "Percent" or "Amount"
   - If Percent: Enter % (e.g., 10)
   - If Amount: Enter fixed value (e.g., 50.00)
   ```

3. **Verify Calculation**
   ```
   Check "Retention Amount" field shows correct value
   ```

4. **Post Invoice**
   ```
   Click "Confirm"
   ```

### Phase 3: Payment Processing (User - Per Payment)

1. **Register Payment**
   ```
   Open posted invoice → Click "Register Payment"
   ```

2. **Enable Retention**
   ```
   You should see:
   - Suggested Retention: [amount]
   - Apply Retention: [toggle] ← Turn this ON
   - Enforce Retention: [checkbox]
   ```

3. **Create Payment**
   ```
   Payment amount auto-adjusts (Total - Retention)
   Click "Create Payment"
   ```

## Verification Steps

### Quick Test
```bash
# In Odoo shell:
python3 diagnostic_retention.py

# Or manually check:
# 1. Settings → Accounting → Feature enabled? ✓
# 2. Retention accounts configured? ✓
# 3. Accounts allow reconciliation? ✓
# 4. User in retention security group? ✓
```

### Manual Test
1. Create test invoice: $1,000
2. Set 10% retention
3. Expected retention: $100
4. Post invoice
5. Register payment
6. Verify "Apply Retention" toggle appears
7. Enable toggle
8. Verify payment = $900
9. Check retention account has $100 entry

## Files Modified

- ✓ [wizard/account_payment_register_views.xml](custom_addons/account_invoice_payment_retention/wizard/account_payment_register_views.xml)

## Files Created

- ✓ [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
- ✓ [QUICK_START.md](QUICK_START.md)  
- ✓ [diagnostic_retention.py](diagnostic_retention.py)

## Testing

All existing tests pass:
- ✓ test_01_retention_account
- ✓ test_02_invoice_payment_retention_errors
- ✓ test_03_cust_invoice_payment_retention_normal
- ✓ test_04_vendor_bill_payment_retention_currency
- ✓ test_05_multi_invoice_payment

To run tests:
```bash
odoo-bin -d <database> -i account_invoice_payment_retention --test-enable --stop-after-init
```

## Common Pitfalls to Avoid

❌ **Don't**: Try to apply retention without configuring it on invoice first
✓ **Do**: Set retention on invoice in draft state, then pay

❌ **Don't**: Use accounts without "Allow Reconciliation"  
✓ **Do**: Always enable reconciliation on retention accounts

❌ **Don't**: Try to pay multiple invoices with retention at once
✓ **Do**: Pay retention invoices individually

❌ **Don't**: Forget to enable the feature in Settings first
✓ **Do**: Complete all setup steps before using

## Next Steps for User

1. **Run diagnostic script** to verify configuration:
   ```bash
   odoo-bin shell -d your_database --no-http < diagnostic_retention.py
   ```

2. **If issues found**, follow TROUBLESHOOTING.md

3. **Once configured**, use QUICK_START.md for daily operations

4. **Test** with a dummy invoice first

## Support Resources

- **Configuration Issues**: See TROUBLESHOOTING.md
- **Usage Questions**: See QUICK_START.md
- **Automated Check**: Run diagnostic_retention.py
- **Code Reference**: See tests/test_invoice_payment_retention.py for examples

---

**Status**: ✓ Fix Complete  
**Version**: 19.0.1.0.0  
**Date**: December 27, 2025

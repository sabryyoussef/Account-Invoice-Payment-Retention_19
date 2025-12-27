# Troubleshooting: Invoice Retention on Payment

## Common Issues and Solutions

### ⚠️ ERROR: "Retention payable account should be set to allow Reconciliation"

**This is the #1 most common error!**

#### Why This Happens:
The retention feature requires accounts that can be reconciled (matched with payments). If the account you selected doesn't have reconciliation enabled, you'll get this error.

#### Step-by-Step Fix:

1. **Open Chart of Accounts**
   - Go to: Accounting → Configuration → Chart of Accounts

2. **Find Your Retention Account**
   - Search for the account name you selected in settings
   - Or filter by account type "Current Liabilities"

3. **Edit the Account**
   - Click on the account to open it
   - Click **Edit** (top right corner)

4. **Enable Reconciliation**
   - Scroll down to find: **"Allow Reconciliation"** checkbox
   - ✅ **CHECK this box**
   - Click **Save**

5. **Repeat for BOTH Accounts**
   - Retention Payable Account (for vendor bills)
   - Retention Receivable Account (for customer invoices)

6. **Go Back to Settings**
   - Settings → Accounting
   - Click **Save** again
   - Error should be gone!

#### Visual Guide:
```
Chart of Accounts → [Your Retention Account] → Edit

┌─────────────────────────────────────┐
│ Account Name: Retention Payable     │
│ Code: RE001                         │
│ Type: Current Liabilities           │
│                                     │
│ ✅ Allow Reconciliation  ← CHECK!   │
│                                     │
│ [Save]                              │
└─────────────────────────────────────┘
```

#### Alternative: Create New Accounts

If easier, create brand new accounts:

```
Accounting → Configuration → Chart of Accounts → Create

Account 1:
- Name: Retention Payable
- Code: RE001
- Type: Current Liabilities
- ✅ Allow Reconciliation: YES

Account 2:
- Name: Retention Receivable  
- Code: RE002
- Type: Current Liabilities
- ✅ Allow Reconciliation: YES
```

Then select these new accounts in Settings → Accounting.

---

### Issue: Cannot Enable Invoice Retention on Payment

#### Checklist:

1. **Enable the Feature First**
   - Navigate to: `Settings` (top menu) → `Accounting` (left sidebar)
   - In the **General Settings** section (top of page)
   - Look for checkbox: "Enable Invoice's Retention on Payment"
   - ✓ Check this box to enable the feature
   - Additional fields will appear below the checkbox

2. **Configure Retention Accounts** (Required!)
   - After enabling, scroll down slightly on the same page
   - You'll see two account selection fields:
     - **Retention Payable Account**: For vendor bills retention
     - **Retention Receivable Account**: For customer invoices retention
   - ⚠️ Both accounts MUST have "Allow Reconciliation" enabled
   - Click each field to select or create an account

3. **Select Retention Method**
   - On the same page, find the **Retention Method** section
   - Choose one radio button:
     - ⚪ **Untaxed Amount**: Retention from subtotal (before tax)
     - ⚪ **Total**: Retention from total amount (including tax)
   - Click **Save** button to apply all settings

4. **Set Retention on Invoice** (Before Payment!)
   - Open the invoice (must be in Draft state)
   - Find the "Payment Retention" field (appears below the Reference field)
   - Select retention type:
     - **Percent**: Enter percentage (e.g., 10 for 10%)
     - **Amount**: Enter fixed amount (e.g., 50.00)
   - The system calculates and displays "Retention Amount"
   - Post/Confirm the invoice

5. **Register Payment with Retention**
   - Open the posted invoice with retention configured
   - Click "Register Payment"
   - You should see:
     - **Suggested Retention**: Auto-calculated amount
     - **Apply Retention**: Toggle to enable/disable
     - **Enforce Retention**: Checkbox for validation
   - Toggle "Apply Retention" ON
   - Complete the payment

### Common Errors:

#### Error: "Retention account should be set to allow Reconciliation"
**Solution**: 
- Go to Accounting → Configuration → Chart of Accounts
- Find your retention accounts
- Edit each one and enable "Allow Reconciliation"

#### Error: "Retention must not exceed the total untaxed amount"
**Solution**: 
- Review your retention amount/percentage
- For percentage: Must be ≤ 100%
- For amount: Must be ≤ invoice untaxed amount

#### Error: Multi-invoice payment not allowed
**Solution**: 
- Invoices with retention must be paid individually
- You cannot select multiple invoices with retention for batch payment

### Visibility Issues:

#### Payment retention fields not visible on invoice
**Cause**: User doesn't have the required security group
**Solution**: 
- Go to Settings → Users & Companies → Users
- Edit your user
- Under "Technical Settings" → ensure you're in the group that has retention enabled

#### "Apply Retention" toggle not appearing in payment
**Causes**:
1. Invoice doesn't have retention configured
2. Retention amount is 0
3. Feature not enabled in settings

**Solution**: 
- Verify invoice has `payment_retention` field set
- Verify `retention_amount_currency` > 0
- Verify settings are properly configured

### Debug Mode:

To check current configuration, activate Debug mode and inspect:
- Invoice: Check fields `payment_retention`, `amount_retention`, `retention_amount_currency`
- Payment Register: Check `retention_amount_currency`, `apply_payment_retention`, `enforce_payment_retention`

## Feature Flow:

```
1. Settings → Enable Feature → Configure Accounts
                    ↓
2. Create/Edit Invoice → Set Payment Retention (Percent/Amount)
                    ↓
3. Post Invoice → Retention Amount Calculated
                    ↓
4. Register Payment → Apply Retention Toggle Appears
                    ↓
5. Enable "Apply Retention" → Payment Created with Retention
                    ↓
6. Retention Reconciled to Retention Account
```

## Testing:

After configuration, test with:
1. Create a simple invoice (e.g., $1000)
2. Set 10% retention in draft
3. Expected retention: $100
4. Post invoice
5. Register payment
6. Should see suggested retention: $100
7. Enable "Apply Retention"
8. Payment amount should be $900
9. Check retention account for $100 entry

## Recent Fix:

The `apply_payment_retention` toggle now properly respects the `enforce_payment_retention` setting and becomes readonly when enforcement is disabled.

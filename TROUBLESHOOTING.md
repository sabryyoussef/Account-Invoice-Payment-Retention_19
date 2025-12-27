# Troubleshooting: Invoice Retention on Payment

## Common Issues and Solutions

### Issue: Cannot Enable Invoice Retention on Payment

#### Checklist:

1. **Enable the Feature First**
   - Navigate to: `Settings → Accounting`
   - Look for: "Enable Invoice's Retention on Payment"
   - ✓ Check this box to enable the feature
   - ✓ Save settings

2. **Configure Retention Accounts** (Required!)
   - In the same settings page, after enabling the feature:
   - Set **Retention Payable Account**: For vendor bills retention
   - Set **Retention Receivable Account**: For customer invoices retention
   - ⚠️ Both accounts MUST have "Allow Reconciliation" enabled
   - Save settings

3. **Select Retention Method**
   - Choose between:
     - **Untaxed Amount**: Retention calculated from subtotal (before tax)
     - **Total**: Retention calculated from total amount (including tax)

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

# Quick Start Guide: Invoice Payment Retention

## Initial Setup (One-time)

### Step 1: Enable the Feature
1. Go to **Settings** (top menu)
2. Click **Accounting** in the left sidebar
3. In the **General Settings** section (top of page), find:
   - ☑️ **"Enable Invoice's Retention on Payment"**
4. ✓ Check the box
5. The retention account fields will appear below

### Step 2: Configure Retention Accounts
After enabling the checkbox, configure the accounts (same page):

1. **Retention Payable Account**
   - Click the field and select/create an account
   - Use for vendor bills retention
   - ⚠️ Account MUST have "Allow Reconciliation" enabled
   - Recommended: Account type "Current Liabilities"

2. **Retention Receivable Account**
   - Click the field and select/create an account  
   - Use for customer invoices retention
   - ⚠️ Account MUST have "Allow Reconciliation" enabled
   - Recommended: Account type "Current Liabilities"

### Step 3: Select Retention Method
In the same **General Settings** section:

**Retention Method** - Choose one:
- ⚪ **Untaxed Amount**: Calculate retention from subtotal (before tax)
- ⚪ **Total**: Calculate retention from total amount (including tax)

### Step 4: Save Settings
Click **Save** button (top-left) to apply all changes

---

## Using Retention (Daily Operations)

### On Customer Invoice (Outgoing)

1. **Create Invoice** (Sales → Invoices → Create)
   - Add customer and invoice lines as usual
   
2. **Set Retention** (before posting)
   - Look for **"Payment Retention"** field
   - Choose:
     - **Percent**: Enter % (e.g., 10 = 10% retention)
     - **Amount**: Enter fixed amount (e.g., 50.00)
   - System auto-calculates **Retention Amount**
   
3. **Post Invoice**
   - Click "Confirm"
   
4. **Register Payment**
   - Click "Register Payment" button
   - You'll see:
     - **Suggested Retention**: 50.00 (example)
     - **Apply Retention**: Toggle (turn ON)
     - **Enforce Retention**: Checked by default
   
5. **Process Payment**
   - Toggle **Apply Retention** to ON
   - Payment amount auto-adjusts (Total - Retention)
   - Click "Create Payment"
   
**Result**: 
- Customer pays: Invoice Total - Retention Amount
- Retention Amount: Posted to Retention Receivable Account

---

### On Vendor Bill (Incoming)

Same process as customer invoice:

1. Create bill
2. Set retention (percent/amount)
3. Post bill
4. Register payment
5. Enable "Apply Retention"
6. Process payment

**Result**:
- You pay: Bill Total - Retention Amount
- Retention Amount: Posted to Retention Payable Account

---

## Returning Retention

When it's time to return/release the retention:

### For Customer Invoice (return retention to customer)
1. Create new **Customer Invoice**
2. Select the customer
3. Find **"Return Retention"** field
4. Select the retention move(s) to return
5. System auto-populates invoice lines with retention amounts
6. Post and register payment as normal

### For Vendor Bill (receive retention from vendor)
1. Create new **Vendor Bill**
2. Select the vendor
3. Select retention move(s) to return
4. Post and process as normal

---

## Examples

### Example 1: 10% Retention on $1,000 Invoice

**Invoice Setup:**
- Subtotal: $1,000
- Tax (15%): $150
- Total: $1,150
- Payment Retention: **Percent**
- Amount: **10** (10%)
- Retention Method: **Untaxed Amount**

**Calculated:**
- Retention Amount: $100 (10% of $1,000)

**Payment:**
- Apply Retention: ON
- Customer Pays: $1,050 ($1,150 - $100)
- Retention Account: $100

### Example 2: Fixed $200 Retention

**Invoice Setup:**
- Total: $5,000
- Payment Retention: **Amount**
- Amount: **200**

**Calculated:**
- Retention Amount: $200

**Payment:**
- Apply Retention: ON
- Customer Pays: $4,800 ($5,000 - $200)
- Retention Account: $200

---

## Troubleshooting

### "Apply Retention" toggle not visible
**Check:**
1. ✓ Feature enabled in Settings?
2. ✓ Retention accounts configured?
3. ✓ Invoice has payment_retention set?
4. ✓ Retention amount > 0?
5. ✓ User has retention permissions?

### Error: "Retention payable account should be set to allow Reconciliation"
**This is the most common error!**

**Quick Fix:**
1. Go to: **Accounting → Configuration → Chart of Accounts**
2. Search for your retention account (the one you selected)
3. Click on the account to open it
4. Click **Edit** button (top right)
5. Find the checkbox: **"Allow Reconciliation"**
6. ✅ **CHECK this box**
7. Click **Save**
8. Go back to **Settings → Accounting**
9. Click **Save** again

**If you get this for BOTH accounts:**
- Repeat the above steps for BOTH:
  - Retention Payable Account
  - Retention Receivable Account

**Still getting error?**
- Make sure you're editing the SAME accounts you selected in settings
- Try creating new accounts specifically for retention (see Step 2 above)

### Cannot pay multiple invoices with retention
**This is by design:**
- Invoices with retention must be paid individually
- Pay invoices one at a time

---

## Summary

| Step | Action | Location |
|------|--------|----------|
| 1 | Enable feature checkbox | Settings → Accounting → General Settings |
| 2 | Configure retention accounts | Settings → Accounting → General Settings |
| 3 | Select retention method | Settings → Accounting → General Settings |
| 4 | Save settings | Click Save button |
| 5 | Set retention on invoice | Invoice form (draft state) |
| 6 | Post invoice | Invoice → Confirm button |
| 7 | Apply retention on payment | Register Payment → Toggle ON |
| 8 | Return retention later | New invoice → Select retention moves |

---

**Need help?** See TROUBLESHOOTING.md for detailed diagnostic steps.

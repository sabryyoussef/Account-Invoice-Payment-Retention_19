# Quick Start Guide: Invoice Payment Retention

## Initial Setup (One-time)

### Step 1: Enable the Feature
1. Go to **Settings** → **Accounting**
2. Scroll to find **"Enable Invoice's Retention on Payment"**
3. ✓ Check the box
4. Save

### Step 2: Configure Retention Accounts
After enabling, two new fields appear:

1. **Retention Payable Account** (for vendor bills)
   - Select an account with reconciliation enabled
   - Recommended: Create account type "Current Liabilities"

2. **Retention Receivable Account** (for customer invoices)
   - Select an account with reconciliation enabled
   - Recommended: Create account type "Current Liabilities"

3. **Retention Method** (choose one):
   - **Untaxed Amount**: Calculate retention from subtotal (before tax)
   - **Total**: Calculate retention from total (including tax)

4. Save settings

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

### Error: "Retention account should allow reconciliation"
**Fix:**
1. Go to: Accounting → Configuration → Chart of Accounts
2. Find your retention accounts
3. Edit → Enable "Allow Reconciliation"
4. Save

### Cannot pay multiple invoices with retention
**This is by design:**
- Invoices with retention must be paid individually
- Pay invoices one at a time

---

## Summary

| Step | Action | Location |
|------|--------|----------|
| 1 | Enable feature | Settings → Accounting |
| 2 | Configure accounts | Settings → Accounting |
| 3 | Set retention on invoice | Invoice form (draft) |
| 4 | Post invoice | Invoice → Confirm |
| 5 | Apply retention on payment | Register Payment → Toggle ON |
| 6 | Return retention later | New invoice → Select retention moves |

---

**Need help?** See TROUBLESHOOTING.md for detailed diagnostic steps.

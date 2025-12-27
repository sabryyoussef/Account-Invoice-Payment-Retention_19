# How to Fix: "Retention payable account should be set to allow Reconciliation"

## Error Message
```
Validation Error
Retention payable account should be set to allow Reconciliation
```
(You may also get the same error for "Retention receivable account")

---

## What This Means
The retention feature needs accounts that can be **reconciled** (matched with payments). The account you selected doesn't have this enabled.

---

## Quick Fix (5 minutes)

### Step 1: Open Chart of Accounts
1. In Odoo, click: **Accounting** (top menu)
2. Navigate to: **Configuration → Chart of Accounts**

### Step 2: Find the Account
3. Search for the account you selected for retention
   - Look for "Retention Payable" or whatever name you chose
   - Or filter by Type: "Current Liabilities"

### Step 3: Edit the Account  
4. Click on the account name to open it
5. Click **Edit** button (top-right corner)

### Step 4: Enable Reconciliation
6. Scroll down and find the checkbox: **"Allow Reconciliation"**
7. ✅ **CHECK this box**
8. Click **Save**

### Step 5: Repeat for Second Account
9. If you get the same error for "Retention Receivable Account":
   - Find that account
   - Edit it
   - Enable "Allow Reconciliation"
   - Save

### Step 6: Save Settings Again
10. Go back to **Settings → Accounting**
11. Click **Save**
12. ✅ Error should be gone!

---

## Visual Guide

```
1. Accounting → Configuration → Chart of Accounts

2. Click on your Retention Account

3. Click "Edit" button

4. Find and check this box:
   ┌────────────────────────────────────┐
   │ Account Configuration              │
   │                                    │
   │ Name: Retention Payable            │
   │ Code: RE001                        │
   │ Type: Current Liabilities          │
   │                                    │
   │ ✅ Allow Reconciliation  ← CHECK!  │
   │                                    │
   └────────────────────────────────────┘

5. Click "Save"

6. Repeat for second retention account

7. Go to Settings → Accounting → Save
```

---

## Alternative Solution: Create New Accounts

If you can't find your accounts or prefer to start fresh:

### Create Account 1: Retention Payable
1. **Accounting → Configuration → Chart of Accounts → Create**
2. Fill in:
   - **Account Name**: `Retention Payable`
   - **Code**: `RE001` (or your numbering system)
   - **Type**: `Current Liabilities`
   - ✅ **Allow Reconciliation**: **CHECK THIS BOX**
3. Click **Save**

### Create Account 2: Retention Receivable
1. **Accounting → Configuration → Chart of Accounts → Create**
2. Fill in:
   - **Account Name**: `Retention Receivable`
   - **Code**: `RE002` (or your numbering system)
   - **Type**: `Current Liabilities`
   - ✅ **Allow Reconciliation**: **CHECK THIS BOX**
3. Click **Save**

### Configure Settings
1. Go to **Settings → Accounting**
2. **Retention Payable Account**: Select `RE001 - Retention Payable`
3. **Retention Receivable Account**: Select `RE002 - Retention Receivable`
4. Click **Save**
5. ✅ Should work now!

---

## Why Reconciliation is Required

The retention feature works by:
1. Creating payment entries in the retention account
2. Later matching (reconciling) those entries when you return the retention
3. Without reconciliation enabled, the system can't match these entries
4. So Odoo requires reconciliation to be enabled

---

## Troubleshooting

### Still getting the error?
- **Check you edited the SAME account you selected in settings**
  - Compare account codes/names
- **Make sure you saved the account changes**
  - Look for a green checkmark or success message
- **Try selecting different accounts**
  - Use the newly created ones above

### Can't find the checkbox?
- Make sure you clicked **Edit** on the account first
- Scroll down - it might be below the fold
- Try using Developer Mode: Settings → Activate Developer Mode

### Getting error for BOTH accounts?
- You need to enable reconciliation on BOTH:
  - Retention Payable Account (for vendor bills)
  - Retention Receivable Account (for customer invoices)
- Repeat the fix steps for each account

---

## Summary

✅ **DO:**
- Enable "Allow Reconciliation" on BOTH retention accounts
- Save the account changes
- Save the settings again

❌ **DON'T:**
- Use accounts without reconciliation
- Forget to save after enabling reconciliation
- Select the same account for both payable and receivable

---

## Next Steps

Once the error is fixed:
1. Settings should save successfully
2. Follow [QUICK_START.md](QUICK_START.md) to use retention on invoices
3. Create a test invoice with retention to verify it works

---

**Need more help?**
- Full setup guide: [QUICK_START.md](QUICK_START.md)
- Other issues: [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
- Overview: [FIX_SUMMARY.md](FIX_SUMMARY.md)

# Troubleshooting: Can't See "Enable Invoice's Retention on Payment" Setting

## Issue
The setting "Enable Invoice's Retention on Payment" is not visible in Settings → Accounting.

## Common Causes & Solutions

### 1. Module Not Installed/Upgraded ⚠️ MOST COMMON

**Check:**
- Go to Apps menu
- Remove "Apps" filter, select "All" 
- Search for: `account_invoice_payment_retention`
- Check status

**Solution:**
```bash
# If not installed:
odoo-bin -d <your_database> -i account_invoice_payment_retention

# If installed but not upgraded:
odoo-bin -d <your_database> -u account_invoice_payment_retention

# Or upgrade via Odoo UI:
# Apps → Remove filters → Search module → Click "Upgrade"
```

**After installation:**
- Restart Odoo
- Clear browser cache (Ctrl+F5)
- Reload Settings page

---

### 2. Wrong Section in Settings

**Location:** The setting appears in the **General Settings** section of Accounting.

**Steps to find it:**
1. Click **Settings** in top menu bar
2. Click **Accounting** in the left sidebar
3. Look for **General Settings** section at the top of the page
4. Find the checkbox: **"Enable Invoice's Retention on Payment"**
5. Below it you'll see: "This enable retention option in invoice, to be retained on its payment."

**Visual Guide (based on actual UI):**
```
Settings → Accounting → General Settings
┌──────────────────────────────────────────────────────┐
│ General Settings                                     │
│                                                      │
│ ☑ Enable Invoice's Retention on Payment             │  ← Checkbox here!
│   This enable retention option in invoice, to be    │
│   retained on its payment.                          │
│                                                      │
│   Retention Payable Account:    [________]          │  ← Appears after checking
│   Retention Receivable Account: [________]          │  ← Appears after checking
│                                                      │
│ Retention Method                                     │
│ Default your retention method                       │
│ ○ Untaxed Amount                                    │
│ ○ Total                                             │
└──────────────────────────────────────────────────────┘
```

---

### 3. Access Rights Issue

**Check your user permissions:**
1. Go to Settings → Users & Companies → Users
2. Find your user
3. Check if you have:
   - ✓ **Accounting / Billing** rights
   - ✓ **Settings** access rights

**Solution:**
- Ask administrator to grant you:
  - Settings access
  - Accounting Administrator rights

---

### 4. View Not Loading (Technical Issue)

**Update the view:**
```bash
# Method 1: Upgrade module
odoo-bin -d <database> -u account_invoice_payment_retention

# Method 2: Update module list
# In Odoo UI: Apps → Update Apps List
```

**Clear cache:**
```bash
# In browser:
Ctrl + F5 (Windows/Linux)
Cmd + Shift + R (Mac)

# Or:
Clear browser cache completely
```

---

### 5. Developer Mode Check

**Enable Developer Mode:**
1. Settings → Activate Developer Mode
2. Go back to Settings → Accounting
3. The setting should now be visible

**If still not visible in Developer Mode:**
- Check browser console for errors (F12)
- Look for XML view errors

---

### 6. Database/Module Path Issue

**Verify module is in addons path:**
```bash
# Check if module exists
ls -la custom_addons/account_invoice_payment_retention/

# Should show:
# __manifest__.py
# models/
# views/
# wizard/
# etc.
```

**Check Odoo configuration:**
```ini
# In odoo.conf
addons_path = /path/to/odoo/addons,/path/to/custom_addons
```

---

## Step-by-Step Verification

### **Test 1: Verify Module Installation**
```bash
# Run in terminal:
cd /workspaces/Account-Invoice-Payment-Retention_19
./check_module.sh
```

### **Test 2: Check via Odoo Shell**
```bash
# Run diagnostic:
odoo-bin shell -d <your_database> --no-http < diagnostic_retention.py
```

### **Test 3: Manual Database Check**
```python
# In Odoo shell:
module = env['ir.module.module'].search([('name', '=', 'account_invoice_payment_retention')])
print(f"State: {module.state}")
print(f"Installed: {module.state == 'installed'}")

# Check if view exists:
view = env.ref('account_invoice_payment_retention.res_config_settings_view_form', raise_if_not_found=False)
print(f"View exists: {view is not None}")
```

---

## Installation Commands

### **Fresh Installation:**
```bash
# Stop Odoo if running
# Then run:
odoo-bin -d <database> \
  -i account_invoice_payment_retention \
  --stop-after-init

# Start Odoo normally
odoo-bin -d <database>
```

### **Upgrade Existing:**
```bash
odoo-bin -d <database> \
  -u account_invoice_payment_retention \
  --stop-after-init
```

### **Via Odoo UI:**
1. Go to **Apps**
2. Remove "Apps" filter
3. Search: `account_invoice_payment_retention`
4. Click **Install** or **Upgrade**
5. Wait for installation
6. **Refresh browser** (F5)

---

## Expected Result

After successful installation, you should see:

**Settings → Accounting → (Top of page)**
```
┌─────────────────────────────────────────────────────┐
│ ☐ Enable Invoice's Retention on Payment            │
│   This enable retention option in invoice, to be   │
│   retained on its payment.                         │
│                                                     │
│   [Hidden until checkbox enabled]                  │
│   Retention Payable Account:                       │
│   Retention Receivable Account:                    │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│ Retention Method                                    │
│ Default your retention method                      │
│                                                     │
│ ○ Untaxed Amount                                   │
│ ○ Total                                            │
└─────────────────────────────────────────────────────┘
```

---

## Still Not Visible?

### Check logs for errors:
```bash
# View Odoo logs
tail -f /var/log/odoo/odoo.log

# Or if running in terminal:
# Check terminal output for XML view errors
```

### Common error messages:
- **"View not found"** → Module not properly installed
- **"Field not found"** → Database not updated
- **"Access denied"** → User permissions issue

### Last resort:
```bash
# Complete reinstall:
# 1. Uninstall module (Apps → Uninstall)
# 2. Restart Odoo
# 3. Update app list (Apps → Update Apps List)
# 4. Install module again
# 5. Clear browser cache
# 6. Reload settings page
```

---

## Quick Command Reference

```bash
# Install module
odoo-bin -d DB_NAME -i account_invoice_payment_retention --stop-after-init

# Upgrade module  
odoo-bin -d DB_NAME -u account_invoice_payment_retention --stop-after-init

# Run diagnostics
./diagnostic_retention.py

# Check module files
./check_module.sh
```

---

## Need More Help?

If the setting is still not visible after trying all above:

1. **Share error logs** from Odoo
2. **Check Odoo version** (must be v19.0)
3. **Verify module compatibility**
4. **Contact support** with:
   - Odoo version
   - Module installation status
   - Error messages (if any)
   - Screenshots of Settings page

---

**Remember:** Always **restart Odoo** and **clear browser cache** after installing/upgrading modules!

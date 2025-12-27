#!/bin/bash

# Quick Installation Checker for Invoice Payment Retention Module
# This checks if the module is properly installed in your Odoo database

echo "========================================"
echo "Invoice Retention - Installation Check"
echo "========================================"
echo ""

# Check if we're in the right directory
if [ ! -d "custom_addons/account_invoice_payment_retention" ]; then
    echo "❌ Error: Module directory not found"
    echo "   Please run this from the Odoo workspace root"
    exit 1
fi

echo "✓ Module files found"
echo ""

# Ask for database name
read -p "Enter your Odoo database name: " DB_NAME

if [ -z "$DB_NAME" ]; then
    echo "❌ Database name required"
    exit 1
fi

echo ""
echo "Checking installation status..."
echo ""

# Create a Python script to check module status
cat > /tmp/check_module_status.py << 'EOF'
import sys

try:
    # Check if module is installed
    module = env['ir.module.module'].search([
        ('name', '=', 'account_invoice_payment_retention')
    ])
    
    if not module:
        print("❌ Module NOT found in database")
        print("   Run: odoo-bin -d {} -i account_invoice_payment_retention".format(env.cr.dbname))
        sys.exit(1)
    
    print(f"Module found: {module.name}")
    print(f"State: {module.state}")
    print(f"Version: {module.latest_version}")
    print("")
    
    if module.state == 'installed':
        print("✓ Module is INSTALLED")
        print("")
        
        # Check if view exists
        try:
            view = env.ref('account_invoice_payment_retention.res_config_settings_view_form')
            print("✓ Settings view is loaded")
            print(f"  View ID: {view.id}")
            print(f"  View Name: {view.name}")
            print("")
        except:
            print("⚠️  Settings view NOT found")
            print("   Try: odoo-bin -d {} -u account_invoice_payment_retention".format(env.cr.dbname))
            print("")
        
        # Check if fields exist
        config = env['res.config.settings'].create({})
        if hasattr(config, 'group_payment_retention'):
            print("✓ Settings fields are available")
            print("")
        else:
            print("❌ Settings fields NOT available")
            print("   Database needs update!")
            print("")
        
        print("═══════════════════════════════════════")
        print("RESULT: Module is properly installed!")
        print("═══════════════════════════════════════")
        print("")
        print("To see the setting:")
        print("1. Go to Settings → Accounting")
        print("2. Scroll to the TOP of the page")
        print("3. Look for: 'Enable Invoice's Retention on Payment'")
        print("")
        
    elif module.state == 'to upgrade':
        print("⚠️  Module needs UPGRADE")
        print("")
        print("Run this command:")
        print(f"odoo-bin -d {env.cr.dbname} -u account_invoice_payment_retention --stop-after-init")
        print("")
        
    elif module.state == 'to install':
        print("⚠️  Module is marked for installation but not installed yet")
        print("")
        print("Run this command:")
        print(f"odoo-bin -d {env.cr.dbname} -i account_invoice_payment_retention --stop-after-init")
        print("")
        
    else:
        print(f"⚠️  Module state: {module.state}")
        print("")
        print("To install:")
        print(f"odoo-bin -d {env.cr.dbname} -i account_invoice_payment_retention --stop-after-init")
        print("")

except Exception as e:
    print(f"❌ Error checking module: {e}")
    print("")
    print("This might mean:")
    print("1. Database connection failed")
    print("2. Module not in database at all")
    print("3. Odoo shell not working properly")
    sys.exit(1)
EOF

# Try to run the check
if command -v odoo-bin &> /dev/null; then
    echo "Running check via Odoo shell..."
    odoo-bin shell -d "$DB_NAME" --no-http < /tmp/check_module_status.py 2>&1 | grep -v "WARNING\|INFO\|DEBUG" || {
        echo ""
        echo "❌ Could not connect to database or run check"
        echo ""
        echo "Manual check needed:"
        echo "1. Start Odoo"
        echo "2. Go to Apps menu"
        echo "3. Remove 'Apps' filter"
        echo "4. Search: account_invoice_payment_retention"
        echo "5. Check if it shows 'Installed'"
        echo ""
    }
else
    echo "⚠️  odoo-bin not found in PATH"
    echo ""
    echo "Please check manually:"
    echo "1. In Odoo: Go to Apps"
    echo "2. Remove filters, search: account_invoice_payment_retention"
    echo "3. Check installation status"
    echo ""
    echo "Or run:"
    echo "  /path/to/odoo-bin shell -d $DB_NAME --no-http < /tmp/check_module_status.py"
    echo ""
fi

# Cleanup
rm -f /tmp/check_module_status.py

echo ""
echo "For more help, see: SETTINGS_NOT_VISIBLE.md"
echo ""

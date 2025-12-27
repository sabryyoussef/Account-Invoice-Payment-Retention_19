#!/bin/bash

echo "=========================================="
echo "Upgrade Invoice Payment Retention Module"
echo "=========================================="
echo ""

# Get database name
read -p "Enter your Odoo database name: " DB_NAME

if [ -z "$DB_NAME" ]; then
    echo "❌ Database name required"
    exit 1
fi

echo ""
echo "Upgrading module in database: $DB_NAME"
echo ""

# Check if odoo-bin exists
if command -v odoo-bin &> /dev/null; then
    echo "Running upgrade..."
    odoo-bin -d "$DB_NAME" -u account_invoice_payment_retention --stop-after-init
    
    echo ""
    echo "✓ Upgrade complete!"
    echo ""
    echo "Next steps:"
    echo "1. Start Odoo normally"
    echo "2. Clear browser cache (Ctrl+F5)"
    echo "3. Go to Settings → Accounting"
    echo "4. Look for 'Payment Retention' section"
    echo ""
else
    echo "⚠️  odoo-bin not found in PATH"
    echo ""
    echo "Please run manually:"
    echo "  /path/to/odoo-bin -d $DB_NAME -u account_invoice_payment_retention --stop-after-init"
    echo ""
fi

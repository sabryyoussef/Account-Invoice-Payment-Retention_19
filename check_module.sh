#!/bin/bash

# Invoice Payment Retention - Configuration Checker
# Quick bash script to verify basic setup

echo "=========================================="
echo "Invoice Payment Retention - Quick Check"
echo "=========================================="
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "This script helps verify your Odoo instance has the retention module."
echo ""

# Check if in Odoo directory
if [ ! -f "odoo-bin" ]; then
    echo -e "${RED}✗ Not in Odoo directory${NC}"
    echo "  Please run this from your Odoo installation directory"
    exit 1
fi

echo -e "${GREEN}✓ Odoo installation found${NC}"
echo ""

# Check if module exists
MODULE_PATH="custom_addons/account_invoice_payment_retention"
if [ -d "$MODULE_PATH" ]; then
    echo -e "${GREEN}✓ Module directory exists: $MODULE_PATH${NC}"
else
    echo -e "${RED}✗ Module directory not found${NC}"
    echo "  Expected: $MODULE_PATH"
    exit 1
fi

# Check manifest
if [ -f "$MODULE_PATH/__manifest__.py" ]; then
    echo -e "${GREEN}✓ Module manifest found${NC}"
    VERSION=$(grep "version" "$MODULE_PATH/__manifest__.py" | cut -d'"' -f2)
    echo "  Version: $VERSION"
else
    echo -e "${RED}✗ Module manifest not found${NC}"
    exit 1
fi

# Check key files
echo ""
echo "Checking module files..."

FILES=(
    "models/account_move.py"
    "models/res_company.py"
    "models/res_config_settings.py"
    "wizard/account_payment_register.py"
    "views/account_move_views.xml"
    "views/res_config_settings_views.xml"
    "wizard/account_payment_register_views.xml"
    "security/security.xml"
)

for file in "${FILES[@]}"; do
    if [ -f "$MODULE_PATH/$file" ]; then
        echo -e "  ${GREEN}✓${NC} $file"
    else
        echo -e "  ${RED}✗${NC} $file (missing)"
    fi
done

echo ""
echo "=========================================="
echo "Next Steps:"
echo "=========================================="
echo ""
echo "1. Install/upgrade the module:"
echo "   odoo-bin -d <database> -u account_invoice_payment_retention"
echo ""
echo "2. Run comprehensive diagnostics in Odoo shell:"
echo "   odoo-bin shell -d <database> --no-http < diagnostic_retention.py"
echo ""
echo "3. Configure in Odoo UI:"
echo "   Settings → Accounting → Enable Invoice's Retention on Payment"
echo ""
echo "4. Read documentation:"
echo "   - QUICK_START.md for usage guide"
echo "   - TROUBLESHOOTING.md for common issues"
echo "   - FIX_SUMMARY.md for complete overview"
echo ""

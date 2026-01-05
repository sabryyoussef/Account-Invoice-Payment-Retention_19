# Use Case: Bill of Quantities (BOQ) Management

## Overview
This document covers all use cases related to creating, managing, and approving Bill of Quantities (BOQ) documents in the TPO Management system. BOQ is a detailed list of materials, quantities, and cost breakdowns used for project estimation and procurement.

## Business Context
BOQ is one of the most critical documents in construction projects, as it:
- Provides detailed cost breakdown for the project
- Serves as basis for procurement decisions
- Forms foundation for payment applications
- Enables accurate budget planning

---

## Use Case 2.1: Create a New BOQ from Scratch

### Scenario
A technical office engineer needs to create a comprehensive BOQ for a new building project with multiple items, quantities, and pricing.

### Prerequisites
- TPO Project must be created
- User has Technical Office Engineer or Estimator role
- Access to material pricing information

### Steps

#### Step 1: Navigate to BOQ
1. Go to **TPO Management > Pre-Execution & Planning > Bill of Quantities**
2. Click **Create** button

#### Step 2: Fill BOQ Header Information
1. **BOQ Reference**: Enter unique reference (e.g., `BOQ-ART-001`)
   - Follow naming convention: `BOQ-[Project Code]-[Sequence]`
2. **Project**: Select the project from dropdown (e.g., `Al-Riyadh Tower`)
3. **Date**: Set BOQ creation date (defaults to today)
4. **Technical Office Engineer**: Select responsible engineer
5. **Estimator**: Select person who prepared the estimate
6. **Description**: Add any notes or remarks about this BOQ

#### Step 3: Add BOQ Lines
1. Click on the **BOQ Lines** tab (or scroll down if using editable list)
2. Click **Add a line** button
3. For each line item, fill:

   **Line 1 - Excavation Work:**
   - **Item Code**: `EXC-001`
   - **Description**: `Excavation for foundation - Depth 3m`
   - **Unit**: `m³` (cubic meters)
   - **Quantity**: `500`
   - **Unit Price**: `25.00` (currency automatically from project)
   - **Amount**: Automatically calculated (500 × 25.00 = 12,500.00)

   **Line 2 - Concrete Work:**
   - **Item Code**: `CONC-001`
   - **Description**: `Ready-mix concrete C30/37`
   - **Unit**: `m³`
   - **Quantity**: `1,200`
   - **Unit Price**: `85.00`
   - **Amount**: Automatically calculated

   **Line 3 - Rebar:**
   - **Item Code**: `REB-001`
   - **Description**: `Reinforcement steel grade 420/500`
   - **Unit**: `ton`
   - **Quantity**: `150`
   - **Unit Price**: `550.00`
   - **Amount**: Automatically calculated

   **Continue adding all items...**

4. You can:
   - **Reorder lines**: Use drag handles (if enabled)
   - **Delete lines**: Click on line and press Delete
   - **Copy lines**: Duplicate similar items and modify

#### Step 4: Verify Total Amount
1. The **Total Amount** field at the top automatically calculates from all line amounts
2. Verify the total matches your calculation
3. Review all line items for accuracy

#### Step 5: Attach Supporting Documents (Optional)
1. Click on **Documents** tab
2. Click **Add** or drag and drop files:
   - Excel file with detailed breakdown
   - PDF specifications
   - Material catalogs
   - Any other supporting documents

#### Step 6: Save BOQ
1. Click **Save** button
2. BOQ is now in **Draft** status
3. Review all information before submission

### Expected Result
- BOQ created with all line items
- Total amount automatically calculated
- BOQ ready for review and submission
- Supporting documents attached

---

## Use Case 2.2: Submit BOQ for Approval

### Scenario
After creating and reviewing the BOQ, the engineer needs to submit it for management approval.

### Prerequisites
- BOQ is in Draft status
- All line items are complete
- Total amount is verified

### Steps

#### Step 1: Review BOQ
1. Open the BOQ you want to submit
2. Review all information:
   - Verify all line items are correct
   - Check quantities and prices
   - Confirm total amount
   - Review attached documents

#### Step 2: Submit for Approval
1. In the status bar at the top, click **Submit**
   - Or click the **Submit** button if available
2. Status changes from **Draft** to **Submitted**
3. Notification is sent to approvers

### Expected Result
- BOQ status changed to "Submitted"
- Approvers are notified
- BOQ appears in approver's review queue
- Cannot be edited until approved/rejected

---

## Use Case 2.3: Approve or Reject BOQ

### Scenario
A project manager or TPO manager reviews the submitted BOQ and makes an approval decision.

### Prerequisites
- User has approval permissions
- BOQ is in Submitted status

### Steps for Approval

#### Step 1: Open Submitted BOQ
1. Go to **TPO Management > Pre-Execution & Planning > Bill of Quantities**
2. Apply filter: **Status = Submitted**
3. Open the BOQ to review

#### Step 2: Review BOQ Details
1. Check all line items for:
   - Accurate quantities
   - Reasonable unit prices
   - Correct calculations
   - Complete descriptions
2. Review total amount
3. Check attached documents if any

#### Step 3: Approve BOQ
1. If BOQ is correct:
   - Click **Approve** button (or change status to Approved)
   - Add comments in Chatter if needed
   - Status changes to **Approved**
2. If BOQ needs changes:
   - Click **Reject** button
   - Add rejection reason in Chatter
   - Status changes to **Rejected**
   - BOQ creator is notified

### Expected Result
- BOQ status updated to Approved or Rejected
- Appropriate notifications sent
- If rejected, creator can revise and resubmit

---

## Use Case 2.4: Revise Rejected BOQ

### Scenario
A BOQ was rejected and needs to be corrected and resubmitted.

### Prerequisites
- BOQ is in Rejected status
- User is the BOQ creator or has edit permissions

### Steps

#### Step 1: Open Rejected BOQ
1. Go to **TPO Management > Pre-Execution & Planning > Bill of Quantities**
2. Apply filter: **Status = Rejected**
3. Open the rejected BOQ

#### Step 2: Review Rejection Comments
1. Check Chatter tab for rejection reason
2. Review comments from approver
3. Identify what needs to be corrected

#### Step 3: Make Corrections
1. Edit line items as needed:
   - Modify quantities
   - Update prices
   - Add missing items
   - Remove incorrect items
2. Update description if needed
3. Verify new total amount

#### Step 4: Resubmit
1. Change status back to **Draft** first (if needed)
2. Click **Submit** again
3. Add comment in Chatter explaining changes made

### Expected Result
- BOQ corrected with accurate information
- Status changed back to Submitted
- Approvers notified of resubmission

---

## Use Case 2.5: Import BOQ from Excel

### Scenario
BOQ data exists in Excel and needs to be imported into the system.

### Steps

#### Step 1: Prepare Excel File
1. Create Excel file with columns:
   - Item Code
   - Description
   - Unit
   - Quantity
   - Unit Price
2. Save as CSV or Excel format

#### Step 2: Create BOQ Header
1. Create new BOQ as described in Use Case 2.1
2. Fill header information
3. Save BOQ

#### Step 3: Import Lines
1. Go to BOQ Lines tab
2. Click **Import** button (if available)
3. Select your Excel/CSV file
4. Map columns:
   - Match Excel columns to BOQ line fields
   - Verify mapping is correct
5. Click **Import**

**OR Manual Entry:**
- Copy data from Excel
- Paste into BOQ lines (if bulk paste supported)
- Or enter line by line

### Expected Result
- BOQ lines imported successfully
- All items available in system
- Ready for review and submission

---

## Use Case 2.6: Compare Multiple BOQ Versions

### Scenario
A project manager wants to compare different BOQ versions to see cost changes.

### Steps

#### Step 1: View BOQ History
1. Open the project
2. Click on **BOQs** smart button
3. View all BOQ versions in list

#### Step 2: Compare Versions
1. Open first BOQ version
2. Note total amount and key items
3. Open second BOQ version
4. Compare:
   - Total amounts
   - Line item differences
   - Quantity changes
   - Price variations

#### Step 3: Export for Comparison
1. Export both BOQ versions to Excel
2. Use Excel to create comparison spreadsheet
3. Highlight differences

### Expected Result
- Clear comparison of BOQ versions
- Understanding of cost changes
- Documented history of revisions

---

## Use Case 2.7: Link BOQ to Payment Applications

### Scenario
When creating payment applications, reference should be made to approved BOQ items.

### Steps

#### Step 1: Verify BOQ Status
1. Ensure BOQ is **Approved**
2. Note approved quantities and prices

#### Step 2: Create Payment Application
1. Go to **TPO Management > Financial & Closure > Payment Applications**
2. Create new payment application for same project
3. Reference BOQ items when adding application lines:
   - Use same item codes
   - Reference approved quantities
   - Apply approved unit prices

### Expected Result
- Payment applications aligned with approved BOQ
- Consistent pricing throughout project
- Accurate progress billing

---

## Best Practices

### BOQ Creation
- **Start with template**: Use standard BOQ templates if available
- **Be comprehensive**: Include all project items, even small ones
- **Use clear descriptions**: Detailed item descriptions prevent confusion
- **Verify prices**: Cross-check unit prices with current market rates
- **Add markups**: Include overhead, profit, and contingencies appropriately

### BOQ Management
- **Version control**: Keep track of BOQ revisions
- **Approve promptly**: Don't delay approval process
- **Document changes**: Always comment on modifications
- **Link to contracts**: Reference contract BOQ when applicable

### BOQ Accuracy
- **Review calculations**: Verify all amounts before submission
- **Check quantities**: Ensure quantities match project scope
- **Validate prices**: Confirm prices are current and accurate
- **Include contingencies**: Add appropriate percentage for unknowns

---

## Common Workflows

### Workflow 1: Standard BOQ Creation and Approval
```
Create BOQ → Add Lines → Review → Submit → Approve → Use in Project
```

### Workflow 2: BOQ with Revisions
```
Create BOQ → Submit → Reject → Revise → Resubmit → Approve
```

### Workflow 3: BOQ for Tender
```
Create BOQ → Add All Items → Review Pricing → Submit → Approve → Use in Tender
```

---

## Related Use Cases

- [Project Setup](../01_project_management/project_setup.md)
- [Payment Application](../04_financial_closure/payment_application.md)
- [Change Order](../03_execution_monitoring/change_order.md)

---

## Troubleshooting

### Issue: Total amount not calculating
**Solution**: Check if all line items have valid quantities and prices. Ensure no empty fields.

### Issue: Cannot submit BOQ
**Solution**: Verify all required fields are filled. Check if BOQ has at least one line item.

### Issue: Cannot approve BOQ
**Solution**: Check user permissions. Only TPO Manager or Project Manager can approve.

### Issue: Lines disappearing after save
**Solution**: Ensure line items are properly saved. Check for validation errors.

---

**Last Updated**: November 2025


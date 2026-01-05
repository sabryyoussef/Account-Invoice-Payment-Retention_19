# Use Case: Change Order / Variation Order (VO) Management

## Overview
Change Orders (also called Variation Orders or VOs) document changes to contract scope, quantity, specifications, or timeline. This document covers creating, submitting, and managing change orders with financial and time impact tracking.

---

## Use Case 8.1: Create Change Order for Scope Addition

### Scenario
During construction, client requests additional work not included in original contract. A change order needs to be created to document the scope, cost, and time impact.

### Steps

#### Step 1: Create Change Order
1. Go to **TPO Management > Execution & Monitoring > Change Orders / VO**
2. Click **Create**

#### Step 2: Fill Change Order Header
1. **VO Number**: Enter number (e.g., `VO-ART-001`)
2. **Project**: Select project
3. **Date**: Set change order date
4. **Change Type**: Select:
   - `Scope Change` - Addition or deletion of work
   - `Quantity Change` - Change in quantities
   - `Specification Change` - Material or method change
   - `Time Extension` - Schedule change
   - `Cost Change` - Price adjustment
   - `Other` - Other types
5. **Subject**: Brief subject (e.g., `Additional waterproofing for basement extension`)
6. **Location**: Site location affected

#### Step 3: Describe Change Details
1. **Description**: Detailed description:
   ```
   Client requested extension of basement area requiring 
   additional waterproofing membrane. Original contract 
   covered 500 sqm. Extension adds 150 sqm requiring same 
   waterproofing treatment.
   ```
2. **Reason for Change**: Explain why change is needed

#### Step 4: Add Change Order Lines
1. Click **Change Order Lines** tab
2. Add line items affected:
   - **Item Code**: Reference to BOQ item
   - **Description**: Item description
   - **Unit**: Unit of measurement
   - **Original Quantity**: Original contract quantity
   - **Revised Quantity**: New total quantity
   - **Quantity Change**: Auto-calculated difference
   - **Unit Price**: Price per unit
   - **Amount**: Auto-calculated

#### Step 5: Calculate Financial Impact
1. **Original Amount**: Total original contract value (if change affects total)
2. **Revised Amount**: New total after change
3. **Change Amount**: Auto-calculated difference

#### Step 6: Document Time Impact
1. **Original Duration**: Original project duration in days
2. **Revised Duration**: New duration after change
3. **Duration Change**: Auto-calculated days added

#### Step 7: Link Related Documents
1. Link **Related Shop Drawings** if change affects drawings
2. Link **Related RFIs** that led to this change

#### Step 8: Request Site Visit (if needed)
1. Check **Site Visit Required**
2. Set **Site Visit Date** when scheduled
3. Select **Site Visit Participants**
4. Add **Site Visit Notes** after visit

#### Step 9: Attach Supporting Documents
1. Attach:
   - Client request letter/email
   - Revised drawings
   - Cost estimates
   - Any other relevant documents

#### Step 10: Submit for Approval
1. Review all information
2. Click **Submit**
3. Status changes to "Submitted"

---

## Use Case 8.2: Approve Change Order

### Scenario
Project manager reviews submitted change order and approves it after verification.

### Steps

#### Step 1: Review Change Order
1. Open submitted change order
2. Verify:
   - Change description and reason
   - Financial impact calculations
   - Time impact assessment
   - Supporting documents

#### Step 2: Approve or Reject
1. If approved:
   - Click **Approve**
   - Set **Approval Date**
   - Status changes to "Approved"
2. If rejected:
   - Click **Reject**
   - Add rejection reason in Chatter

---

## Use Case 8.3: Process Change Order with Site Visit

### Scenario
A change order requires site visit to verify conditions before approval.

### Steps

#### Step 1: Schedule Site Visit
1. Open change order
2. Check **Site Visit Required**
3. Set **Site Visit Date**
4. Select participants
5. Submit change order

#### Step 2: Conduct Site Visit
1. On visit date, update change order
2. Add **Site Visit Notes**:
   - Conditions observed
   - Measurements taken
   - Photos attached
   - Recommendations

#### Step 3: Complete Change Order
1. Update change order lines based on site findings
2. Recalculate financial and time impact
3. Submit for final approval

---

## Best Practices

- **Document thoroughly** - Include all relevant details
- **Calculate accurately** - Verify all financial impacts
- **Link related documents** - Connect to RFIs, shop drawings
- **Get approvals** before starting changed work
- **Track all changes** - Maintain complete history

---

## Related Use Cases
- [RFI Management](rfi.md)
- [Payment Application](../04_financial_closure/payment_application.md)
- [TPO Visits](../05_site_management/tpo_visit.md)


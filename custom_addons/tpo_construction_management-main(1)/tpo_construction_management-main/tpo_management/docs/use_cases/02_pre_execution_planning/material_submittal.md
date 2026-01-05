# Use Case: Material Submittal Management

## Overview
Use cases for submitting materials for approval, tracking revisions, and managing the approval workflow with samples and specifications.

---

## Use Case 3.1: Submit Material for Approval

### Scenario
A technical office engineer needs to submit a new material (e.g., waterproofing membrane) for consultant approval before procurement.

### Steps

#### Step 1: Create Material Submittal
1. Go to **TPO Management > Pre-Execution & Planning > Material Submittal**
2. Click **Create**

#### Step 2: Fill Submittal Details
1. **Submittal Reference**: Enter reference (e.g., `MAT-ART-001`)
2. **Project**: Select project
3. **Submittal Date**: Set submission date
4. **Technical Office Engineer**: Assign engineer
5. **Material Description**: `Self-adhesive waterproofing membrane for basement`
6. **Specification**: Add technical specifications
7. **Manufacturer**: `ABC Waterproofing Co.`
8. **Model**: `WP-MB-5000`

#### Step 3: Attach Documents and Samples
1. Click **Documents** tab
   - Attach technical data sheets
   - Attach material specifications
   - Attach manufacturer certificates
2. Click **Samples** tab
   - Upload sample photos
   - Attach test reports

#### Step 4: Submit for Approval
1. Review all information
2. Click **Submit**
3. Revision number automatically set to 0
4. Submission log entry created

### Expected Result
- Material submittal created and submitted
- All documents attached
- Ready for consultant review

---

## Use Case 3.2: Resubmit Rejected Material

### Scenario
A material submittal was rejected and needs to be revised with new specifications.

### Steps
1. Open rejected submittal
2. Review rejection comments in Chatter
3. Update material details or attach new documents
4. Click **Resubmit**
5. Revision number automatically increments
6. New submission log entry created

---

## Related Use Cases
- [Shop Drawing Management](../03_execution_monitoring/shop_drawing.md)


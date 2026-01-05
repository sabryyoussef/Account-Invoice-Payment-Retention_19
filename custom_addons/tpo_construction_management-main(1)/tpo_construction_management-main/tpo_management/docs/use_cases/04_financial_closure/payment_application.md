# Use Case: Payment Application / Invoice Management

## Overview
Payment Applications (also called invoices or payment requests) are monthly statements for work executed, submitted to client for payment. This document covers creating, submitting, and tracking payment applications.

---

## Use Case 10.1: Create Monthly Payment Application

### Scenario
At month end, create a payment application for work completed during the month based on approved BOQ items and progress.

### Steps

#### Step 1: Create Payment Application
1. Go to **TPO Management > Financial & Closure > Payment Applications**
2. Click **Create**

#### Step 2: Fill Application Header
1. **Application Number**: Enter number (e.g., `PA-ART-2025-03` for March 2025)
2. **Project**: Select project
3. **Application Date**: Set application date
4. **Period Start Date**: First day of billing period
5. **Period End Date**: Last day of billing period
6. **Technical Office Engineer**: Assign engineer
7. **Accountant**: Assign accountant

#### Step 3: Add Application Lines
1. Click **Application Lines** tab
2. Click **Add a line**
3. For each item:
   - **Item Code**: Reference to BOQ item code
   - **Description**: Item description
   - **Unit**: Unit of measurement
   - **Planned Quantity**: Total quantity from BOQ
   - **Completed Quantity**: Quantity completed to date
   - **Quantity**: Quantity for this period
   - **Progress Percentage**: Auto-calculated
   - **Unit Price**: Price from approved BOQ
   - **Amount**: Auto-calculated

#### Step 4: Verify Total Amount
1. **Total Amount** auto-calculates from all lines
2. Review total against expected payment

#### Step 5: Verify Work on Site (Optional)
1. If site verification done:
   - Check **Site Verified**
   - Set **Site Verification Date**
   - Add **Site Verification Notes**

#### Step 6: Attach Supporting Documents
1. Attach:
   - Progress photos
   - Material delivery notes
   - Signed inspection reports
   - Any other supporting documents

#### Step 7: Link to Invoice (if created in Accounting)
1. If invoice created in Odoo Accounting:
   - Link **Related Invoice** field
   - Connect payment application to invoice

#### Step 8: Submit Application
1. Review all information
2. Verify calculations
3. Click **Submit**
4. Status changes to "Submitted"

---

## Use Case 10.2: Track Payment Application Status

### Scenario
Track payment application through approval and payment process.

### Steps

#### Step 1: Monitor Status
1. Open payment application
2. Track status progression:
   - `Submitted` → Under client review
   - `Under Review` → Client reviewing
   - `Approved` → Approved for payment
   - `Paid` → Payment received

#### Step 2: Update Status
1. When approved: Click **Approve**
2. When paid: Click **Pay**

---

## Use Case 10.3: Create Retention Release Application

### Scenario
Create payment application for release of retention held from previous payments.

### Steps

#### Step 1: Create Application
1. Create payment application as in Use Case 10.1
2. Mark as retention release in description

#### Step 2: Reference Original Applications
1. Reference original payment applications
2. Calculate retention amount to be released

---

## Best Practices

- **Submit timely** - Submit by contract deadline
- **Reference BOQ** - Always reference approved BOQ items
- **Support with documents** - Include all required supporting documents
- **Verify on site** - Site verification adds credibility
- **Track payments** - Monitor payment status closely

---

## Related Use Cases
- [BOQ Management](../02_pre_execution_planning/boq.md)
- [Change Order Management](../03_execution_monitoring/change_order.md)


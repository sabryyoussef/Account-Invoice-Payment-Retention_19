# Use Case: Shop Drawing Management

## Overview
Shop drawings translate design intent into executable construction instructions. This document covers submission, revision tracking, and approval workflows.

---

## Use Case 5.1: Submit Shop Drawing for Approval

### Scenario
A technical office engineer needs to submit architectural shop drawings for consultant approval before construction.

### Steps

#### Step 1: Create Shop Drawing
1. Go to **TPO Management > Execution & Monitoring > Shop Drawings**
2. Click **Create**

#### Step 2: Fill Drawing Details
1. **Drawing Reference**: Follow naming convention
   - Format: `[Project Code]-SD-[Discipline]-[Number]`
   - Example: `ART-SD-ARCH-001`
2. **Project**: Select project
3. **Discipline**: Select:
   - `Architectural`
   - `Structural`
   - `MEP` (Mechanical, Electrical, Plumbing)
   - `Civil`
   - `Other`
4. **Drawing Number**: Enter drawing number
5. **Description**: Add drawing description
6. **Technical Office Engineer**: Assign engineer
7. **Submission Date**: Set date
8. **Revision Number**: Starts at 0 for initial submission

#### Step 3: Attach Drawing Files
1. Click **Drawings** tab
2. Upload drawing files (PDF, DWG, etc.)
3. Ensure files follow naming convention

#### Step 4: Submit for Approval
1. Review all information
2. Click **Submit**
3. Submission log entry created automatically
4. Status changes to "Submitted"

---

## Use Case 5.2: Resubmit Shop Drawing After Rejection

### Scenario
A shop drawing was rejected with comments, requiring revisions and resubmission.

### Steps

#### Step 1: Review Rejection Comments
1. Open rejected drawing
2. Check Chatter for consultant comments
3. Review rejection reasons

#### Step 2: Make Revisions
1. Update drawing files with corrections
2. Modify description if needed
3. Upload revised drawing files

#### Step 3: Resubmit
1. Click **Resubmit** button
2. Revision number automatically increments (0 → 1)
3. New submission log entry created
4. Status changes to "Resubmitted"

---

## Use Case 5.3: Verify Shop Drawing on Site

### Scenario
After approval, verify that the shop drawing matches the actual construction.

### Steps

#### Step 1: Open Approved Drawing
1. Navigate to approved shop drawings
2. Open the drawing to verify

#### Step 2: Site Verification
1. Click **Verify Site** button
2. Enter **Site Verification Date**
3. Add **Site Verification Notes**:
   - What was verified
   - Any discrepancies found
   - Photos if needed
4. Save

---

## Use Case 5.4: Track Drawing Revision History

### Scenario
Review the complete submission and revision history of a shop drawing.

### Steps

#### Step 1: Open Shop Drawing
1. Navigate to shop drawings
2. Open the drawing

#### Step 2: View Submission Log
1. Click **Submission Log** tab
2. View all submission attempts:
   - Submission dates
   - Revision numbers
   - Status at each submission
   - Response dates
   - Comments

---

## Best Practices

- **Follow naming conventions** strictly
- **Submit complete packages** - all related drawings together
- **Track revisions carefully** - maintain revision history
- **Verify on site** after approval
- **Document all changes** in submission log

---

## Related Use Cases
- [RFI Management](rfi.md)
- [TPO Visits](../05_site_management/tpo_visit.md)


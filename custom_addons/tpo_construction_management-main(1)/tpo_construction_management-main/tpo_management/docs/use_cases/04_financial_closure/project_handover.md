# Use Case: Project Handover Management

## Overview
Project Handover Certificate is the formal document confirming project completion and handover to client. This document covers creating handover checklist, completing items, obtaining signatures, and finalizing handover.

---

## Use Case 12.1: Create Project Handover Certificate

### Scenario
Project is near completion, and handover certificate needs to be prepared with checklist of all completion requirements.

### Steps

#### Step 1: Create Handover Certificate
1. Go to **TPO Management > Financial & Closure > Project Handover**
2. Click **Create**

#### Step 2: Fill Handover Details
1. **Certificate Number**: Enter number (e.g., `HC-ART-001`)
2. **Project**: Select project
3. **Handover Date**: Set planned handover date
4. **Completion Date**: Set actual completion date
5. **Handover Type**: Select:
   - `Partial Handover` - Handing over part of project
   - `Final Handover` - Complete project handover
6. **Project Manager**: Assign project manager
7. **Administration**: Assign administration person
8. **Description**: Handover description

#### Step 3: Create Handover Checklist
1. Click **Handover Checklist** tab
2. Add checklist items (click **Add a line**):

   **Item 1:**
   - **Item**: `All construction work completed`
   - **Description**: Verify all construction activities finished
   - **Completed**: Check when done
   - **Completed Date**: Set date
   - **Completed By**: Assign person

   **Item 2:**
   - **Item**: `As-built drawings submitted and approved`
   - Link to as-built drawings

   **Item 3:**
   - **Item**: `All test certificates provided`
   - Attach test certificates

   **Item 4:**
   - **Item**: `Material warranties submitted`
   - Attach warranty documents

   **Item 5:**
   - **Item**: `Defect liability period conditions explained`
   - Document explanation

   **Continue adding all required items...**

#### Step 4: Link Related Documents
1. Link **Related As-Built Drawings**
2. Ensure all drawings are approved

#### Step 5: Attach Handover Documents
1. Attach:
   - Completion certificates
   - Test reports
   - Warranty documents
   - Operation manuals
   - Any other required documents

---

## Use Case 12.2: Complete Handover Checklist Items

### Scenario
Work through each checklist item, mark completion, and document.

### Steps

#### Step 1: Review Checklist
1. Open handover certificate
2. Review all checklist items
3. Prioritize items that need action

#### Step 2: Complete Each Item
1. For each item:
   - Perform required work/verification
   - Check **Completed** checkbox
   - Set **Completed Date**
   - Assign **Completed By**
   - Add **Notes** if needed

#### Step 3: Verify All Items Completed
1. System shows **All Items Completed** when all checked
2. Verify no items remain incomplete

---

## Use Case 12.3: Obtain Signatures and Finalize Handover

### Scenario
After all checklist items completed, obtain signatures from contractor and client to finalize handover.

### Steps

#### Step 1: Prepare Handover
1. Verify all checklist items completed
2. Ensure all documents attached
3. Click **Prepare** button
4. Status changes to "Prepared"

#### Step 2: Submit for Signatures
1. Click **Submit**
2. Status changes to "Submitted"
3. Send to client for review

#### Step 3: Contractor Signature
1. After client review, obtain contractor signature
2. Upload **Contractor Signature** (scanned or digital)
3. Set **Contractor Signed By** (person who signed)
4. Set **Contractor Signed Date**
5. Click **Sign** button
6. Status changes to "Signed"

#### Step 4: Client Signature
1. Obtain client signature
2. Upload **Client Signature**
3. Set **Client Signed By** (client representative)
4. Set **Client Signed Date**

#### Step 5: Complete Handover
1. Click **Complete** button
2. Status changes to "Completed"
3. Handover is now finalized
4. Project can be marked as completed

---

## Best Practices

- **Start early** - Begin handover preparation before project completion
- **Be thorough** - Ensure all checklist items are complete
- **Document everything** - Keep records of all handover activities
- **Get signatures** - Obtain all required signatures
- **Link documents** - Connect all related project documents

---

## Related Use Cases
- [As-Built Drawing Management](as_built_drawing.md)
- [Payment Application Management](payment_application.md)


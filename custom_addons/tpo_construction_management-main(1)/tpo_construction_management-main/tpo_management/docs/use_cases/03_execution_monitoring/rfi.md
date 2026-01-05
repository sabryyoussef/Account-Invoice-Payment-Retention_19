# Use Case: Request for Information (RFI) Management

## Overview
RFIs are formal documents to clarify discrepancies, errors, omissions, or seek clarifications during construction. This document covers creating, submitting, and managing RFIs.

---

## Use Case 6.1: Create and Submit RFI for Design Clarification

### Scenario
A site engineer discovers a discrepancy between shop drawings and site conditions and needs clarification before proceeding.

### Steps

#### Step 1: Create RFI
1. Go to **TPO Management > Execution & Monitoring > Request for Information (RFI)**
2. Click **Create**

#### Step 2: Fill RFI Details
1. **RFI Number**: Auto-generated (e.g., `RFI-ART-001`)
2. **Project**: Select project
3. **Date**: Set RFI date
4. **Subject**: Enter brief subject (e.g., `Steel beam connection detail discrepancy`)
5. **Issue Type**: Select:
   - `Design Discrepancy`
   - `Omission`
   - `Error`
   - `Clarification Needed`
   - `Unforeseen Condition`
   - `Other`
6. **Priority**: Select:
   - `Low` - Not urgent
   - `Medium` - Normal priority
   - `High` - Important
   - `Urgent` - Requires immediate attention
7. **Location**: Enter specific site location (e.g., `Level 3, Grid A-B`)
8. **Description**: Detailed description of the issue:
   ```
   While installing steel beam connections at Level 3, we found that 
   the shop drawing shows connection type A, but the structural 
   drawings specify connection type B. Please clarify which 
   connection type should be used.
   ```

#### Step 3: Assign Responsible Engineers
1. **Site Engineer**: Assign site engineer
2. **Technical Office Engineer**: Assign if technical office involvement needed

#### Step 4: Request Site Visit (if needed)
1. Check **Site Visit Required** if physical inspection needed
2. Set **Site Visit Date** when scheduled
3. Add **Site Visit Notes** after visit

#### Step 5: Attach Supporting Documents
1. Attach photos of the issue
2. Attach relevant drawings
3. Attach any other supporting documents

#### Step 6: Submit RFI
1. Review all information
2. Click **Submit**
3. Status changes to "Submitted"
4. Notifications sent to recipients

---

## Use Case 6.2: Answer and Close RFI

### Scenario
After receiving response from consultant/client, update RFI with answer and close it.

### Steps

#### Step 1: Open Submitted RFI
1. Navigate to RFIs
2. Filter by status: **Submitted**
3. Open the RFI

#### Step 2: Add Response
1. In **Response** field, enter the answer received:
   ```
   Connection type A should be used as per shop drawing revision 2.
   The structural drawing will be updated accordingly.
   ```
2. Set **Response Date**

#### Step 3: Mark as Answered
1. Click **Answer** button
2. Status changes to "Answered"

#### Step 4: Close RFI
1. Verify issue is resolved
2. Click **Close** button
3. Status changes to "Closed"
4. Add final notes if needed

---

## Use Case 6.3: Create Urgent RFI for Site Issue

### Scenario
An urgent site issue requires immediate clarification to avoid work stoppage.

### Steps

#### Step 1: Create RFI with Urgent Priority
1. Create new RFI as in Use Case 6.1
2. Set **Priority** to `Urgent`
3. Set **Due Date** for response if contractually required
4. Add urgent description explaining time sensitivity

#### Step 2: Notify Immediately
1. Use Chatter to @mention relevant users
2. Send immediate notifications
3. Follow up via phone if critical

---

## Use Case 6.4: Link RFI to Related Documents

### Scenario
Link RFI to related shop drawings, ITRs, or change orders.

### Steps

#### Step 1: Open RFI
1. Navigate to and open the RFI

#### Step 2: Link Related Documents
1. In **Related Shop Drawings** field, select related drawings
2. In **Related ITRs** field, select related ITRs
3. In **Related Change Orders** field, select if RFI leads to change order

---

## Best Practices

- **Be specific** in descriptions and locations
- **Attach photos** for visual clarity
- **Set appropriate priority** - don't overuse urgent
- **Follow up** on unanswered RFIs
- **Close promptly** after resolution
- **Link related documents** for context

---

## Related Use Cases
- [Shop Drawing Management](shop_drawing.md)
- [Change Order Management](change_order.md)
- [TPO Visits](../05_site_management/tpo_visit.md)


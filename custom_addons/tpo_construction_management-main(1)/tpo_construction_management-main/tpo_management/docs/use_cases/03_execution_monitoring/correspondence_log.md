# Use Case: Correspondence Log Management

## Overview
The Correspondence Log is the master log tracking all official communications (letters, emails, memos, faxes) in and out of the project. This document covers logging, tracking, and managing all project correspondence.

---

## Use Case 9.1: Log Incoming Correspondence

### Scenario
A document controller receives an official letter from the client and needs to log it in the system.

### Steps

#### Step 1: Create Correspondence Entry
1. Go to **TPO Management > Execution & Monitoring > Correspondence Log**
2. Click **Create**

#### Step 2: Fill Correspondence Details
1. **Reference**: Enter reference number (e.g., `CORR-ART-001`)
2. **Project**: Select project
3. **Date**: Set correspondence date
4. **Correspondence Type**: Select:
   - `Letter`
   - `Email`
   - `Fax`
   - `Memo`
   - `Other`
5. **Direction**: Select `Incoming`
6. **From**: Select sender partner (client, consultant, etc.)
7. **To**: Select recipient (your company)
8. **Subject**: Enter subject line
9. **Description**: Brief description of content

#### Step 3: Set Priority and Response Requirements
1. **Priority**: Set priority level
2. **Requires Response**: Check if response needed
3. **Received Date**: Set when received

#### Step 4: Attach Original Document
1. Click **Documents** tab
2. Upload:
   - Scanned letter/email
   - PDF attachment
   - Any enclosures

#### Step 5: Link Related Documents
1. Link **Related Shop Drawings** if applicable
2. Link **Related RFIs** if applicable
3. Link **Related Change Orders** if applicable

#### Step 6: Mark as Received
1. Click **Receive** button
2. Status changes to "Received"

---

## Use Case 9.2: Log Outgoing Correspondence

### Scenario
A project manager sends an official letter to the client and needs to log it.

### Steps

#### Step 1: Create Correspondence Entry
1. Create new correspondence as in Use Case 9.1
2. **Direction**: Select `Outgoing`
3. **From**: Your company
4. **To**: Select recipient partner

#### Step 2: Attach Sent Document
1. Attach copy of sent letter/email
2. Include any attachments sent

#### Step 3: Mark as Sent
1. Click **Send** button
2. Status changes to "Sent"
3. Date automatically set

---

## Use Case 9.3: Track Response to Correspondence

### Scenario
Track that a response has been sent for correspondence that required response.

### Steps

#### Step 1: Open Correspondence Requiring Response
1. Navigate to correspondence log
2. Filter by: **Requires Response = Yes**, **Status = Received**
3. Open the correspondence

#### Step 2: Create Response Correspondence
1. Create new outgoing correspondence (as response)
2. Link to original in description or related documents

#### Step 3: Update Original Correspondence
1. Return to original correspondence
2. Set **Response Date**
3. Enter **Response Reference** (reference of response letter)
4. Click **Acknowledge**
5. Status changes to "Acknowledged"

---

## Best Practices

- **Log immediately** - Don't delay logging correspondence
- **Be complete** - Include all details and attachments
- **Link related documents** - Connect to relevant project documents
- **Track responses** - Ensure all required responses are sent
- **Maintain chronology** - Keep dates accurate for audit trail

---

## Related Use Cases
- [RFI Management](rfi.md)
- [Change Order Management](change_order.md)


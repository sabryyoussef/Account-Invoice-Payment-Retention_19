# Use Case: Technical & Financial Offers Management

## Overview
This document covers use cases for creating and managing technical and financial offers for bids, tenders, and commercial proposals.

---

## Use Case 4.1: Create Technical & Financial Offer for Tender

### Scenario
A company needs to prepare a comprehensive technical and financial offer for a construction project tender submission.

### Steps

#### Step 1: Navigate to Technical Offers
1. Go to **TPO Management > Pre-Execution & Planning > Technical & Financial Offers**
2. Click **Create**

#### Step 2: Fill Offer Header
1. **Offer Reference**: Enter reference (e.g., `OFF-ART-2025-001`)
2. **Project**: Select project
3. **Date**: Set offer date
4. **Estimating Department**: Assign department/user
5. **Offer Type**: Select:
   - `Technical Only` - Technical proposal only
   - `Financial Only` - Financial proposal only
   - `Technical & Financial` - Complete offer (most common)
6. **Validity Date**: Enter offer validity period end date
7. **Description**: Add offer description

#### Step 3: Add Offer Items
1. Click **Offer Items** tab
2. Click **Add a line**
3. For each item:
   - **Item Code**: Reference code
   - **Description**: Detailed item description
   - **Unit**: Unit of measurement
   - **Quantity**: Quantity offered
   - **Unit Price**: Price per unit
   - **Amount**: Auto-calculated

#### Step 4: Submit Offer
1. Review total amount
2. Attach supporting documents
3. Click **Submit**

---

## Use Case 4.2: Track Offer Status (Won/Lost)

### Scenario
After submission, track whether the offer was won or lost.

### Steps
1. Open submitted offer
2. Update status:
   - `Won` - If offer was accepted
   - `Lost` - If offer was rejected
3. Add notes about outcome

---

## Related Use Cases
- [BOQ Management](boq.md)
- [Project Setup](../01_project_management/project_setup.md)


# Use Case: Inspection & Test Request (ITR) Management

## Overview
ITRs are formal requests for consultant inspection before proceeding with critical work. This document covers the complete ITR workflow from request to approval.

---

## Use Case 7.1: Request Inspection Before Concrete Pour

### Scenario
Before pouring concrete for a foundation, a site engineer needs to request inspection of rebar and formwork.

### Steps

#### Step 1: Create ITR
1. Go to **TPO Management > Execution & Monitoring > Inspection & Test Request (ITR)**
2. Click **Create**

#### Step 2: Fill ITR Details
1. **ITR Number**: Auto-generated (e.g., `ITR-ART-001`)
2. **Project**: Select project
3. **Request Date**: Set request date
4. **Inspection Type**: Select:
   - `Rebar Inspection`
   - `Pre-Concrete Pour`
   - `Formwork Inspection`
   - `MEP Inspection`
   - `Finishes Inspection`
   - `Final Inspection`
   - `Other`
5. **Location**: Enter specific location (e.g., `Foundation F-01, Grid 3-4`)
6. **Description**: Describe what needs inspection:
   ```
   Request inspection of rebar reinforcement and formwork 
   for Foundation F-01 before concrete pour. All rebar is 
   in place per shop drawing SD-STR-005 Rev 2. Formwork 
   is complete and ready for inspection.
   ```
7. **Priority**: Set priority level
8. **Site Engineer**: Assign site engineer

#### Step 3: Schedule Inspection
1. Set desired **Inspection Date**
2. Click **Submit**
3. After submission, click **Schedule** to confirm date

---

## Use Case 7.2: Record Inspection Results

### Scenario
After inspection is completed, record the results and outcome.

### Steps

#### Step 1: Open Scheduled ITR
1. Navigate to ITRs
2. Filter by status: **Scheduled** or **Inspected**
3. Open the ITR

#### Step 2: Record Inspection Details
1. **Inspector Name**: Enter consultant inspector name
2. **Inspection Date**: Set actual inspection date
3. **Inspection Result**: Select:
   - `Approved` - Work can proceed
   - `Approved as Noted` - Proceed with minor corrections
   - `Rejected` - Work must be corrected
   - `Conditional Approval` - Proceed with conditions
4. **Inspection Notes**: Add detailed notes:
   ```
   Inspection completed. Rebar spacing verified per drawing.
   Formwork dimensions correct. Minor issue with rebar cover 
   at corner - corrected on site. Approved for concrete pour.
   ```

#### Step 3: Record Technical Office Participation
1. If technical office participated, check **Technical Office Participated**
2. Add **Participation Notes** about involvement

#### Step 4: Approve or Reject
1. If approved: Click **Approve**
2. If rejected: Click **Reject** and add rejection reason

---

## Use Case 7.3: Resubmit ITR After Rejection

### Scenario
An ITR was rejected, corrections made, and re-inspection requested.

### Steps

#### Step 1: Review Rejection
1. Open rejected ITR
2. Review inspection notes and rejection reason

#### Step 2: Make Corrections
1. Address all issues mentioned in rejection
2. Document corrections made

#### Step 3: Resubmit
1. Click **Resubmit**
2. Update description with corrections made
3. Set new inspection date if needed
4. Submit again

---

## Best Practices

- **Request inspections early** - Don't wait until last minute
- **Prepare work thoroughly** before inspection
- **Attend inspections** whenever possible
- **Document everything** - photos and detailed notes
- **Follow up promptly** on rejected ITRs

---

## Related Use Cases
- [Shop Drawing Management](shop_drawing.md)
- [RFI Management](rfi.md)
- [TPO Visits](../05_site_management/tpo_visit.md)


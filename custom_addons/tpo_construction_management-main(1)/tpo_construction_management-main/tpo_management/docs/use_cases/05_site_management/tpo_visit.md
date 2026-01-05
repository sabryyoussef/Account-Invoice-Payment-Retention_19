# Use Case: TPO Site Visit Management

## Overview
TPO Visits track site visits by technical office team for measurement, clarification, inspection, and validation purposes. This document covers planning, conducting, and documenting site visits.

---

## Use Case 13.1: Plan Site Visit for Measurement

### Scenario
A site visit is needed to measure actual dimensions for as-built drawings or to verify work progress.

### Steps

#### Step 1: Create Site Visit
1. Go to **TPO Management > TPO Visits**
2. Click **Create**

#### Step 2: Fill Visit Details
1. **Visit Reference**: Enter reference (e.g., `VIS-ART-001`)
2. **Project**: Select project
3. **Visit Date**: Set planned visit date
4. **Visit Time**: Set time of visit
5. **Visit Type**: Select:
   - `Site Measurement & Verification`
   - `RFI Clarification/Investigation`
   - `Shop Drawing Implementation Check`
   - `Change Order Scoping & Validation`
   - `Quality Inspection Participation`
   - `Other`
6. **Location**: Enter specific site location
7. **Purpose**: Describe visit purpose:
   ```
   Measure actual dimensions of completed structure 
   for Level 2 to prepare as-built drawings. Verify 
   column positions and wall dimensions.
   ```

#### Step 3: Assign Participants
1. **Technical Office Engineer**: Assign engineer
2. **Site Engineer**: Assign site engineer
3. **Surveyor**: Assign if survey needed
4. **Project Manager**: Assign if PM attending
5. **Other Participants**: Add any other attendees

#### Step 4: Link Related Documents
1. Link **Related Shop Drawings** if checking implementation
2. Link **Related RFIs** if investigating RFI
3. Link **Related ITRs** if attending inspection
4. Link **Related Change Orders** if scoping change
5. Link **Related As-Built Drawings** if measuring for as-built

#### Step 5: Save Visit Plan
1. Click **Save**
2. Status is "Planned"
3. Visit is scheduled

---

## Use Case 13.2: Conduct Site Visit

### Scenario
On the visit day, conduct the site visit, take measurements/photos, and document findings.

### Steps

#### Step 1: Start Visit
1. Open planned visit
2. Click **Start** button
3. Status changes to "In Progress"

#### Step 2: Document Findings
1. During/after visit, add **Findings**:
   ```
   - All measurements taken for Level 2 columns and walls
   - Found 3 columns shifted 30-50cm from original positions
   - Wall thicknesses verified as per drawings
   - Photos taken of all measured areas
   - Surveyor provided coordinates for key points
   ```

#### Step 3: Add Recommendations
1. Add **Recommendations**:
   ```
   - Update as-built drawings to reflect actual positions
   - Document column shifts in changes description
   - Coordinate with structural engineer if positions affect design
   ```

#### Step 4: Attach Photos and Documents
1. Click **Photos** tab
   - Upload photos taken during visit
   - Organize by location/topic
2. Click **Documents** tab
   - Attach measurement sheets
   - Attach survey reports
   - Attach any other documents

#### Step 5: Record Duration
1. Set **Duration (Hours)**: Time spent on site

---

## Use Case 13.3: Complete Site Visit

### Scenario
After documenting all findings and recommendations, complete the visit record.

### Steps

#### Step 1: Review Visit Documentation
1. Verify all findings are documented
2. Ensure photos are attached
3. Check recommendations are clear

#### Step 2: Complete Visit
1. Click **Complete** button
2. Status changes to "Completed"
3. Visit date automatically set
4. Visit is now closed

---

## Use Case 13.4: Site Visit for RFI Clarification

### Scenario
Visit site to investigate an RFI and clarify the issue with actual site conditions.

### Steps

#### Step 1: Create Visit Linked to RFI
1. Create visit as in Use Case 13.1
2. **Visit Type**: `RFI Clarification/Investigation`
3. Link **Related RFIs** to the specific RFI
4. **Purpose**: Reference the RFI subject and issue

#### Step 2: Conduct Investigation
1. Visit site on scheduled date
2. Investigate the RFI issue
3. Take photos of the problem area
4. Discuss with site team

#### Step 3: Document Findings
1. Document findings in visit record
2. Provide recommendations for resolution
3. Update linked RFI with findings
4. Complete visit

---

## Use Case 13.5: Shop Drawing Implementation Check

### Scenario
Visit site to verify that approved shop drawings are being implemented correctly.

### Steps

#### Step 1: Create Visit
1. Create visit linked to **Related Shop Drawings**
2. **Visit Type**: `Shop Drawing Implementation Check`
3. **Purpose**: Specify which drawings to check

#### Step 2: Verify Implementation
1. Compare actual construction to drawings
2. Check dimensions, positions, details
3. Document any deviations

#### Step 3: Update Shop Drawing
1. If deviations found, update shop drawing record
2. Add site verification notes
3. Mark drawing as site verified if correct

---

## Best Practices

- **Plan ahead** - Schedule visits with sufficient notice
- **Prepare checklist** - Know what to check/measure before visit
- **Document thoroughly** - Take detailed notes and photos
- **Link related documents** - Connect to relevant project documents
- **Follow up** - Ensure recommendations are implemented

---

## Related Use Cases
- [RFI Management](../03_execution_monitoring/rfi.md)
- [Shop Drawing Management](../03_execution_monitoring/shop_drawing.md)
- [Change Order Management](../03_execution_monitoring/change_order.md)
- [As-Built Drawing Management](../04_financial_closure/as_built_drawing.md)

---

**Last Updated**: November 2025


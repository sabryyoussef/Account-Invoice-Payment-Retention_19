# Use Case: As-Built Drawing Management

## Overview
As-Built Drawings document the final constructed state of the project, showing changes from original design. This document covers creating, measuring, and submitting as-built drawings.

---

## Use Case 11.1: Create As-Built Drawing

### Scenario
After construction completion, create as-built drawings showing actual constructed dimensions and changes from original design.

### Steps

#### Step 1: Create As-Built Drawing
1. Go to **TPO Management > Financial & Closure > As-Built Drawings**
2. Click **Create**

#### Step 2: Fill Drawing Details
1. **Drawing Reference**: Enter reference (e.g., `AB-ART-ARCH-001`)
2. **Project**: Select project
3. **Discipline**: Select:
   - `Architectural`
   - `Structural`
   - `MEP`
   - `Civil`
   - `Other`
4. **Drawing Number**: Reference to original drawing
5. **Description**: Description of drawing
6. **Technical Office Engineer**: Assign engineer
7. **Surveyor**: Assign surveyor if available

#### Step 3: Link Original Shop Drawing
1. In **Related Shop Drawings** field, link original shop drawing
2. This helps track what changed

#### Step 4: Document Changes
1. In **Changes Description** field, describe all changes:
   ```
   - Column moved 50cm from original position
   - Additional door added at room 101
   - Window dimensions changed from 1.2m to 1.5m
   - Drainage slope adjusted per site conditions
   ```

#### Step 5: Perform Site Measurement
1. On site, take actual measurements
2. Record measurements in drawing
3. Click **Measure Site** button
4. Set **Site Measurement Date**
5. Add **Site Measurement Notes**

#### Step 6: Create Drawing
1. Update original shop drawing with actual measurements
2. Mark all changes clearly
3. Upload completed as-built drawing

#### Step 7: Complete and Submit
1. Click **Start** to begin work
2. Status changes to "In Progress"
3. When drawing complete: Click **Complete**
4. Status changes to "Completed"
5. Upload final drawing files
6. Click **Submit** for approval

---

## Use Case 11.2: Approve As-Built Drawing

### Scenario
Client/consultant reviews and approves as-built drawing.

### Steps
1. Open submitted as-built drawing
2. Review changes description
3. Verify against site measurements
4. Click **Approve**
5. Status changes to "Approved"

---

## Best Practices

- **Measure accurately** - Use proper surveying equipment
- **Document all changes** - No change is too small
- **Link to originals** - Always link to original shop drawings
- **Complete promptly** - Don't delay as-built drawings
- **Get approvals** - Ensure all drawings are approved

---

## Related Use Cases
- [Shop Drawing Management](../03_execution_monitoring/shop_drawing.md)
- [Project Handover](project_handover.md)


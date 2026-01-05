# Use Case: Creating and Setting Up a TPO Project

## Overview
This use case covers the initial setup of a TPO project, including project creation, team assignment, and configuration for the complete document management cycle.

## Business Context
Before any construction work begins, a project must be properly configured in the system with all necessary information, team members, and project parameters.

## Prerequisites
- User has access to TPO Management module
- User has appropriate permissions (Project Manager or TPO Manager)
- Client/Partner record exists in Odoo

## Use Case 1.1: Create a New TPO Project

### Scenario
A project manager needs to create a new construction project called "Al-Riyadh Tower" for client "ABC Construction Company" and set up the project team.

### Steps

#### Step 1: Navigate to Projects
1. Log in to Odoo
2. Click on **TPO Management** in the main menu
3. Click on **Projects** from the TPO Management menu
4. You will see the Projects list view

#### Step 2: Create New Project
1. Click the **Create** button (or press `Ctrl+N`)
2. The project form will open

#### Step 3: Fill Basic Project Information
1. **Project Code**: This is auto-generated (e.g., `TPO-0001`) - DO NOT EDIT
2. **Project Name**: Enter `Al-Riyadh Tower`
3. **Client**: Click the search icon and select `ABC Construction Company`
   - If client doesn't exist, create it first via Contacts
4. **Project**: (Optional) Link to standard Odoo project if applicable

#### Step 4: Set Project Phase
1. **Current Phase**: Select from dropdown:
   - `Pre-Execution & Planning` (default for new projects)
   - `Execution & Monitoring`
   - `Financial & Closure`

#### Step 5: Set Project Timeline
1. **Start Date**: Click calendar icon and select project start date (e.g., `2025-01-15`)
2. **End Date**: Select expected completion date (e.g., `2026-12-31`)
3. **Handover Date**: Leave blank until project completion

#### Step 6: Assign Project Team
1. **Project Manager**: Select from user dropdown (e.g., `Ahmed Ali`)
   - This person oversees the entire project
2. **Technical Office Engineer**: Select engineer (e.g., `Mohammed Hassan`)
   - Responsible for technical documents and drawings
3. **Site Engineer**: Select site engineer (e.g., `Omar Ibrahim`)
   - Manages site-related documents (RFIs, ITRs)
4. **Document Controller**: Select document controller (e.g., `Sara Ahmed`)
   - Manages correspondence and document logs

#### Step 7: Configure Document Control
1. **Document Control Code**: Enter prefix for document naming (e.g., `ART` for Al-Riyadh Tower)
   - This will be used in naming conventions like: `ART-SD-ARCH-01`
   - Format: `[Project Code]-[Document Type]-[Discipline]-[Revision]`

#### Step 8: Save Project
1. Click **Save** button (or press `Ctrl+S`)
2. Project code is automatically assigned
3. You will see the project form with additional tabs

### Expected Result
- Project is created with auto-generated code
- Project appears in Projects list
- All assigned team members are visible
- Project is ready for document management

---

## Use Case 1.2: Update Project Phase

### Scenario
As the project progresses from planning to execution, the project manager needs to update the current phase.

### Steps

#### Step 1: Open Project
1. Navigate to **TPO Management > Projects**
2. Search for and open the project you want to update

#### Step 2: Change Phase
1. Click on the **Current Phase** field
2. Select the new phase:
   - `Pre-Execution & Planning` → `Execution & Monitoring`
   - `Execution & Monitoring` → `Financial & Closure`
3. Click **Save**

### Expected Result
- Project phase is updated
- System can filter documents by phase
- Relevant menus and workflows become available

---

## Use Case 1.3: View Project Document Summary

### Scenario
A project manager wants to see a quick overview of all documents related to a project.

### Steps

#### Step 1: Open Project
1. Navigate to **TPO Management > Projects**
2. Open the desired project

#### Step 2: View Documents Summary Tab
1. Click on the **Documents Summary** tab
2. View the document counts:
   - **BOQs**: Number of Bill of Quantities
   - **Shop Drawings**: Number of shop drawings
   - **RFIs**: Number of Requests for Information
   - **ITRs**: Number of Inspection & Test Requests
   - **Change Orders**: Number of change orders
   - **Payment Applications**: Number of payment applications

#### Step 3: Access Documents via Smart Buttons
1. Click on any count number to see the list of documents
2. Use the action buttons in the header:
   - **BOQs** button → Opens BOQ list filtered to this project
   - **Shop Drawings** button → Opens shop drawings list
   - **RFIs** button → Opens RFI list

### Expected Result
- Quick overview of all project documents
- Easy navigation to specific document types
- Real-time document counts

---

## Use Case 1.4: Archive or Deactivate a Project

### Scenario
A project is completed or cancelled and needs to be archived (hidden from active view but kept for reference).

### Steps

#### Step 1: Open Project
1. Navigate to **TPO Management > Projects**
2. Open the project to archive

#### Step 2: Deactivate Project
1. Click on the **Active** checkbox to uncheck it
2. Click **Save**

### Expected Result
- Project is hidden from default list view
- Can be viewed by adding "Active = False" filter
- All documents remain accessible
- Historical data is preserved

---

## Use Case 1.5: Search and Filter Projects

### Scenario
A user needs to find specific projects among many active projects.

### Steps

#### Step 1: Use Search Bar
1. Navigate to **TPO Management > Projects**
2. In the search bar, type:
   - Project name: `Al-Riyadh`
   - Project code: `TPO-0001`
   - Client name: `ABC Construction`

#### Step 2: Apply Filters
1. Click the **Filters** button
2. Select from predefined filters:
   - **My Projects**: Shows projects where you are assigned
   - **Active Projects**: Shows only active projects
   - **By Phase**: Filter by current phase
3. Or create custom filter:
   - Click **Add Custom Filter**
   - Select field (e.g., `Project Manager`)
   - Select operator (e.g., `is equal to`)
   - Select value
   - Click **Apply**

#### Step 3: Use Group By
1. Click **Group By** button
2. Group projects by:
   - Project Phase
   - Project Manager
   - Client
   - Start Date

### Expected Result
- Easy project discovery
- Organized view of projects
- Efficient navigation

---

## Best Practices

### Project Creation
- **Complete all fields** during creation to avoid missing information later
- **Assign all team members** upfront to enable proper workflow
- **Set realistic dates** based on project scope
- **Use descriptive project names** for easy identification

### Project Management
- **Update phase regularly** as project progresses
- **Review document summary** frequently to track progress
- **Use filters** to manage multiple projects efficiently
- **Archive completed projects** to keep active list clean

### Document Control
- **Establish clear naming conventions** using Document Control Code
- **Train team members** on naming standards
- **Review document counts** weekly for project health

---

## Related Use Cases

- [BOQ Management](../02_pre_execution_planning/boq.md)
- [Shop Drawing Management](../03_execution_monitoring/shop_drawing.md)
- [RFI Management](../03_execution_monitoring/rfi.md)

---

## Troubleshooting

### Issue: Cannot see Projects menu
**Solution**: Check user permissions - ensure you have TPO Manager or Project Manager role

### Issue: Cannot assign team members
**Solution**: Verify users exist in Odoo and have appropriate access rights

### Issue: Project code not auto-generating
**Solution**: Check if sequence is configured in system parameters

### Issue: Client not appearing in dropdown
**Solution**: Create client first via Contacts app, then return to project creation

---

**Last Updated**: November 2025


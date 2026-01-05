# TPO Construction Management System
## Complete User Guide

---

## 📋 Table of Contents

1. [Introduction](#introduction)
2. [What is TPO?](#what-is-tpo)
3. [System Overview](#system-overview)
4. [Getting Started](#getting-started)
5. [Project Setup](#project-setup)
6. [Pre-Execution & Planning Phase](#pre-execution--planning-phase)
7. [Execution & Monitoring Phase](#execution--monitoring-phase)
8. [Financial & Closure Phase](#financial--closure-phase)
9. [Work Management](#work-management)
10. [Reports & Analytics](#reports--analytics)
11. [Best Practices](#best-practices)

---

## 🎯 Introduction

Welcome to the **TPO Construction Management System** – your complete solution for managing construction projects from planning to handover. This guide will help you understand and use the system effectively, whether you're a project manager, site engineer, or document controller.

### Who Should Use This Guide?
- **Project Managers** - Oversee entire projects and monitor progress
- **TPO Managers** - Manage technical documentation and compliance
- **Site Engineers** - Handle day-to-day site operations and inspections
- **Document Controllers** - Maintain and organize all project documents
- **Technical Office Engineers** - Process submittals, RFIs, and technical documents

---

## 🏗️ What is TPO?

**Technical Project Office (TPO)** is the backbone of construction project management. Think of it as the central hub that:
- **Organizes** all project documents
- **Tracks** work progress from start to finish
- **Ensures** quality and compliance
- **Facilitates** communication between all parties
- **Controls** changes and variations
- **Manages** financial applications and handover

---

## 🌟 System Overview

The TPO Construction Management System consists of **two powerful modules**:

### Module 1: TPO Management
Your complete document and work management system covering:
- Planning documents (BOQ, schedules, submittals)
- Execution documents (shop drawings, RFIs, ITRs)
- Financial documents (payment applications, handover)
- Site visit management
- Document control

### Module 2: TPO Reports
Professional reporting and analytics for:
- Progress tracking
- Document status monitoring
- Financial reporting
- Quality control insights
- Project performance analysis

---

## 🚀 Getting Started

### First Login
1. Log into your Odoo system
2. Look for **TPO Management** in the main menu
3. You'll see organized sections for each project phase

### User Roles & Access
The system has built-in roles:
- **TPO Manager** - Full access to all documents and reports
- **Technical Office Engineer** - Technical document processing
- **Site Engineer** - Site operations and inspections
- **Document Controller** - Document organization and tracking
- **Project Manager** - Project oversight and approval

---

## 📂 Project Setup

### Creating Your First Project

**Step 1: Navigate to Projects**
- Go to **TPO Management → Projects**
- Click the **Create** button

**Step 2: Fill Project Information**
Enter the following details:
- **Project Name** - Full project title (e.g., "Al Riyadh Shopping Mall Construction")
- **Project Code** - Auto-generated unique identifier
- **Client/Customer** - Select from existing contacts or create new
- **Start Date** - Project commencement date
- **Expected End Date** - Planned completion date

**Step 3: Assign Team Members**
Assign key personnel:
- **Project Manager** - Overall project responsibility
- **TPO Manager** - Technical documentation oversight
- **Technical Office Engineer** - Document processing
- **Site Engineer** - Site operations
- **Document Controller** - Document management

**Step 4: Save & Begin**
- Click **Save**
- Your project is now ready for document management!

---

## 📊 Pre-Execution & Planning Phase

This phase sets the foundation for successful project execution.

### 1. Bill of Quantities (BOQ)

**What is it?**
A detailed breakdown of all materials, quantities, and costs for the project.

**How to Create:**
1. Go to **TPO Management → Pre-Execution → Bill of Quantities**
2. Click **Create**
3. Fill in:
   - **Project** - Select your project
   - **BOQ Reference** - Document number
   - **Discipline** - (Civil, MEP, Architectural, etc.)
   - **Prepared By** - Engineer name
   - **Status** - Draft, Approved, Revised, etc.

4. Add line items:
   - **Item Description** - What's being priced
   - **Quantity** - How much
   - **Unit** - Measurement unit (m², m³, kg, etc.)
   - **Unit Rate** - Price per unit
   - **Total** - Auto-calculated

**Use Case:**
"I need to prepare the initial cost estimate for the structural works. I create a BOQ with all concrete, steel, and formwork items with their quantities and unit rates."

---

### 2. Project Schedule (Gantt Chart)

**What is it?**
Your project timeline showing all activities, durations, and dependencies.

**How to Create:**
1. Go to **TPO Management → Pre-Execution → Project Schedule**
2. Click **Create**
3. Define:
   - **Schedule Name** - Baseline, Updated, Final, etc.
   - **Project** - Link to your project
   - **Version** - Track schedule updates
   - **Baseline Start/End Dates**

4. Add activities:
   - **Activity Name** - Task description
   - **Start Date** - When it begins
   - **End Date** - When it completes
   - **Duration** - Auto-calculated
   - **Responsible** - Who's accountable
   - **Progress %** - Track completion

**Use Case:**
"I create a baseline schedule showing all project phases from mobilization to handover, with each activity's start date, duration, and responsible party."

---

### 3. Material Submittal

**What is it?**
Official submission of proposed materials for client/consultant approval.

**How to Create:**
1. Go to **TPO Management → Pre-Execution → Material Submittal**
2. Click **Create**
3. Enter details:
   - **Submittal Number** - Unique reference
   - **Project** - Your project
   - **Material Description** - What you're submitting
   - **Manufacturer** - Brand/supplier
   - **Specification Reference** - Relevant specs
   - **Submission Date**
   - **Required Approval Date**

4. Attach documents:
   - Product catalogs
   - Technical datasheets
   - Test certificates
   - Samples (photo/description)

**Tracking:**
- Monitor status: Submitted → Under Review → Approved/Rejected/Revise & Resubmit
- Track response dates
- Maintain revision history

**Use Case:**
"I'm submitting ceramic tiles for bathroom areas. I attach the manufacturer's catalog, test certificates, and sample photos for consultant approval."

---

### 4. Technical & Financial Offers

**What is it?**
Commercial bids and tenders for project works.

**How to Create:**
1. Go to **TPO Management → Pre-Execution → Technical Offers**
2. Click **Create**
3. Complete:
   - **Offer Reference**
   - **Project**
   - **Client/Recipient**
   - **Offer Date**
   - **Valid Until**
   - **Scope Description**
   - **Total Amount**

**Use Case:**
"I'm preparing a tender response for additional landscaping works, including scope, timeline, and pricing."

---

## 🔨 Execution & Monitoring Phase

This is where construction happens – manage it all here.

### 1. Shop Drawings

**What is it?**
Detailed construction drawings showing exactly how to build elements.

**How to Create:**
1. Go to **TPO Management → Execution → Shop Drawings**
2. Click **Create**
3. Enter:
   - **Drawing Number** - Unique identifier
   - **Drawing Title** - Clear description
   - **Project**
   - **Discipline** - Structural, MEP, Architectural, etc.
   - **Revision Number** - Start with 0, increment with changes
   - **Prepared By** - Draftsman/engineer
   - **Submission Date**

4. Attach drawing files (PDF, DWG)

**Workflow:**
- Submit for review
- Track review status (Approved, Approved with Comments, Rejected)
- Maintain revision history
- Link to related RFIs if needed

**Use Case:**
"I submit shop drawings for the steel structure connections, showing bolt sizes, weld details, and assembly sequence for site execution."

---

### 2. Request for Information (RFI)

**What is it?**
Official questions to clarify design issues, discrepancies, or missing information.

**How to Create:**
1. Go to **TPO Management → Execution → RFI**
2. Click **Create**
3. Fill in:
   - **RFI Number** - Auto-generated or manual
   - **Project**
   - **Subject** - Brief description
   - **Discipline**
   - **Priority** - Low, Medium, High, Critical
   - **Raised By** - Your name
   - **Directed To** - Consultant/Client
   - **Date Raised**
   - **Required By Date** - When you need the answer

4. Describe the question:
   - **Question/Issue** - Detailed description
   - **Proposed Solution** - Your suggestion (optional)
   - **Impact** - Effect on schedule/cost

5. Attach references:
   - Drawing extracts
   - Photos
   - Specification sections

**Tracking:**
- Monitor response status
- Track turnaround time
- Link to affected drawings or schedule activities

**Use Case:**
"The architectural drawings show a door in a location where plumbing is routed. I raise an RFI asking for clarification on which takes priority."

---

### 3. Inspection & Test Request (ITR)

**What is it?**
Official request for consultant inspection before proceeding to next phase.

**How to Create:**
1. Go to **TPO Management → Execution → ITR**
2. Click **Create**
3. Enter details:
   - **ITR Number**
   - **Project**
   - **Location** - Where inspection needed
   - **Work Description** - What to inspect
   - **Inspection Type** - Visual, Testing, Measurement, etc.
   - **Requested Date** - When you need inspector
   - **Requested By** - Site engineer name

4. Add checklist items:
   - Items to be inspected
   - Acceptance criteria
   - Reference standards

**Workflow:**
- Submit request
- Await inspection
- Record result (Passed/Failed)
- Address deficiencies if failed
- Close when passed

**Use Case:**
"Before pouring concrete for Column C-15, I submit an ITR for the consultant to inspect rebar placement, spacing, and cover."

---

### 4. Change Orders (Variation Orders)

**What is it?**
Official documents for changes in scope, quantity, or specification.

**How to Create:**
1. Go to **TPO Management → Execution → Change Orders**
2. Click **Create**
3. Complete:
   - **Change Order Number**
   - **Project**
   - **Title** - Change description
   - **Category** - Addition, Deletion, Modification
   - **Reason** - Client request, site condition, design change, etc.
   - **Date Issued**

4. Detail the change:
   - **Original Work** - What was planned
   - **Changed Work** - What's now required
   - **Quantity Change**
   - **Cost Impact** - Additional/credit
   - **Time Impact** - Schedule extension if needed

5. Attach:
   - Revised drawings
   - Cost breakdown
   - Client approval letter

**Use Case:**
"Client requests adding a service room on the 2nd floor. I create a change order documenting the additional work, cost increase, and 2-week schedule extension."

---

### 5. Correspondence Log

**What is it?**
Central register of all official project communications.

**How to Use:**
1. Go to **TPO Management → Execution → Correspondence Log**
2. Click **Create**
3. Record:
   - **Correspondence Number**
   - **Project**
   - **Date**
   - **From** - Sender
   - **To** - Recipient
   - **Subject**
   - **Type** - Letter, Email, Memo, Meeting Minutes, etc.
   - **Category** - Technical, Commercial, Administrative

4. Attach the actual correspondence

**Benefits:**
- Complete communication history
- Easy retrieval of past correspondence
- Audit trail for disputes
- Reference for decisions made

**Use Case:**
"I log the client's email requesting material substitution, ensuring we have a record of the request and our response."

---

## 💰 Financial & Closure Phase

Manage payments and complete project handover.

### 1. Payment Applications

**What is it?**
Monthly invoices for work completed during the period.

**How to Create:**
1. Go to **TPO Management → Financial → Payment Applications**
2. Click **Create**
3. Enter:
   - **Application Number**
   - **Project**
   - **Billing Period** - Month/dates covered
   - **Submission Date**
   - **Work Completed To Date** - Percentage or value

4. Add work items:
   - **Item Description** - From BOQ
   - **Quantity Completed This Period**
   - **Total Quantity Completed**
   - **Unit Rate**
   - **Amount**

5. Include:
   - Previous payments
   - Current period amount
   - Retention held
   - Net payment due

**Use Case:**
"I prepare the monthly payment application showing 25% progress on structural works, including quantities completed and the amount due for this month."

---

### 2. As-Built Drawings

**What is it?**
Final drawings showing the project as actually constructed.

**How to Create:**
1. Go to **TPO Management → Financial → As-Built Drawings**
2. Click **Create**
3. Enter:
   - **Drawing Number** - Match shop drawing number with "AB" prefix
   - **Drawing Title**
   - **Project**
   - **Discipline**
   - **Finalization Date**

4. Mark all field changes:
   - Show deviations from original design
   - Note all approved changes
   - Indicate final dimensions and materials

**Purpose:**
- Handover requirement
- Future maintenance reference
- Legal record of what was built

**Use Case:**
"I update all electrical drawings to show the actual cable routing which changed during construction due to structural conflicts."

---

### 3. Project Handover Certificate

**What is it?**
Official document confirming project completion and transfer to client.

**How to Create:**
1. Go to **TPO Management → Financial → Project Handover**
2. Click **Create**
3. Complete:
   - **Certificate Number**
   - **Project**
   - **Handover Date**
   - **Handed Over By** - Your company
   - **Received By** - Client representative

4. Checklist:
   - All works completed
   - All snagging items addressed
   - As-built drawings submitted
   - O&M manuals provided
   - Warranties transferred
   - Training completed

5. Attach:
   - Signed completion certificate
   - Defect liability period terms
   - Warranty documents

**Use Case:**
"After completing all punch list items, I prepare the handover certificate with all required documents for the client's signature."

---

## 📍 Work Management

### TPO Site Visits

**What are they?**
Structured site visits for specific technical purposes.

**Visit Types:**
1. **Measurement Visits** - Quantity verification
2. **RFI Clarification** - On-site issue resolution
3. **Shop Drawing Check** - Verify construction vs. drawings
4. **Change Order Scoping** - Assess variation work
5. **Quality Inspection** - Workmanship verification

**How to Create:**
1. Go to **TPO Management → Work Management → TPO Visits**
2. Click **Create**
3. Enter:
   - **Visit Number**
   - **Project**
   - **Visit Type**
   - **Visit Date**
   - **Participants** - Who attended
   - **Purpose** - What to check/verify

4. Record findings:
   - Observations
   - Measurements taken
   - Issues identified
   - Photos
   - Actions required

**Use Case:**
"I schedule a site visit to verify excavation quantities for payment application, taking measurements and photos as evidence."

---

## 📈 Reports & Analytics

The **TPO Reports** module provides powerful insights into your projects.

### Available Reports

#### 1. BOQ Reports
- **What it shows:** Cost breakdown by discipline
- **Use it for:** Budget tracking, variance analysis
- **Export:** PDF, Excel

#### 2. Shop Drawing Status Reports
- **What it shows:** Submission status of all drawings
- **Use it for:** Identifying delayed approvals, tracking revisions
- **Filters:** By discipline, status, date range

#### 3. RFI Tracking Reports
- **What it shows:** All RFIs with response times
- **Use it for:** Monitoring consultant responsiveness
- **Highlights:** Overdue responses, critical RFIs

#### 4. ITR Status Reports
- **What it shows:** Inspection schedules and results
- **Use it for:** Quality control monitoring
- **Includes:** Pass/fail rates, pending inspections

#### 5. Change Order Reports
- **What it shows:** All variations with cost and time impact
- **Use it for:** Contract value tracking
- **Breakdown:** By category, approval status, cumulative impact

#### 6. Payment Application Reports
- **What it shows:** Billing history and outstanding amounts
- **Use it for:** Cash flow analysis, invoice tracking
- **Details:** Progress by item, retention, net payments

#### 7. Document Status Dashboard
- **What it shows:** Overall document health
- **Use it for:** Quick project overview
- **Metrics:** 
  - Documents pending approval
  - Overdue submissions
  - Approval rates by type

#### 8. Submission Log Reports
- **What it shows:** Complete submission history
- **Use it for:** Audit compliance, document tracking
- **Sortable by:** Date, type, status, discipline

#### 9. Project Progress Reports
- **What it shows:** Overall project completion
- **Use it for:** Stakeholder updates, performance review
- **Includes:**
  - Schedule progress
  - Financial progress
  - Document completion rates
  - Key milestones

### How to Generate Reports

**Step 1: Access Reports**
- Go to **TPO Reports** in the main menu

**Step 2: Select Report Type**
- Choose the report you need

**Step 3: Set Filters**
- **Project** - Select specific project or all
- **Date Range** - Custom period
- **Status** - Filter by approval status
- **Discipline** - Filter by trade

**Step 4: Generate & Export**
- Click **Generate Report**
- View on screen
- Export to PDF or Excel
- Print or share

**Pro Tip:** Schedule automated reports to be sent weekly/monthly to project stakeholders!

---

## ✅ Best Practices

### Document Control
1. **Use Standard Naming**
   - Format: `[ProjectCode]-[DocType]-[Discipline]-[Rev]`
   - Example: `RAMS-SD-MEP-R02` (RAMS Project, Shop Drawing, MEP, Revision 2)

2. **Maintain Revision History**
   - Never delete old revisions
   - Track why changes were made
   - Keep superseded documents for reference

3. **Timely Updates**
   - Update document status immediately
   - Record approvals same day
   - Don't let pending items accumulate

### Communication
1. **Log Everything**
   - All official communications in Correspondence Log
   - Attach evidence (emails, meeting minutes)
   - Note verbal agreements in writing

2. **RFI Management**
   - Raise RFIs early – don't wait
   - Be specific in questions
   - Propose solutions where possible
   - Follow up on overdue responses

### Quality Control
1. **ITR Compliance**
   - Request inspection before covering work
   - Allow adequate notice (24-48 hours)
   - Have checklist ready
   - Address failures immediately

2. **Shop Drawing Reviews**
   - Submit with adequate lead time
   - Include all required information
   - Track approval status
   - Don't start work on unapproved drawings

### Financial Management
1. **Payment Applications**
   - Submit on time (usually by 5th of month)
   - Support with accurate measurements
   - Include photos of completed work
   - Track retention releases

2. **Change Orders**
   - Document before execution
   - Get approvals in writing
   - Track cost and time impacts
   - Update BOQ and schedule accordingly

### Project Handover
1. **Start Early**
   - Begin collecting O&M manuals during construction
   - Update as-builts progressively
   - Don't wait until end

2. **Completeness**
   - Verify all items on handover checklist
   - No pending defects or punch items
   - All warranties and guarantees ready
   - Training materials prepared

---

## 🎓 Quick Reference Guide

### Daily Tasks Checklist

**For Site Engineers:**
- [ ] Update ITR results
- [ ] Log daily correspondence
- [ ] Update work progress
- [ ] Raise RFIs for any issues
- [ ] Document site photos

**For Technical Office Engineers:**
- [ ] Review new submittals
- [ ] Process shop drawing reviews
- [ ] Respond to RFI assignments
- [ ] Update BOQ quantities
- [ ] Track document approvals

**For Document Controllers:**
- [ ] Register incoming documents
- [ ] Distribute approved documents
- [ ] Update submission logs
- [ ] File hard copies
- [ ] Generate status reports

**For Project Managers:**
- [ ] Review progress reports
- [ ] Approve change orders
- [ ] Monitor critical RFIs
- [ ] Review payment applications
- [ ] Check schedule updates

---

## 🎨 Tips for Your Canva Presentation

This guide is structured for easy conversion to presentation slides. Here's how:

### Suggested Slide Structure:

1. **Title Slide** - TPO Construction Management System
2. **Introduction** - What is TPO? (Use icon graphics)
3. **System Overview** - Two modules showcase
4. **Project Phases** - Visual timeline of 3 phases
5. **Pre-Execution Phase** - BOQ, Schedule, Submittals (with icons)
6. **Execution Phase** - Shop Drawings, RFI, ITR (with workflow diagrams)
7. **Financial Phase** - Payment, As-Built, Handover (with document icons)
8. **Reports Dashboard** - Screenshots of report types
9. **Best Practices** - Infographic style tips
10. **Benefits Summary** - Key takeaways

### Design Tips:
- Use **construction-themed colors** (orange, yellow, blue, gray)
- Add **icons** for each document type
- Create **workflow diagrams** for processes
- Use **before/after comparisons** for benefits
- Include **screenshots** (if available) of the actual system
- Add **infographics** for statistics and metrics
- Use **timeline graphics** for project phases

### Visual Elements to Include:
- Construction icons (hard hat, blueprint, crane, checklist)
- Document icons (for each document type)
- Workflow arrows showing processes
- Progress bars for project phases
- Team role icons
- Report dashboard mockups

---

## 🚀 Getting Support

If you need help:
1. **Check this guide** - Most answers are here
2. **Contact your system administrator** - For access issues
3. **Reach out to Edafa Co.** - For technical support
   - Website: https://www.edafa.sa

---

## 📝 Summary

The TPO Construction Management System gives you complete control over:
- ✅ All project documentation from planning to handover
- ✅ Work progress tracking and quality control
- ✅ Financial management and payment tracking
- ✅ Communication and correspondence logging
- ✅ Comprehensive reporting and analytics

**Start using it today to transform your construction project management!**

---

*Last Updated: January 2026*  
*Version: 19.0.1.0.0*  
*Created for: Canva Presentation & User Training*

# TPO Management - User Manual

## Table of Contents
1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Project Management](#project-management)
4. [Document Management](#document-management)
5. [Workflow Phases](#workflow-phases)
6. [Reports](#reports)
7. [Frequently Asked Questions](#frequently-asked-questions)

---

## Introduction

The Technical Project Office (TPO) Management system is designed to manage the complete documentary cycle and work control for construction projects. It helps track all project documents from pre-execution planning through execution monitoring to financial closure.

### Key Features

- **Complete Document Lifecycle Management**: Track all project documents from creation to approval
- **Document Control System (DCC)**: Standard naming conventions and submission tracking
- **Multi-Phase Workflow**: Pre-execution, Execution, and Financial phases
- **Comprehensive Reporting**: Generate detailed reports for all document types
- **Site Visit Management**: Track and manage TPO site visits

---

## Getting Started

### Accessing the Module

1. Log in to Odoo
2. Navigate to **TPO Management** from the main menu
3. You will see the main TPO Management dashboard

### User Roles

The system supports different user roles:

- **TPO Manager**: Full access to all features
- **Technical Office Engineer**: Manages technical documents and drawings
- **Site Engineer**: Manages site-related documents (RFIs, ITRs)
- **Document Controller**: Manages correspondence and document logs
- **Project Manager**: Oversees project progress and schedules

---

## Project Management

### Creating a New TPO Project

1. Go to **TPO Management > Projects**
2. Click **Create**
3. Fill in the project details:
   - **Project Code**: Auto-generated (e.g., TPO-0001)
   - **Project Name**: Enter the project name
   - **Client**: Select the client/partner
   - **Project Manager**: Assign project manager
   - **Technical Office Engineer**: Assign technical engineer
   - **Site Engineer**: Assign site engineer
   - **Document Controller**: Assign document controller
4. Set the **Current Phase**: Pre-Execution & Planning (default)
5. Click **Save**

### Project Phases

Projects progress through three main phases:

1. **Pre-Execution & Planning**: Initial planning and documentation
2. **Execution & Monitoring**: Active construction and monitoring
3. **Financial & Closure**: Finalization and handover

---

## Document Management

### Pre-Execution & Planning Phase Documents

#### 1. Bill of Quantities (BOQ)

**Purpose**: Detailed list of materials, quantities, and cost breakdown

**Steps**:
1. Go to **TPO Management > Pre-Execution & Planning > Bill of Quantities**
2. Click **Create**
3. Select the **Project**
4. Fill in BOQ details:
   - **BOQ Reference**: Enter reference number
   - **Date**: Set the date
   - **Technical Office Engineer**: Assign responsible engineer
   - **Estimator**: Assign estimator
5. Add **BOQ Lines**:
   - Click on **BOQ Lines** tab
   - Click **Add a line**
   - Enter: Item Code, Description, Unit, Quantity, Unit Price
   - Amount is calculated automatically
6. Attach documents if needed
7. Click **Submit** to change status to "Submitted"
8. After review, click **Approve** or **Reject**

#### 2. Project Schedule (Gantt Chart)

**Purpose**: Official timeline with activity sequence and dependencies

**Steps**:
1. Go to **TPO Management > Pre-Execution & Planning > Project Schedule**
2. Click **Create**
3. Fill in schedule details:
   - **Schedule Name**: Enter name
   - **Project**: Select project
   - **Project Manager**: Assign project manager
   - **Planner**: Assign planner
   - **Baseline Date**: Set baseline
   - **Planned Start/End Dates**: Set timeline
4. Add **Activities**:
   - Click on **Activities** tab
   - Add activities with:
     - Activity Name
     - Planned Start/End Dates
     - Predecessors (if any)
     - Mark as Critical Path if needed
5. Click **Submit** for approval

#### 3. Material Submittal

**Purpose**: Formal request to approve proposed materials

**Steps**:
1. Go to **TPO Management > Pre-Execution & Planning > Material Submittal**
2. Click **Create**
3. Fill in submittal details:
   - **Submittal Reference**: Enter reference
   - **Project**: Select project
   - **Material Description**: Describe the material
   - **Specification**: Add specifications
   - **Manufacturer**: Enter manufacturer name
   - **Model**: Enter model number
4. Attach documents and samples
5. Click **Submit**
6. Track submission in **Submission Log** tab
7. If rejected, click **Resubmit** (revision number increments automatically)

**Status Flow**: Draft → Submitted → Approved/Rejected → Resubmitted (if needed)

#### 4. Technical & Financial Offers

**Purpose**: Commercial documentation for bids and tenders

**Steps**:
1. Go to **TPO Management > Pre-Execution & Planning > Technical & Financial Offers**
2. Click **Create**
3. Select **Offer Type**: Technical Only, Financial Only, or Both
4. Fill in offer details
5. Add **Offer Lines** with items, quantities, and prices
6. Set **Validity Date**
7. Click **Submit** for review

---

### Execution & Monitoring Phase Documents

#### 1. Shop Drawings

**Purpose**: Detailed drawings translating design into construction instructions

**Steps**:
1. Go to **TPO Management > Execution & Monitoring > Shop Drawings**
2. Click **Create**
3. Fill in drawing details:
   - **Drawing Reference**: Enter reference (follow naming convention)
   - **Project**: Select project
   - **Discipline**: Select (Architectural, Structural, MEP, Civil, Other)
   - **Drawing Number**: Enter drawing number
   - **Description**: Add description
4. Attach drawing files
5. Click **Submit**
6. Track revisions in **Submission Log**
7. After approval, verify on site:
   - Click **Verify Site** button
   - Add verification notes

**Naming Convention**: `[Project Code]-[Document Type]-[Discipline]-[Revision Number]`

#### 2. Request for Information (RFI)

**Purpose**: Formal document to clarify discrepancies or omissions

**Steps**:
1. Go to **TPO Management > Execution & Monitoring > Request for Information (RFI)**
2. Click **Create**
3. Fill in RFI details:
   - **RFI Number**: Auto-generated
   - **Project**: Select project
   - **Subject**: Enter subject
   - **Issue Type**: Select (Discrepancy, Omission, Error, Clarification, etc.)
   - **Priority**: Set priority (Low, Medium, High, Urgent)
   - **Location**: Enter specific site location
   - **Description**: Describe the issue
4. If site visit needed:
   - Check **Site Visit Required**
   - Schedule visit date
   - Add visit notes
5. Click **Submit**
6. After receiving response:
   - Add **Response** text
   - Click **Answer**
   - Click **Close** when resolved

#### 3. Inspection & Test Request (ITR)

**Purpose**: Formal request for consultant inspection before proceeding

**Steps**:
1. Go to **TPO Management > Execution & Monitoring > Inspection & Test Request (ITR)**
2. Click **Create**
3. Fill in ITR details:
   - **ITR Number**: Auto-generated
   - **Project**: Select project
   - **Inspection Type**: Select (Rebar, Pre-Concrete Pour, Formwork, etc.)
   - **Location**: Enter site location
   - **Description**: Describe what needs inspection
   - **Priority**: Set priority
4. Click **Submit**
5. After inspection:
   - Add **Inspection Result** (Approved, Approved as Noted, Rejected)
   - Add **Inspection Notes**
   - Enter **Inspector Name**
   - If Technical Office participated, check the box and add notes
6. Click **Approve** or **Reject**

#### 4. Change Orders / Variation Orders (VO)

**Purpose**: Official documents for contract changes

**Steps**:
1. Go to **TPO Management > Execution & Monitoring > Change Orders / VO**
2. Click **Create**
3. Fill in change order details:
   - **VO Number**: Enter number
   - **Project**: Select project
   - **Change Type**: Select (Scope, Quantity, Specification, Time, Cost)
   - **Subject**: Enter subject
   - **Location**: Enter affected location
   - **Description**: Describe the change
   - **Reason**: Explain why change is needed
4. Add financial impact:
   - **Original Amount**: Enter original amount
   - **Revised Amount**: Enter revised amount
   - Change amount is calculated automatically
5. Add **Change Order Lines**:
   - Original and revised quantities
   - Unit prices
   - Amounts
6. If site visit needed for scoping:
   - Check **Site Visit Required**
   - Add participants
   - Add visit notes
7. Click **Submit** for approval

#### 5. Correspondence Log

**Purpose**: Master log tracking all official communications

**Steps**:
1. Go to **TPO Management > Execution & Monitoring > Correspondence Log**
2. Click **Create**
3. Fill in correspondence details:
   - **Reference**: Enter reference
   - **Project**: Select project
   - **Correspondence Type**: Select (Letter, Email, Fax, Memo)
   - **Direction**: Select (Outgoing or Incoming)
   - **From/To**: Select partners
   - **Subject**: Enter subject
   - **Priority**: Set priority
4. Attach documents
5. If response required:
   - Check **Requires Response**
   - Add response reference when received
6. Click **Send** (for outgoing) or **Receive** (for incoming)

---

### Financial & Closure Phase Documents

#### 1. Payment Applications / Invoices

**Purpose**: Monthly statements for work executed

**Steps**:
1. Go to **TPO Management > Financial & Closure > Payment Applications**
2. Click **Create**
3. Fill in application details:
   - **Application Number**: Enter number
   - **Project**: Select project
   - **Period Start/End Dates**: Set period
   - **Technical Office Engineer**: Assign engineer
   - **Accountant**: Assign accountant
4. Add **Application Lines**:
   - Item descriptions
   - Quantities
   - Unit prices
   - Progress percentages
5. Verify on site:
   - Click **Verify Site** button
   - Add verification notes
6. Click **Submit**
7. After approval, click **Pay**

#### 2. As-Built Drawings

**Purpose**: Final drawings showing actual construction

**Steps**:
1. Go to **TPO Management > Financial & Closure > As-Built Drawings**
2. Click **Create**
3. Fill in drawing details:
   - **Drawing Reference**: Enter reference
   - **Project**: Select project
   - **Discipline**: Select type
   - **Description**: Add description
4. Measure site:
   - Click **Measure Site** button
   - Add measurement notes
5. Add **Changes Description**: Describe changes from original design
6. Attach final drawings
7. Click **Start** to begin work
8. Click **Complete** when finished
9. Click **Submit** for approval

#### 3. Project Handover Certificate

**Purpose**: Formal document confirming project completion

**Steps**:
1. Go to **TPO Management > Financial & Closure > Project Handover**
2. Click **Create**
3. Fill in handover details:
   - **Certificate Number**: Enter number
   - **Project**: Select project
   - **Handover Type**: Select (Partial or Final)
   - **Handover Date**: Set date
4. Complete **Handover Checklist**:
   - Add checklist items
   - Mark items as completed
   - Add completion dates and notes
5. After all items completed:
   - Click **Prepare**
   - Click **Submit**
   - Add signatures (Contractor and Client)
   - Click **Sign**
   - Click **Complete**

---

## Workflow Phases

### Phase 1: Pre-Execution & Planning

**Key Documents**:
- Bill of Quantities (BOQ)
- Project Schedule
- Material Submittal
- Technical & Financial Offers

**Typical Workflow**:
1. Create project
2. Prepare BOQ
3. Create project schedule
4. Submit materials for approval
5. Prepare technical/financial offers

### Phase 2: Execution & Monitoring

**Key Documents**:
- Shop Drawings
- RFIs
- ITRs
- Change Orders
- Correspondence Log

**Typical Workflow**:
1. Submit shop drawings for approval
2. Issue RFIs for clarifications
3. Request ITRs before critical work
4. Process change orders as needed
5. Maintain correspondence log

### Phase 3: Financial & Closure

**Key Documents**:
- Payment Applications
- As-Built Drawings
- Project Handover Certificate

**Typical Workflow**:
1. Submit monthly payment applications
2. Prepare as-built drawings
3. Complete handover checklist
4. Obtain signatures
5. Close project

---

## TPO Visits

### Creating a Site Visit

1. Go to **TPO Management > TPO Visits**
2. Click **Create**
3. Fill in visit details:
   - **Visit Reference**: Enter reference
   - **Project**: Select project
   - **Visit Type**: Select type:
     - Site Measurement & Verification
     - RFI Clarification/Investigation
     - Shop Drawing Implementation Check
     - Change Order Scoping & Validation
     - Quality Inspection Participation
   - **Location**: Enter site location
   - **Purpose**: Describe purpose
   - **Participants**: Select team members
4. After visit:
   - Add **Findings**
   - Add **Recommendations**
   - Attach photos and documents
   - Link related documents (Shop Drawings, RFIs, etc.)
5. Click **Complete**

---

## Reports

The TPO Reports module provides comprehensive reporting capabilities:

### Available Reports

1. **BOQ Report**: Detailed BOQ with all line items
2. **Shop Drawing Status Report**: Status and revision history
3. **RFI Tracking Report**: All RFIs with responses
4. **ITR Status Report**: Inspection results and notes
5. **Change Order Report**: All change orders with financial impact
6. **Payment Application Report**: Payment applications with line items
7. **Document Status Dashboard**: Overview of all document types
8. **Submission Log Report**: Complete submission history
9. **Project Progress Report**: Overall project progress

### Generating Reports

1. Go to **TPO Management > TPO Reports**
2. Select the desired report
3. Choose project(s) and date range
4. Click **Print** or **Generate**

---

## Document Control System (DCC)

### Naming Convention

All documents should follow the standard naming convention:

**Format**: `[Project Code]-[Document Type]-[Discipline]-[Revision Number]`

**Example**: `TPO-0001-SD-ARCH-01`
- TPO-0001: Project Code
- SD: Shop Drawing
- ARCH: Architectural
- 01: Revision 01

### Submission Log

The system automatically maintains submission logs for:
- Shop Drawings
- Material Submittals

Each submission records:
- Submission Date
- Revision Number
- Status
- Response Date
- Comments

---

## Frequently Asked Questions

### Q: How do I track document revisions?

**A**: The system automatically tracks revisions in the Submission Log. Each time you resubmit a document, the revision number increments automatically.

### Q: Can I link related documents?

**A**: Yes, most documents have fields to link related documents. For example, RFIs can be linked to Shop Drawings and ITRs.

### Q: How do I know which documents need attention?

**A**: Use the Document Status Dashboard report to see an overview of all document statuses. You can also filter by state in list views.

### Q: Can I export data?

**A**: Yes, you can export any list view to Excel or CSV using the standard Odoo export functionality.

### Q: How do I manage document approvals?

**A**: Use the status bar in each document form. Documents flow through: Draft → Submitted → Approved/Rejected. Some documents support additional states like "Approved as Noted" or "Resubmitted".

### Q: What if I need to make changes after approval?

**A**: For documents that support resubmission (Shop Drawings, Material Submittals), you can click **Resubmit** which will increment the revision number and change status to "Resubmitted".

---

## Support

For technical support or questions, please contact:
- **System Administrator**
- **TPO Manager**

---

**Last Updated**: November 2025


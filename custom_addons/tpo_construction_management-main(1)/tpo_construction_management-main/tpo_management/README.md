# TPO Management - Technical Project Office

## Overview

This module provides comprehensive document management and work control for Technical Project Office (TPO) operations in construction projects.

## Features

### Pre-Execution & Planning Phase
- **Bill of Quantities (BOQ)**: Detailed list specifying materials, quantities, and cost breakdown
- **Project Schedule (Gantt Chart)**: Official timeline with activity sequence and dependencies
- **Material Submittal**: Formal request to approve proposed materials with samples and specifications
- **Technical & Financial Offers**: Commercial documentation for bids and tenders

### Execution & Monitoring Phase
- **Shop Drawings**: Detailed drawings translating design intent into executable construction instructions
- **Request for Information (RFI)**: Formal documents to clarify discrepancies, errors, or omissions
- **Inspection & Test Request (ITR)**: Formal requests for consultant inspection before proceeding
- **Change Orders / Variation Orders (VO)**: Official documents for contract scope, quantity, or specification changes
- **Correspondence Log**: Master log tracking all official communications

### Financial & Closure Phase
- **Payment Applications / Invoices**: Monthly statements for work executed
- **As-Built Drawings**: Final drawings showing the structure as actually constructed
- **Project Handover Certificate**: Formal document confirming project completion and handover

### Work Management
- **TPO Visit Tasks**: Track site visits for measurement, RFI clarification, shop drawing checks, change order scoping, and quality inspections
- **Document Control System (DCC)**: Standard naming conventions and submission logs
- **Technical Task Management**: Link tasks to project schedule with prioritization

## Installation

1. Copy the module to your Odoo addons directory
2. Update the apps list in Odoo
3. Install the module from Apps menu

## Configuration

1. Create user groups as needed:
   - TPO Manager
   - Technical Office Engineer
   - Site Engineer
   - Document Controller
   - Project Manager

2. Assign users to appropriate groups

3. Create TPO Projects and start managing documents

## Usage

### Creating a TPO Project

1. Go to **TPO Management > Projects**
2. Click **Create**
3. Fill in project details:
   - Project Code (auto-generated)
   - Project Name
   - Client
   - Project Manager
   - Technical Office Engineer
   - Site Engineer
   - Document Controller

### Managing Documents

All documents are organized by project and phase. Each document type has its own menu under the appropriate phase section.

### Document Control

- Use standard naming convention: `[Project Code]-[Document Type]-[Discipline]-[Revision Number]`
- Track submission status and revision history
- Maintain central repository of all documents

## Support

For support, please contact your system administrator.

## License

AGPL-3


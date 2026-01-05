# TPO Management - Technical Manual

## Table of Contents
1. [Architecture Overview](#architecture-overview)
2. [Module Structure](#module-structure)
3. [Models](#models)
4. [Views](#views)
5. [Security](#security)
6. [Workflows](#workflows)
7. [Integration Points](#integration-points)
8. [Customization Guide](#customization-guide)
9. [Troubleshooting](#troubleshooting)

---

## Architecture Overview

The TPO Management system is built on Odoo 19 framework and follows standard Odoo development patterns:

- **Model-View-Controller (MVC) Architecture**
- **ORM-based Data Access**
- **XML-based View Definitions**
- **Security Rules and Access Control**

### Technology Stack

- **Backend**: Python 3.x with Odoo Framework
- **Frontend**: Odoo Web Framework (JavaScript/XML)
- **Database**: PostgreSQL (via Odoo ORM)
- **Reporting**: QWeb Templates

---

## Module Structure

```
tpo_management/
├── __init__.py                 # Module initialization
├── __manifest__.py             # Module manifest
├── models/                     # Python models
│   ├── __init__.py
│   ├── tpo_project.py         # Main project model
│   ├── boq.py                  # Bill of Quantities
│   ├── project_schedule.py    # Project Schedule
│   ├── material_submittal.py   # Material Submittal
│   ├── technical_offer.py      # Technical Offers
│   ├── shop_drawing.py         # Shop Drawings
│   ├── rfi.py                  # Request for Information
│   ├── itr.py                  # Inspection & Test Request
│   ├── change_order.py         # Change Orders
│   ├── correspondence_log.py  # Correspondence Log
│   ├── payment_application.py # Payment Applications
│   ├── as_built_drawing.py     # As-Built Drawings
│   ├── project_handover.py     # Project Handover
│   └── tpo_visit.py            # TPO Visits
├── views/                      # XML views
│   ├── menu_views.xml          # Menu definitions
│   ├── tpo_project_views.xml  # Project views
│   ├── boq_views.xml           # BOQ views
│   └── ...                     # Other view files
├── security/                   # Security definitions
│   ├── ir.model.access.csv     # Access rights
│   └── security.xml            # User groups
├── data/                       # Data files
│   ├── sequence_data.xml       # Sequences
│   └── document_type_data.xml # Document types
├── i18n/                       # Translations
│   └── ar.po                   # Arabic translation
└── docs/                       # Documentation
    ├── USER_MANUAL.md
    ├── USER_MANUAL_AR.md
    ├── TECHNICAL_MANUAL.md
    └── TECHNICAL_MANUAL_AR.md
```

---

## Models

### Core Models

#### 1. TPO Project (`tpo.project`)

**Purpose**: Main project container

**Key Fields**:
- `name`: Project name
- `code`: Project code (auto-generated)
- `partner_id`: Client/Partner
- `phase`: Current project phase
- `project_manager_id`: Project manager
- `technical_office_engineer_id`: Technical engineer
- `site_engineer_id`: Site engineer
- `document_controller_id`: Document controller

**Relations**:
- One2many to all document types
- Computed fields for document counts

**Methods**:
- `_compute_document_counts()`: Computes document counts
- `name_get()`: Custom display name with code

#### 2. BOQ (`tpo.boq`)

**Purpose**: Bill of Quantities

**Key Fields**:
- `name`: BOQ reference
- `project_id`: Related project
- `state`: Status (draft, submitted, approved, rejected)
- `total_amount`: Computed total
- `line_ids`: One2many to `tpo.boq.line`

**Methods**:
- `action_submit()`: Submit for approval
- `action_approve()`: Approve BOQ
- `action_reject()`: Reject BOQ
- `_compute_total_amount()`: Calculate total from lines

#### 3. Shop Drawing (`tpo.shop.drawing`)

**Purpose**: Shop drawings with revision tracking

**Key Fields**:
- `name`: Drawing reference
- `discipline`: Drawing discipline
- `revision_number`: Current revision
- `submission_log_ids`: One2many to log entries
- `site_verified`: Site verification flag

**Methods**:
- `action_submit()`: Submit drawing
- `action_resubmit()`: Resubmit with new revision
- `action_verify_site()`: Mark as site verified

**Log Model**: `tpo.shop.drawing.log`
- Tracks all submission attempts
- Records revision numbers and status changes

#### 4. RFI (`tpo.rfi`)

**Purpose**: Request for Information

**Key Fields**:
- `name`: RFI number
- `issue_type`: Type of issue
- `priority`: Priority level
- `location`: Site location
- `site_visit_required`: Flag for site visit
- `response`: Response text

**Methods**:
- `action_submit()`: Submit RFI
- `action_answer()`: Mark as answered
- `action_schedule_site_visit()`: Schedule site visit

#### 5. ITR (`tpo.itr`)

**Purpose**: Inspection & Test Request

**Key Fields**:
- `name`: ITR number
- `inspection_type`: Type of inspection
- `inspection_result`: Result of inspection
- `technical_office_participated`: Participation flag

**Methods**:
- `action_submit()`: Submit ITR
- `action_inspect()`: Mark as inspected
- `action_approve()`: Approve inspection

#### 6. Change Order (`tpo.change.order`)

**Purpose**: Variation Orders

**Key Fields**:
- `name`: VO number
- `change_type`: Type of change
- `original_amount`: Original contract amount
- `revised_amount`: Revised amount
- `change_amount`: Computed difference
- `line_ids`: One2many to change order lines

**Methods**:
- `action_submit()`: Submit for approval
- `action_approve()`: Approve change order
- `_compute_change_amount()`: Calculate change amount

#### 7. Payment Application (`tpo.payment.application`)

**Purpose**: Payment applications/invoices

**Key Fields**:
- `name`: Application number
- `period_start_date`: Period start
- `period_end_date`: Period end
- `total_amount`: Computed total
- `site_verified`: Site verification flag
- `line_ids`: One2many to application lines

**Methods**:
- `action_submit()`: Submit application
- `action_approve()`: Approve application
- `action_verify_site()`: Verify on site

#### 8. TPO Visit (`tpo.visit`)

**Purpose**: Site visit tracking

**Key Fields**:
- `name`: Visit reference
- `visit_type`: Type of visit
- `location`: Site location
- `purpose`: Visit purpose
- `findings`: Visit findings
- `recommendations`: Recommendations
- Multiple Many2many relations to related documents

**Methods**:
- `action_start()`: Start visit
- `action_complete()`: Complete visit

---

## Views

### View Types

1. **List Views**: Display records in table format
2. **Form Views**: Detailed record editing
3. **Kanban Views**: Card-based display (if implemented)
4. **Search Views**: Filtering and searching

### Key View Features

- **Status Bars**: Visual workflow indicators
- **Smart Buttons**: Quick access to related records
- **Editable Lists**: Inline editing for line items
- **Document Attachments**: File upload and management
- **Chatter**: Activity and message tracking

---

## Security

### User Groups

Defined in `security/security.xml`:

1. **TPO Manager** (`group_tpo_manager`)
   - Full access to all features

2. **Technical Office Engineer** (`group_tpo_technical_office_engineer`)
   - Access to technical documents

3. **Site Engineer** (`group_tpo_site_engineer`)
   - Access to site-related documents

4. **Document Controller** (`group_tpo_document_controller`)
   - Access to correspondence and logs

5. **Project Manager** (`group_tpo_project_manager`)
   - Access to project management features

### Access Rights

Defined in `security/ir.model.access.csv`:

- Standard CRUD permissions per model
- Group-based access control
- All models accessible to base.group_user by default

---

## Workflows

### Document State Flows

#### Standard Flow
```
Draft → Submitted → Approved/Rejected
```

#### With Resubmission
```
Draft → Submitted → Rejected → Resubmitted → Submitted → Approved
```

#### Payment Application Flow
```
Draft → Submitted → Under Review → Approved → Paid
```

### State Management

States are managed through:
- **Status Bar Widget**: Visual state indicator
- **Action Methods**: State transition methods
- **Computed Fields**: State-dependent calculations

---

## Integration Points

### Odoo Standard Modules

1. **Project Module** (`project`)
   - Links to `project.project` for integration

2. **Account Module** (`account`)
   - Payment applications can link to invoices

3. **Mail Module** (`mail`)
   - Chatter integration for all models
   - Activity tracking
   - Message notifications

4. **Document Module** (`document`)
   - File attachment support

### External Integrations

- **File Storage**: Standard Odoo attachment system
- **Email**: Via mail module
- **Reporting**: QWeb templates for PDF reports

---

## Customization Guide

### Adding a New Document Type

1. **Create Model** (`models/new_document.py`):
```python
class TPONewDocument(models.Model):
    _name = 'tpo.new.document'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(required=True)
    project_id = fields.Many2one('tpo.project', required=True)
    state = fields.Selection([...])
    # Add other fields
```

2. **Create Views** (`views/new_document_views.xml`):
```xml
<record id="view_tpo_new_document_form" model="ir.ui.view">
    <!-- Form view definition -->
</record>
```

3. **Add Menu** (`views/menu_views.xml`):
```xml
<menuitem name="New Document" 
          parent="menu_tpo_root" 
          action="action_tpo_new_document"/>
```

4. **Add Security** (`security/ir.model.access.csv`):
```csv
access_tpo_new_document_user,tpo.new.document.user,model_tpo_new_document,base.group_user,1,1,1,1
```

5. **Update Manifest** (`__manifest__.py`):
```python
'data': [
    # ... existing files
    'views/new_document_views.xml',
]
```

### Extending Existing Models

Use `_inherit` to extend models:

```python
class TPOProjectExtension(models.Model):
    _inherit = 'tpo.project'
    
    new_field = fields.Char(string='New Field')
    
    def new_method(self):
        # Custom logic
        pass
```

### Custom Workflows

Override action methods to customize workflows:

```python
def action_submit(self):
    # Custom validation
    if not self.custom_validation():
        raise UserError(_("Validation failed"))
    
    # Call parent method
    super().action_submit()
    
    # Additional logic
    self.send_notification()
```

---

## Troubleshooting

### Common Issues

#### 1. Documents Not Appearing in Project

**Problem**: Documents created but not showing in project view

**Solution**:
- Check `project_id` is set correctly
- Verify access rights
- Check domain filters in views

#### 2. Revision Numbers Not Incrementing

**Problem**: Resubmit doesn't increment revision

**Solution**:
- Check `action_resubmit()` method
- Verify `revision_number` field is being updated
- Check for validation errors

#### 3. Submission Log Not Creating

**Problem**: Log entries not created on submit

**Solution**:
- Check `action_submit()` method
- Verify log model exists
- Check for permission errors

#### 4. Computed Fields Not Updating

**Problem**: Computed totals not refreshing

**Solution**:
- Check `@api.depends` decorator
- Verify dependencies are correct
- Use `invalidate_recordset()` if needed

### Debugging Tips

1. **Enable Developer Mode**: Access technical features
2. **Check Logs**: Review Odoo server logs
3. **Use Debugger**: Set breakpoints in Python code
4. **Test in Console**: Use Odoo shell for testing
5. **Check Database**: Direct SQL queries for verification

### Performance Optimization

1. **Index Fields**: Add database indexes for frequently searched fields
2. **Batch Operations**: Use `create()` with `vals_list` for bulk operations
3. **Lazy Loading**: Use `read_group()` for aggregations
4. **Cache Management**: Proper use of `invalidate_recordset()`

---

## Best Practices

### Code Organization

1. **Model Separation**: One model per file
2. **View Organization**: Group related views
3. **Security First**: Define access rights early
4. **Documentation**: Comment complex logic

### Naming Conventions

1. **Models**: `tpo.model.name` (lowercase with underscores)
2. **Fields**: `field_name` (lowercase with underscores)
3. **Methods**: `action_method_name()` (action prefix for buttons)
4. **Views**: `view_model_type` (descriptive names)

### Data Integrity

1. **Required Fields**: Mark critical fields as required
2. **Constraints**: Use `@api.constrains` for validation
3. **Defaults**: Provide sensible defaults
4. **Onchange**: Use `@api.onchange` for UI logic

---

## API Reference

### Common Patterns

#### Creating Records
```python
self.env['tpo.boq'].create({
    'name': 'BOQ-001',
    'project_id': project_id,
    'date': fields.Date.today(),
})
```

#### Searching Records
```python
boqs = self.env['tpo.boq'].search([
    ('project_id', '=', project_id),
    ('state', '=', 'approved'),
])
```

#### Updating Records
```python
record.write({
    'state': 'approved',
    'approval_date': fields.Date.today(),
})
```

#### Computed Fields
```python
@api.depends('line_ids.amount')
def _compute_total(self):
    for record in self:
        record.total = sum(record.line_ids.mapped('amount'))
```

---

## Version History

- **19.0.1.0.0**: Initial release
  - Complete document management system
  - All three workflow phases
  - TPO visit tracking
  - Integration with reporting module

---

**Last Updated**: November 2025


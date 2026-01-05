# -*- coding: utf-8 -*-
{
    'name': 'Technical Project Office (TPO)',
    'version': '19.0.1.0.0',
    'category': 'Project',
    'summary': 'Documentary Cycle and Work Management for Technical Project Office',
    'description': """
        TPO Management System
        =====================
        
        This module provides comprehensive document management and work control
        for Technical Project Office (TPO) operations.
        
        Features:
        ---------
        * Pre-Execution & Planning Phase Documents
          - Bill of Quantities (BOQ)
          - Project Schedule (Gantt Chart)
          - Material Submittal
          - Technical & Financial Offers
        
        * Execution & Monitoring Phase Documents
          - Shop Drawings
          - Request for Information (RFI)
          - Inspection & Test Request (ITR)
          - Change Orders / Variation Orders (VO)
          - Correspondence Log
        
        * Financial & Closure Phase Documents
          - Payment Applications / Invoices
          - As-Built Drawings
          - Project Handover Certificate
        
        * Document Control System (DCC)
        * Technical Task Management
        * TPO Visit Tasks
    """,
    'author': 'Edafa',
    'company': 'Edafa Co.',
    'website': 'https://www.edafa.sa',
    'license': 'AGPL-3',
    'depends': [
        'base',
        'project',
        'account',
        'purchase',
        'mail',
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/sequence_data.xml',
        'data/document_type_data.xml',
        'views/tpo_project_views.xml',
        'views/boq_views.xml',
        'views/project_schedule_views.xml',
        'views/material_submittal_views.xml',
        'views/technical_offer_views.xml',
        'views/shop_drawing_views.xml',
        'views/rfi_views.xml',
        'views/itr_views.xml',
        'views/change_order_views.xml',
        'views/correspondence_log_views.xml',
        'views/payment_application_views.xml',
        'views/as_built_drawing_views.xml',
        'views/project_handover_views.xml',
        'views/tpo_visit_views.xml',
        'views/menu_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'icon': 'static/description/icon.svg',
}


# -*- coding: utf-8 -*-
{
    'name': 'TPO Reports - Technical Project Office',
    'version': '19.0.1.0.0',
    'category': 'Reporting',
    'summary': 'Detailed Reports for Technical Project Office',
    'description': """
        TPO Reports Module
        ==================
        
        This module provides comprehensive reporting capabilities for
        Technical Project Office (TPO) operations.
        
        Features:
        ---------
        * BOQ Reports
        * Shop Drawing Status Reports
        * RFI Tracking Reports
        * ITR Status Reports
        * Change Order Reports
        * Payment Application Reports
        * Document Status Dashboard
        * Submission Log Reports
        * Project Progress Reports
    """,
    'author': 'Edafa',
    'company': 'Edafa Co.',
    'website': 'https://www.edafa.sa',
    'license': 'AGPL-3',
    'depends': [
        'base',
        'tpo_management',
    ],
    'data': [
        'security/ir.model.access.csv',
        'reports/report_actions.xml',
        'reports/boq_report.xml',
        'reports/shop_drawing_report.xml',
        'reports/rfi_report.xml',
        'reports/itr_report.xml',
        'reports/change_order_report.xml',
        'reports/payment_application_report.xml',
        'reports/document_status_report.xml',
        'reports/submission_log_report.xml',
        'reports/project_progress_report.xml',
        'views/report_menus.xml',
        'views/report_wizard_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}


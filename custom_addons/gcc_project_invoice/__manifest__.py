# -*- coding: utf-8 -*-
{
    "name": "GCC Project Invoice (Advance, Retention, Deductions)",
    "version": "19.0.1.0.0",
    "category": "Accounting/Accounting",
    "summary": "Project invoicing with advance payment deduction, retention, performance bond and penalties",
    "description": """
        Extends customer invoices with:
        - Contract/PO/Invoice references
        - Advance payment deduction (dedicated account, not reserve)
        - Penalties & deductions
        - Performance bond
        - Retention %
        Creates extra journal lines on post to split receivable (receivable, retention receivable, performance bond, advance, deductions).
    """,
    "author": "GCC",
    "license": "LGPL-3",
    "depends": ["account"],
    "data": [
        "views/account_move_views.xml",
        "views/res_config_settings_views.xml",
    ],
    "installable": True,
    "application": False,
}

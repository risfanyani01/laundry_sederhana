# -*- coding: utf-8 -*-
{
    'name': "module_costum/m_laundry",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management', 'hr', 'account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/m_cucian_view.xml',
        'views/menu_item_views.xml',
        'views/jenis_cucian_view.xml',
        'views/m_karyawan_view.xml',
        'views/m_transaksi_view.xml',
        # 'report/cucian_report_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    # 'application' : True,
    # 'installable' : True,
}

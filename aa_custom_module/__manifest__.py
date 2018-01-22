# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Custom Module',
    'version' : '1.1',
    # 'summary': 'Send Invoices and Track Payments',
    'description':'Here goes Description of our new module ',
    # 'images' : ['images/accounts.jpeg','images/bank_statement.jpeg','images/cash_register.jpeg','images/chart_of_accounts.jpeg','images/customer_invoice.jpeg','images/journal_entries.jpeg'],
    'depends' : ['base','sale'],
    'data': [
        'views/custom_view.xml',
    ],
    
    'installable': True,
    # 'application': False,
    # 'auto_install': False,
    # 'post_init_hook': '_auto_install_l10n',
}

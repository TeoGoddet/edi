# Copyright 2019 Tecnativa - Ernesto Tejeda
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Voxel sale order",
    "summary": "Import sale order from Voxel.",
    "version": "11.0.1.0.0",
    "category": "Sale",
    "author": "Tecnativa, Odoo Community Association (OCA)",
    "website": "https://github.com/oca/edi/",
    "license": "AGPL-3",
    "depends": [
        "edi_voxel",
        "sale",
        "sale_order_dates",
    ],
    "data": [
        'security/ir.model.access.csv',
        'security/voxel_sale_order_security.xml',
        'data/ir_cron_data.xml',
        'views/res_company_views.xml',
        'views/res_config_settings_views.xml',
        'views/sale_order_views.xml',
    ],
    "installable": True,
}

from odoo import models, fields

class CustomModel(models.Model):
    _name = 'custom.model'
    name = fields.Char(string='Name')
    age = fields.Integer("your Age")


class SaleOrderInherited(models.Model):
    _inherit = 'sale.order'
    custom_field = fields.Char(string="Custom Field sankey")
  


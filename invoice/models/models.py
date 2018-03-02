# -*- coding: utf-8 -*-

from odoo import models, fields, api

class invoice(models.Model):
 _inherit = 'account.invoice'

 royal_quantity = fields.Integer(compute="get_quantity_",string='Cantidades', copy=False,readonly=True)
 royal_money = fields.Integer(compute="get_money_",string='Costo Lps',copy=False,readonly=True)
#Show the royalties amounts
 @api.one   
 def get_quantity_(self):
     for invoice in self:
          for inv_line in invoice.invoice_line_ids:
              if inv_line.price_unit == 0.00: 
                 self.royal_quantity  += inv_line.quantity
#Show the money amounts
 @api.one   
 def get_money_(self):
     for invoice in self:
          for inv_line in invoice.invoice_line_ids:
              if inv_line.price_unit == 0.00: 
                 self.royal_money  += inv_line.quantity * (inv_line.product_id.standard_price)
                
                
class sale_order_(models.Model):
 _inherit = 'sale.order'
 
 royal_quantity_order = fields.Integer(compute="get_quantity_",string='Cantidades', copy=False,readonly=True)
 royal_money_order = fields.Integer(compute="get_price_",string='Costo Lps',copy=False,readonly=True)
 #Show the royalties amounts
 @api.one   
 def get_quantity_(self):
     for order in self:
          for order_line in order.order_line:
              if order_line.price_unit == 0.00: 
                 self.royal_quantity_order  += order_line.product_uom_qty
                
 
 @api.one                
 def get_price_(self):
     for order in self:
          for order_line in order.order_line:
              if order_line.price_unit == 0.00: 
                 self.royal_money_order  += order_line.product_uom_qty * (order_line.product_id.standard_price)
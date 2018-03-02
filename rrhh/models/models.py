# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, date, time, timedelta
import re
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta

class rrhh(models.Model):
   _inherit = 'hr.employee'

   date_ = fields.Datetime("Fecha de Ingreso")
   date_string = fields.Char(compute='get_str')
   func_general = fields.Text("Funcion General", size=200)
   addrs = fields.Text("Funcion General", size=100)
   date_number = fields.Char("# Dias en la Empresa",compute='get_date')
   acc_are = fields.Selection([('1', 'Nacional'),('2', 'Internacional')])
   relacc_ext = fields.Selection([('1', 'Clientes'),('2', 'Proveedores')])
   objti = fields.Text("Objetivos", size=200)
   relacc_in = fields.Many2many('hr.department')
   rtn = fields.Char("RTN", size=16)
   child = fields.Integer("Hijos?") 
   #edu = fields.Selection([('1', 'Primaria'),('2', 'Secundaria'),('3', 'Superior'),('4', 'Postgrado'),('4', 'Master'),('5', 'Doctor')])
   salary = fields.Integer("Salario")
   email_per = fields.Char()    
   height_ = fields.Float("Estatura")    
   weight_ = fields.Float("Peso")
   age_ = fields.Char(compute='set_age')
   fami_datails = fields.One2many('info.family','id' ,copy=True,required=True)
   studies_datails = fields.One2many('info.studies','id' ,copy=True,required=True)
   license = fields.Boolean("Licencia de Conducir?")    
   type_livi = fields.Boolean("Liviana")
   type_pesada = fields.Boolean("Pesada")   
   number_license = fields.Char(size=16)

    
   @api.one
   def set_age(self):
       for rec in self:
           if rec.birthday:
              datee = datetime(rec.birthday)
              #d = datetime(int(datee.year),int(datee.month), int(datee.day))
              calculate = relativedelta(datetime.today(),datee) 
              self.age_ = str(calculate.years)
            
            
   @api.one   
   def get_date(self):
       for rec in self:
           if rec.date_: 
              datee = datetime.strptime(rec.date_, "%Y-%m-%d  %H:%M:%S")   
              d = datetime(int(datee.year),int(datee.month), int(datee.day),)
              calculate = datetime.today() - d 
              self.date_number = int(calculate.days)
        
   @api.one   
   def get_str(self):
       for rec in self:
           if rec.date_:    
              datee = datetime.strptime(rec.date_, "%Y-%m-%d  %H:%M:%S")   
              d = datetime(int(datee.year),int(datee.month), int(datee.day))
              self.date_string =  d.strftime("%A") + "  " + d.strftime("%B") + "  " + d.strftime("%Y")
               

class family_details_(models.Model):
   _name = 'info.family'
     
   nombre_ = fields.Char("Nombre", required=True)
   addrs_fam = fields.Char("Direccion", required=True)
   job = fields.Char("Ocupación", required=True)
   tel = fields.Char("Telefono",required=True)
   age = fields.Integer("Edad", required=True)
   paren = fields.Selection([('1', 'Madre'),('2', 'Padre'),('3', 'Hijo"(a)"'),('4', 'Abuelo"(a)"'),('5', 'Primo"(a)"'),('6', 'Otro'),('7', 'Esposo"(a)"')], required=True)    
    
    
class studies_details_(models.Model):
   _name = 'info.studies'
     
   edu = fields.Selection([('1', 'Primaria'),('2', 'Secundaria'),('3', 'Superior'),('4', 'Postgrado'),('5', 'Master'),('6', 'Doctor')], required=True)
   addrs_studi = fields.Char("Direccion", required=True)
   nombre_studi = fields.Char("Institucion", required=True)
   date_in = fields.Date("Ingreso", required=True)
   date_out = fields.Date("Egreso", required=True)
   final = fields.Boolean()
# -*- coding: utf-8 -*-


from odoo import api, models, fields
from datetime import date, datetime

class Doctor(models.Model):
    _name ='doctor'
    
    photo = fields.Binary("Photo")
    unique_id = fields.Char()
    name = fields.Char()
    category = fields.Many2one('category')
    qualification_ids = fields.Many2many('qualification', 'doctor_qualification_rel', 'doctor_id', 'qualification_id', 'Qualification')
    degree_ids = fields.Many2many('degree','degree_doctor_rel','degree_id','doctor_id', 'Degree')
    college = fields.Many2one('college')
    experience = fields.Char('Experience')
    department = fields.Many2one('department')
    patient_ids = fields.Many2many('patient.patient', 'doctor_patient_rel', 'doctor_id', 'patient_id', 'Patient Details')
    text = fields.Text()
    
    mobile = fields.Char("Mobile")
    email = fields.Char("Email")
    phone = fields.Char("Phone")
    
#    def a_method(self):
#        
#        self.do_operation()
        
    @api.onchange('unique_id') 
    def onchange_name(self):
        self.name = self.unique_id
       
    
    
    
class Category(models.Model):
    _name ='category'
    
    name = fields.Char(string="Category")
    code = fields.Char(string="Code")
    
    
class Degree(models.Model):
    _name = 'degree'
    
    name = fields.Char(string = "degree")
    
class College(models.Model):
    _name = 'college'
    
    name = fields.Char(string="Name of College")
    state = fields.Many2one('res.country.state', string="State") 
    
    
class Department(models.Model):
    _name ='department'
    
    name = fields.Char(string = "Name of Department")
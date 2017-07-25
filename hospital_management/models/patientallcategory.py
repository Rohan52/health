# -*- coding: utf-8 -*-


from odoo import models, fields
from datetime import date, datetime

class Patient(models.Model):
    _name ='patient.patient'
    
    photo = fields.Binary()
    unique_id = fields.Char()
    name = fields.Char()
    category = fields.Many2many('categorypatient', 'patient_catagorypatient_rel', 'patient_id', 'categorypatient_id', 'Category')
    birthdate = fields.Date()
    deseased_date = fields.Datetime(
        string='Deceased Date',
    )
    room_no = fields.Many2one('roomno', string='Room No')
    doctor_id = fields.Many2one('doctor')
    
    age = fields.Char()
    
    address = fields.Char()
    general_info = fields.Text(
        string='General Information',
    )
    is_deceased = fields.Selection([
        ('y', 'Yes'),
        ('m', 'No'),   
    ], )
    marital_status = fields.Selection([
        ('s', 'Single'),
        ('m', 'Married'),
        ('w', 'Widowed'),
        ('d', 'Divorced'),
        ('x', 'Separated'),
        ('z', 'law marriage'),
    ], )
    
    doctorassigned_ids = fields.Many2many('doctor', 'patient_doctor_rel', 'patient_id', 'doctor_id', 'Assidned Doctor') 

class Roomno(models.Model):
    _name = 'roomno'
    
    
    name = fields.Char("Room No")
    
    
class Categorypatient(models.Model):
    _name='categorypatient'
    
    
    name = fields.Char(string = 'Type')
    code = fields.Char(string='code')
    
    
    
    
    
    
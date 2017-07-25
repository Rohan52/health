# -*- coding: utf-8 -*-


from odoo import models, fields
from datetime import date, datetime

class Facility(models.Model):
    _name='facility'
    
    name = fields.Char()
    
class Food(models.Model):
    _name='food'
    
    name = fields.Char(string="food")
    code = fields.Char(string="code")
    
class Room(models.Model):
    _name='room'
    
    name = fields.Char(string="Type of Room")
    no = fields.Integer(string="Room No")
    

from odoo import models, fields, api


class Title(models.Model):
    _name = 'student.title'
    _description = 'คำนำหน้าชื่อ'

    name = fields.Char(string='คำนำหน้า', required=True)
    code = fields.Char(string='รหัส')
    active = fields.Boolean(string='เปิดใช้งาน', default=True)
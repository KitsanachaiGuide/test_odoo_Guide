from odoo import models, fields, api
from datetime import date


class Student(models.Model):
    _name = 'student.student'
    _description = 'ข้อมูลนักเรียน'
    _inherit = ['mail.thread']  # ถ้าต้องการการติดตามข้อความแป

    name = fields.Char(string='ชื่อ', required=True)
    title_id = fields.Many2one('student.title', string='คำนำหน้า')
    birthdate = fields.Date(string="วันเกิด")
    age = fields.Integer(string='อายุ', compute='_compute_age', store=True)
    photo = fields.Binary(string='Image')
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female'), ('others', 'Others')],
        string='เพศ'
    )
    student_blood_group = fields.Selection(
        [('A+ve', 'A+'), ('B+ve', 'B+'), ('O+ve', 'O+'), ('AB+ve', 'AB+'),
         ('A-ve', 'A-'), ('B-ve', 'B-'), ('O-ve', 'O-'), ('AB-ve', 'AB-')],
        string='กรุ๊ปเลือด'
    )
    nationality = fields.Many2one('res.country', string='สัญชาติ')
    level_education = fields.Selection([
        ('kinder_garden', 'Kindergarten'),
        ('primary', 'Primary'),
        ('secondary', 'Secondary')
    ], compute="_compute_level_education", store=True)

    active = fields.Boolean(string='เปิดใช้งาน', default=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done'),
        ('reset', 'Reset'),
        ('cancel', 'Cancelled'),
    ], required=True, default='draft')

    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'ชื่อนักเรียนนี้มีอยู่ในระบบแล้ว กรุณาใช้ชื่ออื่น!'),
    ]


    @api.depends('birthdate')
    def _compute_age(self):
        for record in self:
            if record.birthdate:
                today = date.today()
                born = record.birthdate
                record.age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
            else:
                record.age = 0

    @api.depends('age')
    def _compute_level_education(self):
        for record in self:  # แก้ไขจาก ensure_one() เป็น loop เพื่อให้ทำงานกับหลายเรคอร์ด
            if record.age < 1:
                record.level_education = "kinder_garden"
            elif (record.age >= 1) and (record.age < 2):
                record.level_education = "kinder_garden"
            elif (record.age >= 2) and (record.age < 10):
                record.level_education = "primary"
            else:
                record.level_education = "--"

    def button_done(self):
        for rec in self:
            rec.write({'state': 'done'})

    def button_reset(self):
        for rec in self:
            rec.state = 'reset'

    def button_cancel(self):
        for rec in self:
            rec.write({'state': 'cancel'})


# from odoo import models, fields, api
# from datetime import date
#
# class Student(models.Model):
#     _name = 'student.student'
#     _description = 'ข้อมูลนักเรียน'
#
#     name = fields.Char(string='ชื่อ', required=True)
#     title_id = fields.Many2one('student.title', string='คำนำหน้า')
#     birthdate = fields.Date(string='วันเกิด')
#     age = fields.Integer(string='อายุ', compute='_compute_age', store=True)
#     active = fields.Boolean(string='เปิดใช้งาน', default=True)
#
#     _sql_constraints = [
#         ('name_unique', 'UNIQUE(name)', 'ชื่อนักเรียนนี้มีอยู่ในระบบแล้ว กรุณาใช้ชื่ออื่น!'),
#     ]
#
#     @api.depends('birthdate')
#     def _compute_age(self):
#         for record in self:
#             if record.birthdate:
#                 today = date.today()
#                 born = record.birthdate
#                 record.age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
#             else:
#                 record.age = 0
#
#     @api.constrains('name')
#     def _check_unique_name(self):
#         for record in self:
#             domain = [('name', '=', record.name), ('id', '!=', record.id)]
#             count = self.search_count(domain)
#             if count > 0:
#                 raise ValidationError(_('ชื่อนักเรียน "%s" มีอยู่ในระบบแล้ว!') % record.name)
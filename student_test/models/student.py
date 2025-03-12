from odoo import models, fields, api
from datetime import date
from odoo.exceptions import ValidationError


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
        ('secondary', 'Secondary'),
        ('high_school', 'High School'),
        ('university', 'University')
    ], compute="_compute_level_education", store=True)

    user_id = fields.Many2one('res.users', string="User", default=lambda self: self.env.user, readonly=True)

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
        for record in self:
            if record.age < 1:
                record.level_education = 'kinder_garden'
            elif 1 <= record.age < 10:
                record.level_education = 'primary'
            elif 10 <= record.age < 15:
                record.level_education = 'secondary'
            elif 15 <= record.age < 18:
                record.level_education = 'high_school'
            elif 18 <= record.age <= 20:
                record.level_education = 'university'
            else:
                record.level_education = 'Empty Value'

    def button_done(self):
        for rec in self:
            rec.write({'state': 'done'})

    def button_reset(self):
        for rec in self:
            rec.state = 'reset'

    def button_cancel(self):
        for rec in self:
            rec.write({'state': 'cancel'})

    @api.model
    def create(self, vals):
        """ Prevent users from creating more than one student record """
        existing_student = self.search([('user_id', '=', self.env.uid)], limit=1)
        if existing_student:
            raise ValidationError("You can only create one student record.")
        return super(Student, self).create(vals)

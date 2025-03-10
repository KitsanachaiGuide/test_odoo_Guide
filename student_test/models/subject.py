from odoo import models, fields ,api

class Subject(models.Model):
    _name = 'student_test.subject'
    _description = 'วิชาที่สอน'

    name = fields.Char(string="ชื่อวิชา", required=True)
    description = fields.Text(string="คำอธิบายวิชา")
    datates_ids = fields.Many2many('student.student', string="นักเรียนที่เรียน",
                                   domain="[('level_education', '!=', False)]")
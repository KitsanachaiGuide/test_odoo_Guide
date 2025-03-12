from odoo import models, fields

class Subject(models.Model):
    _name = 'student_test.subject'
    _description = 'วิชาที่สอน'

    name = fields.Char(string="ชื่อวิชา", required=True)
    description = fields.Text(string="คำอธิบายวิชา")
    subject_code = fields.Char(string="Subject Code", required=True, unique=True)
    unit_ids = fields.One2many('subject.unit', 'subject_id', string="Units")  # One2many Relationship


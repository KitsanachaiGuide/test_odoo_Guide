from odoo import models, fields

class SubjectUnit(models.Model):
    _name = 'subject.unit'
    _description = 'Subjects'

    name = fields.Char(string="Subject Name", required=True)
    subject_code = fields.Char(string="Subject Code", required=True, unique=True)
    subject_id = fields.Many2one('student_test.subject', string="Subject")  # เปลี่ยนเป็น Many2one และให้เชื่อมโยงกับ subject_test.subject
 # One2many Relationship


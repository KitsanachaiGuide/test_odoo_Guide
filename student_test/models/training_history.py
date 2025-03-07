from odoo import models, fields

class TrainingHistory(models.Model):
    _name = 'student_test.training_history'
    _description = 'ประวัติการอบรมของนักเรียน'

    name = fields.Char(string="ชื่อการอบรม")
    student_name = fields.Char(string="ชื่อนักเรียน")
    date = fields.Date(string="วันที่อบรม")

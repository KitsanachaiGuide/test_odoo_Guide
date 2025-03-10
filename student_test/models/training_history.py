from odoo import models, fields

class TrainingHistory(models.Model):
    _name = 'student_test.training_history'
    _description = 'ประวัติการอบรมของนักเรียน'

    name = fields.Char(string="ชื่อการอบรม")
    student_id = fields.Many2one('student.student', string="ชื่อนักเรียน")
    teacher_id = fields.Many2one('res.users', string="ครู")
    date = fields.Date(string="วันที่อบรม")

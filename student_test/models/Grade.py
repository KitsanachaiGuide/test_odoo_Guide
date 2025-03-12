from Tools.scripts.dutree import store

from odoo import models, fields, api

class Grade(models.Model):
    _name = 'student_test.grade'
    _description = 'เกรดของนักเรียน'
    _rec_name = 'student_name'

    teacher_id = fields.Many2one('student_test.teacher_address', string="ครูผู้ให้เกรด", required=True, domain="[('user_id', '=', uid)]")
    student_id = fields.Many2one('student.student', string="นักเรียน", required=True)
    student_name = fields.Char(related='student_id.name', string="Student Name", store=False)
    subject_id = fields.Many2one('student_test.subject', string="วิชา", required=True)
    unit = fields.Many2one('subject.unit', string="Unit", domain="[('subject_id', '=', subject_id)]")

    mark = fields.Float(string="คะแนน", required=True)
    grade = fields.Selection([
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('F', 'F')
    ], string="เกรด",read=True)
    comments = fields.Text(string="ความคิดเห็น")

    @api.onchange('mark')
    def _onchange_mark(self):
        """คำนวณเกรดโดยอัตโนมัติเมื่อกรอกคะแนน"""
        if self.mark >= 90:
            self.grade = 'A'
        elif self.mark >= 80:
            self.grade = 'B'
        elif self.mark >= 70:
            self.grade = 'C'
        elif self.mark >= 60:
            self.grade = 'D'
        else:
            self.grade = 'F'

    @api.onchange('teacher_id')
    def _onchange_teacher(self):
        """เมื่อเลือกครูแล้วให้แสดงนักเรียนที่ครูดูแล"""
        if self.teacher_id:
            return {'domain': {'student_id': [('id', 'in', self.teacher_id.student_ids.ids)]}}

    @api.onchange('teacher_id')
    def _onchange_teacher_subject(self):
        """เมื่อเลือกครูแล้วให้แสดงวิชาที่ครูสอน"""
        if self.teacher_id:
            return {'domain': {'subject_id': [('id', 'in', self.teacher_id.subject_ids.ids)]}}



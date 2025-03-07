from odoo import models, fields

class Teacher(models.Model):
    _name = 'student_test.teacher'
    _description = 'ข้อมูลครูผู้สอน'

    name = fields.Char(string="ชื่อครู", required=True)
    subject = fields.Char(string="วิชาที่สอน")
    phone = fields.Char(string="เบอร์โทรศัพท์")

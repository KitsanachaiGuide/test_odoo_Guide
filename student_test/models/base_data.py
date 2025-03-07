from odoo import models, fields

class BaseData(models.Model):
    _name = 'student_test.base_data'
    _description = 'ข้อมูลพื้นฐาน (จังหวัด, อำเภอ, ตำบล, เลขไปรษณีย์)'

    name = fields.Char(string="ชื่อ")
    province = fields.Char(string="จังหวัด")
    district = fields.Char(string="อำเภอ")
    sub_district = fields.Char(string="ตำบล")
    postal_code = fields.Char(string="รหัสไปรษณีย์")

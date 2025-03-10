from odoo import models, fields ,api

class TeacherAddress(models.Model):
    _name = 'student_test.teacher_address'
    _description = 'Teacher Address'

    name = fields.Char(string="ชื่อ")
    province_id = fields.Many2one('mdm.province', string="จังหวัด", required=True, ondelete='cascade')
    district_id = fields.Many2one('mdm.district', string="อำเภอ", required=True, domain="[('province_id', '=', province_id)]", ondelete='cascade')
    subdistrict_id = fields.Many2one('mdm.sub.district', string="ตำบล", required=True, domain="[('district_id', '=', district_id)]", ondelete='cascade')
    postal_code = fields.Many2one('mdm.postcode', string="รหัสไปรษณีย์", required=True, ondelete='cascade')

    subject_ids = fields.Many2one('student_test.subject', string="วิชาที่สอน")

    @api.onchange('subdistrict_id')
    def onchange_subdistrict_id(self):
        for rec in self:
            # การกรองรหัสไปรษณีย์
            return {'domain': {'postal_code': [
                ('sub_district_id', '=', rec.subdistrict_id.id),
                ('district_id', '=', rec.district_id.id),
                ('province_id', '=', rec.province_id.id)
            ]}}

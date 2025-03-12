from odoo import models, fields ,api
from odoo.exceptions import ValidationError


class TeacherAddress(models.Model):
    _name = 'student_test.teacher_address'
    _description = 'Teacher Address'

    name = fields.Char(string="ชื่อ")
    teacher_code = fields.Char(string="Teacher ID", unique=True)
    province_id = fields.Many2one('mdm.province', string="จังหวัด", required=True, ondelete='cascade')
    district_id = fields.Many2one('mdm.district', string="อำเภอ", required=True, domain="[('province_id', '=', province_id)]", ondelete='cascade')
    subdistrict_id = fields.Many2one('mdm.sub.district', string="ตำบล", required=True, domain="[('district_id', '=', district_id)]", ondelete='cascade')
    postal_code = fields.Many2one('mdm.postcode', string="รหัสไปรษณีย์", required=True, ondelete='cascade')

    subject_ids = fields.Many2many('student_test.subject', string="วิชาที่สอน")  # เปลี่ยนเป็น Many2many
    student_ids = fields.Many2many('student.student', string="นักเรียนที่ครูดูแล")
    user_id = fields.Many2one('res.users', string="User", default=lambda self: self.env.user, readonly=True)

    @api.onchange('subdistrict_id')
    def onchange_subdistrict_id(self):
        for rec in self:
            # การกรองรหัสไปรษณีย์
            return {'domain': {'postal_code': [
                ('sub_district_id', '=', rec.subdistrict_id.id),
                ('district_id', '=', rec.district_id.id),
                ('province_id', '=', rec.province_id.id)
            ]}}

    @api.model
    def create(self, vals):
        """ Prevent users from creating more than one teacher record """
        existing_teacher = self.search([('user_id', '=', self.env.uid)], limit=1)
        if existing_teacher:
            raise ValidationError("You can only create one teacher record.")
        return super(TeacherAddress, self).create(vals)

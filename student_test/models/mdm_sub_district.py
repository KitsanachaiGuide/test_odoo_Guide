from odoo import models, fields, api, _


class SubDistrict(models.Model):
    _name = 'mdm.sub.district'
    _rec_name = "sub_district_name_tha"
    _description = "Subdistrict Data"

    province_id = fields.Many2one(comodel_name="mdm.province", string="จังหวัด", required=True)
    province_code = fields.Char(string=_('จังหวัด'), required=True, related='province_id.province_name_tha')
    district_id = fields.Many2one(comodel_name="mdm.district", string="อำเภอ", required=True)
    district_code = fields.Char(string=_('อำเภอ'), required=True, related='district_id.district_name_tha')
    sub_district_code = fields.Char(string=_('รหัสตำบล'), required=True)
    sub_district_name_tha = fields.Char(string=_('ชื่อตำบลภาษาไทย'), required=True)
    sub_district_name_eng = fields.Char(string=_('ชื่อตำบลภาษาอังกฤษ'), required=False)
    postcode = fields.Char(string=_('รหัสไปรษณีย์'), required=False, size=10)

    @api.onchange('province_id')
    def onchange_province_id(self):
        for rec in self:
            rec.district_id = ""
            return {'domain': {'district_id': [('province_id', '=', rec.province_id.id)]}}
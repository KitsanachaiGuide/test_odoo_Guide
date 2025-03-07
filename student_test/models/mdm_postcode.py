from odoo import fields, models, _, api


class PostCode(models.Model):
    _name = 'mdm.postcode'
    _rec_name = "postcode_code"
    _description = "PostCode Data"

    postcode_code = fields.Char(string=_("รหัสไปรษณีย์"), required=True, size=10)
    province_id = fields.Many2one(comodel_name="mdm.province", string="จังหวัด",
                                  required=True, )
    province_code = fields.Char(string=_('จังหวัด'), required=True, related='province_id.province_name_tha')
    district_id = fields.Many2one(comodel_name="mdm.district", string="อำเภอ",
                                  required=True, )
    district_code = fields.Char(string=_('อำเภอ'), required=True, related='district_id.district_name_tha')
    sub_district_id = fields.Many2one(comodel_name="mdm.sub.district", string="ตำบล",
                                  required=True, )
    sub_district_code = fields.Char(string=_('ตำบล'), required=True, related='sub_district_id.sub_district_name_tha')

        # กรอง อำเภอ
    @api.onchange('province_id')
    def onchange_province_id(self):
        for rec in self:
            rec.district_id = ""
            rec.sub_district_id = ""
            return {'domain': {'district_id': [('province_id', '=', rec.province_id.id)]}}

    # กรอง ตำบล
    @api.onchange('district_id')
    def onchange_district_id(self):
        for rec in self:
            rec.sub_district_id = ""
            return {
                'domain': {'sub_district_id': [('district_id', '=', rec.district_id.id)]}}

    @api.onchange('sub_district_id')
    def onchange_sub_district_id(self):
        for rec in self:
            return {'domain': {'postcode_code': [('sub_district_id', '=', rec.sub_district_id.id)]}}

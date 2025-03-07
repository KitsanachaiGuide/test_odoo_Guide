from odoo import models, fields, _


class Province(models.Model):
    _name = 'mdm.province'
    _rec_name = "province_name_tha"
    _description = "Province Data"

    province_code = fields.Char(string=_('รหัสจังหวัด'), required=True)
    province_name_tha = fields.Char(string=_('ชื่อจังหวัดภาษาไทย'), required=True)
    province_name_eng = fields.Char(string=_('ชื่อจังหวัดภาษาอังกฤษ'), required=False)


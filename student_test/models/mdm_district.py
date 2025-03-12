from odoo import models, fields, _ ,api

class District(models.Model):
    _name = 'mdm.district'
    _rec_name = "district_name_tha"
    _description = "District Data"

    province_id = fields.Many2one(comodel_name="mdm.province", string=_('จังหวัด'), required=True)
    province_code= fields.Char(string=_('รหัสจังหวัด'), related='province_id.province_code', required=True)
    district_code = fields.Char(string=_('รหัสอำเภอ'), required=True)
    district_name_tha = fields.Char(string=_('ชื่ออำเภอภาษาไทย'), required=True)
    district_name_eng = fields.Char(string=_('ชื่ออำเภอภาษาอังกฤษ'), required=False)


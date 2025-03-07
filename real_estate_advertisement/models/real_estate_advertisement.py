from odoo import models, fields

class RealEstateAdvertisement(models.Model):
    _name = 'real.estate.advertisement'
    _description = 'Real Estate Advertisement'

    # ฟิลด์ที่ใช้ในการเก็บข้อมูลของโฆษณา
    name = fields.Char('Advertisement Title', required=True)

    # ฟิลด์ One2many เพื่อแสดงรายการของอสังหาริมทรัพย์ที่เกี่ยวข้องกับโฆษณานี้
    property_ids = fields.One2many('real.estate.property', 'advertisement_id', string='Properties')

from odoo import models, fields,api

class RealEstateProperty(models.Model):
    _name = 'real.estate.property'
    _description = 'Real Estate Property'

    name = fields.Char('Property Name', required=True)
    advertisement_id = fields.Many2one('real.estate.advertisement', string='Advertisement')
    description = fields.Text('Description')
    postcode = fields.Char('Postcode')
    date_availability = fields.Date('Availability Date')
    expected_price = fields.Float('Expected Price', required=True)
    selling_price = fields.Float('Selling Price')
    bedrooms = fields.Integer('Number of Bedrooms')
    living_area = fields.Integer('Living Area')
    facades = fields.Integer('Number of Facades')
    garage = fields.Boolean('Has Garage')
    garden = fields.Boolean('Has Garden')
    garden_area = fields.Integer('Garden Area')
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')
    ], string='Garden Orientation')

    @api.onchange('expected_price', 'bedrooms')
    def _onchange_selling_price(self):
        if self.expected_price and self.bedrooms:
            self.selling_price = self.expected_price + (self.bedrooms * 1000)
        else:
            self.selling_price = 0



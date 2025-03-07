# -*- coding: utf-8 -*-
# from odoo import http


# class RealEstateAdvertisement(http.Controller):
#     @http.route('/real_estate_advertisement/real_estate_advertisement', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/real_estate_advertisement/real_estate_advertisement/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('real_estate_advertisement.listing', {
#             'root': '/real_estate_advertisement/real_estate_advertisement',
#             'objects': http.request.env['real_estate_advertisement.real_estate_advertisement'].search([]),
#         })

#     @http.route('/real_estate_advertisement/real_estate_advertisement/objects/<model("real_estate_advertisement.real_estate_advertisement"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('real_estate_advertisement.object', {
#             'object': obj
#         })

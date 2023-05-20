# -*- coding: utf-8 -*-
# from odoo import http


# class CarRequestBase(http.Controller):
#     @http.route('/car_request_base/car_request_base', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/car_request_base/car_request_base/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('car_request_base.listing', {
#             'root': '/car_request_base/car_request_base',
#             'objects': http.request.env['car_request_base.car_request_base'].search([]),
#         })

#     @http.route('/car_request_base/car_request_base/objects/<model("car_request_base.car_request_base"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('car_request_base.object', {
#             'object': obj
#         })

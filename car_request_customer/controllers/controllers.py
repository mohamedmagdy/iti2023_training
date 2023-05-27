# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request, route


class CarRequestCustomer(http.Controller):
    # @http.route('/car_request_customer/car_request_customer', auth='public')
    # def index(self, **kw):
    #     return "Hello, world

    @route('/request/list/objects', auth='public', website=True, type='http')
    def list(self, **kw):

        return request.render('car_request_customer.listing', {
            'root': '/request/detail',
            'objects': request.env['car.request'].search([]),
        })

    @route('/request/detail/objects/<model("car.request"):obj>', auth='public', website=True)
    def object(self, obj, **kw):
        return request.render('car_request_customer.object', {
            'object': obj
        })

    @route('/api/list/request', type='json', auth='public', methods=['POST'])
    def car_request_api_list(self, **kw):
        domain = []
        if 'say' in kw:
            print(kw)
        #     domain.append()
        car_requests = request.env['car.request'].sudo().search_read(domain, fields=['name', 'destination', 'start_date', 'end_date'], order='name DESC')
        return {'message': "Success!", 'data': car_requests}
# -*- coding: utf-8 -*-

from odoo import models, fields, api


class FleetVehicle(models.Model):
    _name = 'fleet.vehicle'
    _inherit = 'fleet.vehicle'

    requests_count = fields.Integer(string="Requests", compute="_compute_requests_count")

    @api.depends()
    def _compute_requests_count(self):
        env_car_request = self.env['car.request']
        for rec in self:
            rec.requests_count = env_car_request.search_count([('car_id', '=', rec.id)])
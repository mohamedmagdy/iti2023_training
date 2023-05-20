# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class CarRequest(models.Model):
    _name = 'car.request'
    _description = 'Car Request'
    _order = 'id DESC'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    # _rec_name = 'req_no'

    name = fields.Char(string="Request No.", required=True, tracking=True)
    destination = fields.Text(string="Destination")
    note = fields.Html(string="Note")
    request_creator = fields.Many2one(comodel_name="res.users", string="Created By", required=True, default=lambda s: s.env.uid)
    driver = fields.Many2one(comodel_name="res.users", string="Driver", default=lambda s: s.env.uid)
    start_date = fields.Datetime(string="Start Date", default=fields.Datetime.now, tracking=True)
    end_date = fields.Datetime(string="End Date", tracking=True)
    car_id = fields.Many2one(comodel_name="fleet.vehicle", string="Requested Car", required=True)
    active = fields.Boolean(default=True)
    state = fields.Selection([('new', 'New'), ('inprogress', 'In Progress'), ('accepted', 'Accepted'), ('rejected', 'Rejected'), ('cancelled', 'Cancelled')], default="new", tracking=True)

    def set_inprogress(self):
        self.state = 'inprogress'

    def set_accepted(self):
        self.state = 'accepted'

    def set_rejected(self):
        self.state = 'rejected'

    def set_cancelled(self):
        self.state = 'cancelled'

    def reset_new(self):
        self.state = 'new'

    @api.constrains('start_date', 'end_date')
    def _dates_validator(self):
        if self.end_date < self.start_date:
            raise ValidationError("Dates Are not valid !")




from datetime import timedelta

from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Property Offer"
    _sql_constraints = [
    (
        "check_price",
        "CHECK(price > 0)",
        "The offer price must be strictly positive.",
    ),
]

    price = fields.Float()

    status = fields.Selection(
        selection=[
            ('accepted', 'Accepted'),
            ('refused', 'Refused'),
        ],
        copy=False,
    )

    partner_id = fields.Many2one(
        "res.partner",
        required=True,
    )

    property_id = fields.Many2one(
        "estate.property",
        required=True,
    )

    validity = fields.Integer(
        default=7,
    )

    date_deadline = fields.Date(
        compute="_compute_date_deadline",
        inverse="_inverse_date_deadline",
    )

    @api.depends("create_date", "validity")
    def _compute_date_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline = (
                    record.create_date.date()
                    + timedelta(days=record.validity)
                )
            else:
                record.date_deadline = (
                    fields.Date.today()
                    + timedelta(days=record.validity)
                )

    def _inverse_date_deadline(self):
        for record in self:
            if record.create_date and record.date_deadline:
                record.validity = (
                    record.date_deadline - record.create_date.date()
                ).days

    @api.constrains("price")
    def _check_price(self):
        for offer in self:
            if offer.price <= 0:
                raise ValidationError(
                    "The offer price must be greater than 0."
                )

    def action_accept(self):
        for offer in self:
            other_accepted = self.search([
                ("property_id", "=", offer.property_id.id),
                ("status", "=", "accepted"),
                ("id", "!=", offer.id),
            ], limit=1)

            if other_accepted:
                raise UserError(
                    "Only one offer can be accepted for a property."
                )

            offer.status = "accepted"
            offer.property_id.selling_price = offer.price
            offer.property_id.buyer_id = offer.partner_id

        return True

    def action_refuse(self):
        for offer in self:
            offer.status = "refused"

        return True
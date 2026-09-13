from odoo import api, fields, models
from odoo.exceptions import ValidationError


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Property Offer"

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

    @api.constrains('price')
    def _check_price(self):
        for offer in self:
            if offer.price <= 0:
                raise ValidationError("The offer price must be greater than 0.")
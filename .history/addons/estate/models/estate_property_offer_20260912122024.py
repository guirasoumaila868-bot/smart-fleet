from datetime import timedelta

from odoo import api, fields, models
from odoo.exceptions import ValidationError

class EstatePropertyOffer(models.Model):
_name = "estate.property.offer"
_description = "Property Offer"

```
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
            record.date_deadline = record.create_date.date() + timedelta(
                days=record.validity
            )
        else:
            record.date_deadline = fields.Date.today() + timedelta(
                days=record.validity
            )

def _inverse_date_deadline(self):
    for record in self:
        if record.create_date and record.date_deadline:
            record.validity = (
                record.date_deadline - record.create_date.date()
            ).days

@api.constrains('price')
def _check_price(self):
    for offer in self:
        if offer.price <= 0:
            raise ValidationError(
                "The offer price must be greater than 0."
            )

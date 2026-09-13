from odoo import fields, models


class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Property Tag"
    models.Constraint(
    (
        "unique_name",
        "UNIQUE(name)",
        "The property tag name must be unique.",
    ),
    )

    name = fields.Char(required=True)
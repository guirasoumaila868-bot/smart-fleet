from odoo import fields, models


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Property Type"
    models.Constraint(
    (
        "unique_name",
        "UNIQUE(name)",
        "The property type name must be unique.",
    ),
    )

    name = fields.Char(required=True)
    property_ids = fields.One2many(
        "estate.property",
        "property_type_id",
    )
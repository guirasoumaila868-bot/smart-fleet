from odoo import fields, models


class EstatePropertyWizard(models.TransientModel):
    _name = "estate.property.wizard"
    _description = "Estate Property Wizard"

    name = fields.Char(string="Nom")
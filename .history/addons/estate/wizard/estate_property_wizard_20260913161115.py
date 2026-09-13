from odoo import fields, models


class EstatePropertyWizard(models.TransientModel):
    _name = "estate.property.wizard"
    _description = "Estate Property Wizard"

    name = fields.Char(string="Nom")

    def action_confirm(self):
        return {
            "type": "ir.actions.act_window_close"
        }
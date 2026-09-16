# -*- coding: utf-8 -*-

from odoo import models, fields


class FleetVehicle(models.Model):

    _inherit = 'fleet.vehicle'

    smart_categorie = fields.Selection(
        selection=[
            ('tracteur', 'Tracteur'),
            ('porteur', 'Porteur'),
            ('remorque', 'Remorque / semi-remorque'),
        ],
        string="Categorie",
        default='porteur',
        required=True,
        help="Categorie au sens du cahier des charges M4. "
             "Une remorque n'a pas de kilometrage propre (RG8).",
    )
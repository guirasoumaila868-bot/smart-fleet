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
        string="Catégorie",
        default='porteur',
        required=True,
        help="Catégorie du véhicule selon le cahier des charges SMART Fleet.",
    )
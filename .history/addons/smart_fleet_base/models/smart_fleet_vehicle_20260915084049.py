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

    smart_nombre_essieux = fields.Integer(
        string="Nombre d'essieux"
    )

    smart_ptac = fields.Float(
        string="PTAC (kg)",
        help="Poids total autorise en charge (M4)"
    )

    smart_ptra = fields.Float(
        string="PTRA (kg)",
        help="Poids total roulant autorise, ensemble tracteur + remorque (M4)"
    )

    smart_date_mise_service = fields.Date(
        string="Date de mise en service"
    )

    smart_etat_service = fields.Selection(
        selection=[
            ('service', 'En service'),
            ('immobilise', 'Immobilise'),
            ('reforme', 'Reforme'),
        ],
        string="Etat de service",
        default='service',
        required=True,
        tracking=True
    )
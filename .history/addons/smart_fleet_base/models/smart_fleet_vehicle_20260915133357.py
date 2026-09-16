# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import ValidationError


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
        help=(
            "Catégorie au sens du cahier des charges M4. "
            "Une remorque n'a pas de kilométrage propre (RG8)."
        ),
    )

    smart_nombre_essieux = fields.Integer(
        string="Nombre d'essieux",
        default=0,
    )

    smart_ptac = fields.Float(
        string="PTAC (kg)",
        help="Poids total autorisé en charge (M4).",
    )

    smart_ptra = fields.Float(
        string="PTRA (kg)",
        help=(
            "Poids total roulant autorisé, "
            "ensemble tracteur + remorque (M4)."
        ),
    )

    smart_date_mise_service = fields.Date(
        string="Date de mise en service",
    )

    smart_etat_service = fields.Selection(
        selection=[
            ('service', 'En service'),
            ('immobilise', 'Immobilisé'),
            ('reforme', 'Réformé'),
        ],
        string="État de service",
        default='service',
        required=True,
        tracking=True,
    )

    _sql_constraints = [
        (
            'smart_nombre_essieux_positif',
            'CHECK(smart_nombre_essieux >= 0)',
            "Le nombre d'essieux ne peut pas être négatif.",
        ),
    ]

    @api.constrains('smart_nombre_essieux')
    def _check_nombre_essieux_positif(self):
        for vehicle in self:
            if vehicle.smart_nombre_essieux < 0:
                raise ValidationError(
                    "Le nombre d'essieux ne peut pas être négatif."
                )

    @api.constrains('smart_ptac', 'smart_ptra')
    def _check_ptra_superieur_ptac(self):
        for vehicle in self:
            if (
                vehicle.smart_ptac
                and vehicle.smart_ptra
                and vehicle.smart_ptra < vehicle.smart_ptac
            ):
                raise ValidationError(
                    "Le PTRA doit être supérieur ou égal au PTAC."
                )

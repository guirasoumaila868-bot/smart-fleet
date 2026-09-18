# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import ValidationError

class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    # CONTRAT D'INTERFACE : utilisé par S2
    smart_categorie = fields.Selection(
        selection=[
            ('tracteur', 'Tracteur'),
            ('porteur', 'Porteur'),
            ('remorque', 'Remorque / semi-remorque'),
        ],
        string="Catégorie",
        default='porteur',
        required=True,
        help="Catégorie au sens du cahier des charges M4. "
             "Une remorque n'a pas de kilométrage propre (RG8).",
    )
    
    smart_nombre_essieux = fields.Integer(string="Nombre d'essieux")
    
    smart_ptac = fields.Float(
        string="PTAC (kg)",
        help="Poids total autorisé en charge (M4)"
    )
    
    smart_ptra = fields.Float(
        string="PTRA (kg)",
        help="Poids total roulant autorisé, ensemble tracteur + remorque (M4)"
    )
    
    smart_date_mise_service = fields.Date(string="Date de mise en service")
    
    smart_etat_service = fields.Selection(
        selection=[
            ('service', 'En service'),
            ('immobilise', 'Immobilisé'),
            ('reforme', 'Réformé'),
        ],
        string="État de service",
        default='service',
        required=True,
        tracking=True  # tracking : toute modification est historisée dans le chatter
    )

    # Relations One2many : Historique des attelages (vue inverse)
    smart_attelage_tracteur_ids = fields.One2many(
        'smart.fleet.coupling', 'tracteur_id', 
        string="Attelages (en tant que tracteur)"
    )
    
    smart_attelage_remorque_ids = fields.One2many(
        'smart.fleet.coupling', 'remorque_id', 
        string="Attelages (en tant que remorque)"
    )

    # Contraintes au niveau de la BASE DE DONNÉES (SQL)
    _sql_constraints = [
        ('smart_license_plate_unique', 'unique(license_plate)',
         "Cette immatriculation existe déjà. "
         "Recherchez le véhicule existant au lieu d'en créer un second."),
        ('smart_nombre_essieux_positif', 'check(smart_nombre_essieux >= 0)',
         "Le nombre d'essieux ne peut pas être négatif.")
    ]

    # Contrainte Python : Validation logique métier complexe
    @api.constrains('smart_ptac', 'smart_ptra')
    def _check_ptra_superieur_ptac(self):
        """M4 : le PTRA (ensemble roulant) ne peut pas être inférieur au PTAC."""
        for vehicle in self:
            if vehicle.smart_ptac and vehicle.smart_ptra \
               and vehicle.smart_ptra < vehicle.smart_ptac:
                raise ValidationError(
                    "Le PTRA de %s (%s kg) est inférieur à son PTAC (%s kg).\n"
                    "Le PTRA est le poids de l'ensemble tracteur + remorque : "
                    "il est toujours supérieur ou égal. Vérifiez la carte grise."
                    % (vehicle.name or 'ce véhicule', vehicle.smart_ptra, vehicle.smart_ptac)
                )
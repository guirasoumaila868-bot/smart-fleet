# -- coding: utf-8 --
from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError

class SmartFleetCoupling(models.Model):
    _name = 'smart.fleet.coupling'
    _description = "Attelage tracteur / remorque (M4)"
    _order = 'date_debut desc'

    tracteur_id = fields.Many2one(
        'fleet.vehicle', string="Tracteur / porteur", required=True,
        domain="[('smart_categorie', 'in', ['tracteur', 'porteur'])]",
        ondelete='restrict'  # restrict : interdit de supprimer un véhicule qui a un historique (RG6)
    )
    
    remorque_id = fields.Many2one(
        'fleet.vehicle', string="Remorque", required=True,
        domain="[('smart_categorie', '=', 'remorque')]",
        ondelete='restrict'
    )
    
    date_debut = fields.Datetime(
        string="Date d'attelage", required=True, default=fields.Datetime.now
    )
    
    date_fin = fields.Datetime(string="Date de dételage")
    
    motif_detelage = fields.Char(string="Motif du dételage")
    
    en_cours = fields.Boolean(
        string="En cours", compute='_compute_en_cours', store=True
    )

    @api.depends('date_fin')
    def _compute_en_cours(self):
        for coupling in self:
            coupling.en_cours = not coupling.date_fin

    @api.depends('tracteur_id', 'remorque_id')
    def _compute_display_name(self):
        """Le nom affiché partout : « Tracteur + Remorque »."""
        for coupling in self:
            coupling.display_name = "%s + %s" % (
                coupling.tracteur_id.name or "?",
                coupling.remorque_id.name or "?"
            )

    # -----------------------------------------------------------------
    # Règles de gestion
    # -----------------------------------------------------------------
    @api.constrains('remorque_id', 'date_fin')
    def _check_remorque_libre(self):
        """M4 : une remorque ne peut être attelée qu'à un seul tracteur à la fois."""
        for coupling in self:
            if coupling.date_fin:
                continue
            autre = self.search([
                ('remorque_id', '=', coupling.remorque_id.id),
                ('date_fin', '=', False),
                ('id', '!=', coupling.id),
            ], limit=1)
            if autre:
                raise ValidationError(
                    "La remorque %s est déjà attelée au tracteur %s "
                    "depuis le %s. Dételage obligatoire d'abord."
                    % (coupling.remorque_id.name,
                       autre.tracteur_id.name,
                       autre.date_debut)
                )

    @api.constrains('tracteur_id', 'remorque_id')
    def _check_categories(self):
        """M4 : on attelle une remorque à un tracteur ou un porteur, rien d'autre."""
        for coupling in self:
            if coupling.tracteur_id.smart_categorie not in ('tracteur', 'porteur'):
                raise ValidationError(
                    "%s est une remorque : elle ne peut pas tirer une autre remorque. "
                    "Choisissez un tracteur ou un porteur."
                    % coupling.tracteur_id.name
                )
            if coupling.remorque_id.smart_categorie != 'remorque':
                raise ValidationError(
                    "%s n'est pas une remorque. Seul un véhicule de catégorie "
                    "« Remorque » peut être attelé." % coupling.remorque_id.name
                )

    @api.constrains('date_debut', 'date_fin')
    def _check_dates(self):
        for coupling in self:
            if coupling.date_fin and coupling.date_fin < coupling.date_debut:
                raise ValidationError(
                    "La date de dételage ne peut pas précéder la date d'attelage."
                )

    # -----------------------------------------------------------------
    # Actions métier
    # -----------------------------------------------------------------
    def action_deteler(self):
        """Un attelage n'est jamais supprimé : il est terminé, avec un motif."""
        for coupling in self:
            if not coupling.motif_detelage:
                raise UserError(
                    "Saisissez le motif du dételage avant de cliquer sur « Dételer »."
                )
            coupling.date_fin = fields.Datetime.now()
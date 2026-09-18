Jour 1 — Mise en place de l’environnement Odoo

Fait :
Installation et vérification de Docker Desktop.
Création du projet smart-fleet.
Mise en place de l’environnement Odoo avec Docker.
Configuration de PostgreSQL pour la base de données.
Création du fichier docker-compose.yml.
Création du fichier de configuration odoo.conf.
Création des dossiers addons, config et _reference.
Lancement des conteneurs Odoo et PostgreSQL.
Accès à Odoo depuis le navigateur avec localhost:8069.
Création et connexion à la base de données de test smart_fleet_test.
Vérification du fonctionnement général de l’environnement.

Bloqué sur :
Difficultés lors du premier lancement du conteneur Odoo.
Quelques erreurs de configuration et de connexion à la base de données.

Appris :
Docker permet d’exécuter Odoo et PostgreSQL dans des conteneurs.
Odoo utilise PostgreSQL comme système de gestion de base de données.
Le fichier docker-compose.yml permet de définir et lancer les différents services.
Le fichier odoo.conf permet de configurer Odoo.
Le dossier addons permet de stocker les modules personnalisés.

Demain :
Commencer l’apprentissage du développement Odoo avec le module pédagogique estate.
Comprendre la structure d’un module Odoo et créer le premier modèle.

Jour 2 — Apprendre Odoo sur un module jetable

Fait :
Découverte de l’architecture d’Odoo.
Création et prise en main du module pédagogique estate.
Création du modèle estate.property.
Ajout des champs de base : texte, date, nombre, booléen et sélection.
Compréhension du rôle de **manifest**.py, **init**.py, models et views.

Bloqué sur :
Quelques difficultés pour comprendre la structure d’un module Odoo et le rôle de chaque fichier.

Appris :
Odoo utilise Python pour la logique métier et XML pour les vues.
Un modèle Odoo permet de représenter les données métier.
Le fichier **manifest**.py décrit le module et ses fichiers.

Demain :
Continuer avec les relations entre les modèles et les vues.

Jour 3 — Relations, vues et logique métier

Fait :
Création des relations entre les modèles avec Many2one, One2many et Many2many.
Création et modification des vues.
Création des menus et des actions.
Ajout de champs calculés.
Mise en place de contraintes métier.
Création des actions pour vendre ou annuler une propriété.

Bloqué sur :
Difficultés à comprendre au début le fonctionnement des relations et des champs calculés.

Appris :
Les modèles peuvent être liés entre eux.
api.depends permet de recalculer automatiquement un champ lorsque certaines données changent.
Les vues XML permettent de contrôler l’affichage des données dans Odoo.

Demain :
Étudier l’héritage des modèles et des vues.

Jour 4 — Héritage, assistant, automatisation et sécurité

Fait :
Étude de l’héritage dans Odoo avec _inherit.
Extension du modèle res.users.
Ajout du champ property_ids.
Création d’une vue héritée de res.users.
Ajout de l’onglet Properties dans la fiche utilisateur.
Création d’un Wizard avec TransientModel.
Création de la vue du Wizard et de ses boutons.
Création d’une tâche automatique avec ir.cron.
Configuration de l’exécution automatique toutes les minutes.
Vérification du fonctionnement de la tâche automatique dans les journaux Odoo.
Création d’un groupe de sécurité Properties - Restricted.
Création d’une règle ir.rule pour limiter les propriétés visibles par les utilisateurs du groupe.

Bloqué sur :
Erreur lors de la mise en place de la tâche automatique : Odoo ne trouvait pas la méthode _cron_test.
Erreur lors du chargement de la règle de sécurité : le groupe n’était pas encore chargé avant la règle.

Appris :
_inherit permet de personnaliser un modèle Odoo existant sans modifier directement son code.
TransientModel est utilisé pour les données temporaires des Wizards.
ir.cron permet d’exécuter automatiquement une opération selon un intervalle défini.
Un groupe de sécurité définit les utilisateurs concernés.
ir.rule permet de définir quelles données les utilisateurs peuvent consulter ou modifier.
L’ordre des fichiers dans le manifeste du module peut être important lorsqu’un fichier dépend d’un autre.

Demain :
Commencer la conception du squelette du vrai module Smart Fleet.
Identifier les premiers modèles nécessaires à la gestion de la flotte.
Commencer à adapter les connaissances acquises sur le module estate au projet Smart Fleet.



JOUR 5 le squelette contractuel

fait:
 le module Odoo installable 
 les groupes de sécurité 
 la catégorie du véhicule 
 la structure de base du module 
 le menu principal SMART Fleet

 J'ai également créé les deux groupes de sécurité nécessaires au projet :
SMART Fleet / Utilisateur 
SMART Fleet / Responsable

Bloqués: le module utilisait la version 18 dans son manifeste alors que l'environnement docker utilise 19 (j'ai corrigé)

SUITE PREVU C2-C3 / J6-J7 : le véhicule poids lourd.


JOUR 6
Fait:
Notre module ajoute des informations au modèle véhicule déjà fourni par Odoo.

Les champs ajoutés sont :
smart_categorie : tracteur, porteur ou remorque 
smart_nombre_essieux : nombre d'essieux 
smart_ptac : poids total autorisé en charge 
smart_ptra : poids total roulant autorisé 
smart_date_mise_service : date de mise en service 
smart_etat_service : en service, immobilisé ou réformé

Deux contrôles ont été ajoutés :

Le nombre d'essieux ne peut pas être négatif.
Le PTRA doit être supérieur ou égal au PTAC.

La règle sur le nombre d'essieux est protégée à deux niveaux :

par une contrainte SQL ;
par une contrainte Python avec `@api.constrains

Bloqués 
Le contrôle du nombre d'essieux nécessitait également une contrainte Python complémentaire à la contrainte SQL afin de bloquer clairement la saisie dans Odoo.

SUITE PREVU C4-C5 / J8-J9 — L'attelage
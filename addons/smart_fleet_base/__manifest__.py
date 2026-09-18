{
    'name': 'SMART Fleet - Socle',
    'version': '19.0.1.0.0',
    'category': 'Services/Fleet',
    'summary': 'Parc poids lourds, attelage et compteur - LICELI SMART Fleet',
    'author': 'LICELI Technologies',
    'license': 'LGPL-3',

    'depends': [
        'base',
        'mail',
        'fleet',
    ],

    'data': [
        'security/smart_fleet_security.xml',
        'security/ir.model.access.csv',
        'views/smart_fleet_vehicle_views.xml',
        'views/smart_fleet_coupling_views.xml',
        'views/smart_fleet_menus.xml',
    ],

    'application': True,
    'installable': True,
}
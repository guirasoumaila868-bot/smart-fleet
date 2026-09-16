{
    'name': 'SMART Fleet - Socle',
    'version': '19.0.1.0.0',
    'category': 'Services/Fleet',
    'summary': "Socle de gestion de flotte poids lourds - LICELI SMART Fleet",
    'author': 'LICELI Technologies',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'mail',
        'fleet',
        'hr',
    ],
    'demo': [
        'demo/demo_data.xml',
    ],
    'application': True,
    'installable': True,
    'data': [
        'security/ir.model.access.csv',
        'views/smart_fleet_vehicle_views.xml',
        'views/smart_fleet_menus.xml',
    ],
}
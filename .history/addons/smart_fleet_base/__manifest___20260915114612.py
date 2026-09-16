{
    'name': 'SMART Fleet - Socle',
    'version': '18.0.1.0.0',
    'depends': [
        'base',
        'mail',
        'fleet',
    ],
    'data': [
        'security/smart_fleet_security.xml',
        'security/ir.model.access.csv',
        'views/fleet_vehicle_views.xml',
        'views/smart_fleet_menus.xml',
    ],
    'installable': True,
    'application': True,
}

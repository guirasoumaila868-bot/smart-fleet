{
    'name': 'SMART Fleet Base',
    'version': '19.0.1.0.0',
    'category': 'Fleet',
    'summary': 'Gestion de flotte de véhicules poids lourds',
    'description': """
        SMART Fleet
        Gestion de flotte de véhicules poids lourds.
    """,
    'depends': [
        'base',
        'fleet',
        'mail',
        'hr',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/smart_fleet_vehicle_views.xml',
    ],
    'installable': True,
    'application': True,
}
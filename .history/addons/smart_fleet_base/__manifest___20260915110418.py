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
    'application': True,
    'installable': True,
    'data': [
        'data': [
    'security/smart_fleet_security.xml',
    'security/ir.model.access.csv',
],

    ],
}
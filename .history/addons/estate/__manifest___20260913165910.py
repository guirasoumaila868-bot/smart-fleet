{
    'name': 'Real Estate',

    'depends': [
        'base',
    ],

    'application': True,

    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/ir_cron.xml',
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_property_wizard_views.xml',
        'views/estate_menus.xml',
        'views/res_users_views.xml',
    ],
}
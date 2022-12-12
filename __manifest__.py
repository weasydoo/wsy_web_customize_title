# -*- encoding: utf-8 -*-
##############################################################################
#    Copyright © 2020,Weasydoo. All rights reserved.
##############################################################################
{
    'name': 'Web Change Title',
    'summary': "Web Customize Title",
    "author": "Weasydoo",
    'version': '15.0.1.1.0',
    'category': 'Web',
    'website': 'https://weasydoo.com',
    "application": False,
    "installable": True,
    'depends': ['wsy_web'],
    'data': [
        'views/res_config.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'wsy_web_customize_title/static/src/js/webclient.js',
        ],
    },
    'demo': [],
    'test': [],
}

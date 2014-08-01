{
    'name': 'Training',
    'version': '0.1',
    'category': 'Training',
    'description': """
    Hello world!
    """,
    'author': 'HoomamLabs',
    'website': 'http://Hoomamlabs.com',
    'depends': ['base'],
    'data': ['data/data.xml'],
    'update_xml' : [
        'view/order.xml',
        'view/product.xml',
        'view/order_line.xml'
    ],
    'installable': True,
    'auto_install': False,
}
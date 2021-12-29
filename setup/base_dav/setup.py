import setuptools

setuptools.setup(
    setup_requires=['setuptools-odoo'],
    odoo_addon={
        'external_dependencies_override': {
            'python': {
                'radicale': 'Radicale==2.1.11'
            }
        }
    },
)

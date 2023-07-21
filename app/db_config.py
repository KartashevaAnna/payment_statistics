db_config = {
    'connections': {
        # Dict format for connection
        'payment_statistics': {
            'engine': 'tortoise.backends.asyncpg',
            'credentials': {
                'host': 'localhost',
                'port': '5432',
                'user': 'postgres',
                'password': 'anna',
                'database': 'payment_statistics',
            }
        },

    },
    'apps': {
        'payment_statistics': {
            'models': ['app.models.company', 'app.models.user'],
            # If no default_connection specified, defaults to 'default'
            'default_connection': 'payment_statistics',
        }
    }
}
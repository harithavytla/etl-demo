import os

DB_DETAILS = {
    'dev': {
        'RETAIL_DB': {
            'DB_TYPE': 'mysql',
            'DB_HOST': '34.70.54.149',
            'DB_NAME': 'retail',
            'DB_USER': os.environ.get('RETAIL_DB_USER'),
            'DB_PASS': os.environ.get('RETAIL_DB_PASS')
        },
        'CUSTOMER_DB': {
            'DB_TYPE': 'postgres',
            'DB_HOST': '34.70.54.149',
            'DB_NAME': 'retail_dw',
            'DB_USER': os.environ.get('CUSTOMER_DB_USER'),
            'DB_PASS': os.environ.get('CUSTOMER_DB_PASS')
        }
    }
}
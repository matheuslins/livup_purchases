from decouple import config


HOST = config('HOST', default="0.0.0.0")
PORT = config('PORT', default='8080')
DEBUG = config('DEBUG', default=True, cast=bool)


DATABASE = {
    'DB_HOST': config('DB_HOST'),
    'DB_USER': config('DB_USER'),
    'DB_PASSWORD': config('DB_PASSWORD'),
    'DB_NAME': config('DB_NAME')
}


EXTERNAL_DB = {
    'DB_HOST': config('EXTERNAL_DB_HOST').format(config('EXTERNAL_DB_USER'), config('EXTERNAL_DB_PASSWORD'))
}

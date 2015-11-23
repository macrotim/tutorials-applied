#BROKER_URL = 'sqla+sqlite:////tmp/celerydb.sqlite'
#CELERY_RESULT_BACKEND = 'sqla+sqlite:////tmp/celerydb.sqlite'

BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'

#CELERY_TASK_SERIALIZER = 'json'
#CELERY_RESULT_SERIALIZER = 'json'
#CELERY_ACCEPT_CONTENT=['json']
#CELERY_TIMEZONE = 'Europe/Oslo'
#CELERY_ENABLE_UTC = True

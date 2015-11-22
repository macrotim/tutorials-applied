# In a production setting, use supervisord to keep 
# this worker running as a daemon.
celery -A tasks worker --loglevel=info

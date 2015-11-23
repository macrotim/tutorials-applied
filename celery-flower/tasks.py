import time
from celery import Celery

app = Celery('tasks')
app.config_from_object('celeryconfig')

@app.task
def crawl(url):
    import random
    delay = random.randint(1,10)
    time.sleep(delay)
    return delay

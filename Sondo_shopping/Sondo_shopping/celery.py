import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Sondo_shopping.settings')

app = Celery('Sondo_shopping')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'every-5-minutes':{
        'task':'notifications.tasks.SendAdvert',
        'schedule': 5,

    }

}
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
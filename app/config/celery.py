import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('currencies')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-client-notifications': {
        'task': 'catalogs.task.load_currencies',
        'schedule': crontab(minute='0', hour='0')
    }
}

import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject4.settings')

app = Celery('djangoProject4')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
from celery import Celery

from .settings import SETTINGS


celery = Celery()
celery.config_from_object(SETTINGS, namespace='CELERY')
celery.autodiscover_tasks(
    packages=['src']
)

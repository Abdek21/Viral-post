from celery import Celery
import os

def make_celery(app_name=__name__):
    return Celery(
        app_name,
        broker=os.getenv('REDIS_URL', 'redis://localhost:6379/0'),
        backend=os.getenv('REDIS_URL', 'redis://localhost:6379/0')
    )

celery = make_celery()

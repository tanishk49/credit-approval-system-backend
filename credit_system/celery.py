from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set default Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'credit_system.settings')

app = Celery('credit_approval_system')

# Load config from settings.py using django.conf settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Discover tasks from all registered Django app configs
app.autodiscover_tasks()

from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bringel.settings")

app = Celery("bringel")

app.config_from_object("django.conf:settings", namespace="CELERY")
# "namespace" refers to a container or scope that holds a set of identifiers
# (such as variables, functions, classes, or objects)

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")

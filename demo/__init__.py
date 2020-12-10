from __future__ import absolute_import, unicode_literals

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from apps.core.celery_job import app as celery_app

#디렉토리 내의 모든 python 파일들이 celery_app을 import
__all__ = ('celery_app',)
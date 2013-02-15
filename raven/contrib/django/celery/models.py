"""
raven.contrib.django.celery.models
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2010-2012 by the Sentry Team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

if not any(app in settings.INSTALLED_APPS
           for app in ('djcelery', 'djcelery_email')):
    raise ImproperlyConfigured("Put 'djcelery' or 'djcelery_email' in your "
        "INSTALLED_APPS setting in order to use the sentry celery client.")

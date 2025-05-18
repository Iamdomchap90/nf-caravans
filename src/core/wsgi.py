"""
WSGI config for NF caravans.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

application = get_wsgi_application()

# This needs to be called after we bootstrapped the application
# otherwise the settings wouldn't be configured
from django.conf import settings  # noqa isort:skip

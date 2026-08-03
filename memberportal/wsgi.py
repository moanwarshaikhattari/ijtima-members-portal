"""
WSGI config for memberportal project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'memberportal.settings')

application = get_wsgi_application()

# Vercel par Static Files serve karne ke liye WhiteNoise integration
app = WhiteNoise(application, root=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static'))
app.add_files(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'staticfiles_storage'), prefix='static/')

import os
import sys
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'memberportal.settings')

application = get_wsgi_application()

# Auto-collect static files if missing on Vercel boot
try:
    call_command('collectstatic', '--noinput')
except Exception as e:
    print(f"Collectstatic error: {e}")

app = application
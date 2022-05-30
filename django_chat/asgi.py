"""
ASGI config for django_chat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
import django
from django.core.asgi import get_asgi_application
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter,URLRouter
import chat.routing
from channels.auth import AuthMiddlewareStack

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_chat.settings')
django.setup()
#application = get_asgi_application()
application = ProtocolTypeRouter({
    "http":get_asgi_application(),
    "websocket":AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})

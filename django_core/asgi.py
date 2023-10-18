"""
ASGI config for django_core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from channels.routing import URLRouter, ProtocolTypeRouter

from django.core.asgi import get_asgi_application
import chat.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_core.settings')
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
	"http": django_asgi_app,
	"websocket": AllowedHostsOriginValidator(
		AuthMiddlewareStack(
			URLRouter(chat.routing.websocket_urlpatterns)
		)
	)
})

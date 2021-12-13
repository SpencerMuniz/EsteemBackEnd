"""
ASGI config for drf_jwt_capstone_backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""
# Original Settings
# import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE',
#                       'drf_jwt_capstone_backend.settings')

# application = get_asgi_application()


# import os
# import django
# from channels.routing import get_default_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE',
#                       'drf_jwt_capstone_backend.settings')
# django.setup()
# application = get_default_application()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})

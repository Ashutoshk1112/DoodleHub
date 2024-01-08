from email.mime import application
from channels.routing import ProtocolTypeRouter , URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack
from django.urls import path
from django.urls import re_path
from whiteboard.consumers import BoardConsumer 


# application = ProtocolTypeRouter({
#     'websocket': AuthMiddlewareStack(
#         URLRouter([
#             #path('ws/board/', BoardConsumer.as_asgi()),
#             re_path(r'ws/board/$', BoardConsumer.as_asgi()),
#         ])
#     ),
# })



application = ProtocolTypeRouter({
    'websocket' : AllowedHostsOriginValidator(
        URLRouter([
                path('' , BoardConsumer)
        ])
    )
})
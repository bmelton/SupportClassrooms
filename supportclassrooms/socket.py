import os
import uwsgi
import time
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "supportclassrooms.settings")

HTTP_SEC_WEBSOCKET_KEY="asdfzxcv9adfkj09df-"

from django.core.wsgi import get_wsgi_application

def application(env, start_response):
    uwsgi.websocket_handshake(HTTP_SEC_WEBSOCKET_KEY, env.get('HTTP_ORIGIN', ''))
    while True:
        msg = uwsgi.websocket_recv()
        uwsgi.websocket_send(msg)

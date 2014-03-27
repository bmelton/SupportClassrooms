import os
import uwsgi
import time
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "supportclassrooms.settings")

from django.core.wsgi import get_wsgi_application

def fake_start_response(status, headers, exc_info=None):
    pass

def application(env, start_response):
    if env['PATH_INFO'] == "/ws/":
        uwsgi.websocket_handshake(env.get('HTTP_SEC_WEBSOCKET_KEY', ''), env.get('HTTP_ORIGIN', ''))
        while True:
            msg = uwsgi.websocket_recv()
            uwsgi.websocket_send(msg)
    else:
        return get_wsgi_application()(env, start_response)

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)

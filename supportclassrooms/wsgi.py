import os
import uwsgi
import time
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "supportclassrooms.settings")

HTTP_SEC_WEBSOCKET_KEY="asdfzxcv9adfkj09df-"

from django.core.wsgi import get_wsgi_application

def fake_start_response(status, headers, exc_info=None):
    pass

def application(env, start_response):
    if env['PATH_INFO'] == "/ws/":
        uwsgi.websocket_handshake(HTTP_SEC_WEBSOCKET_KEY, env.get('HTTP_ORIGIN', ''))
        while True:
            time.sleep(10)
            uwsgi.websocket_send(str(time.time()))
    else:
        return get_wsgi_application()(env, start_response)

def app2():
    f = open('/var/log/nginx/access.log', 'r')
    yield f.read()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)

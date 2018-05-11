from __future__ import absolute_import, unicode_literals

from controllers.status import status_route
from controllers.summarize import summarize_route
from flask import Flask

def get_app():
    application = Flask("too_lazy")

    routes = [
        status_route,
        summarize_route
    ]
    for route in routes:
        application.register_blueprint(route, url_prefix='/api')

    return application

def main():
    application = get_app()
    application.run(host='127.0.0.1', port=8080)

app = get_app()

if __name__ == '__main__':
    main()
from __future__ import absolute_import, unicode_literals

from controllers.static import static_route
from controllers.status import status_route
from controllers.summarize import summarize_route
from flask import Flask

def get_app():
    application = Flask("too_lazy", static_url_path='')

    routes = [
        status_route,
        summarize_route
    ]
    for route in routes:
        application.register_blueprint(route, url_prefix='/api')
    
    application.register_blueprint(static_route)

    return application

def main():
    application = get_app()
    application.run(host='127.0.0.1', port=8080)

app = get_app()

if __name__ == '__main__':
    main()
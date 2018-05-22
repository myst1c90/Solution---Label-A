from pyramid.config import Configurator
from pyramid.response import Response


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('add', '/add/{1}')
    config.add_route('edit', '/edit/{1}')
    config.scan()
    return config.make_wsgi_app()




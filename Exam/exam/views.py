from pyramid.view import view_config
from pyramid.response import Response
from exam.Connection import Add, Edit


@view_config(route_name='add')
def add(request):
    response = Add()
    return Response(response)


@view_config(route_name='edit')
def edit(request):
    response = Edit()
    return Response(response)


@view_config(route_name='home', renderer='templates/mytemplate.jinja2')
def my_view(request):
    return {'project': 'Exam'}

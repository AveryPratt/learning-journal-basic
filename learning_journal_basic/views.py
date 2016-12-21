from pyramid.response import Response

def home_page(request):
    return Response("This is my first view!")


@view_config(route_name='home', renderer='/')
def my_view(request):
    return {'project': 'learning_journal_basic'}


@view_config(route_name='detail', renderer='/journal/{id:\d+}')
def my_view(request):
    return {'project': 'learning_journal_basic'}


@view_config(route_name='create', renderer='/journal/new-entry')
def my_view(request):
    return {'project': 'learning_journal_basic'}


@view_config(route_name='update', renderer='/journal/{id:\d+}/edit-entry')
def my_view(request):
    return {'project': 'learning_journal_basic'}
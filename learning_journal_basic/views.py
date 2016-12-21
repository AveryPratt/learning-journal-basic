# from pyramid.view import view_config

# def home_page(request):
#     return Response("This is my first view!")


# @view_config(route_name='home', renderer='/')
# def my_view(request):
#     return {'project': 'learning_journal_basic'}


# @view_config(route_name='detail', renderer='/journal/{id:\d+}')
# def my_view(request):
#     return {'project': 'learning_journal_basic'}


# @view_config(route_name='create', renderer='/journal/new-entry')
# def my_view(request):
#     return {'project': 'learning_journal_basic'}


# @view_config(route_name='update', renderer='/journal/{id:\d+}/edit-entry')
# def my_view(request):
#     return {'project': 'learning_journal_basic'}


import io
from pyramid.response import Response


def home(request):
    pass


def detail(request):
    pass


def create(request):
    pass


def update(request):
    pass


def includeme(config):
    config.add_view(home, route_name='home')
    config.add_view(detail, route_name='detail')
    config.add_view(create, route_name='create')
    config.add_view(update, route_name='update')


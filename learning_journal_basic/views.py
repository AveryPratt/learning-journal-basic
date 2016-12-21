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


import os
import io
from pyramid.view import view_config


@view_config(route_name="home", renderer="templates/averypratt-mockups/home.jinja2")
def home(request):
    return {
        "title": "Entry 11",
        "date": "12/19/16",
        "body": "body placeholder"
    }


@view_config(route_name="detail", renderer="templates/averypratt-mockups/detail.jinja2")
def detail(request):
    return {
        "title": "Entry 11",
        "body": "body placeholder",
        "date": "12/19/16"
    }


@view_config(route_name="create", renderer="templates/averypratt-mockups/create_form.jinja2")
def create(request):
    return {}


@view_config(route_name="update", renderer="templates/averypratt-mockups/edit_form.jinja2")
def update(request):
    return {
        "title": "Entry 11",
        "body": "body placeholder",
        "date": "12/19/16"
    }

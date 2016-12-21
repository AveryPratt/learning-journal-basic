import os
import io
from pyramid.view import view_config


ENTRIES = [
    {"id": 1, "title": "Entry 1", "date": "12/19/16", "body": "this is the body for entry 1"},
    {"id": 2, "title": "Entry 2", "date": "12/20/16", "body": "this is the body for entry 2"},
    {"id": 3, "title": "Entry 3", "date": "12/21/16", "body": "this is the body for entry 3"}
]


@view_config(route_name="home", renderer="templates/averypratt-mockups/home.jinja2")
def home(request):
    return {
        "entries": ENTRIES
    }


@view_config(route_name="detail", renderer="templates/averypratt-mockups/detail.jinja2")
def detail(request):
    return {
        "entries": ENTRIES
    }


@view_config(route_name="create", renderer="templates/averypratt-mockups/create_form.jinja2")
def create(request):
    return {
        "entries": ENTRIES
    }


@view_config(route_name="update", renderer="templates/averypratt-mockups/edit_form.jinja2")
def update(request):
    return {
        "entries": ENTRIES
    }

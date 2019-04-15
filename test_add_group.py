# -*- coding: utf-8 -*-


import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
        app.login(username="admin", password="secret")
        app.create_group(Group(name="new_group", header="new_group", footer="wow"))
        app.logout()


def test_add_group_empty(app):
        app.login(username="admin", password="secret")
        app.create_group(Group(name="", header="", footer=""))
        app.logout()




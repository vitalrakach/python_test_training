# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
        app.group.create(Group(name="new_group", header="new_group", footer="wow"))
        app.session.logout()


def test_add_group_empty(app):
        app.group.create(Group(name="", header="", footer=""))
        app.session.logout()




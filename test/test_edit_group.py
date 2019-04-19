# -*- coding: utf-8 -*-
from model.group import Group

def test_edit_first_group(app):

    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="edit_group", header="edit_group", footer="edited"))
    app.session.logout()
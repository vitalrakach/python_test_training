# -*- coding: utf-8 -*-
from model.group import Group

def test_edit_first_group_name(app):
    app.group.edit_first_group(Group(name="EDIT"))
    app.session.logout()


def test_edit_first_group_header(app):
    app.group.edit_first_group(Group(header="edit_group_HEADER"))
    app.session.logout()


def test_edit_first_group_footer(app):
    app.group.edit_first_group(Group(footer="edit_group_FOOTER"))
    app.session.logout()
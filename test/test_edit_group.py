# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(name="EDIT"))
    new_groups = app.group.get_group_list()
    assert len(old_groups)  == len(new_groups)



def test_edit_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(header="edit_group_HEADER"))
    new_groups = app.group.get_group_list()
    assert len(old_groups)  == len(new_groups)


def test_edit_first_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(footer="edit_group_FOOTER"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

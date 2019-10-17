# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    group_var = Group(name="edit")
    group_var.id = old_groups[0].id
    app.group.edit_first_group(group_var)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group_var
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


'''
def test_edit_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    group_var = Group(header="edit")
    group_var.id = old_groups[0].id
    app.group.edit_first_group(group_var)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group_var
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_edit_first_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(footer="edit_group_FOOTER"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
'''
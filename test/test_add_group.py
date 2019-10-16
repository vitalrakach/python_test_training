# -*- coding: utf-8 -*-

from model.group import Group



def test_add_group(app):
        old_groups = app.group.get_group_list()
        group_var = Group(name="new_group", header="new_group", footer="wow")
        app.group.create(group_var)
        new_groups = app.group.get_group_list()
        assert len(old_groups) + 1 == len(new_groups)
        old_groups.append(group_var)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_add_group_empty(app):
        old_groups = app.group.get_group_list()
        group_var = Group(name="new_group", header="new_group", footer="wow")
        app.group.create(group_var)
        new_groups = app.group.get_group_list()
        assert len(old_groups) + 1 == len(new_groups)
        old_groups.append(group_var)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)





# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    if check_ui:
        old_groups = app.group.get_group_list()
        app.group.create(group)
        new_groups = app.group.get_group_list()
        assert new_count_groups(old_groups) == app.group.count()
        old_groups.append(group)
    else:
        old_groups = db.get_group_list()
        app.group.create(group)
        new_groups = db.get_group_list()
        assert new_count_groups(old_groups) == app.group.count()
        old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def new_count_groups(old_groups):
    return len(old_groups) + 1

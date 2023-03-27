# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_modify_group_name(app, db, json_groups, check_ui):
    group = json_groups
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test name"))
    old_groups = db.get_group_list()
    selected_group = random.choice(old_groups)
    id = selected_group.id
    app.group.modify_group_by_index(id, group)
    new_groups = db.get_group_list()
    index = app.id_to_index(id, old_groups)
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

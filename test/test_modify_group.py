# -*- coding: utf-8 -*-
from model.group import Group
import random
from random import randrange


def test_modify_group_name(app, db, json_groups, check_ui):
    group = json_groups
    if app.group.count() == 0:
        app.group.create(Group(name="test name"))

    if check_ui:
        old_groups = app.group.get_group_list()
        index = randrange(len(old_groups))
        group.id = old_groups[index].id
        app.group.modify_group_by_index(index, group, check_ui)
        new_groups = app.group.get_group_list()
        old_groups[index] = group
    else:
        old_groups = db.get_group_list()
        db_group_selected = random.choice(old_groups)
        group.id = db_group_selected.id
        app.group.modify_group_by_index(db_group_selected.id, group, check_ui)
        new_groups = db.get_group_list()
        i = 0
        # old_groups = map(lambda x: x.id == db_group_selected.id, [group.id, group.name, group.header, group.footer])
        while i < len(old_groups):
            if old_groups[i].id == db_group_selected.id:
                old_groups[i].name = group.name
                old_groups[i].header = group.header
                old_groups[i].footer = group.footer
            i += 1

    assert len(old_groups) == len(new_groups)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
    else:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

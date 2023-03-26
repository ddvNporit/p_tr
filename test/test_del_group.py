# -*- coding: utf-8 -*-
import random
from random import randrange

from model.group import Group
import random


def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test name"))
    if check_ui:
        old_groups = app.group.get_group_list()
        index = randrange(len(old_groups))
        app.group.delete_group_by_index(index, check_ui)
        new_groups = app.group.get_group_list()
        assert new_count_groups(old_groups) == app.group.count()
        old_groups[index:index + 1] = []
        assert old_groups == new_groups
    else:
        old_groups = db.get_group_list()
        group = random.choice(old_groups)
        app.group.delete_group_by_id(group.id)
        new_groups = db.get_group_list()
        assert new_count_groups(old_groups) == len(new_groups)
        old_groups.remove(group)
        assert old_groups == new_groups


def new_count_groups(old_groups):
    return len(old_groups) - 1





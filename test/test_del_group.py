# -*- coding: utf-8 -*-
from model.group import Group
def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test name"))
    app.group.delete_group()

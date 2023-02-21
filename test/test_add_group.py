# -*- coding: utf-8 -*-
from model.group import Group

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.open_groups_page()
    app.group.fill(Group(name="", header="", footer=""))
    app.session.logout()
def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.open_groups_page()
    app.group.fill(Group(name="test add group name", header="test add group header", footer="test add group footer"))
    app.session.logout()



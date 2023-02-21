# -*- coding: utf-8 -*-
from model.group import Group

def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.open_groups_page()
    app.group.edit_group()
    app.group.fill(Group(name="test_edit_name", header="test_edit_header", footer="test_edit_footer"))
    app.group.edit_group_submit()
    app.session.logout()

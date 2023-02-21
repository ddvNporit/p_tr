# -*- coding: utf-8 -*-
from model.group import Group

def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.fill(Group(name="fdfdwedsds", header="sdssssdd", footer="вавпапапа"))
    app.session.logout()
# -*- coding: utf-8 -*-
from model.group import Group

def test_edit_first_group(app):
    app.group.open_groups_page()
    app.group.edit_group()
    app.group.fill_group_form(Group(name="test_edit_name", header="test_edit_header", footer="test_edit_footer"))
    app.group.edit_group_submit()

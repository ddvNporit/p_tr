# -*- coding: utf-8 -*-
def test_delete_first_group(app):
    # app.session.login(username="admin", password="secret")
    app.group.delete_group()
    # app.session.logout()

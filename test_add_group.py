# -*- coding: utf-8 -*-
from group import Group
from application import Application
import pytest

@pytest.fixture()
def app(request):
    fixture =Application()
    request.addfinalizer(fixture.destoy)
    return fixture
def test_add_group(app):
    app.login(username="admin", password="secret")
    app.add_new_group(Group(name="fggf", header="dsfdffd", footer="вавпр"))
    app.logout()
def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.add_new_group(Group(name="", header="", footer=""))
    app.logout()


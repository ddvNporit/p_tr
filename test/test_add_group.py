# -*- coding: utf-8 -*-
from model.group import Group
from fixture.application import Application
import pytest

@pytest.fixture()
def app(request):
    fixture =Application()
    request.addfinalizer(fixture.destoy)
    return fixture
def test_add_group(app):
    app.login(username="admin", password="secret")
    app.addNewGroup(Group(name="fggf", header="dsfdffd", footer="вавпр"))
    app.logout()
def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.addNewGroup(Group(name="", header="", footer=""))
    app.logout()

# Name : group_steps.py
# Author : "Denisov Dmitry"
# Time : 14.04.2023
from fixture.session import SessionHelper
from pytest_bdd import given, when, then, parsers
from fixture.group import Group


@given("a group list", target_fixture="group_list")
def group_list(db):
    return db.get_group_list()


#@given('a group with <name>, <header> and <footer>', target_fixture="new_groups")
@given(parsers.parse('a group with {name}, {header} and {footer}'), target_fixture='new_group')
def new_group(name, header, footer):
    return Group(name=name, header=header, footer=footer)


@when("I add the group to the list")
def add_new_group(app, new_group):
    app.group.create(new_group)


@then("the new group list is equal to the old list with the added group")
def verify_group_added(app, db, group_list, new_group, check_ui):
    old_groups = group_list
    new_groups = db.get_group_list()
    old_groups.append(new_group)
    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)

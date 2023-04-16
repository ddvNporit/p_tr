# Name : group_scenarios.py
# Author : "Denisov Dmitry"
# Time : 15.04.2023
from pytest_bdd import scenario
from .group_steps import *


@scenario("groups.feature", "Add new group")
def test_add_new_group():
    pass


@scenario("groups.feature", "Delete a group")
def test_delete_group():
    pass

# Name : contact_scenarios.ry.py
# Author : "Denisov Dmitry"
# Time : 16.04.2023
from pytest_bdd import scenario
from .contact_steps import *


@scenario("contacts.feature", "Add new contact")
def test_add_new_contact():
    pass


@scenario("contacts.feature", "Delete a contact")
def test_delete_contact():
    pass


@scenario("contacts.feature", "Edit a contact")
def test_modify_contact():
    pass

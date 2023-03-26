# Name: test_add_contact_to_group.py
# Author: Denisov
from model.group import Group
import random
from random import randrange
from model.contact import Contact


def test_add_contact_to_group(app, db, json_contact):
    new_contact = json_contact
    # new_group = json_groups
    if len(db.get_contact_list()) == 0:
        app.contact.create(new_contact)
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test name"))
    groups = db.get_group_list()
    db_group_selected = random.choice(groups)
    contacts = db.get_contact_list()
    db_contact_selected = random.choice(contacts)
    app.contact.add_contact_to_group_by_id(db_contact_selected.id, db_group_selected.id)


# Name: test_add_contact_to_group.py
# Author: Denisov
from model.group import Group
import random
from random import randrange
from model.contact import Contact

def test_add_contact_to_group(app, db, json_groups, json_contact):
    contact = json_contact
    group = json_groups
    if len(db.get_contact_list()) == 0:
        app.contact.create(contact)
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test name"))
    groups = db.get_group_list()
    db_group_selected = random.choice(groups)
    group.id = db_group_selected.id
    contacts = db.get_contact_list()
    db_contact_selected = random.choice(contacts)
    contact.id = db_contact_selected.id
# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_user(app, db, json_contact):
    contact = json_contact
    old_users = app.contact.get_contact_list()
    app.contact.create(contact)
    new_users = db.get_contact_list()
    # assert len(old_users) + 1 == app.contact.count()
    old_users.append(contact)
    assert sorted(old_users, key=Contact.id_or_max) == sorted(new_users, key=Contact.id_or_max)

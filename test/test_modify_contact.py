from model.contact import Contact
from random import randrange
import random


def test_modify_contact(app, db, json_contact, check_ui):
    contact = json_contact
    if len(db.get_contact_list()) == 0:
        app.contact.create(contact)
    old_contacts = db.get_contact_list()
    db_contact_selected = random.choice(old_contacts)
    id = db_contact_selected.id
    app.contact.modify_contact_by_index(db_contact_selected.id, contact)
    new_contacts = db.get_contact_list()
    index = app.id_to_index(id, old_contacts)
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)

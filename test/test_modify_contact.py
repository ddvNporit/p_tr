from model.contact import Contact
from random import randrange
import random

def test_modify_contact(app, db, json_contact, check_ui):
    contact = json_contact
    if app.contact.count() == 0:
        app.contact.create(contact)
    if check_ui:
        old_contact = app.contact.get_contact_list()
        index = randrange(len(old_contact))
        contact.id = old_contact[index].id
        app.contact.modify_contact_by_index(index, contact, check_ui)
        new_contact = app.contact.get_contact_list()
        old_contact[index] = contact
        assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
    else:
        old_contact = db.get_contact_list()
        db_contact_selected = random.choice(old_contact)
        contact.id = db_contact_selected.id
        app.contact.modify_contact_by_index(db_contact_selected.id, contact, check_ui)
        new_contacts = db.get_contact_list()
        assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



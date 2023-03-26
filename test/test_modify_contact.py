from model.contact import Contact
from random import randrange
import random

def test_modify_contact(app, db, json_contact, check_ui):
    contact = json_contact
    if app.contact.count() == 0:
        app.contact.create(contact)
    if check_ui:
        old_contacts = app.contact.get_contact_list()
        index = randrange(len(old_contacts))
        contact.id = old_contacts[index].id
        app.contact.modify_contact_by_index(index, contact, check_ui)
        new_contacts = app.contact.get_contact_list()
        old_contacts[index] = contact
        assert len(old_contacts) == len(new_contacts)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    else:
        old_contacts = db.get_contact_list()
        db_contact_selected = random.choice(old_contacts)
        contact.id = db_contact_selected.id
        app.contact.modify_contact_by_index(db_contact_selected.id, contact, check_ui)
        new_contacts = db.get_contact_list()
        i = 0
        while i < len(old_contacts):
            if old_contacts[i].id == db_contact_selected.id:
                old_contacts[i].firstname = contact.firstname
                old_contacts[i].header = contact.lastname
            i += 1
        assert len(old_contacts) == len(new_contacts)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



from model.contact import Contact
from random import randrange

def test_edit_user(app, json_contact):
    contact = json_contact
    if app.contact.count() == 0:
        app.contact.create(contact)
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    contact.id = old_contact[index].id
    app.contact.modify_user_by_index(index, contact)
    new_contact = app.contact.get_contact_list()
    old_contact[index] = contact
    assert len(old_contact) == len(new_contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


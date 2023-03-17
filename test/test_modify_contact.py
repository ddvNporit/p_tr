from model.contact import Contact
from random import randrange

def test_edit_user(app, json_contact):
    user = json_contact
    if app.contact.count() == 0:
        app.contact.create(user)
    old_users = app.contact.get_contact_list()
    index = randrange(len(old_users))
    user.id = old_users[index].id
    app.contact.modify_user_by_index(index, user)
    new_users = app.contact.get_contact_list()
    old_users[index] = user
    assert len(old_users) == len(new_users)
    assert sorted(old_users, key=Contact.id_or_max) == sorted(new_users, key=Contact.id_or_max)


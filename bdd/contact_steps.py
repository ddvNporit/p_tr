# Name : contact_steps.py
# Author : "Denisov Dmitry"
# Time : 16.04.2023
from pytest_bdd import given, when, then, parsers
import random, time
from model.contact import Contact


@given("a non-empty contact list", target_fixture="non_empty_contact_list")
def non_empty_contact_list(db, app):
    if not db.get_contact_list():
        app.contact.create(Contact(firstname="First_test", lastname="Last_test", address="ghhgh"))
    return db.get_contact_list()


@given("a random contact from the list", target_fixture="random_contact")
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


@when("I delete the contact from the list")
def delete_contact(app, random_contact):
    app.contact.delete_contact_by_index(random_contact.id)


@then("the new contact list is equal to the old list without the deleted contact")
def verify_contact_deleted(app, db, non_empty_contact_list, random_contact, check_ui):
    time.sleep(2)
    old_contacts = non_empty_contact_list
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) \
               == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


@given("a contact list", target_fixture="contact_list")
def contact_list(app, db):
    return db.get_contact_list()

@given(parsers.parse("a contact with {firstname}, {lastname} and {address}"),target_fixture="new_contact")
def new_contact(firstname, lastname, address):
    return Contact(firstname=firstname, lastname=lastname, address=address)


@when("I add the contact to the list")
def add_new_contact(app, new_contact):
    app.contact.create(new_contact)


@then("the new contact list is equal to the old list with the added contact")
def verify_contact_added(app, db, contact_list, new_contact, check_ui):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == \
               sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


@when("I edit the contact from the list according to given contact")
def edit_contact(app, random_contact, new_contact):
    app.contact.edit_contact_by_id(random_contact.id, new_contact)


@then("the new contact list is equal to the old list with the edited contact")
def verify_contact_edited(app, db, non_empty_contact_list, random_contact, new_contact, check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    old_contacts.remove(random_contact)
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    a = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    b = sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) \
               == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

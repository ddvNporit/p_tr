from model.contact import Contact
import random
import time
from random import randrange


def test_delete_any_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Петров", middlename="Иван", lastname="Иванович", nickname="кличка", \
                                   title="title", company="comp", address="address", home_phone="home",
                                   mobile_phone="232323", work_phone="232344354", \
                                   fax="232323", email="sd@test.com", email2="we@test.net", email3="wewd@t.er",
                                   homepage="http://ya.ru", \
                                   bday="23", bmonth="December", byear="1987", address2="jhdufyhdh", phone2="233443",
                                   notes="test add dfdjdj"))
    if check_ui:
        old_contacts = app.contact.get_contact_list()
        index = randrange(len(old_contacts))
        app.contact.delete_contact_by_index(index, check_ui)
        time.sleep(2)
        new_contacts = app.contact.get_contact_list()
        assert new_count_contacts(old_contacts) == app.contact.count()
        old_contacts[index:index + 1] = []
        assert old_contacts == new_contacts
    else:
        old_contacts = db.get_contact_list()
        contact = random.choice(old_contacts)
        app.contact.delete_contact_by_index(contact.id, check_ui)
        time.sleep(2)
        new_contact = db.get_contact_list()
        assert new_count_contacts(old_contacts) == app.contact.count()
        old_contacts.remove(contact)
        assert old_contacts == new_contact


def new_count_contacts(old_contact):
    return len(old_contact) - 1

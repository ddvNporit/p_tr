from model.contact import Contact
import random
import time


def test_delete_first_user(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Петров", middlename="Иван", lastname="Иванович", nickname="кличка", \
                                   title="title", company="comp", address="address", home_phone="home", mobile_phone="232323", work_phone="232344354", \
                                   fax="232323", email="sd@test.com", email2="we@test.net", email3="wewd@t.er", homepage="http://ya.ru", \
                                   bday="23", bmonth="December", byear="1987", address2="jhdufyhdh", phone2="233443", notes="test add dfdjdj"))
    old_contacts = db.get_contact_list()
    db_contact_selected = random.choice(old_contacts)
    id = db_contact_selected.id
    app.contact.delete_contact_by_index(id)
    time.sleep(2)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(db_contact_selected)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

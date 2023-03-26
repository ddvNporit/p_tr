from model.contact import Contact
import random
import time


def test_delete_first_user(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Петров", middlename="Иван", lastname="Иванович", nickname="кличка", \
                                   title="title", company="comp", address="address", home_phone="home",
                                   mobile_phone="232323", work_phone="232344354", \
                                   fax="232323", email="sd@test.com", email2="we@test.net", email3="wewd@t.er",
                                   homepage="http://ya.ru", \
                                   bday="23", bmonth="December", byear="1987", address2="jhdufyhdh", phone2="233443",
                                   notes="test add dfdjdj"))
    if check_ui:
        pass
    else:
        old_contact = db.get_contact_list()
        contact = random.choice(old_contact)
        app.contact.delete_contact_by_index(contact.id, check_ui)
        time.sleep(2)
        new_contact = db.get_contact_list()
    assert len(old_contact) - 1 == app.contact.count()
    old_contact.remove(contact)
    assert old_contact == new_contact

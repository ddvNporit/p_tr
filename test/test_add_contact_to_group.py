# Name: test_add_contact_to_group.py
# Author: Denisov
from model.group import Group
import random
from model.contact import Contact


def test_add_contact_to_group(app, db, orm):
    new_contact = Contact(firstname="firstname", middlename="Иван", lastname="Иванович", nickname="кличка", \
                          photo="D:\\PycharmProjects\\p_tr\\test\\placeimg_1000_459_arch.png", \
                          title="title", company="comp", address="address", home_phone="home", mobile_phone="232323",
                          work_phone="232344354", \
                          fax="232323", email="sd@test.com", email2="we@test.net", email3="wewd@t.er",
                          homepage="http://ya.ru", \
                          bday="23", bmonth="December", byear="1987", address2="jhdufyhdh", phone2="233443",
                          notes="test add dfdjdj")
    if len(db.get_contact_list()) == 0:
        app.contact.create(new_contact)
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test name"))
    groups = db.get_group_list()
    db_group_selected = random.choice(groups)
    contacts = orm.get_contacts_not_in_group(db_group_selected)
    if len(contacts) == 0:
        app.contact.create(new_contact)
        contacts = orm.get_contacts_not_in_group(db_group_selected)
    db_contact_selected = random.choice(contacts)
    app.contact.add_contact_to_group_by_id(db_contact_selected.id, db_group_selected.id)
    test_list = orm.get_contacts_in_group(db_group_selected)
    assert app.contact.search_contact_in_list(test_list, db_contact_selected) == True

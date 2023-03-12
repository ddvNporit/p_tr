# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_user(app):
    old_users = app.contact.get_contact_list()
    user = Contact(firstname="firstname", middlename="Иван", lastname="Иванович", nickname="кличка",\
                                   photo="D:\\PycharmProjects\\p_tr\\test\\placeimg_1000_459_arch.png", \
                                   title="title", company="comp", address="address", home_phone="34343 54 55", mobile_phone="232-323", work_phone="+2(323)44354", \
                                   fax="232323", email="sd@test.com", email2="we@test.net", email3="wewd@t.er", homepage="http://ya.ru", \
                                   bday="23", bmonth="December", byear="1987", address2="jhdufyhdh", phone2="233443", notes="test add dfdjdj")
    # user = Contact(firstname="firstname", middlename="Иван", lastname="Иванович")
    app.contact.create(user)
    new_users = app.contact.get_contact_list()
    assert len(old_users) + 1 == app.contact.count()
    old_users.append(user)
    assert sorted(old_users, key=Contact.id_or_max) == sorted(new_users, key=Contact.id_or_max)





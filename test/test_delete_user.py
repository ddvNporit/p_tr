from model.userfield import Contact
from random import randrange
import time


def test_delete_first_user(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Петров", middlename="Иван", lastname="Иванович", nickname="кличка", \
                                   title="title", company="comp", address="address", home_phone="home", mobile_phone="232323", work_phone="232344354", \
                                   fax="232323", email="sd@test.com", email2="we@test.net", email3="wewd@t.er", homepage="http://ya.ru", \
                                   bday="23", bmonth="December", byear="1987", address2="jhdufyhdh", phone2="233443", notes="test add dfdjdj"))
    old_users = app.contact.get_user_list()
    index = randrange(len(old_users))
    app.contact.delete_user_by_index(index)
    time.sleep(5)
    new_users = app.contact.get_user_list()
    assert len(old_users) - 1 == app.contact.count()
    old_users[index:index + 1] = []
    assert old_users == new_users



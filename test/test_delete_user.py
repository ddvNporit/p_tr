from model.userfield import UserfieldsName
import time


def test_delete_first_user(app):
    if app.user.count() == 0:
        app.user.create(UserfieldsName(firstname="Петров", middlename="Иван", lastname="Иванович", nickname="кличка", \
                                title="title", company="comp", address="address", home_phone="home", mobile_phone="232323", work_phone="232344354", \
                                fax="232323", email="sd@test.com", email2="we@test.net", email3="wewd@t.er", homepage="http://ya.ru", \
                                bday="23", bmonth="December", byear="1987", address2="jhdufyhdh", phone2="233443", notes="test add dfdjdj"))
    old_users = app.user.get_user_list()
    app.user.delete_user()
    time.sleep(5)
    new_users = app.user.get_user_list()
    assert len(old_users) - 1 == len(new_users)
    old_users[0:1] = []
    assert old_users == new_users



from model.userfield import UserfieldsName
from random import randrange

def test_edit_user(app):
    user = UserfieldsName(firstname="Петрова", middlename="Иванна", lastname="Ивановна", nickname="кличка", photo="", \
                                title="title", company="comp", address="address", home_phone="home", mobile_phone="232323", work_phone="232344354", \
                                fax="232323", email="sd@test.com", email2="we@test.net", email3="wewd@t.er", homepage="http://ya.ru", \
                                bday="23", bmonth="December", byear="1987", address2="jhdufyhdh", phone2="233443", notes="test add dfdjdj")
    if app.user.count() == 0:
        app.user.create(user)
    old_users = app.user.get_user_list()
    index = randrange(len(old_users))
    user.id = old_users[index].id
    app.user.modify_user_by_index(index, user)
    new_users = app.user.get_user_list()
    old_users[index] = user
    assert len(old_users) == len(new_users)
    assert sorted(old_users, key=UserfieldsName.id_or_max) == sorted(new_users, key=UserfieldsName.id_or_max)


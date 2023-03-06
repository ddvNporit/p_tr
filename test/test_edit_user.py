from model.userfield import UserfieldsName

def test_edit_user(app):
    user = UserfieldsName(firstname="Петров", middlename="Иван", lastname="Иванович", nickname="кличка", photo="", \
                                title="title", company="comp", address="address", home_phone="home", mobile_phone="232323", work_phone="232344354", \
                                fax="232323", email="sd@test.com", email2="we@test.net", email3="wewd@t.er", homepage="http://ya.ru", \
                                bday="23", bmonth="December", byear="1987", address2="jhdufyhdh", phone2="233443", notes="test add dfdjdj")
    if app.user.count() == 0:
        app.user.create(user)
    old_users = app.user.get_user_list()
    user.id = old_users[0].id
    app.user.modify_first_user(user)
    new_users = app.user.get_user_list()
    old_users[0] = user
    assert len(old_users) == len(new_users)

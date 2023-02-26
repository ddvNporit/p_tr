from model.userfield import UserfieldsName


def test_delete_first_user(app):
    if app.user.count() == 0:
        app.user.create(UserfieldsName(firstname="Петров", middlename="Иван", lastname="Иванович", nickname="кличка", \
                                title="title", company="comp", address="address", home_phone="home", mobile_phone="232323", work_phone="232344354", \
                                fax="232323", email="sd@test.com", email2="we@test.net", email3="wewd@t.er", homepage="http://ya.ru", \
                                bday="23", bmonth="December", byear="1987", address2="jhdufyhdh", phone2="233443", notes="test add dfdjdj"))
    app.user.delete_user()


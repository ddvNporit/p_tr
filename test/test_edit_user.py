from model.userfield import UserfieldsName

def test_edit_user(app):
    if app.user.count() == 0:
        app.user.create(UserfieldsName(firstname="Петров", middlename="Иван", lastname="Иванович", nickname="кличка", photo="", \
                                title="title", company="comp", address="address", home_phone="home", mobile_phone="232323", work_phone="232344354", \
                                fax="232323", email="sd@test.com", email2="we@test.net", email3="wewd@t.er", homepage="http://ya.ru", \
                                bday="23", bmonth="December", byear="1987", address2="jhdufyhdh", phone2="233443", notes="test add dfdjdj"))
    app.user.modify_first_user(UserfieldsName(firstname="956 test edit Иванов", middlename="test edit Джан", lastname="956 test edit Иныч", nickname="test edit  фунт", photo="", \
                                 title="title1", company="comp1", address="address1", home_phone="home1", mobile_phone="232323123", work_phone="23234435433", \
                                 fax="23232345", email="sd1@test.com", email2="we1@test.net", email3="wew1d@t.er", homepage="http://ya.ru/", \
                                 bday="25", bmonth="December", byear="1967", address2="jhdufyhdhttt", phone2="23344323", notes="956 test edit dfdjdjweer"))

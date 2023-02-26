from model.userfield import UserfieldsName

def test_edit_user(app):
    app.open_home_page()
    app.user.open_users_page()
    app.user.select_user()
    app.user.fill(UserfieldsName(firstname="956 test edit Иванов", middlename="test edit Джан", lastname="956 test edit Иныч", nickname="test edit  фунт", \
                                 title="title1", company="comp1", address="address1", home_phone="home1", mobile_phone="232323123", work_phone="23234435433", \
                                 fax="23232345", email="sd1@test.com", email2="we1@test.net", email3="wew1d@t.er", homepage="http://ya.ru/", \
                                 bday="25", bmonth="December", byear="1967", address2="jhdufyhdhttt", phone2="23344323", notes="956 test edit dfdjdjweer"))
    app.user.edit_user_submit()

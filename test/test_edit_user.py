from model.userfield import UserfieldsName

def test_edit_user(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.user.edit(UserfieldsName(firstname="Иванов", middlename="Джан", lastname="Иныч", nickname="фунт", \
                                title="title1", company="comp1", address="address1", home="home1", mobile="232323123", work="23234435433", \
                                fax="23232345", email="sd1@test.com", email2="we1@test.net", email3="wew1d@t.er", homepage="http://ya.ru/", \
                                bday="25", bmonth="December", byear="1967", address2="jhdufyhdhttt", phone2="23344323", notes="dfdjdjweer"))
    app.session.logout()
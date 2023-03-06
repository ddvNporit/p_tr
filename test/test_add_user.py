# -*- coding: utf-8 -*-
from model.userfield import UserfieldsName

def test_add_user(app):
    old_users = app.user.get_user_list()
    # user = UserfieldsName(firstname="firstname", middlename="Иван", lastname="Иванович", nickname="кличка",\
    #                                photo="D:\\PycharmProjects\\p_tr\\test\\placeimg_1000_459_arch.png", \
    #                                title="title", company="comp", address="address", home_phone="home", mobile_phone="232323", work_phone="232344354", \
    #                                fax="232323", email="sd@test.com", email2="we@test.net", email3="wewd@t.er", homepage="http://ya.ru", \
    #                                bday="23", bmonth="December", byear="1987", address2="jhdufyhdh", phone2="233443", notes="test add dfdjdj")
    user = UserfieldsName(firstname="firstname", middlename="Иван", lastname="Иванович")
    app.user.create(user)
    new_users = app.user.get_user_list()
    assert len(old_users) + 1 == len(new_users)





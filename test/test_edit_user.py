from model.userfield import Contact
from random import randrange

def test_edit_user(app):
    user = Contact(firstname="Петрова", middlename="Иванна", lastname="Ивановна", nickname="кличка",
                   photo="", \
                   title="title", company="comp", address="address", home_phone="454546556",
                   mobile_phone="232323", work_phone="232344354", \
                   fax="232323", email="sd@test.com", email2="we@test.net", email3="wewd@t.er",
                   homepage="http://ya.ru", \
                   bday="23", bmonth="December", byear="1987", address2="jhdufyhdh", phone2="233443",
                   notes="test add dfdjdj")
    if app.contact.count() == 0:
        app.contact.create(user)
    old_users = app.contact.get_user_list()
    index = randrange(len(old_users))
    user.id = old_users[index].id
    app.contact.modify_user_by_index(index, user)
    new_users = app.contact.get_user_list()
    old_users[index] = user
    assert len(old_users) == len(new_users)
    assert sorted(old_users, key=Contact.id_or_max) == sorted(new_users, key=Contact.id_or_max)


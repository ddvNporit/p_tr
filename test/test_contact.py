from model.contact import Contact
from random import randrange
import re
from fixture.orm import ORMFixture
def test_of_all_contact(app, json_contact):
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    contact = json_contact
    if len(db.get_contact_list()) == 0:
        app.contact.create(contact)
    list_contacts = db.get_contact_list()
    contact_from_home_page = app.contact.get_contact_list()
    assert sorted(contact_from_home_page, key=Contact.id_or_max) == sorted(list_contacts, key=Contact.id_or_max)
    i = 0
    while i < len(contact_from_home_page):
        id = contact_from_home_page[i].id
        contact_db = db.get_contact(id)
        assert contact_from_home_page[i].all_phones_from_home_page == merge_fields_like_on_home_page([contact_db[0].home_phone,
             contact_db[0].mobile_phone,
             contact_db[0].work_phone,
             contact_db[0].phone2])

        i += 1
        # assert contact_from_home_page.lastname.strip() == contact_from_db.lastname.strip()
        # assert contact_from_home_page.address == contact_from_db.address
        # assert contact_from_home_page.all_emails_from_home_page == merge_fields_like_on_home_page_email(
        #     [contact_from_edit_page.email,
        #      contact_from_edit_page.email2,
        #      contact_from_edit_page.email3])
# def test_of_any_contact(app):
#     user = Contact(firstname="Петрова", middlename="Иванна", lastname="Ивановна", nickname="кличка",
#                    photo="", \
#                    title="title", company="comp", address="address", home_phone="454546556",
#                    mobile_phone="232323", work_phone="232344354", \
#                    fax="232323", email="sd@test.com", email2="we@test.net", email3="wewd@t.er",
#                    homepage="http://ya.ru", \
#                    bday="23", bmonth="December", byear="1987", address2="jhdufyhdh", phone2="233443",
#                    notes="test add dfdjdj")
#     if app.contact.count() == 0:
#         app.contact.create(user)
#     old_users = app.contact.get_contact_list()
#     index = randrange(len(old_users))
#     user.id = old_users[index].id
#     contact_from_home_page = app.contact.get_contact_list()[index]
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
#
#     assert contact_from_home_page.all_phones_from_home_page == merge_fields_like_on_home_page(
#         [contact_from_edit_page.home_phone,
#          contact_from_edit_page.mobile_phone,
#          contact_from_edit_page.work_phone,
#          contact_from_edit_page.phone2])
#     assert contact_from_home_page.firstname.strip() == contact_from_edit_page.firstname.strip()
#     assert contact_from_home_page.lastname.strip() == contact_from_edit_page.lastname.strip()
#     assert contact_from_home_page.address.strip() == contact_from_edit_page.address.strip()
#     assert contact_from_home_page.all_emails_from_home_page == merge_fields_like_on_home_page_email(
#         [contact_from_edit_page.email,
#          contact_from_edit_page.email2,
#          contact_from_edit_page.email3])


def clear(s):
    return re.sub("[()  -]", "", s)


def merge_fields_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, contact))))


def c_new_str(s):
    if s is None:
        out = ""
    else:
        out = s
    return out.strip()


def merge_fields_like_on_home_page_email(contact):
    return "\n".join(filter(lambda x: x.strip() != "", map(lambda x: c_new_str(x), contact)))

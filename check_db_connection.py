# -*- coding: utf-8 -*-
# import mysql.connector
from fixture.db import DbFixture
from model.group import Group
from fixture.orm import ORMFixture

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
# db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")
try:
    # contacts = db.get_contact_list()
    # for contact in contacts:
    #     print(contact)
    # print(len(contacts))
    # l = db.get_group_list()
    # l = db.get_contacts_not_in_group(Group(id="628"))
    l = db.get_contact("541")
    # l = db.get_contact_list()
    for item in l:
        print(item.firstname)
    print(len(l))
finally:
    pass
    # db.destroy()
print(l[0].home_phone)

# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest, random, string


def random_string(prefix, maxlen):
    # symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_digits_for_phone(maxlen):
    symbols = string.digits + " " * 3 + "+" + "(" + ")" + "-"
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_for_email(maxlen):
    symbols = string.digits + string.ascii_letters + "@" + "_" + "."
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_for_http(maxlen):
    symbols = string.digits + string.ascii_letters + "/" + "_" + "." + ":"
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_for_month():
    list_month = ["December", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November" ]
    random_index = random.randint(0, len(list_month) - 1)
    return list_month[random_index]


testdata = [Contact(firstname=random_string("firstname", 10),
                    middlename=random_string("middlename", 10),
                    lastname=random_string("lastname", 10),
                    nickname=random_string("nickname", 10),
                    title=random_string("title", 10),
                    company=random_string("company", 10),
                    address=random_string("address", 10),
                    home_phone=random_digits_for_phone(12),
                    mobile_phone=random_digits_for_phone(12),
                    work_phone=random_digits_for_phone(12),
                    fax=random_digits_for_phone(12),
                    email=random_for_email(30),
                    email2=random_for_email(30),
                    email3=random_for_email(30),
                    homepage=random_for_http(100),
                    bday=str(random.randint(1, 28)),
                    bmonth=random_for_month(),
                    byear=str(random.randint(1930, 3028)),
                    address2=random_string("address2 ", 10),
                    phone2=random_digits_for_phone(12),
                    notes=random_string("notes ", 10)

                    # for firstname in ["", random_string("firstname", 10)]
                    # for middlename in ["", random_string("middlename", 10)]
                    # for lastname in ["", random_string("lastname", 10)]
                    # for nickname in ["", random_string("nickname", 10)]
                    # for title in ["", random_string("title", 10)]
                    # for company in ["", random_string("company", 10)]
                    # for address in ["", random_string("address", 10)]
                    # for home_phone in ["", random_digits_for_phone("home_phone", 12)]
                    # for mobile_phone in ["", random_digits_for_phone("mobile_phone", 12)]
                    # for work_phone in ["", random_digits_for_phone("work_phone", 12)]
                    # for fax in ["", random_digits_for_phone("fax", 12)]
                    # for email in ["", random_for_email("email", 30)]
                    # for email2 in ["", random_for_email("email2", 30)]
                    # for email3 in ["", random_for_email("email3", 30)]
                    # for homepage in ["", random_for_http("homepage", 100)]
                    # for bday in ["", random_for_date("bday", 28)]
                    # for bmonth in ["", random_for_date("bmonth", 12)]
                    # for byear in ["", random_for_date("byear", 9999)]
                    # for address2 in ["", random_string("address2", 100)]
                    # for phone2 in ["", random_digits_for_phone("phone2", 12)]
                    # for notes in ["", random_string("notes", 100)]

                    )
            for i in range(2)
            ]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_user(app, contact):
    old_users = app.contact.get_contact_list()
    app.contact.create(contact)
    new_users = app.contact.get_contact_list()
    assert len(old_users) + 1 == app.contact.count()
    old_users.append(contact)
    assert sorted(old_users, key=Contact.id_or_max) == sorted(new_users, key=Contact.id_or_max)

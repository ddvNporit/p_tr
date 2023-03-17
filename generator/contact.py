import random, string, os, jsonpickle, getopt, sys
from model.contact import Contact

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 1
f = "data/contacts.json"
for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    # symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    symbols = string.ascii_letters + string.digits + " "
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
    list_month = ["December", "January", "February", "March", "April", "May", "June", "July", "August", "September",
                  "October", "November"]
    random_index = random.randint(0, len(list_month) - 1)
    return list_month[random_index]


testdata = [Contact(firstname=random_string("firstname", 10).strip(),
                    middlename=random_string("middlename", 10).strip(),
                    lastname=random_string("lastname", 10).strip(),
                    nickname=random_string("nickname", 10).strip(),
                    title=random_string("title", 10).strip(),
                    company=random_string("company", 10).strip(),
                    address=random_string("address", 10).strip(),
                    home_phone=random_digits_for_phone(12).strip(),
                    mobile_phone=random_digits_for_phone(12).strip(),
                    work_phone=random_digits_for_phone(12).strip(),
                    fax=random_digits_for_phone(12).strip(),
                    email=random_for_email(30).strip(),
                    email2=random_for_email(30).strip(),
                    email3=random_for_email(30).strip(),
                    homepage=random_for_http(100).strip(),
                    bday=str(random.randint(1, 28)),
                    bmonth=random_for_month(),
                    byear=str(random.randint(1930, 3028)),
                    address2=random_string("address2 ", 10).strip(),
                    phone2=random_digits_for_phone(12),
                    notes=random_string("notes ", 10).strip()
                    )
            for i in range(n)
            ]
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))

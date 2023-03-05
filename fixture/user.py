from model.userfield import UserfieldsName
class UserFieldsHelper():
    def __init__(self, app):
        self.app = app


    def delete_user(self):
        wd = self.app.wd
        self.open_users_page()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td/input").click()
        self.accept_next_alert = True
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
    def create(self, add_new_user):
        wd = self.app.wd
        self.click_addnew()
        self.fill(add_new_user)
        self.add_user_submit()
        self.return_home_page()

    def return_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def open_users_page(self):
        wd = self.app.wd
        if not (wd.current_url == "http://localhost/addressbook/"):
            wd.find_element_by_link_text("home").click()

    def select_user(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
    def input_field_value(self, element_name, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(element_name).click()
            wd.find_element_by_name(element_name).clear()
            wd.find_element_by_name(element_name).send_keys(value)
    def fill(self, userfield):
        self.input_field_value("firstname", userfield.firstname)
        self.input_field_value("middlename", userfield.middlename)
        self.input_field_value("lastname", userfield.lastname)
        self.input_field_value("nickname", userfield.nickname)
        if userfield.photo != "":
            self.input_field_value("photo", userfield.photo)
        self.input_field_value("title", userfield.title)
        self.input_field_value("company", userfield.company)
        self.input_field_value("address", userfield.address)
        self.input_field_value("home", userfield.home_phone)
        self.input_field_value("mobile", userfield.mobile_phone)
        self.input_field_value("work", userfield.work_phone)
        self.input_field_value("fax", userfield.fax)
        self.input_field_value("email", userfield.email)
        self.input_field_value("email2", userfield.email2)
        self.input_field_value("email3", userfield.email3)
        self.input_field_value("homepage", userfield.homepage)
        self.input_field_value("bday", userfield.bday)
        # wd.find_element_by_xpath("//option[@value='" + userfield.bday + "']").click()
        self.input_field_value("bday", userfield.bday)
        # wd.find_element_by_xpath("//option[@value='" + userfield.bmonth + "']").click()
        self.input_field_value("byear", userfield.byear)
        self.input_field_value("address2", userfield.address2)
        self.input_field_value("phone2", userfield.phone2)
        self.input_field_value("notes", userfield.notes)

    def click_addnew(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def add_user_submit(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def edit_user_submit(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[22]").click()
    def count(self):
        wd = self.app.wd
        self.open_users_page()
        return len(wd.find_elements_by_name("selected[]"))
    def modify_first_user(self, userfield):
        self.open_users_page()
        self.select_user()
        self.fill(userfield)
        self.edit_user_submit()
        self.return_home_page()

    def get_user_list(self):
        wd = self.app.wd
        self.open_users_page()
        users = []
        for element in wd.find_elements_by_xpath("// tr[@name = 'entry']"):
            lastname = element.find_element_by_xpath("//*[@name='entry']/td[2]").text
            firstname = element.find_element_by_xpath("//*[@name='entry']/td[3]").text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            users.append(UserfieldsName(firstname=firstname, lastname=lastname, id=id))
        return users




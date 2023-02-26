
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
        self.return_home_page(wd)

    def return_home_page(self, wd):
        wd.find_element_by_link_text("home").click()

    def open_users_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def select_user(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
    def fill(self, userfield):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(userfield.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(userfield.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(userfield.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(userfield.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(userfield.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(userfield.company)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(userfield.address)
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(userfield.home_phone)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(userfield.mobile_phone)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(userfield.work_phone)
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(userfield.fax)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(userfield.email)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(userfield.email2)
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(userfield.email3)
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(userfield.homepage)
        wd.find_element_by_name("bday").click()
        wd.find_element_by_xpath("//option[@value='" + userfield.bday + "']").click()
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_xpath("//option[@value='" + userfield.bmonth + "']").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(userfield.byear)
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(userfield.address2)
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(userfield.phone2)
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(userfield.notes)

    def click_addnew(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def add_user_submit(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        wd.find_element_by_link_text("home").click()

    def edit_user_submit(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[22]").click()
        wd.find_element_by_link_text("home").click()

from selenium import webdriver
from selenium.webdriver.support.select import Select
from fixture.session_user import SessionHelper
class Application_u():
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
    def addNewUser(self, userfield, useraddress):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()
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
        wd.find_element_by_name("title").send_keys(useraddress.title)
        wd.find_element_by_name("company").send_keys(useraddress.company)
        wd.find_element_by_name("address").send_keys(useraddress.address)
        wd.find_element_by_name("home").send_keys(useraddress.home)
        wd.find_element_by_name("mobile").send_keys(useraddress.mobile)
        wd.find_element_by_name("work").send_keys(useraddress.work)
        wd.find_element_by_name("fax").send_keys(useraddress.fax)
        wd.find_element_by_name("email").send_keys(useraddress.email)
        wd.find_element_by_name("email2").send_keys(useraddress.email2)
        wd.find_element_by_name("email3").send_keys(useraddress.email3)
        wd.find_element_by_name("homepage").send_keys(useraddress.homepage)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(useraddress.bday)
        wd.find_element_by_xpath("//option[@value='25']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(useraddress.bmonth)
        wd.find_element_by_xpath("//option[@value='December']").click()
        wd.find_element_by_name("byear").send_keys(useraddress.byear)
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("address2").send_keys(useraddress.address2)
        wd.find_element_by_name("phone2").send_keys(useraddress.phone2)
        wd.find_element_by_name("notes").send_keys(useraddress.notes)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        wd.find_element_by_link_text("home").click()

    def openHomePage(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destoy(self):
        self.wd.quit()
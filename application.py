# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()
    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()
    def add_new_group(self, group):
        wd = self.wd
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()
    
    def add_new_user(self, userfield):
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
        wd.find_element_by_name("title").send_keys(userfield.title)
        wd.find_element_by_name("company").send_keys(userfield.company)
        wd.find_element_by_name("address").send_keys(userfield.address)
        wd.find_element_by_name("home").send_keys(userfield.home)
        wd.find_element_by_name("mobile").send_keys(userfield.mobile)
        wd.find_element_by_name("work").send_keys(userfield.work)
        wd.find_element_by_name("fax").send_keys(userfield.fax)
        wd.find_element_by_name("email").send_keys(userfield.email)
        wd.find_element_by_name("email2").send_keys(userfield.email2)
        wd.find_element_by_name("email3").send_keys(userfield.email3)
        wd.find_element_by_name("homepage").send_keys(userfield.homepage)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(userfield.bday)
        wd.find_element_by_xpath("//option[@value='" + userfield.bday + "']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(userfield.bmonth)
        wd.find_element_by_xpath("//option[@value='" + userfield.bmonth + "']").click()
        wd.find_element_by_name("byear").send_keys(userfield.byear)
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("address2").send_keys(userfield.address2)
        wd.find_element_by_name("phone2").send_keys(userfield.phone2)
        wd.find_element_by_name("notes").send_keys(userfield.notes)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        wd.find_element_by_link_text("home").click()
    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()
        self.open_groups_page()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
    def destoy(self):
        self.wd.quit()

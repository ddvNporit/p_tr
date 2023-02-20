# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from login import LoginS
from userfield import UserfieldsName
import unittest

class TestAddUser(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_user(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, LoginS(username="admin", password="secret"))
        self.add_new_user(wd, UserfieldsName(firstname="Петров", middlename="Иван", lastname="Иванович", nickname="кличка", \
                                             title="title", company="comp", address="address", home="home", mobile="232323", work="232344354", \
                                             fax="232323", email="sd@test.com", email2="we@test.net", email3="wewd@t.er", homepage="http://ya.ru", \
                                             bday="25", bmonth="December", byear="1987", address2="jhdufyhdh", phone2="233443", notes="dfdjdj"))
        self.logout(wd)
    def add_new_user(self, wd, userfield):
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


    def login(self, wd, login):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(login.username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(login.password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True
    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()

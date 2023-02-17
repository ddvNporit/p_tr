# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from group import Group
from login import LoginS
from selenium.webdriver.firefox.options import Options
import unittest

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        self.wd = webdriver.Firefox(executable_path=r'C:\Windows\SysWOW64\geckodriver.exe', options=options)
        # self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.wd

    def test_add_group(self):
        wd = self.wd
        self.login(wd, LoginS(username="admin", password="secret"))
        self.addNewGroup(wd, Group(name="fggf", header="dsfdffd", footer="вавпр"))
        self.logout(wd)
    def test_add_empty_group(self):
        wd = self.wd
        self.login(wd, LoginS(username="admin", password="secret"))
        self.addNewGroup(wd, Group(name="", header="", footer=""))
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()
    # def open_page_group(self, wd):
    #     wd.find_element_by_link_text("groups").click()
    def return_to_groups_page(self, wd):
        wd.find_element_by_link_text("group page").click()
    def addNewGroup(self, wd, group):
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page(wd)

    def open_groups_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def login(self, wd, login):
        self.openHomePage(wd)

        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(login.username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(login.password)
        wd.find_element_by_xpath("//input[@value='Login']").click()
        self.open_groups_page(wd)

    def openHomePage(self, wd):
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()

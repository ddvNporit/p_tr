# -*- coding: utf-8 -*-
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.userfield import UserFieldsHelper

class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.user = UserFieldsHelper(self)

    def openHomePage(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destoy(self):
        self.wd.quit()


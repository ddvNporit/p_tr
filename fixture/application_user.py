from selenium import webdriver
from fixture.session_user import SessionHelper
from fixture.userfield import UserFieldsHelper
class Application_u():
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.user = UserFieldsHelper(self)

    def openHomePage(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destoy(self):
        self.wd.quit()
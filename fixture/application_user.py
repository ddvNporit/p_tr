from selenium import webdriver
from fixture.session_user import UserSessionHelper
from fixture.userfield import UserFieldsHelper
class Application_u():
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = UserSessionHelper(self)
        self.user = UserFieldsHelper(self)

    def openHomePage(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destoy(self):
        self.wd.quit()
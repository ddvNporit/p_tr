from model.contact import Contact
from selenium.webdriver.support.ui import Select
import re


# -*- coding: utf-8 -*-
class UserFieldsHelper():
    def __init__(self, app):
        self.app = app

    def delete_user(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index, check_ui):
        wd = self.app.wd
        self.open_users_page()
        if check_ui:
            self.select_user_by_index(index)
        else:
            self.select_delete_user_by_id(index)
        self.accept_next_alert = True
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.user_cache = None

    def select_user_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_modify_user_by_id(self, index):
        wd = self.app.wd
        # wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//a[@href='edit.php?id=" + index + "']").click()

    def select_delete_user_by_id(self, index):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[id='%s']" % index).click()

    def create(self, add_new_user):
        wd = self.app.wd
        self.click_addnew()
        self.fill(add_new_user)
        self.add_user_submit()
        self.return_home_page()
        self.user_cache = None

    def return_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def open_users_page(self):
        wd = self.app.wd
        if not (wd.current_url == self.app.base_url):
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

    def dropdown_field_value(self, element_name, value):
        wd = self.app.wd
        if value is not None:
            Select(wd.find_element_by_name(element_name)).select_by_visible_text(value)

    def fill(self, userfield):
        self.input_field_value("firstname", userfield.firstname)
        self.input_field_value("middlename", userfield.middlename)
        self.input_field_value("lastname", userfield.lastname)
        self.input_field_value("nickname", userfield.nickname)
        # if userfield.photo != "":
        #     self.input_field_value("photo", userfield.photo)
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
        self.dropdown_field_value("bday", userfield.bday)
        # wd.find_element_by_xpath("//option[@value='" + userfield.bday + "']").click()
        self.dropdown_field_value("bmonth", userfield.bmonth)
        # self.dropdown_field_value("bday", userfield.bday)
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
        self.modify_contact_by_index(0, userfield, )

    def select_user_modify_by_index(self, index):
        wd = self.app.wd
        id = wd.find_elements_by_name("selected[]")[index].get_attribute("value")
        # wd.find_element_by_xpath("//img[@alt='Edit']").click()
        wd.find_element_by_xpath(
            "//table[@id='maintable']/tbody/tr[*]/td[8]/a[@href='edit.php?id=" + str(id) + "']").click()

    def modify_contact_by_index(self, index, userfield, check_ui):
        self.open_users_page()
        if check_ui:
            self.select_user_modify_by_index(index)
        else:
            self.select_modify_user_by_id(index)
        self.fill(userfield)
        self.edit_user_submit()
        self.return_home_page()
        self.user_cache = None

    user_cache = None

    def get_contact_list(self):
        if self.user_cache is None:
            wd = self.app.wd
            self.open_users_page()
            self.user_cache = []
            for element in wd.find_elements_by_xpath("// tr[@name = 'entry']"):
                cells = element.find_elements_by_tag_name("td")
                lastname = element.find_element_by_xpath("./td[2]").text
                # firstname=cell[1].text
                firstname = element.find_element_by_xpath("./td[3]").text
                address = element.find_element_by_xpath("./td[4]").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.user_cache.append(Contact(lastname=lastname, firstname=firstname, id=id,
                                               all_phones_from_home_page=all_phones, address=address,
                                               all_emails_from_home_page=all_emails))
        return list(self.user_cache)

    def open_contact_to_edit_by_index(self, index):
        pass

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        # self.open_users_page()
        # row = wd.find_elements_by_name("entry")[index]
        # cell = row.find_elements_by_tag_name("td")[6]
        # cell.find_element_by_tag_name("a").click
        id = wd.find_elements_by_name("selected[]")[index].get_attribute("value")
        wd.find_element_by_xpath(
            "//table[@id='maintable']/tbody/tr[*]/td[7]/a[@href='view.php?id=" + str(id) + "']").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_users_page()
        self.select_user_modify_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, home_phone=homephone,
                       work_phone=workphone, mobile_phone=mobilephone, phone2=secondaryphone, address=address,
                       email=email, email2=email2, email3=email3)

    def get_contact_view_page(self, index):
        wd = self.app.wd
        self.open_users_page()
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        try:
            homephone = re.search("H: (.*)", text).group(1)
        except:
            homephone = ""
        try:
            workphone = re.search("W: (.*)", text).group(1)
        except:
            workphone = ""
        try:
            mobilephone = re.search("M: (.*)", text).group(1)
        except:
            mobilephone = ""
        try:
            secondaryphone = re.search("P: (.*)", text).group(1)
        except:
            secondaryphone = ""
        return Contact(home_phone=homephone,
                       work_phone=workphone, mobile_phone=mobilephone, phone2=secondaryphone)

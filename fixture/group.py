from model.group import Group


class GroupHelper():
    def __init__(self, app):
        self.app = app

    def modify_first_group(self):
        self.modify_group_by_index(0)

    def modify_group_by_index(self, index, new_group_data, check_ui):
        wd = self.app.wd
        self.open_groups_page()
        if check_ui:
            self.select_group_by_index(index)
        else:
            self.select_group_by_id(index)
        # open modify group form
        self.edit_group()
        # fill group form
        self.fill_group_form(new_group_data)
        # submit modification
        self.edit_group_submit()
        self.return_to_groups_page()
        self.group_cache = None

    def create(self, add_new_group):
        wd = self.app.wd
        self.open_groups_page()
        self.new_group()
        self.fill_group_form(add_new_group)
        self.add_group_submit()
        self.return_to_groups_page()
        self.group_cache = None

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def add_group_submit(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()
        # self.return_to_groups_page()

    def edit_group_submit(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def new_group(self):
        wd = self.app.wd
        wd.find_element_by_name("new").click()

    def edit_group(self):
        wd = self.app.wd
        # self.select_first_group()
        wd.find_element_by_name("edit").click()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()
        # wd.find_element_by_xpath("//input[@value='" + index + "']").click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def delete_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index, check_ui):
        wd = self.app.wd
        self.open_groups_page()
        if check_ui:
            self.select_group_by_index(index)
        else:
            self.select_group_by_id(index)
        # submit delete
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None


    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def select_first_group(self):
        wd = self.app.wd
        # select first group
        wd.find_element_by_name("selected[]").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                if text is None:
                    text = ''
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)

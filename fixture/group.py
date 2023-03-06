from model.group import Group
class GroupHelper():
    def __init__(self, app):
        self.app = app
    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # open modify group form
        self.edit_group()
        # fill group form
        self.fill_group_form(new_group_data)
        # submit modification
        self.edit_group_submit()
        self.return_to_groups_page()
    def create(self, add_new_group):
        wd = self.app.wd
        self.open_groups_page()
        self.new_group()
        self.fill_group_form(add_new_group)
        self.add_group_submit()
        self.return_to_groups_page()

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

    def open_groups_page(self):
        wd = self.app.wd
        if not(wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new"))>0):
            wd.find_element_by_link_text("groups").click()
    def delete_group(self):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))
    group_cashe = None
    def get_group_list(self):
        if self.group_cashe is not None:
            wd = self.app.wd
            self.open_groups_page()
            groups = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                groups.append(Group(name=text, id=id))
        return groups




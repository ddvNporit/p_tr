from model.group import Group

def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="New group name"))
    # app.session.logout()
def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="Group new header"))
    # app.session.logout()
def test_modify_group_footer(app):
    app.group.modify_first_group(Group(footer="Group new footer"))
    # app.session.logout()
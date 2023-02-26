from model.group import Group

def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test name"))
    app.group.modify_first_group(Group(name="New group name"))
def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test name"))
    app.group.modify_first_group(Group(header="Group new header"))
def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test name"))
    app.group.modify_first_group(Group(footer="Group new footer"))
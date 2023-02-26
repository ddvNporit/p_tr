from model.userfield import UserfieldsName

def test_delete_first_user(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test name"))
    app.user.delete_user()


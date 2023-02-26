from model.userfield import UserfieldsName

def test_delete_first_user(app):
    app.open_home_page()
    app.user.delete_user()


from model.userfield import UserfieldsName

def test_delete_first_user(app):
    app.open_home_page()
    # app.session.login(username="admin", password="secret")
    app.user.delete_user()
    # app.session.logout()

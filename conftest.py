from fixture.application import Application
import pytest

fixture = None


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--baseUrl")
    password = request.config.getoption("--pass")
    if fixture is None:
        fixture = Application(browser=browser, base_url=base_url)
        # fixture.session.login(username="admin", password="secret")
    else:
        if not fixture.is_valid():
            fixture = Application(browser=browser, base_url=base_url)
    fixture.session.ensure_login(username="admin", password=password)
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    # fixture =Application()
    # fixture.session.login(username="admin", password="secret")
    def fin():
        fixture.session.ensure_logout()
        fixture.destoy()

    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook/")
    parser.addoption("--pass", action="store", default="secret") # можно default удалить, ноя для удобства не стал

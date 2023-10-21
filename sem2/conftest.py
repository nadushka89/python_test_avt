import pytest
import yaml
from module import Site

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


@pytest.fixture()
def selector_login():
    return """// *[ @ id = "login"] / div[1] / label / input"""


@pytest.fixture()
def selector_password():
    return """//*[@id="login"]/div[2]/label/input"""


@pytest.fixture()
def selector_button():
    return "button"


@pytest.fixture()
def selector_error():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""


@pytest.fixture()
def site():
    site_inst = Site(testdata["address"])
    yield site_inst
    site_inst.my_quit()


@pytest.fixture()
def selector_home():
    return """//*[@id="app"]/main/nav/a/span"""


@pytest.fixture()
def selector_create_post():
    return """/html/body/div[1]/main/div/div[2]/div[1]/button"""


@pytest.fixture()
def selector_title():
    return """//*[@id="create-item"]/div/div/div[1]/div/label/input"""


@pytest.fixture()
def selector_desc():
    return """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""


@pytest.fixture()
def selector_content():
    return """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""

@pytest.fixture()
def selector_save():
    return """//*[@id="create-item"]/div/div/div[7]/div/button/span"""

@pytest.fixture()
def selector_post_create():
    return """//*[@id="app"]/main/div/div[1]/div/div[3]"""

import time

import pytest
import yaml
from module import Site

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


# site = Site(testdata["address"])


def test_step1(site, selector_login, selector_password, selector_button, selector_error):
    input1 = site.find_element("xpath", selector_login)
    input1.send_keys("test")
    input2 = site.find_element("xpath", selector_password)
    input2.send_keys("test")
    btn = site.find_element("css", selector_button)
    btn.click()
    error_text3 = site.find_element("xpath", selector_error)
    assert error_text3.text == "401"


def test_step2(site, selector_login, selector_password, selector_button, selector_home):
    input1 = site.find_element("xpath", selector_login)
    input1.send_keys(testdata.get("username"))
    input2 = site.find_element("xpath", selector_password)
    input2.send_keys(testdata.get("password"))
    btn = site.find_element("css", selector_button)
    btn.click()
    home_path = site.find_element("xpath", selector_home)
    assert home_path.text == "Home", "test Fail"


def test_step3(site, selector_login, selector_password, selector_button, selector_home, selector_create_post,
               selector_title, selector_desc, selector_content, selector_save, selector_post_create):
    input1 = site.find_element("xpath", selector_login)
    input1.send_keys(testdata.get("username_for_post"))
    input2 = site.find_element("xpath", selector_password)
    input2.send_keys(testdata.get("password_for_post"))
    btn = site.find_element("css", selector_button)
    btn.click()
    home_path = site.find_element("xpath", selector_home)
    assert home_path.text == "Home", "test Fail"
    btn_create_post = site.find_element("xpath", selector_create_post)
    btn_create_post.click()
    time.sleep(testdata["sleep_time"])
    input3 = site.find_element("xpath", selector_title)
    input3.send_keys(testdata.get("title"))
    input4 = site.find_element("xpath", selector_desc)
    input4.send_keys(testdata.get("desc"))
    input5 = site.find_element("xpath", selector_content)
    input5.send_keys(testdata.get("content"))
    btn_save = site.find_element("xpath", selector_save)
    btn_save.click()
    time.sleep(testdata["sleep_time"])
    new_post = site.find_element("xpath", selector_post_create)
    assert new_post.text == testdata.get("content"), "test Fail"



if __name__ == '__main__':
    pytest.main(["-vv"])

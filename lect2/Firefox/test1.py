import pytest
import yaml
from module import Site

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
site = Site(testdata["address"])

def test_step1():
    x_selector1 = """// *[ @ id = "login"] / div[1] / label / input"""

    input1= site.find_element("xpath", x_selector1)
    input1.send_keys("test")
    x_selector2 = """//*[@id="login"]/div[2]/label/input"""
    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys("test")
    btn_selector = "button"
    btn = site.find_element("css", btn_selector)
    btn.click()
    x_selector3 = """//*[@id="app"]/main/div/div/div[2]/h2"""
    error_text3 = site.find_element("xpath", x_selector3)
    assert error_text3.text == "401"


if __name__ == '__main__':
    pytest.main(["-vv"])
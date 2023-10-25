import logging
import time
import yaml
from testpage import OperationsHelper


with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)


def test_step1(browser):
    logging.info('Test1 Starting')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login('test')
    testpage.enter_pass('test')
    testpage.click_login_button()
    assert testpage.get_error_text() == '401', 'test1 failed'


def test_step2(browser):
    logging.info('Test2 Starting')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata['username_for_post'])
    testpage.enter_pass(testdata['password_for_post'])
    testpage.click_login_button()
    assert testpage.get_login_text() == f'Hello, {testdata["username_for_post"]}', 'test2 failed'


def test_step3(browser):
    logging.info('Test3 Starting')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata['username_for_post'])
    testpage.enter_pass(testdata['password_for_post'])
    testpage.click_login_button()
    testpage.click_create_post_btn()
    time.sleep(1)
    testpage.enter_post_title(testdata['title'])
    testpage.enter_post_description(testdata['desc'])
    testpage.enter_post_content(testdata['content'])
    testpage.click_save_btn()
    time.sleep(2)
    assert testpage.get_added_post_title() == testdata['title'], 'test3 failed'


# Задание
# Условие: Добавить в проект тест по проверке механики работы формы Contact Us на главной странице личного кабинета.
# Должно проверятся открытие формы, ввод данных в поля, клик по кнопке и появление всплывающего alert.
# Совет: переключиться на alert можно командой alert = self.driver.switch_to.alert
# Вывести текст alert.text

def test_step4(browser):
    logging.info("Test4 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata['username_for_post'])
    testpage.enter_pass(testdata['password_for_post'])
    testpage.click_login_button()
    testpage.click_contact_button()
    testpage.enter_name(testdata["name"])
    testpage.enter_email(testdata["email"])
    testpage.enter_contact_content("contact me")
    testpage.click_contact_save_button()
    time.sleep(3)
    assert testpage.get_alert_text() == "Form successfully submitted", "Test_4 FAIL"
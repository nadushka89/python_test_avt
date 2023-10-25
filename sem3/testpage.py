import logging
from BaseApp import BasePage
from selenium.webdriver.common.by import By


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, 'button')
    LOCATOR_HELLO_LOGIN = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[3]/a""")
    LOCATOR_CREATE_POST_BTN = (By.XPATH, """//*[@id="app"]/main/div/div[2]/div[1]""")
    LOCATOR_POST_TITLE = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input""")
    LOCATOR_POST_DESCRIPTION = (By.XPATH, """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea""")
    LOCATOR_POST_CONTENT = (By.XPATH, """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""")
    LOCATOR_SAVE_BTN = (By.XPATH, """//*[@id="create-item"]/div/div/div[7]/div/button""")
    LOCATOR_POST_ADDED = (By.CSS_SELECTOR, 'h1')
    LOCATOR_TITLE_TEXT = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")
    LOCATOR_CONTACT_BTN = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_CONTACT_NAME_FIELD = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_CONTACT_EMAIL_FIELD = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_CONTACT_CONTENT_FIELD = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_ALERT_FIELD = (By.XPATH, """ """)
    LOCATOR_CONTACT_SAVE_BTN = (By.XPATH, """//*[@id="contact"]/div[4]/button""")


class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def click_login_button(self):
        logging.info("Click login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=2)
        text = error_field.text
        logging.info(f"Found text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        return text

    def get_login_text(self):
        element_successful_login = self.find_element(TestSearchLocators.LOCATOR_HELLO_LOGIN)
        return element_successful_login.text

    # def get_alert_text(self):
    #     alert_field = self.find_element(TestSearchLocators.LOCATOR_ALERT_FIELD, time=2)
    #     text = alert_field.text
    #     logging.info(f"Found text {text} in error field {TestSearchLocators.LOCATOR_ALERT_FIELD[1]}")
    #     return text

    def alert_get_text(self):
        logging.info("Get alert message")
        alert_message = self.get_alert_text()
        logging.info(f"Alert message - {alert_message}")
        return alert_message

    def click_create_post_btn(self):
        logging.info('Click create new post button')
        self.find_element(TestSearchLocators.LOCATOR_CREATE_POST_BTN).click()

    def enter_post_title(self, word):
        logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_POST_TITLE[1]}')
        title_field = self.find_element(TestSearchLocators.LOCATOR_POST_TITLE)
        title_field.clear()
        title_field.send_keys(word)

    def enter_post_description(self, word):
        logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_POST_DESCRIPTION[1]}')
        description_field = self.find_element(TestSearchLocators.LOCATOR_POST_DESCRIPTION)
        description_field.clear()
        description_field.send_keys(word)

    def enter_post_content(self, word):
        logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_POST_CONTENT[1]}')
        content_field = self.find_element(TestSearchLocators.LOCATOR_POST_CONTENT)
        content_field.clear()
        content_field.send_keys(word)

    def click_save_btn(self):
        logging.info('Click save button')
        self.find_element(TestSearchLocators.LOCATOR_SAVE_BTN).click()

    def click_contact_button(self):
        logging.info('Click save button')
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_BTN).click()

    def click_contact_save_button(self):
        logging.info('Click contact save button')
        self.find_element(TestSearchLocators. LOCATOR_CONTACT_SAVE_BTN).click()

    def get_added_post_title(self):
        post_title = self.find_element(TestSearchLocators.LOCATOR_POST_ADDED)
        return post_title.text

    def enter_name(self, word):
        logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_CONTACT_NAME_FIELD[1]}')
        contact_name = self.find_element(TestSearchLocators.LOCATOR_CONTACT_NAME_FIELD)
        return contact_name


    def enter_email(self, word):
        logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_CONTACT_EMAIL_FIELD[1]}')
        contact_email = self.find_element(TestSearchLocators.LOCATOR_CONTACT_EMAIL_FIELD)
        return contact_email

    def enter_contact_content(self, word):
        logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_CONTACT_CONTENT_FIELD[1]}')
        contact_content = self.find_element(TestSearchLocators.LOCATOR_CONTACT_CONTENT_FIELD)
        return contact_content
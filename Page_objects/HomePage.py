import time

from selenium.webdriver.common.by import By

from Page_objects.BasePage import BasePage


class HomePage(BasePage):

    def open_home_page(self):
        self.driver.get("https://guest:welcome2qauto@qauto.forstudy.space/")
        time.sleep(1)

    def click_sign_in_button(self):
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-outline-white header_signin']").click()
        time.sleep(1)

    def click_registration_button(self):
        self.driver.find_element(By.XPATH,
                                 "//button[@class='btn btn-link' and contains(text(),'Registration')]").click()
        time.sleep(1)

    def fill_sign_up_name(self, signupName: str):
        self.driver.find_element(By.ID, "signupName").send_keys(signupName)

    def fiil_sign_up_last_name(self, signupLastName: str):
        self.driver.find_element(By.ID, "signupLastName").send_keys(signupLastName)

    def fill_sign_up_email(self, signupEmail: str):
        self.driver.find_element(By.ID, "signupEmail").send_keys(signupEmail)

    def fill_sign_up_password(self, signupPassword: str):
        self.driver.find_element(By.ID, "signupPassword").send_keys(signupPassword)

    def fill_sign_up_repeat_password(self, signupRepeatPassword: str):
        self.driver.find_element(By.ID, "signupRepeatPassword").send_keys(signupRepeatPassword)

    def click_register_button(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary' and contains(text(),'Register')]").click()
        time.sleep(1)

    def fill_sign_in_form(self):
        self.driver.find_element(By.ID, "signinEmail").send_keys("test12345test12345@gmail.com")
        self.driver.find_element(By.ID, "signinPassword").send_keys("Test12345")
        time.sleep(1)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary' and contains(text(),'Login')]").click()
        time.sleep(1)

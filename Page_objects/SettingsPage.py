import time

from selenium.webdriver.common.by import By

from Page_objects.BasePage import BasePage


class SettingsPage(BasePage):

    def open_settings_page(self):
        self.driver.find_element(By.XPATH, "//a[@routerlink='settings' and contains(text(), 'Settings')]").click()
        time.sleep(1)

    def click_remove_my_account_button(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-danger-bg' and contains(text(),'Remove my "
                                           "account')]").click()
        time.sleep(1)

    def click_remove_button(self):
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-danger' and contains(text(),'Remove')]").click()
        time.sleep(1)
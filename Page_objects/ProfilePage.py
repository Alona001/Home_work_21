import time

from selenium.webdriver.common.by import By

from Page_objects.BasePage import BasePage


class ProfilePage(BasePage):

    def open_profile_page(self):
        self.driver.find_element(By.XPATH, "//a[@routerlink='profile' and contains(text(), 'Profile')]").click()
        time.sleep(1)

    def get_profile_name(self):
        profile_name = self.driver.find_element(By.XPATH, "//p[@class='profile_name display-4']")
        time.sleep(1)
        return profile_name.text

import time

from selenium.webdriver.common.by import By

from Page_objects.BasePage import BasePage


class GaragePage(BasePage):
    def open_garage_page(self):
        self.driver.find_element(By.XPATH, "//a[@routerlink='garage' and contains(text(), 'Garage')]").click()
        time.sleep(1)

    def click_add_car_button(self):
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary' and contains(text(), 'Add car')]").click()
        time.sleep(1)

    def fill_car_brand(self, brand: str):
        self.driver.find_element(By.ID, "addCarBrand").send_keys(brand)

    def fill_car_model(self, model: str):
        self.driver.find_element(By.ID, "addCarModel").send_keys(model)

    def fill_car_mileage(self, mileage: int):
        self.driver.find_element(By.ID, "addCarMileage").send_keys(mileage)

    def click_add_button(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//div[@class='modal-content']//button[@class='btn btn-primary' and "
                                           "contains(text(), 'Add')]").click()
        time.sleep(1)



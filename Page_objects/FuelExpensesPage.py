import time

from selenium.webdriver.common.by import By

from Page_objects.BasePage import BasePage


class FuelExpensesPage(BasePage):

    def open_fuel_expenses_page(self):
        self.driver.find_element(By.XPATH, "//a[@routerlink='expenses' and contains(text(), 'Fuel expenses')]").click()
        time.sleep(1)

    def click_add_an_expense(self):
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary' and contains(text(), 'Add an expense')]").click()
        time.sleep(1)

    def fill_vehicle(self, vehicle: str):
        self.driver.find_element(By.ID, "addExpenseCar").send_keys(vehicle)

    def fill_report_date(self, report_date: str):
        self.driver.find_element(By.ID, "addExpenseDate").send_keys(report_date)

    def fill_mileage(self, mileage: int):
        presenter = self.driver.find_element(By.ID, "addExpenseMileage")
        presenter.clear()
        presenter.send_keys(mileage)
        time.sleep(1)

    def fill_number_of_liters(self, number_of_liters: int):
        self.driver.find_element(By.ID, "addExpenseLiters").send_keys(number_of_liters)
        time.sleep(1)

    def fill_total_cost(self, total_cost: int):
        self.driver.find_element(By.ID, "addExpenseTotalCost").send_keys(total_cost)
        time.sleep(1)

    def click_add_button(self):
        self.driver.find_element(By.XPATH, "//div[@class='modal-content']//button[@class='btn btn-primary' and "
                                           "contains(text(), 'Add')]").click()
        time.sleep(1)



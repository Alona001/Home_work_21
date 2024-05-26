import datetime

from Page_objects.FuelExpensesPage import FuelExpensesPage
from Page_objects.GaragePage import GaragePage
from Page_objects.HomePage import HomePage
from Page_objects.ProfilePage import ProfilePage
from Page_objects.SettingsPage import SettingsPage

NUMBER_OF_LITERS = 10

FUEL_COST = 3

MILEAGE = 500

Q7 = 'Q7'

AUDI = 'Audi'
AUDI_Q7 = AUDI + " " + Q7

SIGN_UP_NAME = "test"

SIGN_UP_LAST_NAME = "test"

SIGN_UP_EMAIL = "test12345test12345@gmail.com"

SIGN_UP_PASSWORD = "Test12345"


def test_create_new_user(driver):
    home_page = HomePage(driver)
    home_page.open_home_page()
    home_page.click_sign_in_button()
    home_page.click_registration_button()
    home_page.fill_sign_up_name(SIGN_UP_NAME)
    home_page.fiil_sign_up_last_name(SIGN_UP_LAST_NAME)
    home_page.fill_sign_up_email(SIGN_UP_EMAIL)
    home_page.fill_sign_up_password(SIGN_UP_PASSWORD)
    home_page.fill_sign_up_repeat_password(SIGN_UP_PASSWORD)
    home_page.click_register_button()


def test_check_profile_name(driver):
    home_page = HomePage(driver)
    profile_page = ProfilePage(driver)
    sign_in(home_page)
    profile_page.open_profile_page()
    profile_name = profile_page.get_profile_name()

    assert profile_name == SIGN_UP_NAME + " " + SIGN_UP_LAST_NAME


def test_add_car(driver):
    home_page = HomePage(driver)
    garage_page = GaragePage(driver)
    sign_in(home_page)
    garage_page.open_garage_page()
    garage_page.click_add_car_button()
    garage_page.fill_car_brand(AUDI)
    garage_page.fill_car_model(Q7)
    garage_page.fill_car_mileage(MILEAGE)
    garage_page.click_add_button()


def test_add_an_expenses(driver):
    home_page = HomePage(driver)
    fuel_expenses_page = FuelExpensesPage(driver)
    sign_in(home_page)
    fuel_expenses_page.open_fuel_expenses_page()
    fuel_expenses_page.click_add_an_expense()
    fuel_expenses_page.fill_vehicle(AUDI_Q7)
    fuel_expenses_page.fill_report_date(datetime.date.today().strftime("DD-mm-YYYY"))
    new_mileage = MILEAGE + 100
    fuel_expenses_page.fill_mileage(new_mileage)
    fuel_expenses_page.fill_number_of_liters(NUMBER_OF_LITERS)
    total_cost = NUMBER_OF_LITERS * FUEL_COST
    fuel_expenses_page.fill_total_cost(total_cost)
    fuel_expenses_page.click_add_button()


def test_delete_user(driver):
    # Delete user
    home_page = HomePage(driver)
    settings_page = SettingsPage(driver)
    sign_in(home_page)
    settings_page.open_settings_page()
    settings_page.click_remove_my_account_button()
    settings_page.click_remove_button()


def sign_in(home_page):
    home_page.open_home_page()
    home_page.click_sign_in_button()
    home_page.fill_sign_in_form()
    home_page.click_login_button()

from .base_page_trip import BasePageTrip
from .locators_trip import MainTripLocators
from .locators_trip import CreateTripLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import datetime
import time
import os


class MainPageTrip(BasePageTrip):
    def click_button_add_trip(self):
        self.browser_dev.find_element(*MainTripLocators.BUTTON_ADD).click()


class CreateBusinessTrip(MainPageTrip):
    def write_deadline_trip(self):
        period = self.browser_dev.find_element(*CreateTripLocators.TRIP_PERIOD)
        period.send_keys(Keys.CONTROL, 'a' + Keys.BACKSPACE)
        date = datetime.date.today().strftime("%d.%m.%Y")
        period.send_keys(date + Keys.ENTER)

    def add_a_weekend_work(self):
        self.browser_dev.find_element(*CreateTripLocators.WEEKEND_SWITCHER).click()
        self.browser_dev.find_element(*CreateTripLocators.REASON_WEEKEND).send_keys("Нужен отдых")
        period_weekend = self.browser_dev.find_element(*CreateTripLocators.WEEKEND_PERIOD)
        period_weekend.send_keys(Keys.CONTROL, 'a' + Keys.BACKSPACE)
        period_weekend.send_keys("26.05.2022 - 27.05.2022" + Keys.ENTER)
        self.browser_dev.find_element(*CreateTripLocators.BUTTON_ADD_MORE_WEEKEND).click()
        period_weekend2 = self.browser_dev.find_element(*CreateTripLocators.WEEKEND_PERIOD_2)
        period_weekend2.send_keys(Keys.CONTROL, 'a' + Keys.BACKSPACE)
        period_weekend2.send_keys("29.05.2022" + Keys.ENTER)

    def add_overtime_work(self):
        self.browser_dev.find_element(*CreateTripLocators.OVERTIME_SWITCHER).click()
        self.browser_dev.find_element(*CreateTripLocators.OVERTIME_REASON).send_keys("Нужно поработать еще")
        self.browser_dev.find_element(*CreateTripLocators.OVERTIME_TASK).send_keys("Чтобы все успеть")
        overtime_start = self.browser_dev.find_element(*CreateTripLocators.OVERTIME_START)
        overtime_start.send_keys(Keys.CONTROL, 'a' + Keys.BACKSPACE)
        overtime_start.send_keys("29.05.2022" + Keys.ENTER)
        overtime_end = self.browser_dev.find_element(*CreateTripLocators.OVERTIME_END)
        overtime_end.send_keys(Keys.CONTROL, 'a' + Keys.BACKSPACE)
        overtime_end.send_keys("30.05.2022" + Keys.ENTER)

    def choose_a_trip_city(self, city):
        self.browser_dev.find_element(*CreateTripLocators.INPUT_CITY).send_keys(city)
        self.browser_dev.find_element(*CreateTripLocators.SELECT_CITY).click()

    def union_business_trip(self, worker):
        union = self.browser_dev.find_element(*CreateTripLocators.UNION_TRIP)
        ActionChains(self.browser_dev).move_to_element(union).click().send_keys(worker).perform()
        self.browser_dev.find_element(*CreateTripLocators.UNION_TRIP_WORKER).click()
        self.browser_dev.find_element(*CreateTripLocators.BUTTON_UNION_LIST).click()

    # добавить норм ожидание
    def choose_company_for_a_trip(self):
        company = self.browser_dev.find_element(*CreateTripLocators.COMPANY)
        ActionChains(self.browser_dev).move_to_element(company).click().send_keys("Тестовый контрагент").perform()
        time.sleep(5)
        self.browser_dev.find_element(*CreateTripLocators.SELECT_COMPANY).click()
        self.browser_dev.find_element(*CreateTripLocators.ADDRESS).send_keys("ул. Ленина 29")

    def add_trip_plan(self):
        stage = self.browser_dev.find_elements(*CreateTripLocators.PLAN)
        ActionChains(self.browser_dev).move_to_element(stage[0]).click().send_keys("1 этап").perform()
        add_stage = self.browser_dev.find_element(*CreateTripLocators.ADD_STAGE_PLAN)
        ActionChains(self.browser_dev).move_to_element(add_stage).click().send_keys("2 этап").perform()
        self.browser_dev.find_elements(*CreateTripLocators.REMOVE_STAGE)[0].click()

    def add_order(self):
        self.browser_dev.find_element(*CreateTripLocators.ORDER).click()

    def write_medical_contraindications(self):
        self.browser_dev.find_element(*CreateTripLocators.MEDICINE).click()
        self.browser_dev.find_element(*CreateTripLocators.MEDICINE_INPUT).send_keys("AIDS")

    # добавить загрузку еще других файлов и подумать как сделать повторную загрузку

    def select_factory_order(self, order=True):
        if order:
            self.browser_dev.find_element(*CreateTripLocators.FACTORY_ORDER_INPUT).send_keys("Портал")
            time.sleep(5)
            self.browser_dev.find_element(*CreateTripLocators.FACTORY_ORDER).click()
            # upload file factory order
            self.browser_dev.find_element(*CreateTripLocators.SUPPORTING_DOCUMENT).click()
            directory = os.path.abspath(os.path.dirname(__file__))
            file_png = "TestImage.png"
            path = os.path.join(directory, file_png)
            self.browser_dev.find_element(*CreateTripLocators.UPLOAD_SUPPORTING_DOCUMENT).send_keys(path)
        else:
            self.browser_dev.find_element(*CreateTripLocators.FACTORY_ORDER_SWITCH).click()
            self.browser_dev.find_element(*CreateTripLocators.EXPENSE_ITEM).click()
            self.browser_dev.find_element(*CreateTripLocators.EXPENSE_INPUT).send_keys("Командировочные затраты")
            self.browser_dev.find_element(*CreateTripLocators.CHOOSING_EXPENSES).click()

    # добавить загрузку других файлов. Подумать как доделать повторную загрузку файлов

    def upload_document_to_the_direction(self):
        self.browser_dev.find_element(*CreateTripLocators.DOCUMENT_DIRECTION).click()
        directory = os.path.abspath(os.path.dirname(__file__))
        file_name = "TestImage.png"
        file_path = os.path.join(directory, file_name)
        self.browser_dev.find_element(*CreateTripLocators.UPLOAD_DOCUMENT_DIRECTION).send_keys(file_path)

    def fill_all_types_expenses(self):
        Select(self.browser_dev.find_element(*CreateTripLocators.DAILY_EXPENSES)).select_by_value("256")
        self.browser_dev.find_element(*CreateTripLocators.TRAVEL_EXPENSES).send_keys("1000")
        self.browser_dev.find_element(*CreateTripLocators.OTHER_EXPENSES).send_keys("1000")

    def get_daily_expenses_in_cash(self):
        # получить деньги(наличкой, по дефолту карта)
        self.browser_dev.find_element(*CreateTripLocators.GET_EXPENSES).click()

    def plot_a_route_by_employee_339(self, route=True):
        self.browser_dev.find_element(*CreateTripLocators.TRANSPORT).click()
        if route:
            # комментарий для билетов
            iframe_comment = self.browser_dev.find_element(*CreateTripLocators.COMMENT_TICKETS)
            self.browser_dev.switch_to_frame(iframe_comment)
            self.browser_dev.find_elements(*CreateTripLocators.IFRAME)[0].send_keys("Test Comment")
            self.browser_dev.switch_to_default_content()
        else:
            self.browser_dev.find_element(*CreateTripLocators.ROUTE_339).click()
            # комментарий для билетов
            iframe_comment = self.browser_dev.find_element(*CreateTripLocators.COMMENT_TICKETS)
            self.browser_dev.switch_to_frame(iframe_comment)
            self.browser_dev.find_elements(*CreateTripLocators.IFRAME)[0].send_keys("Test Comment")
            self.browser_dev.switch_to_default_content()
            # номер билета поезда
            self.browser_dev.find_element(*CreateTripLocators.TRAIN_PLANE_NUMBER).send_keys("666")

    def add_time_and_date(self):
        start = self.browser_dev.find_element(*CreateTripLocators.ARRIVAL_DATE)
        start.send_keys(Keys.CONTROL, 'a' + Keys.BACKSPACE)
        start.send_keys("25.05.2022 12:00" + Keys.ENTER)
        end = self.browser_dev.find_element(*CreateTripLocators.DATE_END)
        end.send_keys(Keys.CONTROL, 'a' + Keys.BACKSPACE)
        end.send_keys("01.06.2022 23:00" + Keys.ENTER)

    def fill_passport_information(self):
        self.browser_dev.find_element(*CreateTripLocators.MOBILE_NUMBER).send_keys("89114567865")
        self.browser_dev.find_element(*CreateTripLocators.CITIZENSHIP).send_keys("РФ")
        passport = self.browser_dev.find_element(*CreateTripLocators.DATE_PASSPORT)
        passport.send_keys(Keys.CONTROL, 'a' + Keys.BACKSPACE)
        passport.send_keys("09.11.2013" + Keys.ENTER)
        self.browser_dev.find_element(*CreateTripLocators.PASSPORT_SERIES_NUMBER).send_keys("1111 333444")
        birth = self.browser_dev.find_element(*CreateTripLocators.DATE_BIRTH)
        birth.send_keys(Keys.CONTROL, 'a' + Keys.BACKSPACE)
        birth.send_keys("25.07.1998" + Keys.ENTER)
        self.browser_dev.find_element(*CreateTripLocators.PLACE_BIRTH).send_keys("Санкт-Петербург")

    def only_required_employees_of_the_process(self):
        self.browser_dev.find_element(*CreateTripLocators.HEAD_DEPARTAMENT).click()
        self.browser_dev.find_element(*CreateTripLocators.SELECT_USERS).click()
        self.browser_dev.find_element(*CreateTripLocators.PAYMENT_DEPARTAMENT).click()
        self.browser_dev.find_element(*CreateTripLocators.SELECT_USERS).click()
        self.browser_dev.find_element(*CreateTripLocators.HEAD_DIRECTION).click()
        self.browser_dev.find_element(*CreateTripLocators.SELECT_USERS).click()
        self.browser_dev.find_element(*CreateTripLocators.APPROVING).click()
        self.browser_dev.find_element(*CreateTripLocators.SELECT_USERS).click()

    def all_employees_of_the_process(self):
        self.browser_dev.find_element(*CreateTripLocators.HEAD_DEPARTAMENT).click()
        self.browser_dev.find_element(*CreateTripLocators.SELECT_USERS).click()
        self.browser_dev.find_element(*CreateTripLocators.CONSTRUCTOR).click()
        self.browser_dev.find_element(*CreateTripLocators.SELECT_USERS).click()
        self.browser_dev.find_element(*CreateTripLocators.FACTORY_ORDER_HEAD).click()
        self.browser_dev.find_element(*CreateTripLocators.SELECT_USERS).click()
        self.browser_dev.find_element(*CreateTripLocators.PAYMENT_DEPARTAMENT).click()
        self.browser_dev.find_element(*CreateTripLocators.SELECT_USERS).click()
        self.browser_dev.find_element(*CreateTripLocators.HEAD_DIRECTION).click()
        self.browser_dev.find_element(*CreateTripLocators.SELECT_USERS).click()
        self.browser_dev.find_element(*CreateTripLocators.RESPONSIBLE_EVENT).click()
        self.browser_dev.find_element(*CreateTripLocators.SELECT_USERS).click()
        self.browser_dev.find_element(*CreateTripLocators.NOTIFY_TRIP).click()
        self.browser_dev.find_element(*CreateTripLocators.SELECT_USERS).click()
        self.browser_dev.find_element(*CreateTripLocators.APPROVING).click()
        self.browser_dev.find_element(*CreateTripLocators.SELECT_USERS).click()

    def add_purpose_trip(self):
        trip_iframe = self.browser_dev.find_element(*CreateTripLocators.PURPOSE_TRIP)
        self.browser_dev.switch_to_frame(trip_iframe)
        self.browser_dev.find_elements(*CreateTripLocators.IFRAME)[0].send_keys("Test Comment")
        self.browser_dev.switch_to_default_content()

    def click_button_submit(self):
        self.browser_dev.find_element(*CreateTripLocators.BUTTON_SUBMIT).click()

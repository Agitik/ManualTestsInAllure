from .trip_card_page import TripCardPage
from .locators_trip import TripRoadMapLocators
from selenium.webdriver.support.select import Select


class TripRoadPage(TripCardPage):
    def select_role_of_a_trip_participant(self, *args, rejection=True, n=0):
        self.click_view_route()
        self.role_switching(*args)
        self.task_description_is_present()
        self.browser_dev.find_elements(*TripRoadMapLocators.BUTTON_START)[n].click()
        if rejection:
            self.browser_dev.find_element(*TripRoadMapLocators.BUTTON_APPROVE).click()
        else:
            self.browser_dev.find_element(*TripRoadMapLocators.REJECT_COMMENT).send_keys("Исправить ошибки")
            self.browser_dev.find_element(*TripRoadMapLocators.BUTTON_CANCEL).click()
        self.browser_dev.close()
        self.browser_dev.switch_to_window(self.browser_dev.window_handles[0])

    def select_role_responsible_person(self, *args, rejection=True):
        self.click_view_route()
        self.role_switching(*args)
        self.task_description_is_present()
        self.browser_dev.find_element(*TripRoadMapLocators.BUTTON_START).click()
        self.browser_dev.find_element(*TripRoadMapLocators.REJECT_COMMENT).send_keys("Замечаний нет")
        if rejection:
            self.browser_dev.find_element(*TripRoadMapLocators.BUTTON_APPROVE).click()
        else:
            self.browser_dev.find_element(*TripRoadMapLocators.BUTTON_NONAPPROVE).click()
        self.browser_dev.close()
        self.browser_dev.switch_to_window(self.browser_dev.window_handles[0])

    def select_role_of_the_approver(self, *args, employee=None, rejection=True):
        self.click_view_route()
        self.role_switching(*args)
        self.task_description_is_present()
        self.browser_dev.find_element(*TripRoadMapLocators.BUTTON_START).click()
        if employee is None:
            pass
        else:
            self.browser_dev.find_element(*TripRoadMapLocators.EXTRA_EMPLOYEE).click()
            self.browser_dev.find_element(*TripRoadMapLocators.CLICK_ADDITIONAL).click()
        if rejection:
            self.browser_dev.find_element(*TripRoadMapLocators.BUTTON_APPROVE).click()
        else:
            self.browser_dev.find_element(*TripRoadMapLocators.BUTTON_CANCEL).click()
        self.browser_dev.close()
        self.browser_dev.switch_to_window(self.browser_dev.window_handles[0])

    # придумать с делегированием
    def select_role_hr_departament(self, *args):
        self.click_view_route()
        self.role_switching(*args)
        self.task_description_is_present()
        self.browser_dev.find_element(*TripRoadMapLocators.BUTTON_START).click()
        self.browser_dev.find_element(*TripRoadMapLocators.BUTTON_TAKE_TO_WORK).click()
        Select(self.browser_dev.find_element(*TripRoadMapLocators.INVITE_INPUT)).select_by_value("Y")
        self.browser_dev.find_element(*TripRoadMapLocators.ORDER_NUMBER).send_keys("1337")
        self.browser_dev.find_element(*TripRoadMapLocators.CALENDAR).click()
        self.browser_dev.find_element(*TripRoadMapLocators.CALENDAR_DAY).click()
        Select(self.browser_dev.find_element(*TripRoadMapLocators.TASK_COMPLETED)).select_by_value("Y")
        self.browser_dev.find_element(*TripRoadMapLocators.BUTTON_APPROVE).click()
        self.browser_dev.close()
        self.browser_dev.switch_to_window(self.browser_dev.window_handles[0])

    # делегирование и продумать загрузку файлов
    def select_role_aho_departament(self, *args):
        self.click_view_route()
        self.role_switching(*args)
        self.task_description_is_present()
        self.browser_dev.find_element(*TripRoadMapLocators.BUTTON_START).click()
        self.browser_dev.find_element(*TripRoadMapLocators.BUTTON_TAKE_TO_WORK).click()
        self.browser_dev.find_element(*TripRoadMapLocators.NUMBER_TRAIN_OR_PLANE).send_keys("666")
        self.browser_dev.find_element(*TripRoadMapLocators.NAME_HOTEL).send_keys("Отель 'Москва'")
        self.browser_dev.find_element(*TripRoadMapLocators.ADDRESS_HOTEL).send_keys("ул. Земельная 29")
        Select(self.browser_dev.find_element(*TripRoadMapLocators.AVAILABLE_ROOMS)).select_by_value("N")
        Select(self.browser_dev.find_element(*TripRoadMapLocators.FREE_TICKETS)).select_by_value("Y")
        self.browser_dev.find_element(*TripRoadMapLocators.TRANSPORT_COSTS).send_keys("15000")
        self.browser_dev.find_element(*TripRoadMapLocators.REASON_PAYMENTS).send_keys("Компания должна оплатить билеты")
        Select(self.browser_dev.find_element(*TripRoadMapLocators.COMPLETE_PROCESS)).select_by_value("Y")
        self.browser_dev.find_element(*TripRoadMapLocators.BUTTON_APPROVE).click()
        self.browser_dev.close()
        self.browser_dev.switch_to_window(self.browser_dev.window_handles[0])

    # делегирование
    def select_role_finance_departament(self, *args):
        self.click_view_route()
        self.role_switching(*args)
        self.task_description_is_present()
        self.browser_dev.find_element(*TripRoadMapLocators.BUTTON_START).click()
        self.browser_dev.find_element(*TripRoadMapLocators.BUTTON_TAKE_TO_WORK).click()
        self.browser_dev.find_element(*TripRoadMapLocators.AMOUNT_PAID).send_keys("50000")
        self.browser_dev.find_element(*TripRoadMapLocators.BUTTON_APPROVE).click()
        self.browser_dev.close()
        self.browser_dev.switch_to_window(self.browser_dev.window_handles[0])

    def select_role_aho_departament_in_the_cancel_process(self, *args):
        self.click_view_route()
        self.role_switching(*args)
        self.task_description_is_present()
        self.browser_dev.find_element(*TripRoadMapLocators.BUTTON_START).click()
        self.browser_dev.find_element(*TripRoadMapLocators.BUTTON_TAKE_TO_WORK).click()
        Select(self.browser_dev.find_element(*TripRoadMapLocators.RETURN_TICKETS)).select_by_value("Y")
        Select(self.browser_dev.find_element(*TripRoadMapLocators.CANCEL_BOOKING)).select_by_value("Y")
        self.browser_dev.find_element(*TripRoadMapLocators.BUTTON_APPROVE).click()
        self.browser_dev.close()
        self.browser_dev.switch_to_window(self.browser_dev.window_handles[0])

    def select_role_finance_departament_in_the_cancel_process(self, *args):
        self.click_view_route()
        self.role_switching(*args)
        self.task_description_is_present()
        self.browser_dev.find_element(*TripRoadMapLocators.BUTTON_START).click()
        self.browser_dev.find_element(*TripRoadMapLocators.BUTTON_TAKE_TO_WORK).click()
        self.browser_dev.find_element(*TripRoadMapLocators.AMOUNT_REFUNDED).send_keys("10000")
        self.browser_dev.find_element(*TripRoadMapLocators.BUTTON_APPROVE).click()
        self.browser_dev.close()
        self.browser_dev.switch_to_window(self.browser_dev.window_handles[0])

    # добавить загрузку документов
    def select_role_aho_departament_in_changing_deadlines(self, *args):
        self.click_view_route()
        self.role_switching(*args)
        self.task_description_is_present()
        self.browser_dev.find_element(*TripRoadMapLocators.BUTTON_START).click()
        self.browser_dev.find_element(*TripRoadMapLocators.BUTTON_TAKE_TO_WORK).click()
        self.browser_dev.find_element(*TripRoadMapLocators.FLIGHT_NUMBER).send_keys("666")
        self.browser_dev.find_element(*TripRoadMapLocators.HOTEL).send_keys("Московская")
        self.browser_dev.find_element(*TripRoadMapLocators.ADDRESS_HOTEL).send_keys("ул. Ленина")
        Select(self.browser_dev.find_element(*TripRoadMapLocators.AVAILABLE_ROOMS)).select_by_value("Y")
        Select(self.browser_dev.find_element(*TripRoadMapLocators.FREE_TICKETS)).select_by_value("N")
        self.browser_dev.find_element(*TripRoadMapLocators.TRANSPORT_COSTS).send_keys("17000")
        self.browser_dev.find_element(*TripRoadMapLocators.REASON_PAYMENTS).send_keys("Компания оплачивает расходы")
        Select(self.browser_dev.find_element(*TripRoadMapLocators.COMPLETE_PROCESS)).select_by_value("Y")
        self.browser_dev.find_element(*TripRoadMapLocators.BUTTON_APPROVE).click()
        self.browser_dev.close()
        self.browser_dev.switch_to_window(self.browser_dev.window_handles[0])

    def select_role_finance_departament_in_changing_deadlines(self, *args):
        self.click_view_route()
        self.role_switching(*args)
        self.task_description_is_present()
        self.browser_dev.find_element(*TripRoadMapLocators.BUTTON_START).click()
        self.browser_dev.find_element(*TripRoadMapLocators.BUTTON_TAKE_TO_WORK).click()
        self.browser_dev.find_element(*TripRoadMapLocators.AMOUNT_PAID).send_keys("35000")
        self.browser_dev.find_element(*TripRoadMapLocators.BUTTON_APPROVE).click()
        self.browser_dev.close()
        self.browser_dev.switch_to_window(self.browser_dev.window_handles[0])

    def select_role_obu_specialist(self, *args):
        self.click_view_route()
        self.role_switching(*args)
        self.task_description_is_present()
        self.browser_dev.find_element(*TripRoadMapLocators.BUTTON_START).click()
        self.browser_dev.find_element(*TripRoadMapLocators.BUTTON_TAKE_TO_WORK).click()
        self.browser_dev.close()
        self.browser_dev.switch_to_window(self.browser_dev.window_handles[0])


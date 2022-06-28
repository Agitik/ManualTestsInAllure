from .locators_trip import TripCardLocators
from .locators_trip import TripRoadMapLocators
from .scenarios_create_trip_page import ScenariosForCompletingTrip
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.color import Color


class TripCardPage(ScenariosForCompletingTrip):
    # ожидание прописать NoSuchElementException
    def start_the_approval_process(self):
        self.browser_dev.find_element(*TripCardLocators.BUTTON_START_APPROVAL).click()

    def approval_button_is_not_active(self):
        assert not self.is_element_not_clickable(*TripCardLocators.BUTTON_START_APPROVAL),\
            "Кнопка запуска согласования не должна быть активной после запуска процесса согласования"

    def click_view_route(self):
        window_before = self.browser_dev.window_handles[0]
        route_map = self.browser_dev.find_element(*TripCardLocators.VIEW_ROUTE)
        try:
            WebDriverWait(self.browser_dev, 25).until_not(
                EC.presence_of_all_elements_located((
                    By.CLASS_NAME, "popup-window bx-messenger-mark bx-notifyManager-animation"))
            )
        finally:
            route_map.click()
        window_after = self.browser_dev.window_handles[1]
        self.browser_dev.switch_to_window(window_after)

    def send_a_report_for_approval(self):
        self.browser_dev.find_element(*TripCardLocators.BUTTON_SEND_REPORT).click()

    def the_send_to_report_button_is_not_active(self):
        assert not self.is_element_not_clickable(*TripCardLocators.BUTTON_SEND_REPORT),\
            "Кнопка запуска отчета не должна быть кликабельной после запуска процесса отчета"

    def add_trip_plan_in_the_card(self):
        # тут еще подумать надо
        add = self.browser_dev.find_element(*TripCardLocators.ADD_PLAN_IN_CARD)
        ActionChains(self.browser_dev).move_to_element(add).click().send_keys("Провести исследование" + Keys.ENTER)\
            .perform()
        self.browser_dev.find_element(*TripCardLocators.DELETE_PLAN).click()
        ActionChains(self.browser_dev).move_to_element(add).click().send_keys("Исследовать повторно" + Keys.ENTER)\
            .perform()
        self.browser_dev.find_element(*TripCardLocators.ADD_RESULT).click()

    def cancel_trip(self):
        window_before = self.browser_dev.window_handles[0]
        self.browser_dev.find_element(*TripCardLocators.CANCEL_TRIP).click()
        window_after = self.browser_dev.window_handles[1]
        self.browser_dev.switch_to_window(window_after)
        self.browser_dev.find_element(*TripRoadMapLocators.REJECT_COMMENT).send_keys("Командировка отменена")
        self.browser_dev.find_element(*TripRoadMapLocators.BUTTON_NONAPPROVE).click()
        self.browser_dev.close()
        self.browser_dev.switch_to_window(window_before)

    def change_deadlines_of_a_trip(self):
        window_before = self.browser_dev.window_handles[0]
        self.browser_dev.find_element(*TripCardLocators.CHANGE_DEADLINES).click()
        window_after = self.browser_dev.window_handles[1]
        self.browser_dev.switch_to_window(window_after)
        self.browser_dev.find_element(*TripRoadMapLocators.CHANGE_DEADLINE_COMMENT).send_keys("Планы изменились")
        self.browser_dev.find_element(*TripRoadMapLocators.BUTTON_APPROVE).click()
        self.browser_dev.close()
        self.browser_dev.switch_to_window(window_before)

    def attract_to_work_on_the_weekend(self, weekend=True):
        window_before = self.browser_dev.window_handles[0]
        if weekend:
            self.browser_dev.find_element(*TripCardLocators.WEEKEND_WORK).click()
        else:
            self.browser_dev.find_element(*TripCardLocators.SHOW_INFO).click()
            self.browser_dev.find_element(*TripCardLocators.LINK_WEEKEND_WORK).click()
        window_after = self.browser_dev.window_handles[1]
        self.browser_dev.switch_to_window(window_after)
        self.browser_dev.find_element(*TripRoadMapLocators.CALENDAR).click()
        self.browser_dev.find_element(*TripRoadMapLocators.CALENDAR_DAY).click()
        self.browser_dev.find_element(*TripRoadMapLocators.REJECT_COMMENT).send_keys("Нужно поработать в выходной")
        self.browser_dev.find_element(*TripRoadMapLocators.BUTTON_APPROVE).click()
        self.browser_dev.close()
        self.browser_dev.switch_to_window(window_before)

    def attracting_overtime_work(self, overtime=True):
        window_before = self.browser_dev.window_handles[0]
        if overtime:
            self.browser_dev.find_element(*TripCardLocators.OVERTIME_WORK).click()
        else:
            self.browser_dev.find_element(*TripCardLocators.SHOW_INFO).click()
            self.browser_dev.find_element(*TripCardLocators.LINK_OVERTIME_WORK).click()
        window_after = self.browser_dev.window_handles[1]
        self.browser_dev.switch_to_window(window_after)
        self.browser_dev.find_element(*TripRoadMapLocators.REASON_OVERTIME).send_keys("Много работы")
        Select(self.browser_dev.find_element(*TripRoadMapLocators.COMPENSATION)).select_by_value("OTGUL")
        self.browser_dev.find_element(*TripRoadMapLocators.BUTTON_APPROVE).click()
        self.browser_dev.close()
        self.browser_dev.switch_to_window(window_before)

    def checking_the_status_of_the_document_new(self):
        status = self.browser_dev.find_element(*TripCardLocators.STATUS_PDF_NEW)
        txt = status.get_attribute("textContent")
        assert txt == "Новый", "Текущий статус не соответствует статусу при создании документа"
        color_txt = Color.from_string(status.value_of_css_property("color")).hex
        assert color_txt == "#0514c8", "Цвет текста должен быть синим"

    def checking_the_status_of_the_document_approval(self):
        status = self.browser_dev.find_element(*TripCardLocators.STATUS_PDF_IN_PROGRESS)
        txt = status.get_attribute("textContent")
        assert txt == "В процессе согласования", "Текущий статус не соответствует статусу при работе с документом"
        color_txt = Color.from_string(status.value_of_css_property("color")).hex
        assert color_txt == "#c80505", "Цвет текста должен быть красным"

    def checking_the_status_of_the_document_approved(self):
        status = self.browser_dev.find_element(*TripCardLocators.STATUS_PDF_APPROVED)
        txt = status.get_attribute("textContent")
        assert txt == "Утвержден", "Текущий статус не соответствует статусу при завершении работы с документом"
        color_txt = Color.from_string(status.value_of_css_property("color")).hex
        assert color_txt == "#47c805", "Цвет текста должен быть зеленым"

    def checking_the_status_of_the_document_rejected(self):
        status = self.browser_dev.find_element(*TripCardLocators.STATUS_PDF_REJECTED)
        txt = status.get_attribute("textContent")
        assert txt == "Отклонен", "Текущий статус не соответствует статусу при отклонении документа"
        color_txt = Color.from_string(status.value_of_css_property("color")).hex
        assert color_txt == "#eb6b56", "Цвет текста должен быть красным"

    def check_text_and_color_status_preparing_for_a_trip(self):
        status_trip = self.browser_dev.find_element(*TripCardLocators.STATUS_TRIP)
        status_txt = status_trip.get_attribute("textContent")
        assert status_txt == "Подготовка к командировке", "Текущий статус не соответствует статусу до утверждения"
        color_txt = Color.from_string(status_trip.value_of_css_property("color")).hex
        assert color_txt == "#ffffff", "Цвет текста должен быть белым"
        color_background = Color.from_string(status_trip.value_of_css_property("background-color")).hex
        assert color_background == "#fbcf57", "Цвет заднего фона не соответствует цвету по ТЗ"

    def check_text_and_color_status_on_a_trip(self):
        status_trip = self.browser_dev.find_element(*TripCardLocators.STATUS_TRIP)
        status_txt = status_trip.get_attribute("textContent")
        assert status_txt == "В командировке", "Текущий статус не соответствует статусу после утверждения"
        color_txt = Color.from_string(status_trip.value_of_css_property("color")).hex
        assert color_txt == "#ffffff", "Цвет текста должен быть белым"
        color_background = Color.from_string(status_trip.value_of_css_property("background-color")).hex
        assert color_background == "#fbcf57", "Цвет заднего фона не соответствует цвету по ТЗ"

    def check_text_and_color_status_report(self):
        status_trip = self.browser_dev.find_element(*TripCardLocators.STATUS_TRIP)
        status_txt = status_trip.get_attribute("textContent")
        assert status_txt == "Отчет", "Текущий статус не соответствует статусу после запуска процесса отчета"
        color_txt = Color.from_string(status_trip.value_of_css_property("color")).hex
        assert color_txt == "#ffffff", "Цвет текста должен быть белым"
        color_background = Color.from_string(status_trip.value_of_css_property("background-color")).hex
        assert color_background == "#2196f3", "Цвет заднего фона не соответствует цвету по ТЗ"

    def check_text_and_color_status_completed(self):
        status_trip = self.browser_dev.find_element(*TripCardLocators.STATUS_TRIP)
        status_txt = status_trip.get_attribute("textContent")
        assert status_txt == "Завершено", "Текущий статус не соответствует статусу после запуска процесса отчета"
        color_txt = Color.from_string(status_trip.value_of_css_property("color")).hex
        assert color_txt == "#ffffff", "Цвет текста должен быть белым"
        color_background = Color.from_string(status_trip.value_of_css_property("background-color")).hex
        assert color_background == "#05c8a1", "Цвет заднего фона не соответствует цвету по ТЗ"

    def check_text_and_color_status_cancel(self):
        status_trip = self.browser_dev.find_element(*TripCardLocators.STATUS_TRIP)
        status_txt = status_trip.get_attribute("textContent")
        assert status_txt == "Отмена", "Текущий статус не соответствует статусу после утверждения отмены командировки"
        color_txt = Color.from_string(status_trip.value_of_css_property("color")).hex
        assert color_txt == "#ffffff", "Цвет текста должен быть белым"
        color_background = Color.from_string(status_trip.value_of_css_property("background-color")).hex
        assert color_background == "#fbcf57", "Цвет заднего фона не соответствует цвету по ТЗ"

    def check_text_and_color_status_attention(self):
        status_trip = self.browser_dev.find_element(*TripCardLocators.STATUS_TRIP)
        status_txt = status_trip.get_attribute("textContent")
        assert status_txt == "Требует внимания", "Текущий статус не соответствует статусу при не всех заполненных полях"
        color_txt = Color.from_string(status_trip.value_of_css_property("color")).hex
        assert color_txt == "#ffffff", "Цвет должен быть белым"
        color_background = Color.from_string(status_trip.value_of_css_property("background-color")).hex
        assert color_background == "#eb6b56", "Цвет заднего фона не соответствует цвету по ТЗ"

    def verification_of_the_opening_of_pdf_documents_of_a_trip(self):
        pdf_documents = self.browser_dev.find_elements(*TripCardLocators.LIST_TRIP_PDF)
        for document in pdf_documents:
            document.click()
            assert self.is_elements_find(*TripCardLocators.PAGE_PDF), "Документы командировки нельзя просмотреть"
            self.browser_dev.find_element(*TripCardLocators.CLOSE_DOCUMENT).click()

    def checking_open_other_trip_documents(self):
        self.browser_dev.find_element(*TripCardLocators.BLANKS).click()
        documents = self.browser_dev.find_elements(*TripCardLocators.LIST_BLANKS)
        for document in documents:
            document.click()
            iframe = self.browser_dev.find_element(*TripCardLocators.IFRAME)
            self.browser_dev.switch_to_frame(iframe)
            self.is_element_find(*TripCardLocators.XLSX_DOCX_DOCUMENTS)
            self.browser_dev.switch_to_default_content()
            self.browser_dev.find_element(*TripCardLocators.CLOSE_DOCUMENT).click()


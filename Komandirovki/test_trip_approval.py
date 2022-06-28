from pages.trip_road_map_page import TripRoadPage
import pytest


@pytest.mark.smoke
@pytest.mark.positive
def test_approval_and_completion_of_a_trip(browser_dev):
    link = "https://dev-bitrix2.onegroup.ru/activity/"
    page = TripRoadPage(browser_dev, link)
    page.open()
    page.click_button_add_trip()
    page.create_trip_only_required_fields()
    page.check_text_and_color_status_preparing_for_a_trip()
    page.start_the_approval_process()
    page.select_role_of_a_trip_participant("Руководитель подразделения | Лебедев Алексей Владимирович")
    page.select_role_of_a_trip_participant("ЗГД/руководитель по направлению | Рубцов Юрий Иванович")
    page.select_role_of_a_trip_participant("Отдел ФЭПиЦ (665) | Выскребова Владислава Олеговна")
    page.select_role_of_the_approver("Утверждает | Выскребов Сергей Евгеньевич")
    page.browser_dev.refresh()
    page.check_text_and_color_status_on_a_trip()
    page.select_role_hr_departament("Отдел кадров (Основные) | Бафталовская Александра Юрьевна")
    page.select_role_aho_departament("Сотрудник отдела 339 (АХО) | Окунева Анна Петровна")
    page.select_role_finance_departament("Выплаты денежных средств (Безнал) | Чернева Анна Владимировна")
    page.verification_of_the_opening_of_pdf_documents_of_a_trip()
    page.checking_open_other_trip_documents()


@pytest.mark.xfail
@pytest.mark.smoke
@pytest.mark.negative
def test_creating_an_empty_trip(browser_dev):
    link = "https://dev-bitrix2.onegroup.ru/activity/"
    page = TripRoadPage(browser_dev, link)
    page.open()
    page.click_button_add_trip()
    page.create_trip_not_with_all_required_fields()
    page.approval_button_is_not_active()


@pytest.mark.all_employees
def test_approval_and_completion_of_a_trip_all_employees(browser_dev):
    link = "https://dev-bitrix2.onegroup.ru/activity/"
    page = TripRoadPage(browser_dev, link)
    page.open()
    page.click_button_add_trip()
    page.create_trip_with_all_employees_in_the_process()
    page.start_the_approval_process()
    page.select_role_of_a_trip_participant("Руководитель подразделения | Лебедев Алексей Владимирович")
    page.select_role_of_a_trip_participant("Главный конструктор по теме | Клевцов Егор Борисович")
    page.select_role_of_a_trip_participant("ЗГД/руководитель по направлению | Рубцов Юрий Иванович")
    page.select_role_of_a_trip_participant("Руководитель заводского заказа | Михайлюк Сергей Иванович")
    page.select_role_of_a_trip_participant("Отдел ФЭПиЦ (665) | Выскребова Владислава Олеговна")
    page.select_role_of_the_approver("Утверждает | Выскребов Сергей Евгеньевич")
    page.browser_dev.refresh()
    page.check_text_and_color_status_on_a_trip()
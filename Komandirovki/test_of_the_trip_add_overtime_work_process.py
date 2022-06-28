from pages.trip_road_map_page import TripRoadPage
import pytest


@pytest.mark.critical_path_test
def test_overtime_work_required_employees(browser_dev):
    link = "https://dev-bitrix2.onegroup.ru/activity/"
    page = TripRoadPage(browser_dev, link)
    page.open()
    page.click_button_add_trip()
    page.create_trip_with_overtime_work()
    page.start_the_approval_process()
    page.select_role_of_a_trip_participant("Руководитель подразделения | Лебедев Алексей Владимирович")
    page.select_role_of_a_trip_participant("ЗГД/руководитель по направлению | Рубцов Юрий Иванович")
    page.select_role_of_a_trip_participant("Отдел ФЭПиЦ (665) | Выскребова Владислава Олеговна")
    page.select_role_of_the_approver("Утверждает | Выскребов Сергей Евгеньевич")
    page.select_role_hr_departament("Отдел кадров (Основные) | Бафталовская Александра Юрьевна")
    page.select_role_aho_departament("Сотрудник отдела 339 (АХО) | Окунева Анна Петровна")
    page.select_role_finance_departament("Выплаты денежных средств (Безнал) | Чернева Анна Владимировна")
    page.attracting_overtime_work()
    page.browser_dev.execute_script("window.scrollTo(100, 0);")
    page.select_role_of_a_trip_participant("Руководитель подразделения | Лебедев Алексей Владимирович")
    page.select_role_of_a_trip_participant("ЗГД/руководитель по направлению | Рубцов Юрий Иванович")
    page.select_role_of_the_approver("Утверждает | Выскребов Сергей Евгеньевич")
    page.select_role_hr_departament("Отдел кадров (Основные) | Бафталовская Александра Юрьевна")


@pytest.mark.critical_path_test
def test_overtime_work_required_employees_other_link(browser_dev):
    link = "https://dev-bitrix2.onegroup.ru/activity/"
    page = TripRoadPage(browser_dev, link)
    page.open()
    page.click_button_add_trip()
    page.create_trip_with_overtime_work()
    page.start_the_approval_process()
    page.select_role_of_a_trip_participant("Руководитель подразделения | Лебедев Алексей Владимирович")
    page.select_role_of_a_trip_participant("ЗГД/руководитель по направлению | Рубцов Юрий Иванович")
    page.select_role_of_a_trip_participant("Отдел ФЭПиЦ (665) | Выскребова Владислава Олеговна")
    page.select_role_of_the_approver("Утверждает | Выскребов Сергей Евгеньевич")
    page.select_role_hr_departament("Отдел кадров (Основные) | Бафталовская Александра Юрьевна")
    page.select_role_aho_departament("Сотрудник отдела 339 (АХО) | Окунева Анна Петровна")
    page.select_role_finance_departament("Выплаты денежных средств (Безнал) | Чернева Анна Владимировна")
    page.attracting_overtime_work(overtime=False)
    page.browser_dev.execute_script("window.scrollTo(100, 0);")
    page.select_role_of_a_trip_participant("Руководитель подразделения | Лебедев Алексей Владимирович")
    page.select_role_of_a_trip_participant("ЗГД/руководитель по направлению | Рубцов Юрий Иванович")
    page.select_role_of_the_approver("Утверждает | Выскребов Сергей Евгеньевич")
    page.select_role_hr_departament("Отдел кадров (Основные) | Бафталовская Александра Юрьевна")


@pytest.mark.all_employees
def test_overtime_work_all_employees(browser_dev):
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
    page.attracting_overtime_work()
    page.select_role_of_a_trip_participant("Руководитель подразделения | Лебедев Алексей Владимирович")
    page.select_role_of_a_trip_participant("Главный конструктор по теме | Клевцов Егор Борисович")
    page.select_role_of_a_trip_participant("ЗГД/руководитель по направлению | Рубцов Юрий Иванович")
    page.select_role_responsible_person("Ответственный за мероприятие | Мешков Вячеслав Анатольевич")
    page.select_role_of_the_approver("Утверждает | Выскребов Сергей Евгеньевич")
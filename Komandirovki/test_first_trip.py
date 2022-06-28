from pages.trip_road_map_page import TripRoadPage
import pytest
# test

@pytest.mark.xfail
def test_rejection_head_direction(browser_dev):
    link = "https://dev-bitrix2.onegroup.ru/activity/"
    page = TripRoadPage(browser_dev, link)
    page.open()
    page.click_button_add_trip()
    page.create_trip_only_required_fields()
    page.start_the_approval_process()
    page.select_role_of_a_trip_participant("Руководитель подразделения | Лебедев Алексей Владимирович")
    page.select_role_of_a_trip_participant("ЗГД/руководитель по направлению | Рубцов Юрий Иванович", rejection=False)
    page.select_role_of_a_trip_participant("Руководитель подразделения | Лебедев Алексей Владимирович")
    page.select_role_of_a_trip_participant("ЗГД/руководитель по направлению | Рубцов Юрий Иванович")
    page.select_role_of_a_trip_participant("Отдел ФЭПиЦ (665) | Выскребова Владислава Олеговна")


@pytest.mark.xfail
def test_rejection_payment_departament(browser_dev):
    link = "https://dev-bitrix2.onegroup.ru/activity/"
    page = TripRoadPage(browser_dev, link)
    page.open()
    page.click_button_add_trip()
    page.create_trip_only_required_fields()
    page.start_the_approval_process()
    page.select_role_of_a_trip_participant("Руководитель подразделения | Лебедев Алексей Владимирович")
    page.select_role_of_a_trip_participant("ЗГД/руководитель по направлению | Рубцов Юрий Иванович")
    page.select_role_of_a_trip_participant("Отдел ФЭПиЦ (665) | Выскребова Владислава Олеговна", rejection=False)
    page.select_role_of_the_approver("Утверждает | Выскребов Сергей Евгеньевич")


def test_rejection_approver(browser_dev):
    link = "https://dev-bitrix2.onegroup.ru/activity/"
    page = TripRoadPage(browser_dev, link)
    page.open()
    page.click_button_add_trip()
    page.create_trip_only_required_fields()
    page.start_the_approval_process()
    page.select_role_of_a_trip_participant("Руководитель подразделения | Лебедев Алексей Владимирович")
    page.select_role_of_a_trip_participant("ЗГД/руководитель по направлению | Рубцов Юрий Иванович")
    page.select_role_of_a_trip_participant("Отдел ФЭПиЦ (665) | Выскребова Владислава Олеговна")
    page.select_role_of_the_approver("Утверждает | Выскребов Сергей Евгеньевич", rejection=False)
    page.browser_dev.refresh()
    page.start_the_approval_process()
    page.select_role_of_a_trip_participant("Руководитель подразделения | Лебедев Алексей Владимирович")
    page.select_role_of_a_trip_participant("ЗГД/руководитель по направлению | Рубцов Юрий Иванович")
    page.select_role_of_a_trip_participant("Отдел ФЭПиЦ (665) | Выскребова Владислава Олеговна")
    page.select_role_of_the_approver("Утверждает | Выскребов Сергей Евгеньевич")
    page.browser_dev.refresh()
    page.check_text_and_color_status_on_a_trip()


@pytest.mark.xfail
def test_rejection_main_constructor(browser_dev):
    link = "https://dev-bitrix2.onegroup.ru/activity/"
    page = TripRoadPage(browser_dev, link)
    page.open()
    page.click_button_add_trip()
    page.create_trip_with_all_employees_in_the_process()
    page.start_the_approval_process()
    page.select_role_of_a_trip_participant("Руководитель подразделения | Лебедев Алексей Владимирович")
    page.select_role_of_a_trip_participant("Главный конструктор по теме | Клевцов Егор Борисович", rejection=False)
    page.select_role_of_a_trip_participant("ЗГД/руководитель по направлению | Рубцов Юрий Иванович")


@pytest.mark.xfail
def test_rejection_factory_order_manager(browser_dev):
    link = "https://dev-bitrix2.onegroup.ru/activity/"
    page = TripRoadPage(browser_dev, link)
    page.open()
    page.click_button_add_trip()
    page.create_trip_with_all_employees_in_the_process()
    page.start_the_approval_process()
    page.select_role_of_a_trip_participant("Руководитель подразделения | Лебедев Алексей Владимирович")
    page.select_role_of_a_trip_participant("Главный конструктор по теме | Клевцов Егор Борисович")
    page.select_role_of_a_trip_participant("ЗГД/руководитель по направлению | Рубцов Юрий Иванович")
    page.select_role_of_a_trip_participant("Руководитель заводского заказа | Михайлюк Сергей Иванович", rejection=False)
    page.select_role_of_a_trip_participant("Отдел ФЭПиЦ (665) | Выскребова Владислава Олеговна")


def test_rejection_cancel_process(browser_dev):
    link = "https://dev-bitrix2.onegroup.ru/activity/"
    page = TripRoadPage(browser_dev, link)
    page.open()
    page.click_button_add_trip()
    page.create_trip_with_all_employees_in_the_process()
    page.cancel_trip()
    page.select_role_of_a_trip_participant("Руководитель подразделения | Лебедев Алексей Владимирович")
    page.select_role_of_a_trip_participant("Главный конструктор по теме | Клевцов Егор Борисович")
    page.select_role_of_a_trip_participant("ЗГД/руководитель по направлению | Рубцов Юрий Иванович")
    page.select_role_responsible_person("Ответственный за мероприятие | Мешков Вячеслав Анатольевич", rejection=False)
    page.select_role_of_the_approver("Утверждает | Выскребов Сергей Евгеньевич")







from pages.trip_road_map_page import TripRoadPage
import pytest


@pytest.mark.rejection
def test_rejection_head_departament(browser_dev):
    link = "https://dev-bitrix2.onegroup.ru/activity/"
    page = TripRoadPage(browser_dev, link)
    page.open()
    page.click_button_add_trip()
    page.create_trip_only_required_fields()
    page.start_the_approval_process()
    page.select_role_of_a_trip_participant("Руководитель подразделения | Лебедев Алексей Владимирович", rejection=False)
    page.browser_dev.refresh()
    page.start_the_approval_process()
    page.select_role_of_a_trip_participant("Руководитель подразделения | Лебедев Алексей Владимирович")
    page.select_role_of_a_trip_participant("ЗГД/руководитель по направлению | Рубцов Юрий Иванович")
    page.select_role_of_a_trip_participant("Отдел ФЭПиЦ (665) | Выскребова Владислава Олеговна")
    page.select_role_of_the_approver("Утверждает | Выскребов Сергей Евгеньевич")
    page.browser_dev.refresh()
    page.check_text_and_color_status_on_a_trip()
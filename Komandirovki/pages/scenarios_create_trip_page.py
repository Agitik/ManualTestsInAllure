from .create_a_business_trip_page import CreateBusinessTrip


class ScenariosForCompletingTrip(CreateBusinessTrip):
    def create_trip_only_required_fields(self):
        self.write_deadline_trip()
        self.choose_a_trip_city(city="Псков")
        self.choose_company_for_a_trip()
        self.add_trip_plan()
        self.add_order()
        self.select_factory_order(order=False)
        self.fill_passport_information()
        self.only_required_employees_of_the_process()
        self.add_purpose_trip()
        self.click_button_submit()

    def create_trip_not_with_all_required_fields(self):
        self.write_deadline_trip()
        self.choose_company_for_a_trip()
        self.click_button_submit()

    def create_trip_with_work_on_the_weekend(self):
        self.write_deadline_trip()
        self.add_a_weekend_work()
        self.choose_a_trip_city(city="Дно")
        self.choose_company_for_a_trip()
        self.add_trip_plan()
        self.add_order()
        self.select_factory_order(order=True)
        self.fill_passport_information()
        self.only_required_employees_of_the_process()
        self.add_purpose_trip()
        self.click_button_submit()

    def create_trip_with_overtime_work(self):
        self.write_deadline_trip()
        self.add_overtime_work()
        self.choose_a_trip_city(city="Порхов")
        self.add_trip_plan()
        self.add_order()
        self.select_factory_order(order=False)
        self.fill_passport_information()
        self.only_required_employees_of_the_process()
        self.add_purpose_trip()
        self.click_button_submit()

    def create_united_trip(self):
        self.write_deadline_trip()
        self.choose_a_trip_city(city="Остров")
        self.union_business_trip(worker="Клевцов Егор")
        self.choose_company_for_a_trip()
        self.add_trip_plan()
        self.add_order()
        self.select_factory_order(order=True)
        self.fill_passport_information()
        self.only_required_employees_of_the_process()
        self.add_purpose_trip()
        self.click_button_submit()

    def create_trip_with_all_employees_in_the_process(self):
        self.write_deadline_trip()
        self.choose_a_trip_city(city="Великий Новгород")
        self.choose_company_for_a_trip()
        self.add_trip_plan()
        self.add_order()
        self.select_factory_order(order=False)
        self.fill_passport_information()
        self.all_employees_of_the_process()
        self.add_purpose_trip()
        self.click_button_submit()

    def create_trip_with_payment_of_expenses_in_cash(self):
        self.write_deadline_trip()
        self.choose_a_trip_city(city="Петрозаводск")
        self.choose_company_for_a_trip()
        self.add_trip_plan()
        self.add_order()
        self.select_factory_order(order=True)
        self.fill_all_types_expenses()
        self.get_daily_expenses_in_cash()
        self.plot_a_route_by_employee_339(route=False)
        self.fill_passport_information()
        self.only_required_employees_of_the_process()
        self.add_purpose_trip()
        self.click_button_submit()

    def create_trip_with_all_optional_fields(self):
        self.write_deadline_trip()
        self.choose_a_trip_city(city="Санкт-Петербург")
        self.choose_company_for_a_trip()
        self.add_trip_plan()
        self.add_order()
        self.write_medical_contraindications()
        self.select_factory_order(order=True)
        self.upload_document_to_the_direction()
        self.plot_a_route_by_employee_339(route=True)
        self.add_time_and_date()
        self.fill_passport_information()
        self.only_required_employees_of_the_process()
        self.add_purpose_trip()
        self.click_button_submit()


from selenium.webdriver.common.by import By


class MainTripLocators:
    BUTTON_ADD = (By.CSS_SELECTOR, "#lists-title-action-add")
    BUTTON_INFO = (By.CSS_SELECTOR, ".info-pages.info-pages-trip .technical-support")
    BUTTON_SUPPORT = (By.CSS_SELECTOR, ".help_problem")


class TripActivity:
    TRIP_LIST = (By.CSS_SELECTOR, "#top_menu_id_activity_2113442480 .main-buttons-item-link")
    AGREEMENT_BUTTON = (By.CSS_SELECTOR, "#top_menu_id_activity_2209440344 .main-buttons-item-link")
    ENTITLEMENT_BUTTON = (By.CSS_SELECTOR, "#top_menu_id_activity_2175581960 .main-buttons-item-link")
    CHECK_SIGNATURE_BUTTON = (By.CSS_SELECTOR, "#top_menu_id_activity_2287164964 .main-buttons-item-link")
    DELEGATE_BUTTON = (By.CSS_SELECTOR, "#top_menu_id_activity_3939553146 .main-buttons-item-link")
    EXCEPTION_BUTTON = (By.CSS_SELECTOR, "#top_menu_id_activity_1389435020 .main-buttons-item-link")


class CreateTripLocators:

    TRIP_PERIOD = (By.CSS_SELECTOR, "#datepicker-1")

    EMPLOYEE_FIELD = (By.CSS_SELECTOR, "#SOTRUDNIKI .ui-tile-selector-select")
    EMPLOYEE_CARD = (By.XPATH, "//*[@data-entity-type='USERS'][2]")

    WEEKEND_SWITCHER = (By.CSS_SELECTOR, "#PKRVVPD #radio-180")
    REASON_WEEKEND = (By.CSS_SELECTOR, "#PRICHINA_VYH_PRAZ .form-control")
    WEEKEND_PERIOD = (By.CSS_SELECTOR, "#DATE_WVVD .input-group.date .form-control") # мб подобрать получше
    BUTTON_ADD_MORE_WEEKEND = (By.CSS_SELECTOR, "#DATE_WVVD .input-group a")
    WEEKEND_PERIOD_2 = (By.CSS_SELECTOR, "#DATE_WVVD .input-group.date.input-group.date.new .form-control")

    OVERTIME_SWITCHER = (By.CSS_SELECTOR, "#PRVKSVR .switch #radio-182")
    OVERTIME_REASON = (By.CSS_SELECTOR, "#VSVZSVER .form-control")
    OVERTIME_TASK = (By.CSS_SELECTOR, "#SVER_TASK .form-control")
    OVERTIME_START = (By.CSS_SELECTOR, "#SVER_START .form-control")
    OVERTIME_END = (By.CSS_SELECTOR, "#SVER_END .form-control")

    INPUT_CITY = (By.CSS_SELECTOR, "#CITY input.bx-ui-sls-fake.form-control")
    SELECT_CITY = (By.CSS_SELECTOR, "#CITY .bx-ui-sls-variants "
                                    ".dropdown-item.bx-ui-sls-variant.bx-ui-sls-variant-active")

    UNION_TRIP = (By.CSS_SELECTOR, "#ui-tile-selector-mail_client_config_queue .ui-tile-selector-select")
    UNION_TRIP_WORKER = (By.CSS_SELECTOR, ".bx-finder-groupbox-content a")
    BUTTON_UNION_LIST = (By.CSS_SELECTOR, ".unite_trip__form.form-group button")

    COMPANY = (By.CSS_SELECTOR, "#ui-tile-selector-form--property-372 .ui-tile-selector-select")
    SELECT_COMPANY = (By.CSS_SELECTOR, ".bx-finder-groupbox-content a")

    ADDRESS = (By.CSS_SELECTOR, "#ADDR input")

    PLAN = (By.CSS_SELECTOR, "#PLAN_TRIP_WORK #tblPROPERTY_382 .business-task")
    ADD_STAGE_PLAN = (By.CSS_SELECTOR, "#PLAN_TRIP_WORK .business-btn input")
    REMOVE_STAGE = (By.CSS_SELECTOR, "#PLAN_TRIP_WORK .business-remove")

    ORDER = (By.CSS_SELECTOR, "#PREDPISANIE #radio-195")

    MEDICINE = (By.CSS_SELECTOR, "#MED_P #radio-197")
    MEDICINE_INPUT = (By.CSS_SELECTOR, "#MED_PROT input")

    FACTORY_ORDER_INPUT = (By.CSS_SELECTOR, "#ZZ [type='text']")
    FACTORY_ORDER = (By.CSS_SELECTOR, "#ZZ .search_result li")
    FACTORY_ORDER_SWITCH = (By.CSS_SELECTOR, "#TRIP_ZZ #radio-199")
    EXPENSE_ITEM = (By.CSS_SELECTOR, "#STATYA #pln9po_select_button")
    EXPENSE_INPUT = (By.CSS_SELECTOR, "#pln9po input#pln9po_search_input")
    CHOOSING_EXPENSES = (By.CSS_SELECTOR, "table.ies-content-columns .ies-content-item-text")

    SUPPORTING_DOCUMENT = (By.CSS_SELECTOR, "#DOC_ZZ_1 a")
    UPLOAD_SUPPORTING_DOCUMENT = (By.CSS_SELECTOR, "#diskuf-selectdialog-xMknNV [type='file']")

    DOCUMENT_DIRECTION = (By.CSS_SELECTOR, "#DOC_NAPR_1 a")
    UPLOAD_DOCUMENT_DIRECTION = (By.CSS_SELECTOR, "#diskuf-selectdialog-D2CKrd [type='file']")

    DAILY_EXPENSES = (By.CSS_SELECTOR, "#SUM_DAY select")
    TRAVEL_EXPENSES = (By.CSS_SELECTOR, "#SUM_DRIVE [type='text']")
    HOUSE_EXPENSES = (By.CSS_SELECTOR, "#SUM_DRIVE [type='text']") # подумать еще
    OTHER_EXPENSES = (By.CSS_SELECTOR, "#SUM_OTHER [type='text']")
    GENERAL_EXPENSES = (By.CSS_SELECTOR, "#SUM_OR_ITOGO [type='text']") # тоже подумать
    GET_EXPENSES = (By.CSS_SELECTOR, "#VYDAM_DENGI #radio-201")
    TRANSPORT = (By.CSS_SELECTOR, "#VID_TRANSPORT #radio-203")

    ROUTE_339 = (By.CSS_SELECTOR, "#MARSHRUT_339 #radio-210")
    MODULE_YANDEX = (By.CSS_SELECTOR, "#RASPISANIE iframe") # с ним ничего не делать наверное

    COMMENT_TICKETS = (By.CSS_SELECTOR, "#MESTO iframe.bx-editor-iframe") # поле комментарий для билетов
    IFRAME = (By.CSS_SELECTOR, "[contenteditable='true']")

    TRAIN_PLANE_NUMBER = (By.CSS_SELECTOR, "#NOMER_POEZD_SAMOLET [type='text']")

    ARRIVAL_DATE = (By.CSS_SELECTOR, "#DATE_TIME_TRIP_START input")
    DATE_END = (By.CSS_SELECTOR, "#DATE_TIME_TRIP_END input")

    HOTEL_339 = (By.CSS_SELECTOR, "#OTEL_339 #radio-212")

    NAME_HOTEL = (By.CSS_SELECTOR, "#GOSTIN [type='text']")

    MOBILE_NUMBER = (By.CSS_SELECTOR, "#MOBILE [type='text']")
    CITIZENSHIP = (By.CSS_SELECTOR, "#CITIZENSHIP [type='text']")
    DATE_PASSPORT = (By.CSS_SELECTOR, "#DATE_PASP [type='text']")
    PASSPORT_SERIES_NUMBER = (By.CSS_SELECTOR, "#PASP [type='text']")
    DATE_BIRTH = (By.CSS_SELECTOR, "#AGE [type='text']")
    PLACE_BIRTH = (By.CSS_SELECTOR, "#MESTO_ROD [type='text']")

    HEAD_DEPARTAMENT = (By.CSS_SELECTOR, "#HEAD_DEPT [data-role='tile-select']")
    SELECT_USERS = (By.CSS_SELECTOR, ".bx-finder-groupbox-content a")
    CONSTRUCTOR = (By.CSS_SELECTOR, "#KONSTR [data-role='tile-select']")
    FACTORY_ORDER_HEAD = (By.CSS_SELECTOR, "#HEAD_ZZ [data-role='tile-select']")
    PAYMENT_DEPARTAMENT = (By.CSS_SELECTOR, "#FEPC665 [data-role='tile-select']")
    HEAD_DIRECTION = (By.CSS_SELECTOR, "#ZGD [data-role='tile-select']")
    RESPONSIBLE_EVENT = (By.CSS_SELECTOR, "#DOP_SOGL [data-role='tile-select']")
    NOTIFY_TRIP = (By.CSS_SELECTOR, "#UVED_O_COMM [data-role='tile-select']")
    APPROVING = (By.CSS_SELECTOR, "#UTV [data-role='tile-select']")

    PURPOSE_TRIP = (By.CSS_SELECTOR, "#TARGET_TRIP iframe.bx-editor-iframe")

    BUTTON_SUBMIT = (By.CSS_SELECTOR, ".submit-success input[type='submit']")


class TripCardLocators:
    BUTTON_STATUS_FIELDS = (By.CSS_SELECTOR, ".report-block .trips-notifications a")
    BUTTON_GROUP_TRIP = (By.CSS_SELECTOR, ".report-block .btn-wrap a")
    BUTTON_SHOW = (By.CSS_SELECTOR, ".title a")
    BUTTON_OPEN_TRIP = (By.CSS_SELECTOR, ".worker-trips_span")
    ADD_PLAN_IN_CARD = (By.CSS_SELECTOR, ".business-btn input")
    DELETE_PLAN = (By.CSS_SELECTOR, ".fas.fa-trash-alt")
    ADD_RESULT = (By.CSS_SELECTOR, ".result-block.col-9 a")

    STATUS_PDF_NEW = (By.XPATH, "//div[@class='subtitle new']")
    STATUS_PDF_APPROVED = (By.XPATH, "//div[@class='subtitle ok']")
    STATUS_PDF_IN_PROGRESS = (By.XPATH, "//div[@class='subtitle no']")
    STATUS_PDF_REJECTED = (By.XPATH, "//div[@class='subtitle off']")
    TRIP_REPORT_PDF = (By.XPATH, "//div//*[contains(text(),'Отчет')]")
    TRIP_DIRECTION_PDF = (By.XPATH, "//div//*[contains(text(),'СЗ о направлении в командировку ')]")
    TRIP_DEADLINES_PDF = (By.XPATH, "//div//*[contains(text(),'СЗ об изменении сроков командировки')]")
    TRIP_CANCEL_PDF = (By.XPATH, "//div//*[contains(text(),'СЗ об отмене командировки')]")
    TRIP_WEEKEND_WORK_PDF = (By.XPATH, "//div//*[contains(text(),'СЗ О работе в выходные')]")
    TRIP_OVERTIME_WORK_PDF = (By.XPATH, "//div//*[contains(text(),'СЗ о работе сверхурочно')]")
    BUTTON_DISCUSSION = (By.XPATH, "//*[@class='doc-wrap']/a/div")

    STATUS_TRIP = (By.XPATH, "//*[@class='sidebar']/a[1]")
    VIEW_ROUTE = (By.XPATH, "//*[@class='sidebar']/a[2]")
    BUTTON_START_APPROVAL = (By.XPATH, "//*[@class='sidebar']/a[3]")
    BUTTON_SEND_REPORT = (By.XPATH, "//*[@class='sidebar']/a[4]")
    SHARE_CARD_TRIP = (By.XPATH, "//*[@class='actions-block']/a[1]")
    EDIT_CARD_DATA = (By.XPATH, "//*[@class='actions-block']/a[2]")
    VIEW_FILES = (By.XPATH, "//*[@class='actions-block']/a[3]")
    CANCEL_TRIP = (By.XPATH, "//*[@class='actions-block']/a[4]")
    CHANGE_DEADLINES = (By.XPATH, "//*[@class='actions-block']/a[5]")
    WEEKEND_WORK = (By.XPATH, "//*[@class='actions-block']/a[6]")
    OVERTIME_WORK = (By.XPATH, "//*[@class='actions-block']/a[7]")

    SHOW_INFO = (By.XPATH, "//*[@class='info-wrap'][2]//a[@class='show-info']")
    LINK_WEEKEND_WORK = (By.CSS_SELECTOR, "#MoreInfo3 a")
    LINK_OVERTIME_WORK = (By.CSS_SELECTOR, "#MoreInfo4 a")
    BLANKS = (By.CSS_SELECTOR, "div.content-block .title a")
    LIST_BLANKS = (By.CSS_SELECTOR, ".doc-wrap.blanki .doc-block.d-flex.align-items-center.row")
    LIST_TRIP_PDF = (By.XPATH, "//*[@class='content-block'][1] //*[@class='doc-title col']")
    PAGE_PDF = (By.CLASS_NAME, "ui-viewer-pdf-text-layer")
    IFRAME = (By.XPATH, "//div/iframe [@src]")
    XLSX_DOCX_DOCUMENTS = (By.XPATH, "//div[@class='cui-topBar2 UITextTranformUpperCase']")
    CLOSE_DOCUMENT = (By.CLASS_NAME, "ui-viewer-close-icon")


class TripRoadMapLocators:

    REJECT_COMMENT = (By.CSS_SELECTOR, "textarea[name='task_comment']")
    CHANGE_DEADLINE_COMMENT = (By.CSS_SELECTOR, "textarea[name=bprioact_SROKI_WHY]")
    CALENDAR = (By.CSS_SELECTOR, "img.calendar-icon")
    CALENDAR_DAY = (By.CSS_SELECTOR, ".bx-calendar-range a.bx-calendar-cell.bx-calendar-active")
    REASON_OVERTIME = (By.CSS_SELECTOR, "input[name='bprioact_text_zadania']")
    COMPENSATION = (By.CSS_SELECTOR, "select#id_bprioact_COMPENSATION")

    BUTTON_START = (By.CSS_SELECTOR, ".bp-btn-panel a")
    BUTTON_APPROVE = (By.CSS_SELECTOR, "button[name='approve']")
    BUTTON_NONAPPROVE = (By.CSS_SELECTOR, "button[name='nonapprove']")
    BUTTON_CANCEL = (By.CSS_SELECTOR, "button[name='cancel']")
    BUTTON_DELEGATE = (By.CSS_SELECTOR, ".bizproc-item-buttons a")
    BUTTON_TAKE_TO_WORK = (By.CSS_SELECTOR, "button[type='submit'].btn-approve")

    SEARCH_EMPLOYEE = (By.CSS_SELECTOR, "#id_bprioact_DOP_N_SOTR_UDAL a")
    EXTRA_EMPLOYEE = (By.CSS_SELECTOR, "#id_bprioact_DOP_N_SOTR a")
    RESPONSIBLE_EMPLOYEE = (By.CSS_SELECTOR, "#id_bprioact_DOP_SOGL a")
    SEND_INFO_EMPLOYEE = (By.CSS_SELECTOR, "#id_bprioact_OPOVEST a")
    CLICK_EMPLOYEE = (By.CSS_SELECTOR, "#BXSocNetLogDestinationSearch a")
    CLICK_ADDITIONAL = (By.CSS_SELECTOR, "#bx-lm-box-last-content a")
    RESOLUTION_FIELD = (By.CSS_SELECTOR, "textarea#id_bprioact_REZOL")

    INVITE_INPUT = (By.CSS_SELECTOR, "select#id_bpriact_PRIGLASIT")
    ORDER_NUMBER = (By.CSS_SELECTOR, "input[name='bpriact_N_PRIK']")
    TASK_COMPLETED = (By.CSS_SELECTOR, "select#id_bpriact_END")
    NUMBER_TRAIN_OR_PLANE = (By.CSS_SELECTOR, "input[name='bpriact_NOMER_POEZD_SAMOLET']")
    NAME_HOTEL = (By.CSS_SELECTOR, "input[name='bpriact_GOSTIN']")
    ADDRESS_HOTEL = (By.CSS_SELECTOR, "textarea#id_bpriact_ADDR_GOST")
    UPLOAD_DOCUMENTS = (By.CSS_SELECTOR, ".bizproc-field-value a")
    AVAILABLE_ROOMS = (By.CSS_SELECTOR, "select#id_bpriact_NO_SN")
    FREE_TICKETS = (By.CSS_SELECTOR, "select#id_bpriact_NO_SB")
    TRANSPORT_COSTS = (By.CSS_SELECTOR, "input#input-hvnngd")
    REASON_PAYMENTS = (By.CSS_SELECTOR, "textarea#id_bpriact_PR_D_SV_DS")
    COMPLETE_PROCESS = (By.CSS_SELECTOR, "select#id_bpriact_END_PROC")
    AMOUNT_PAID = (By.CSS_SELECTOR, "input#input-8zeemt")

    RETURN_TICKETS = (By.CSS_SELECTOR, "select#id_bpriact_VB")
    CANCEL_BOOKING = (By.CSS_SELECTOR, "select#id_bpriact_OB")
    AMOUNT_REFUNDED = (By.CSS_SELECTOR, "input#input-8zeemt")
    FLIGHT_NUMBER = (By.CSS_SELECTOR, "input[name='bpriact_NOMER_POEZD_SAMOLET']")
    HOTEL = (By.CSS_SELECTOR, "input[name='bpriact_GOSTIN']")




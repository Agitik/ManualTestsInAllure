from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class BasePageTrip:
    # инициализирует браузер
    def __init__(self, browser_dev, url):
        self.browser_dev = browser_dev
        self.url = url

    # открывает страницу, которую описывает класс
    def open(self):
        self.browser_dev.get(self.url)

    # проверяет, что элемент есть на странице
    def is_element_find(self, how, what):
        try:
            self.browser_dev.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

        # проверяет, что элементы есть на странице
    def is_elements_find(self, how, what):
        try:
            self.browser_dev.find_elements(how, what)
        except NoSuchElementException:
            return False
        return True

        # проверяет, что кнопка не кликабельна
    def is_element_not_clickable(self, how, what):
        try:
            self.browser_dev.find_element(how, what).click()
        except ElementClickInterceptedException:
            return False
        return True

    # осуществляет переключение ролей между участниками процесса для имитации работы от лица другого сотрудника
    def role_switching(self, *args):
        select_role = self.browser_dev.find_element(By.CSS_SELECTOR, "select[name='role']")
        Select(select_role).select_by_visible_text(*args)
        submit = self.browser_dev.find_element(By.CSS_SELECTOR, ".table-route input[type='submit']")
        submit.click()

    def task_description_is_present(self):
        assert self.is_element_find(By.XPATH, "//td[@class='bx-bizproc-sorted'][1]"),\
            "Нет краткого описания задачи при входе за определенную роль"

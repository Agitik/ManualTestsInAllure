import datetime
import json
import time
import os


def make_test_report():
    with open("test_from_gui.py", "w+", encoding="utf-8") as test_file:
        test_file.write("import allure\n")
        test_file.write("import pytest\n\n\n")
        with open("data_file.json", "r+", encoding="utf-8") as file:
            for test in json.loads(file.read()):
                test_file.write(f'@allure.testcase(\"{test["test_case_link"]}\", \"{test["test_case_name"]}\")\n')
                test_file.write(f'@allure.tag(\"{test["test_stand"]}\")\n')
                test_file.write('@allure.tag("Manual")\n')
                test_file.write(f'@allure.feature(\"{test["feature"]}\")\n')
                test_file.write('@allure.description("Тест добавлен вручную!")\n')
                test_file.write(f'@allure.story(\"{test["test_case_name"]}\")\n')
                test_file.write(f'@allure.suite(\"{test["functionality"]}/")\n')
                test_file.write(f'def test_manual_{str(datetime.datetime.today().strftime("%Y%m%d%H%M%S"))}():\n')
                test_file.write(f'    assert {True if test["status"] == "Успешно" else False}\n\n\n')
                time.sleep(1)
    command = 'pytest -s --alluredir="D:\\Projects\\allure"'
    # Тут указываем свою папку на Allure отчет.
    os.system('cd ""')
    res = os.system(command)

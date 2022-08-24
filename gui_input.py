import json
import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox
from tkinter import *
from tkinter import Radiobutton
from add_manual_allure import *

data = []


class App:
    def __init__(self):
        self.root = tk.Tk()
        # Настройка названия окна
        self.root.title("Ручное добавление теста")
        # Настройка размера окна.
        width = 600
        height = 500
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)

        self.head_text = tk.Label(self.root)
        ft = tkFont.Font(family='Times', size=18)
        self.head_text["font"] = ft
        self.head_text["fg"] = "#333333"
        self.head_text["justify"] = "center"
        self.head_text["text"] = "Ручное добвление тестов в автоотчет Allure."
        self.head_text.place(x=40, y=40, width=450, height=30)

        self.functionality_entry = tk.Entry(self.root)
        self.functionality_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.functionality_entry["font"] = ft
        self.functionality_entry["fg"] = "#333333"
        self.functionality_entry["justify"] = "center"
        self.functionality_entry.place(x=240, y=100, width=201, height=30)

        self.functionality_text = tk.Label(self.root)
        ft = tkFont.Font(family='Times', size=12)
        self.functionality_text["font"] = ft
        self.functionality_text["fg"] = "#333333"
        self.functionality_text["justify"] = "right"
        self.functionality_text["text"] = "Название функционала:"
        self.functionality_text.place(x=60, y=100, width=165, height=30)

        self.feature_text = tk.Label(self.root)
        ft = tkFont.Font(family='Times', size=12)
        self.feature_text["font"] = ft
        self.feature_text["fg"] = "#333333"
        self.feature_text["justify"] = "right"
        self.feature_text["text"] = "Фича функционала:"
        self.feature_text.place(x=90, y=150, width=135, height=30)

        self.feature_entry = tk.Entry(self.root)
        self.feature_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.feature_entry["font"] = ft
        self.feature_entry["fg"] = "#333333"
        self.feature_entry["justify"] = "center"
        self.feature_entry["text"] = ""
        self.feature_entry.place(x=240, y=150, width=201, height=30)

        self.test_case_name_entry = tk.Entry(self.root)
        self.test_case_name_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.test_case_name_entry["font"] = ft
        self.test_case_name_entry["fg"] = "#333333"
        self.test_case_name_entry["justify"] = "center"
        self.test_case_name_entry["text"] = ""
        self.test_case_name_entry.place(x=240, y=200, width=200, height=30)

        self.test_case_link_text = tk.Label(self.root)
        ft = tkFont.Font(family='Times', size=12)
        self.test_case_link_text["font"] = ft
        self.test_case_link_text["fg"] = "#333333"
        self.test_case_link_text["justify"] = "right"
        self.test_case_link_text["text"] = "Ссылка на тест-кейс:"
        self.test_case_link_text.place(x=80, y=280, width=145, height=30)

        self.test_case_link_entry = tk.Entry(self.root)
        self.test_case_link_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.test_case_link_entry["font"] = ft
        self.test_case_link_entry["fg"] = "#333333"
        self.test_case_link_entry["justify"] = "center"
        self.test_case_link_entry["text"] = ""
        self.test_case_link_entry.place(x=240, y=280, width=200, height=30)

        self.test_zone = BooleanVar()
        self.test_zone.set(0)

        self.prod_radio_btn = tk.Radiobutton(self.root, variable=self.test_zone, value=0)
        ft = tkFont.Font(family='Times', size=12)
        self.prod_radio_btn["font"] = ft
        self.prod_radio_btn["fg"] = "#333333"
        self.prod_radio_btn["justify"] = "center"
        self.prod_radio_btn["text"] = "Прод"
        self.prod_radio_btn.place(x=220, y=240, width=85, height=25)

        self.pred_prod_radio_btn: Radiobutton = tk.Radiobutton(self.root, variable=self.test_zone, value=1)
        ft = tkFont.Font(family='Times', size=12)
        self.pred_prod_radio_btn["font"] = ft
        self.pred_prod_radio_btn["fg"] = "#333333"
        self.pred_prod_radio_btn["justify"] = "center"
        self.pred_prod_radio_btn["text"] = "Предпрод"
        self.pred_prod_radio_btn.place(x=310, y=240, width=85, height=25)

        success_button = tk.Button(self.root)
        success_button["bg"] = "#90ee90"
        ft = tkFont.Font(family='Times', size=12)
        success_button["font"] = ft
        success_button["fg"] = "#393d49"
        success_button["justify"] = "center"
        success_button["text"] = "Успешно"
        success_button.place(x=70, y=390, width=70, height=25)
        success_button["command"] = self.success_button_command

        bag_button = tk.Button(self.root)
        bag_button["bg"] = "#fc1212"
        ft = tkFont.Font(family='Times', size=12)
        bag_button["font"] = ft
        bag_button["fg"] = "#000000"
        bag_button["justify"] = "center"
        bag_button["text"] = "Баг"
        bag_button.place(x=180, y=390, width=70, height=25)
        bag_button["command"] = self.bag_button_command

        self.comment_entry = tk.Entry(self.root)
        self.comment_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.comment_entry["font"] = ft
        self.comment_entry["fg"] = "#333333"
        self.comment_entry["justify"] = "center"
        self.comment_entry["text"] = ""
        self.comment_entry.place(x=240, y=320, width=202, height=30)

        self.comment_text = tk.Label(self.root)
        ft = tkFont.Font(family='Times', size=12)
        self.comment_text["font"] = ft
        self.comment_text["fg"] = "#333333"
        self.comment_text["justify"] = "right"
        self.comment_text["text"] = "Комментарий:"
        self.comment_text.place(x=120, y=320, width=105, height=30)

        self.test_case_text = tk.Label(self.root)
        ft = tkFont.Font(family='Times', size=12)
        self.test_case_text["font"] = ft
        self.test_case_text["fg"] = "#333333"
        self.test_case_text["justify"] = "right"
        self.test_case_text["text"] = "Название тест-кейса:"
        self.test_case_text.place(x=80, y=200, width=145, height=30)

        self.test_stand = tk.Label(self.root)
        ft = tkFont.Font(family='Times', size=12)
        self.test_stand["font"] = ft
        self.test_stand["fg"] = "#333333"
        self.test_stand["justify"] = "right"
        self.test_stand["text"] = "Тестовый стенд:"
        self.test_stand.place(x=110, y=240, width=115, height=30)

        self.test_warn = tk.Label(self.root)
        ft = tkFont.Font(family='Times', size=14)
        self.test_warn["font"] = ft
        self.test_warn["fg"] = "#ff0000"
        self.test_warn["justify"] = "right"
        self.test_warn["text"] = "Не все поля заполнены!"

        self.root.mainloop()

    def success_button_command(self):
        ret = {'functionality': self.functionality_entry.get(), 'feature': self.feature_entry.get(),
               'test_case_name': self.test_case_name_entry.get(),
               'test_stand': "Прод" if self.test_zone.get() is False else "Предпрод",
               'test_case_link': self.test_case_link_entry.get(), 'comment': self.comment_entry.get(),
               'status': 'Успешно', 'fill_status': False}
        if ret['functionality'] == "":
            self.head_text["fg"] = "#ff0000"
            self.functionality_text["fg"] = "#ff0000"
            ret['fill_status'] = False
        else:
            self.functionality_text["fg"] = "#333333"
            ret['fill_status'] = True
        if ret['feature'] == "":
            self.head_text["fg"] = "#ff0000"
            self.feature_text["fg"] = "#ff0000"
            ret['fill_status'] = False
        else:
            self.feature_text["fg"] = "#333333"
            ret['fill_status'] = True
        if ret['test_case_name'] == "":
            self.head_text["fg"] = "#ff0000"
            self.test_case_text["fg"] = "#ff0000"
            ret['fill_status'] = False
        else:
            self.test_case_text["fg"] = "#333333"
            ret['fill_status'] = True
        if ret['test_case_link'] == "":
            self.head_text["fg"] = "#ff0000"
            self.test_case_link_text["fg"] = "#ff0000"
            ret['fill_status'] = False
        else:
            self.test_case_link_text["fg"] = "#333333"
            ret['fill_status'] = True
        if ret['comment'] == "":
            self.head_text["fg"] = "#ff0000"
            self.comment_text["fg"] = "#ff0000"
            ret['fill_status'] = False
        else:
            self.comment_text["fg"] = "#333333"
            ret['fill_status'] = True

        if ret['fill_status'] is False:
            self.test_warn.place(x=80, y=450, width=200, height=30)
        else:
            data.append(ret)
            tkinter.messagebox.showinfo("Success", "Тест добавлен!")
            self.root.destroy()
            app = Question()
            self.root.mainloop()

    def bag_button_command(self):
        ret = {'functionality': self.functionality_entry.get(), 'feature': self.feature_entry.get(),
               'test_case_name': self.test_case_name_entry.get(),
               'test_stand': "Прод" if self.test_zone.get() is False else "Предпрод",
               'test_case_link': self.test_case_link_entry.get(), 'comment': self.comment_entry.get(),
               'status': 'Баг', 'fill_status': False}
        if ret['functionality'] == "":
            self.head_text["fg"] = "#ff0000"
            self.functionality_text["fg"] = "#ff0000"
            ret['fill_status'] = False
        else:
            self.functionality_text["fg"] = "#333333"
            ret['fill_status'] = True
        if ret['feature'] == "":
            self.head_text["fg"] = "#ff0000"
            self.feature_text["fg"] = "#ff0000"
            ret['fill_status'] = False
        else:
            self.feature_text["fg"] = "#333333"
            ret['fill_status'] = True
        if ret['test_case_name'] == "":
            self.head_text["fg"] = "#ff0000"
            self.test_case_text["fg"] = "#ff0000"
            ret['fill_status'] = False
        else:
            self.test_case_text["fg"] = "#333333"
            ret['fill_status'] = True
        if ret['test_case_link'] == "":
            self.head_text["fg"] = "#ff0000"
            self.test_case_link_text["fg"] = "#ff0000"
            ret['fill_status'] = False
        else:
            self.test_case_link_text["fg"] = "#333333"
            ret['fill_status'] = True
        if ret['comment'] == "":
            self.head_text["fg"] = "#ff0000"
            self.comment_text["fg"] = "#ff0000"
            ret['fill_status'] = False
        else:
            self.comment_text["fg"] = "#333333"
            ret['fill_status'] = True

        if ret['fill_status'] is False:
            self.test_warn.place(x=80, y=450, width=200, height=30)
        else:
            data.append(ret)
            tkinter.messagebox.showinfo("Success", "Тест добавлен!")
            self.root.destroy()
            app = Question()
            self.root.mainloop()


class Question:
    def __init__(self):
        # setting title
        self.root = tk.Tk()
        self.root.title("undefined")
        # setting window size
        width = 600
        height = 500
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)

        head_text = tk.Label(self.root)
        ft = tkFont.Font(family='Times', size=18)
        head_text["font"] = ft
        head_text["fg"] = "#333333"
        head_text["justify"] = "center"
        head_text["text"] = "Ручное добвление тестов в автоотчет Allure."
        head_text.place(x=50, y=160, width=450, height=30)

        add_manual_test_btn = tk.Button(self.root)
        add_manual_test_btn["bg"] = "#90ee90"
        ft = tkFont.Font(family='Times', size=12)
        add_manual_test_btn["font"] = ft
        add_manual_test_btn["fg"] = "#393d49"
        add_manual_test_btn["justify"] = "center"
        add_manual_test_btn["text"] = "Добавить отчет\n по ручному тесту\nв Allure"
        add_manual_test_btn.place(x=70, y=240, width=200, height=100)
        add_manual_test_btn["command"] = self.GButton_583_command

        close_btn = tk.Button(self.root)
        close_btn["bg"] = "#fc1212"
        ft = tkFont.Font(family='Times', size=12)
        close_btn["font"] = ft
        close_btn["fg"] = "#000000"
        close_btn["justify"] = "center"
        close_btn["text"] = "Выйти из программы"
        close_btn.place(x=320, y=240, width=200, height=100)
        close_btn["command"] = self.GButton_71_command

        self.root.mainloop()

    def GButton_583_command(self):
        self.root.destroy()
        app = App()
        app.root.mainloop()

    def GButton_71_command(self):
        self.root.destroy()


if __name__ == "__main__":
    app = Question()
    with open("data_file.json", "w") as write_file:
        json.dump(data, write_file)
    make_test_report()
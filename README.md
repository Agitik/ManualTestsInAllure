## Ручное добавление тестов
Данная программа решает проблему добавления мануальных тестов в Allure. Написана "**на скорую руку**", поэтому во многих моментах **не продумана**, но свой основной функционал она выполняет. 
Соответственно код выглядит ужасно :)
## Описание работы программы
Точка запуска программы - файл **gui_input.py**.
После запуска скрипта из python, откроется графическое окно.
Там будет две кнопки:

 - Зеленая - "Добавить отчет по ручному тесту в Allure"
 - Красная - "Выйти из программы"

Генерация отчета произойдёт в любом случае, вне зависимости от способа выхода из программы. 

После нажатия на зеленую кнопку, откроется новое графическое окно.
Там будут следующие поля:

 - [Текстовое поле] **Название функционала.** Пример: Регистрация на сайте "vk.com"
 - [Текстовое поле] **Фича функционала.** Пример: Поле ввода пароля при регистрации на сайте "vk.com"
 - [Текстовое поле] **Название тест-кейса.** Пример: Ввод китайских символов в качестве пароля.
 - [Радио переключатель] **Тестовый стенд** Место обнаружения бага. Продакшн и предпродакшн соответственно.
 - [Текстовое поле] **Ссылка на тест-кейс**. Соответственно будет опубликована в отчете Allure. Это сделано для более удобного способа подробного описания тестового кейса. В будущем планирую сделать редактор для описания.
 - [Текстовое поле] **Комментарий**. Здесь будут комментарии по тесту, в случае их отсутствия нужно проставить "-". Пока не придумал, куда это выводить в Allure, но оставлять их все же стоит. 

На данный момент все поля **являются обязательными**, программа уведомит в случае, если какое-то из полей не будет заполнено. 

Потом нужно нажать на одну из двух кнопок:
"**Успешно**" или "**Баг**"
Соответственно в зависимости от нажатой кнопки, это будет отображено в Allure с соответствующим статусом. 
У всех тестов будет проставляться тег "**Manual**" - это означает, что данный тест был добавлен вручную в автоотчет.  

Кстати небольшое, но важное дополнение. В файле "add_manual_allure.py" нужно добавить ссылку на папку, откуда будет генерироваться Allure отчет. Все необходимые модули python для работы с библиотекой указаны в файле 
## Дальнейшее развитие
Как я писал ранее, программа сделана на скорую руку и хочу заняться разработкой ее web версии. Я не особо осваивал графическую библиотеку Python, но с web'ом мне будет в разы приятнее работать и там больше возможностей. Но сделаю я это, когда появится время 😉


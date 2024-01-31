import telebot;
from telebot import types

def timetable_bells_settings_keyboards():
    markup = types.ReplyKeyboardMarkup()
    show_timetable_btn = types.KeyboardButton('Показать расписание 📅')
    markup.row(show_timetable_btn)
    show_bells_btn = types.KeyboardButton('Расписание звонков 🕗')
    show_settings_btn = types.KeyboardButton('Настройки ⚙️')
    show_etc_btn = types.KeyboardButton('О школе 🎓')
    markup.row(show_bells_btn, show_settings_btn, show_etc_btn)
    return markup

def choose_class_keyboards():
    markup = types.ReplyKeyboardMarkup()
    class_11_A_btn = types.KeyboardButton('11А')
    class_11_B_btn = types.KeyboardButton('11Б')
    class_10_A_btn = types.KeyboardButton('10А')
    class_10_B_btn = types.KeyboardButton('10Б')
    markup.row(class_11_A_btn, class_11_B_btn, class_10_A_btn, class_10_B_btn)
    back = types.KeyboardButton('Назад')
    markup.row(back)
    return markup

def settings_keyboards():
    markup = types.ReplyKeyboardMarkup()
    class_11_A_btn = types.KeyboardButton('Сменить класс')
    class_11_B_btn = types.KeyboardButton('11Б')
    class_10_A_btn = types.KeyboardButton('Включить напоминания')
    class_10_B_btn = types.KeyboardButton('10Б')
    markup.row(class_11_A_btn, class_11_B_btn, class_10_A_btn, class_10_B_btn)
    back = types.KeyboardButton('Назад')
    markup.row(back)
    return markup

def etc():
    markup = types.ReplyKeyboardMarkup()
    show_news = types.KeyboardButton('Посмотреть новости в группе школы')
    markup.row(show_news)
    return markup

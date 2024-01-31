import telebot;
from telebot import types

def choose_class_inline_keyboard():
    keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
    key_11A = types.InlineKeyboardButton(text='11А класс', callback_data='11A'); 
    key_11B = types.InlineKeyboardButton(text='11Б класс', callback_data='11B'); 
    key_10A = types.InlineKeyboardButton(text='10А класс', callback_data='10A'); 
    key_10B = types.InlineKeyboardButton(text='10Б класс', callback_data='10B'); 
    key_9A = types.InlineKeyboardButton(text='9А класс', callback_data='9A'); 
    key_9B = types.InlineKeyboardButton(text='9Б класс', callback_data='9B'); 
    key_9V = types.InlineKeyboardButton(text='9В класс', callback_data='9V'); 
    key_9G = types.InlineKeyboardButton(text='9Г класс', callback_data='9G'); 
    keyboard.row(key_11A, key_11B, key_10A, key_10B)
    keyboard.row(key_9A, key_9B, key_9V, key_9G)
    return keyboard

def choose_weekday_inline_keyboard():
    keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
    key_Monday = types.InlineKeyboardButton(text='понедельник', callback_data='Monday'); 
    key_Tuesday  = types.InlineKeyboardButton(text='вторник', callback_data='Tuesday'); 
    key_Wednesday  = types.InlineKeyboardButton(text='среда', callback_data='Wednesday'); 
    key_Thursday = types.InlineKeyboardButton(text='четверг', callback_data='Thursday'); 
    key_Friday = types.InlineKeyboardButton(text='пятница', callback_data='Friday'); 
    key_Saturday = types.InlineKeyboardButton(text='суббота', callback_data='Saturday'); 
    keyboard.add(key_Monday)
    keyboard.add(key_Tuesday)
    keyboard.add(key_Wednesday)
    keyboard.add(key_Thursday)
    keyboard.add(key_Friday)
    keyboard.add(key_Saturday)
    return keyboard

def news_keyboard():
    keyboard = types.InlineKeyboardMarkup(); # клавиатура
    key_news = types.InlineKeyboardButton(text='Новости школы 📰', callback_data='news', url='https://vk.com/school27_nk'); 
    keyboard.add(key_news)
    return keyboard

def settings_keyboard():
    keyboard = types.InlineKeyboardMarkup(); 
    key_changing_class = types.InlineKeyboardButton(text='Изменить класс', callback_data='changing_class'); 
    keyboard.add(key_changing_class)
    key_setup_reminder = types.InlineKeyboardButton(text='Настроить напоминания', callback_data='setup_reminder'); 
    keyboard.add(key_setup_reminder)
    return keyboard

def reminder_keyboard():
    keyboard = types.InlineKeyboardMarkup(); 
    key_tern_on_reminder = types.InlineKeyboardButton(text='Включить', callback_data='tern_on'); 
    key_tern_off_reminder = types.InlineKeyboardButton(text='Выключить', callback_data='tern_off'); 
    keyboard.row(key_tern_on_reminder, key_tern_off_reminder)
    return keyboard

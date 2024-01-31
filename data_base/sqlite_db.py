import sqlite3

base = sqlite3.connect('schedule_bot.db')
cursor = base.cursor()

def start_db():
    if base:
        print('База данных подключена!')
    cursor.execute('CREATE TABLE IF NOT EXISTS users (tg_id int auto_increment primary key, user_name varchar(50), class varchar(50))')
    base.commit()
    cursor.close()
    base.close()

async def get_schedule ():
    return [n for n in cursor.execute('SELECT * FROM schedule')]

import telebot;
from telebot import types
from data_base import sqlite_db, constants
import keyboards.reply_kb as reply_kb
import keyboards.inline_kb as inline_kb
import data_base.sqlite_db as sqlite_db
import sqlite3
from notifiers import get_notifier
import time
import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from pytz import timezone
import os
from dotenv import load_dotenv

load_dotenv()

TIME__LESSONS = constants.time_lessons
LESSONS = constants.lessons
DAYS = constants.days_of_the_week

schedule = {
    "11A": {
        "Monday": [
            {
                "time": TIME__LESSONS[0],
                "lesson": LESSONS["Math"],
            },
            {
                "time": TIME__LESSONS[1],
                "lesson": LESSONS["Fizika"],
            },
            {
                "time": TIME__LESSONS[2],
                "lesson": LESSONS["Russ"],
            },
            {
                "time": TIME__LESSONS[3],
                "lesson": LESSONS["Literature"],
            },
            {
                "time": TIME__LESSONS[4],
                "lesson": LESSONS["ROV"],
            },
            {
                "time": TIME__LESSONS[5],
                "lesson": LESSONS["Bio"],
            },
            {
                "time": TIME__LESSONS[6],
                "lesson": LESSONS["OBZH"],
            }
        ],
        "Tuesday": [
            {
                "time": TIME__LESSONS[0],
                "lesson": f"{LESSONS['English']} / {LESSONS['Infa']}",
            },
            {
                "time": TIME__LESSONS[1],
                "lesson": LESSONS["History"],
            },
            {
                "time": TIME__LESSONS[2],
                "lesson": LESSONS["Math"],
            },
            {
                "time": TIME__LESSONS[3],
                "lesson": LESSONS["Literature"],
            },
            {
                "time": TIME__LESSONS[4],
                "lesson": LESSONS["Fizika"],
            },
            {
                "time": TIME__LESSONS[5],
                "lesson": f"{LESSONS['English']} / {LESSONS['Infa']}",
            },
        ],
        "Wednesday": [
            {
                "time": TIME__LESSONS[0],
                "lesson": LESSONS["Society"],
            },
            {
                "time": TIME__LESSONS[1],
                "lesson":  f"{LESSONS['Infa']} / {LESSONS['R_yaz']}",
            },
            {
                "time": TIME__LESSONS[2],
                "lesson": f"{LESSONS['Infa']} / {LESSONS['R_lit']}",
            },
            {
                "time": TIME__LESSONS[3],
                "lesson": f"{LESSONS['Infa']} / {LESSONS['R_yaz']}",
            },
            {
                "time": TIME__LESSONS[4],
                "lesson": f"{LESSONS['Infa']} / {LESSONS['R_lit']}",
            },
            {
                "time": TIME__LESSONS[5],
                "lesson": f"{LESSONS['Infa']} / {LESSONS['Fizra']}",
            },
            {
                "time": TIME__LESSONS[6],
                "lesson": f"{LESSONS['Infa']} / {LESSONS['Fizra']}",
            },
        ],
        "Thursday": [
            {
                "time": TIME__LESSONS[0],
                "lesson": LESSONS["History"],
            },
            {
                "time": TIME__LESSONS[1],
                "lesson":  f"{LESSONS['English']} / {LESSONS['Infa']}",
            },
            {
                "time": TIME__LESSONS[2],
                "lesson": f"{LESSONS['English']} / {LESSONS['Infa']}",
            },
            {
                "time": TIME__LESSONS[3],
                "lesson": LESSONS["Math"],
            },
            {
                "time": TIME__LESSONS[4],
                "lesson": LESSONS["Math"],
            },
            {
                "time": TIME__LESSONS[5],
                "lesson": LESSONS["Fizika"],
            },
            {
                "time": TIME__LESSONS[6],
                "lesson": LESSONS["Ind_project"],
            },
        ],
        "Friday": [
            {
                "time": TIME__LESSONS[0],
                "lesson": LESSONS["Astronomy"],
            },
            {
                "time": TIME__LESSONS[1],
                "lesson": LESSONS["Math"],
            },
            {
                "time": TIME__LESSONS[2],
                 "lesson": LESSONS["Math"],
            },
            {
                "time": TIME__LESSONS[3],
                "lesson": LESSONS["Fizika"],
            },
            {
                "time": TIME__LESSONS[4],
                "lesson": LESSONS["Literature"],
            },
            {
                "time": TIME__LESSONS[5],
               "lesson": LESSONS["Ind_project"],
            },
        ],
        "Saturday": [
            {
                "time": TIME__LESSONS[0],
                 "lesson":  f"{LESSONS['English']} / {LESSONS['Comp_graph']}",
            },
            {
                "time": TIME__LESSONS[1],
                "lesson": LESSONS["Math"],
            },
            {
                "time": TIME__LESSONS[2],
                "lesson": LESSONS["Fizika"],
            },
            {
                "time": TIME__LESSONS[3],
                "lesson": LESSONS["Fizra"],
            },
            {
                "time": TIME__LESSONS[4],
                "lesson": LESSONS["Chemistry"],
            },
            {
                "time": TIME__LESSONS[5],
                "lesson":  f"{LESSONS['English']} / {LESSONS['Comp_graph']}",
            },
        ],
    },
    "11B": {
        "Monday": [
            {
                "time": TIME__LESSONS[0],
                "lesson": LESSONS["ROV"],
            },
            {
                "time": TIME__LESSONS[1],
                "lesson": LESSONS["Math"],
            },
            {
                "time": TIME__LESSONS[2],
                "lesson": LESSONS["Fizika"],
            },
        ],
        "Tuesday": [
            {
                "time": TIME__LESSONS[0],
                "lesson": LESSONS["Russ"],
            },
            {
                "time": TIME__LESSONS[1],
                "lesson": LESSONS["Literature"],
            },
            {
                "time": TIME__LESSONS[2],
                "lesson": LESSONS["English"],
            },
            {
                "time": TIME__LESSONS[3],
                "lesson": LESSONS["History"],
            },
            {
                "time": TIME__LESSONS[4],
                "lesson": LESSONS["Bio_fizika"],
            },
            {
                "time": TIME__LESSONS[5],
                "lesson": LESSONS["Bio"],
            },
            {
                "time": TIME__LESSONS[6],
                "lesson": LESSONS["Bio"],
            },
        ],
        "Wednesday": [
            {
                "time": TIME__LESSONS[0],
                "lesson": LESSONS["Chemistry"],
            },
            {
                "time": TIME__LESSONS[1],
                "lesson": LESSONS["Math"],
            },
            {
                "time": TIME__LESSONS[2],
               "lesson": LESSONS["Math"],
            },
            {
                "time": TIME__LESSONS[3],
               "lesson": LESSONS["History"],
            },
            {
                "time": TIME__LESSONS[4],
               "lesson": LESSONS["Literature"],
            },
            {
                "time": TIME__LESSONS[5],
                 "lesson": LESSONS["R_yaz"],
            },
            {
                "time": TIME__LESSONS[6],
                "lesson": LESSONS["R_lit"],
            },
        ],
        "Thursday": [
            {
                "time": TIME__LESSONS[0],
                "lesson": LESSONS["English"],
            },
            {
                "time": TIME__LESSONS[1],
                "lesson": LESSONS["Math"],
            },
            {
                "time": TIME__LESSONS[2],
                "lesson": LESSONS["Bio"],
            },
            {
                "time": TIME__LESSONS[3],
                "lesson": LESSONS["Ecology"],
            },
            {
                "time": TIME__LESSONS[4],
                "lesson": LESSONS["OBZH"],
            },
            {
                "time": TIME__LESSONS[5],
                "lesson": LESSONS["Chemistry"],
            },
            {
                "time": TIME__LESSONS[6],
                "lesson": LESSONS["Chemistry"],
            },
        ],
        "Friday": [
            {
                "time": TIME__LESSONS[0],
                "lesson": LESSONS["Math"],
            },
            {
                "time": TIME__LESSONS[1],
                "lesson": LESSONS["Literature"],
            },
            {
                "time": TIME__LESSONS[2],
                 "lesson": LESSONS["Fizra"],
            },
            {
                "time": TIME__LESSONS[3],
                "lesson": LESSONS["Bio"],
            },
            {
                "time": TIME__LESSONS[4],
                "lesson": LESSONS["Chemistry"],
            },
            {
                "time": TIME__LESSONS[5],
               "lesson": LESSONS["Ind_project"],
            },
            {
                "time": TIME__LESSONS[6],
               "lesson": LESSONS["Astronomy"],
            },
        ],
        "Saturday": [
            {
                "time": TIME__LESSONS[0],
                "lesson": LESSONS["Math"],
            },
            {
                "time": TIME__LESSONS[1],
                "lesson":  f"{LESSONS['English']} / {LESSONS['Infa']}",
            },
            {
                "time": TIME__LESSONS[2],
                "lesson":  f"{LESSONS['English']} / {LESSONS['Infa']}",
            },
            {
                "time": TIME__LESSONS[3],
                "lesson": LESSONS["Chemistry"],
            },
            {
                "time": TIME__LESSONS[4],
                "lesson": LESSONS["Bio"],
            },
            {
                "time": TIME__LESSONS[5],
                "lesson": LESSONS["Fizra"],
            },
            {
                "time": TIME__LESSONS[6],
                "lesson": LESSONS["Fizra"],
            },
        ],
    },
    "10A": {
        "Monday": [
            {
                "time": TIME__LESSONS[0],
                "lesson": LESSONS["ROV"],
            },
            {
                "time": TIME__LESSONS[1],
                "lesson": LESSONS["Verstat"],
            },
            {
                "time": TIME__LESSONS[2],
                "lesson": LESSONS["Chemistry"],
            },
            {
                "time": TIME__LESSONS[3],
                "lesson": LESSONS["Fizika"],
            },
            {
                "time": TIME__LESSONS[4],
                "lesson": LESSONS["History"],
            },
            {
                "time": TIME__LESSONS[5],
                "lesson": LESSONS["R_lit"],
            },
        ],
        "Tuesday": [
            {
                "time": TIME__LESSONS[0],
                "lesson": LESSONS["OBZH"],
            },
            {
                "time": TIME__LESSONS[1],
                "lesson":  f"{LESSONS['English']} / {LESSONS['Infa']}",
            },
            {
                "time": TIME__LESSONS[2],
                "lesson":  f"{LESSONS['Infa']} / {LESSONS['R_yaz']}",
            },
            {
                "time": TIME__LESSONS[3],
                "lesson":  f"{LESSONS['English']} / {LESSONS['Infa']}",
            },
            {
                "time": TIME__LESSONS[4],
                "lesson":  f"{LESSONS['Infa']} / {LESSONS['R_yaz']}",
            },
            {
                "time": TIME__LESSONS[5],
                "lesson": LESSONS["Algebra"],
            },
            {
                "time": TIME__LESSONS[6],
                "lesson": LESSONS["Society"],
            },
        ],
        "Wednesday": [
            {
                "time": TIME__LESSONS[0],
                "lesson":  f"{LESSONS['Infa']} / {LESSONS['R_yaz']}",
            },
            {
                "time": TIME__LESSONS[1],
                "lesson": LESSONS["Geography"],
            },
            {
                "time": TIME__LESSONS[2],
               "lesson": LESSONS["Algebra"],
            },
            {
                "time": TIME__LESSONS[3],
               "lesson": LESSONS["Geometry"],
            },
            {
                "time": TIME__LESSONS[4],
               "lesson": LESSONS["Literature"],
            },
            {
                "time": TIME__LESSONS[5],
                "lesson":  f"{LESSONS['Ind_project']} / {LESSONS['R_yaz']}",
            },
            {
                "time": TIME__LESSONS[6],
                "lesson": LESSONS["Infa"],
            },
        ],
        "Thursday": [
            {
                "time": TIME__LESSONS[0],
                "lesson": LESSONS["Infa"],
            },
            {
                "time": TIME__LESSONS[1],
                "lesson": LESSONS["Russ"],
            },
            {
                "time": TIME__LESSONS[2],
                "lesson": LESSONS["Literature"],
            },
            {
                "time": TIME__LESSONS[3],
                "lesson":  f"{LESSONS['English']} / {LESSONS['Infa']}",
            },
            {
                "time": TIME__LESSONS[4],
                "lesson":  f"{LESSONS['Infa']} / {LESSONS['English']}",
            },
            {
                "time": TIME__LESSONS[5],
                "lesson": LESSONS["Fizra"],
            },
            {
                "time": TIME__LESSONS[6],
                "lesson": LESSONS["Fizra"],
            },
        ],
        "Friday": [
            {
                "time": TIME__LESSONS[0],
                "lesson": LESSONS["Geometry"],
            },
            {
                "time": TIME__LESSONS[1],
                "lesson": LESSONS["Fizika"],
            },
            {
                "time": TIME__LESSONS[2],
                "lesson": LESSONS["Society"],
            },
            {
                "time": TIME__LESSONS[3],
                "lesson": LESSONS["Literature"],
            },
            {
                "time": TIME__LESSONS[4],
               "lesson": LESSONS["Algebra"],
            },
            {
                "time": TIME__LESSONS[5],
               "lesson": LESSONS["Russ"],
            },
        ],
        "Saturday": [
            {
                "time": TIME__LESSONS[0],
                "lesson":  f"{LESSONS['English']} / {LESSONS['Technology']}",
            },
            {
                "time": TIME__LESSONS[1],
                "lesson":  f"{LESSONS['English']} / {LESSONS['Technology']}",
            },
            {
                "time": TIME__LESSONS[2],
                "lesson": LESSONS["History"],
            },
            {
                "time": TIME__LESSONS[3],
                "lesson": LESSONS["Geometry"],
            },
            {
                "time": TIME__LESSONS[4],
                "lesson": LESSONS["Algebra"],
            },
            {
                "time": TIME__LESSONS[5],
                "lesson": LESSONS["Bio"],
            },
        ],
    },
    "10B": {
        "Monday": [
            {
                "time": TIME__LESSONS[0],
                "lesson": LESSONS["ROV"],
            },
            {
                "time": TIME__LESSONS[1],
                "lesson":  f"{LESSONS['English']} / {LESSONS['R_yaz']}",
            },
            {
                "time": TIME__LESSONS[2],
                "lesson":  f"{LESSONS['R_yaz']} / {LESSONS['English']}",
            },
            {
                "time": TIME__LESSONS[3],
                "lesson": LESSONS["Fizra"],
            },
            {
                "time": TIME__LESSONS[4],
                "lesson": LESSONS["Fizra"],
            },
            {
                "time": TIME__LESSONS[5],
                "lesson": LESSONS["Fizika"],
            },
            {
                "time": TIME__LESSONS[6],
                "lesson": LESSONS["Verstat"],
            },
            {
                "time": TIME__LESSONS[7],
                "lesson": LESSONS["R_lit"],
            },
        ],
        "Tuesday": [
            {
                "time": TIME__LESSONS[0],
                "lesson": LESSONS["History"],
            },
            {
                "time": TIME__LESSONS[1],
                "lesson": LESSONS["Chemistry"],
            },
            {
                "time": TIME__LESSONS[2],
                "lesson": LESSONS["Society"],
            },
            {
                "time": TIME__LESSONS[3],
                "lesson": LESSONS["Geometry"],
            },
            {
                "time": TIME__LESSONS[4],
                "lesson": LESSONS["Algebra"],
            },
            {
                "time": TIME__LESSONS[5],
                "lesson": LESSONS["Russ"],
            },
            {
                "time": TIME__LESSONS[6],
                "lesson": LESSONS["Literature"],
            },
        ],
        "Wednesday": [
            {
                "time": TIME__LESSONS[0],
                "lesson": LESSONS["R_yaz"],
            },
            {
                "time": TIME__LESSONS[1],
                "lesson": LESSONS["English"],
            },
            {
                "time": TIME__LESSONS[2],
               "lesson": LESSONS["R_yaz"],
            },
            {
                "time": TIME__LESSONS[3],
               "lesson": LESSONS["English"],
            },
        ],
        "Thursday": [
            {
                "time": TIME__LESSONS[0],
                "lesson": LESSONS["OBZH"],
            },
            {
                "time": TIME__LESSONS[1],
                "lesson": LESSONS["Society"],
            },
            {
                "time": TIME__LESSONS[2],
                "lesson": LESSONS["History"],
            },
            {
                "time": TIME__LESSONS[3],
                "lesson": LESSONS["Algebra"],
            },
            {
                "time": TIME__LESSONS[4],
                "lesson": LESSONS["Bio"],
            },
            {
                "time": TIME__LESSONS[5],
                "lesson": LESSONS["Geography"],
            },
            {
                "time": TIME__LESSONS[6],
                "lesson": LESSONS["Fizika"],
            },
        ],
        "Friday": [
            {
                "time": TIME__LESSONS[0],
                "lesson": LESSONS["Russ"],
            },
            {
                "time": TIME__LESSONS[1],
                "lesson": LESSONS["Literature"],
            },
            {
                "time": TIME__LESSONS[2],
                 "lesson": LESSONS["Chemistry"],
            },
            {
                "time": TIME__LESSONS[3],
                "lesson": LESSONS["Ind_project"],
            },
            {
                "time": TIME__LESSONS[4],
                "lesson": LESSONS["Bio"],
            },
            {
                "time": TIME__LESSONS[5],
               "lesson": LESSONS["Bio_fizika"],
            },
            {
                "time": TIME__LESSONS[6],
               "lesson": LESSONS["Ecology"],
            },
        ],
        "Saturday": [
            {
                "time": TIME__LESSONS[0],
                "lesson": LESSONS["Chemistry"],
            },
            {
                "time": TIME__LESSONS[1],
                "lesson": LESSONS["Литература"],
            },
            {
                "time": TIME__LESSONS[2],
                "lesson": LESSONS["Bio"],
            },
            {
                "time": TIME__LESSONS[3],
                "lesson":  f"{LESSONS['English']} / {LESSONS['Infa']}",
            },
            {
                "time": TIME__LESSONS[4],
                "lesson":  f"{LESSONS['Infa']} / {LESSONS['English']}",
            },
            {
                "time": TIME__LESSONS[5],
                "lesson": LESSONS["Geometry"],
            },
            {
                "time": TIME__LESSONS[6],
                "lesson": LESSONS["PrChem"],
            },
        ],
    },
    "9A": {
        "Monday": [
            {
                "time": TIME__LESSONS[0],
                "lesson": LESSONS["ROV"],
            },
            {
                "time": TIME__LESSONS[1],
                "lesson": LESSONS["Math"],
            },
            {
                "time": TIME__LESSONS[2],
                "lesson": LESSONS["Fizika"],
            },
        ],
        "Tuesday": [
            {
                "time": TIME__LESSONS[0],
                "lesson": LESSONS["Russ"],
            },
            {
                "time": TIME__LESSONS[1],
                "lesson": LESSONS["Literature"],
            },
            {
                "time": TIME__LESSONS[2],
                "lesson": LESSONS["English"],
            },
            {
                "time": TIME__LESSONS[3],
                "lesson": LESSONS["History"],
            },
            {
                "time": TIME__LESSONS[4],
                "lesson": LESSONS["Bio_fizika"],
            },
            {
                "time": TIME__LESSONS[5],
                "lesson": LESSONS["Bio"],
            },
            {
                "time": TIME__LESSONS[6],
                "lesson": LESSONS["Bio"],
            },
        ],
        "Wednesday": [
            {
                "time": TIME__LESSONS[0],
                "lesson": LESSONS["Chemistry"],
            },
            {
                "time": TIME__LESSONS[1],
                "lesson": LESSONS["Math"],
            },
            {
                "time": TIME__LESSONS[2],
               "lesson": LESSONS["Math"],
            },
            {
                "time": TIME__LESSONS[3],
               "lesson": LESSONS["History"],
            },
            {
                "time": TIME__LESSONS[4],
               "lesson": LESSONS["Literature"],
            },
            {
                "time": TIME__LESSONS[5],
                 "lesson": LESSONS["R_yaz"],
            },
            {
                "time": TIME__LESSONS[6],
                "lesson": LESSONS["R_lit"],
            },
        ],
        "Thursday": [
            {
                "time": TIME__LESSONS[0],
                "lesson": LESSONS["English"],
            },
            {
                "time": TIME__LESSONS[1],
                "lesson": LESSONS["Math"],
            },
            {
                "time": TIME__LESSONS[2],
                "lesson": LESSONS["Bio"],
            },
            {
                "time": TIME__LESSONS[3],
                "lesson": LESSONS["Ecology"],
            },
            {
                "time": TIME__LESSONS[4],
                "lesson": LESSONS["OBZH"],
            },
            {
                "time": TIME__LESSONS[5],
                "lesson": LESSONS["Chemistry"],
            },
            {
                "time": TIME__LESSONS[6],
                "lesson": LESSONS["Chemistry"],
            },
        ],
        "Friday": [
            {
                "time": TIME__LESSONS[0],
                "lesson": LESSONS["Math"],
            },
            {
                "time": TIME__LESSONS[1],
                "lesson": LESSONS["Literature"],
            },
            {
                "time": TIME__LESSONS[2],
                 "lesson": LESSONS["Fizra"],
            },
            {
                "time": TIME__LESSONS[3],
                "lesson": LESSONS["Bio"],
            },
            {
                "time": TIME__LESSONS[4],
                "lesson": LESSONS["Chemistry"],
            },
            {
                "time": TIME__LESSONS[5],
               "lesson": LESSONS["Ind_project"],
            },
            {
                "time": TIME__LESSONS[6],
               "lesson": LESSONS["Astronomy"],
            },
        ],
        "Saturday": [
            {
                "time": TIME__LESSONS[0],
                "lesson": LESSONS["Math"],
            },
            {
                "time": TIME__LESSONS[1],
                "lesson":  f"{LESSONS['English']} / {LESSONS['Infa']}",
            },
            {
                "time": TIME__LESSONS[2],
                "lesson":  f"{LESSONS['English']} / {LESSONS['Infa']}",
            },
            {
                "time": TIME__LESSONS[3],
                "lesson": LESSONS["Chemistry"],
            },
            {
                "time": TIME__LESSONS[4],
                "lesson": LESSONS["Bio"],
            },
            {
                "time": TIME__LESSONS[5],
                "lesson": LESSONS["Fizra"],
            },
            {
                "time": TIME__LESSONS[6],
                "lesson": LESSONS["Fizra"],
            },
        ],
    },
    "9B": {
        "Monday": [
            {
                "time": TIME__LESSONS[0],
                "lesson": LESSONS["ROV"],
            },
            {
                "time": TIME__LESSONS[1],
                "lesson": LESSONS["Math"],
            },
            {
                "time": TIME__LESSONS[2],
                "lesson": LESSONS["Fizika"],
            },
        ],
        "Tuesday": [
            {
                "time": TIME__LESSONS[0],
                "lesson": LESSONS["Russ"],
            },
            {
                "time": TIME__LESSONS[1],
                "lesson": LESSONS["Literature"],
            },
            {
                "time": TIME__LESSONS[2],
                "lesson": LESSONS["English"],
            },
            {
                "time": TIME__LESSONS[3],
                "lesson": LESSONS["History"],
            },
            {
                "time": TIME__LESSONS[4],
                "lesson": LESSONS["Bio_fizika"],
            },
            {
                "time": TIME__LESSONS[5],
                "lesson": LESSONS["Bio"],
            },
            {
                "time": TIME__LESSONS[6],
                "lesson": LESSONS["Bio"],
            },
        ],
        "Wednesday": [
            {
                "time": TIME__LESSONS[0],
                "lesson": LESSONS["Chemistry"],
            },
            {
                "time": TIME__LESSONS[1],
                "lesson": LESSONS["Math"],
            },
            {
                "time": TIME__LESSONS[2],
               "lesson": LESSONS["Math"],
            },
            {
                "time": TIME__LESSONS[3],
               "lesson": LESSONS["History"],
            },
            {
                "time": TIME__LESSONS[4],
               "lesson": LESSONS["Literature"],
            },
            {
                "time": TIME__LESSONS[5],
                 "lesson": LESSONS["R_yaz"],
            },
            {
                "time": TIME__LESSONS[6],
                "lesson": LESSONS["R_lit"],
            },
        ],
        "Thursday": [
            {
                "time": TIME__LESSONS[0],
                "lesson": LESSONS["English"],
            },
            {
                "time": TIME__LESSONS[1],
                "lesson": LESSONS["Math"],
            },
            {
                "time": TIME__LESSONS[2],
                "lesson": LESSONS["Bio"],
            },
            {
                "time": TIME__LESSONS[3],
                "lesson": LESSONS["Ecology"],
            },
            {
                "time": TIME__LESSONS[4],
                "lesson": LESSONS["OBZH"],
            },
            {
                "time": TIME__LESSONS[5],
                "lesson": LESSONS["Chemistry"],
            },
            {
                "time": TIME__LESSONS[6],
                "lesson": LESSONS["Chemistry"],
            },
        ],
        "Friday": [
            {
                "time": TIME__LESSONS[0],
                "lesson": LESSONS["Math"],
            },
            {
                "time": TIME__LESSONS[1],
                "lesson": LESSONS["Literature"],
            },
            {
                "time": TIME__LESSONS[2],
                 "lesson": LESSONS["Fizra"],
            },
            {
                "time": TIME__LESSONS[3],
                "lesson": LESSONS["Bio"],
            },
            {
                "time": TIME__LESSONS[4],
                "lesson": LESSONS["Chemistry"],
            },
            {
                "time": TIME__LESSONS[5],
               "lesson": LESSONS["Ind_project"],
            },
            {
                "time": TIME__LESSONS[6],
               "lesson": LESSONS["Astronomy"],
            },
        ],
        "Saturday": [
            {
                "time": TIME__LESSONS[0],
                "lesson": LESSONS["Math"],
            },
            {
                "time": TIME__LESSONS[1],
                "lesson":  f"{LESSONS['English']} / {LESSONS['Infa']}",
            },
            {
                "time": TIME__LESSONS[2],
                "lesson":  f"{LESSONS['English']} / {LESSONS['Infa']}",
            },
            {
                "time": TIME__LESSONS[3],
                "lesson": LESSONS["Chemistry"],
            },
            {
                "time": TIME__LESSONS[4],
                "lesson": LESSONS["Bio"],
            },
            {
                "time": TIME__LESSONS[5],
                "lesson": LESSONS["Fizra"],
            },
            {
                "time": TIME__LESSONS[6],
                "lesson": LESSONS["Fizra"],
            },
        ],
    },
    "9V": {
        "Monday": [
            {
                "time": TIME__LESSONS[0],
                "lesson": LESSONS["ROV"],
            },
            {
                "time": TIME__LESSONS[1],
                "lesson": LESSONS["Math"],
            },
            {
                "time": TIME__LESSONS[2],
                "lesson": LESSONS["Fizika"],
            },
        ],
        "Tuesday": [
            {
                "time": TIME__LESSONS[0],
                "lesson": LESSONS["Russ"],
            },
            {
                "time": TIME__LESSONS[1],
                "lesson": LESSONS["Literature"],
            },
            {
                "time": TIME__LESSONS[2],
                "lesson": LESSONS["English"],
            },
            {
                "time": TIME__LESSONS[3],
                "lesson": LESSONS["History"],
            },
            {
                "time": TIME__LESSONS[4],
                "lesson": LESSONS["Bio_fizika"],
            },
            {
                "time": TIME__LESSONS[5],
                "lesson": LESSONS["Bio"],
            },
            {
                "time": TIME__LESSONS[6],
                "lesson": LESSONS["Bio"],
            },
        ],
        "Wednesday": [
            {
                "time": TIME__LESSONS[0],
                "lesson": LESSONS["Chemistry"],
            },
            {
                "time": TIME__LESSONS[1],
                "lesson": LESSONS["Math"],
            },
            {
                "time": TIME__LESSONS[2],
               "lesson": LESSONS["Math"],
            },
            {
                "time": TIME__LESSONS[3],
               "lesson": LESSONS["History"],
            },
            {
                "time": TIME__LESSONS[4],
               "lesson": LESSONS["Literature"],
            },
            {
                "time": TIME__LESSONS[5],
                 "lesson": LESSONS["R_yaz"],
            },
            {
                "time": TIME__LESSONS[6],
                "lesson": LESSONS["R_lit"],
            },
        ],
        "Thursday": [
            {
                "time": TIME__LESSONS[0],
                "lesson": LESSONS["English"],
            },
            {
                "time": TIME__LESSONS[1],
                "lesson": LESSONS["Math"],
            },
            {
                "time": TIME__LESSONS[2],
                "lesson": LESSONS["Bio"],
            },
            {
                "time": TIME__LESSONS[3],
                "lesson": LESSONS["Ecology"],
            },
            {
                "time": TIME__LESSONS[4],
                "lesson": LESSONS["OBZH"],
            },
            {
                "time": TIME__LESSONS[5],
                "lesson": LESSONS["Chemistry"],
            },
            {
                "time": TIME__LESSONS[6],
                "lesson": LESSONS["Chemistry"],
            },
        ],
        "Friday": [
            {
                "time": TIME__LESSONS[0],
                "lesson": LESSONS["Math"],
            },
            {
                "time": TIME__LESSONS[1],
                "lesson": LESSONS["Literature"],
            },
            {
                "time": TIME__LESSONS[2],
                 "lesson": LESSONS["Fizra"],
            },
            {
                "time": TIME__LESSONS[3],
                "lesson": LESSONS["Bio"],
            },
            {
                "time": TIME__LESSONS[4],
                "lesson": LESSONS["Chemistry"],
            },
            {
                "time": TIME__LESSONS[5],
               "lesson": LESSONS["Ind_project"],
            },
            {
                "time": TIME__LESSONS[6],
               "lesson": LESSONS["Astronomy"],
            },
        ],
        "Saturday": [
            {
                "time": TIME__LESSONS[0],
                "lesson": LESSONS["Math"],
            },
            {
                "time": TIME__LESSONS[1],
                "lesson":  f"{LESSONS['English']} / {LESSONS['Infa']}",
            },
            {
                "time": TIME__LESSONS[2],
                "lesson":  f"{LESSONS['English']} / {LESSONS['Infa']}",
            },
            {
                "time": TIME__LESSONS[3],
                "lesson": LESSONS["Chemistry"],
            },
            {
                "time": TIME__LESSONS[4],
                "lesson": LESSONS["Bio"],
            },
            {
                "time": TIME__LESSONS[5],
                "lesson": LESSONS["Fizra"],
            },
            {
                "time": TIME__LESSONS[6],
                "lesson": LESSONS["Fizra"],
            },
        ],
    },
    "9G": {
        "Monday": [
            {
                "time": TIME__LESSONS[0],
                "lesson": LESSONS["ROV"],
            },
            {
                "time": TIME__LESSONS[1],
                "lesson": LESSONS["Math"],
            },
            {
                "time": TIME__LESSONS[2],
                "lesson": LESSONS["Fizika"],
            },
        ],
        "Tuesday": [
            {
                "time": TIME__LESSONS[0],
                "lesson": LESSONS["Russ"],
            },
            {
                "time": TIME__LESSONS[1],
                "lesson": LESSONS["Literature"],
            },
            {
                "time": TIME__LESSONS[2],
                "lesson": LESSONS["English"],
            },
            {
                "time": TIME__LESSONS[3],
                "lesson": LESSONS["History"],
            },
            {
                "time": TIME__LESSONS[4],
                "lesson": LESSONS["Bio_fizika"],
            },
            {
                "time": TIME__LESSONS[5],
                "lesson": LESSONS["Bio"],
            },
            {
                "time": TIME__LESSONS[6],
                "lesson": LESSONS["Bio"],
            },
        ],
        "Wednesday": [
            {
                "time": TIME__LESSONS[0],
                "lesson": LESSONS["Chemistry"],
            },
            {
                "time": TIME__LESSONS[1],
                "lesson": LESSONS["Math"],
            },
            {
                "time": TIME__LESSONS[2],
               "lesson": LESSONS["Math"],
            },
            {
                "time": TIME__LESSONS[3],
               "lesson": LESSONS["History"],
            },
            {
                "time": TIME__LESSONS[4],
               "lesson": LESSONS["Literature"],
            },
            {
                "time": TIME__LESSONS[5],
                 "lesson": LESSONS["R_yaz"],
            },
            {
                "time": TIME__LESSONS[6],
                "lesson": LESSONS["R_lit"],
            },
        ],
        "Thursday": [
            {
                "time": TIME__LESSONS[0],
                "lesson": LESSONS["English"],
            },
            {
                "time": TIME__LESSONS[1],
                "lesson": LESSONS["Math"],
            },
            {
                "time": TIME__LESSONS[2],
                "lesson": LESSONS["Bio"],
            },
            {
                "time": TIME__LESSONS[3],
                "lesson": LESSONS["Ecology"],
            },
            {
                "time": TIME__LESSONS[4],
                "lesson": LESSONS["OBZH"],
            },
            {
                "time": TIME__LESSONS[5],
                "lesson": LESSONS["Chemistry"],
            },
            {
                "time": TIME__LESSONS[6],
                "lesson": LESSONS["Chemistry"],
            },
        ],
        "Friday": [
            {
                "time": TIME__LESSONS[0],
                "lesson": LESSONS["Math"],
            },
            {
                "time": TIME__LESSONS[1],
                "lesson": LESSONS["Literature"],
            },
            {
                "time": TIME__LESSONS[2],
                 "lesson": LESSONS["Fizra"],
            },
            {
                "time": TIME__LESSONS[3],
                "lesson": LESSONS["Bio"],
            },
            {
                "time": TIME__LESSONS[4],
                "lesson": LESSONS["Chemistry"],
            },
            {
                "time": TIME__LESSONS[5],
               "lesson": LESSONS["Ind_project"],
            },
            {
                "time": TIME__LESSONS[6],
               "lesson": LESSONS["Astronomy"],
            },
        ],
        "Saturday": [
            {
                "time": TIME__LESSONS[0],
                "lesson": LESSONS["Math"],
            },
            {
                "time": TIME__LESSONS[1],
                "lesson":  f"{LESSONS['English']} / {LESSONS['Infa']}",
            },
            {
                "time": TIME__LESSONS[2],
                "lesson":  f"{LESSONS['English']} / {LESSONS['Infa']}",
            },
            {
                "time": TIME__LESSONS[3],
                "lesson": LESSONS["Chemistry"],
            },
            {
                "time": TIME__LESSONS[4],
                "lesson": LESSONS["Bio"],
            },
            {
                "time": TIME__LESSONS[5],
                "lesson": LESSONS["Fizra"],
            },
            {
                "time": TIME__LESSONS[6],
                "lesson": LESSONS["Fizra"],
            },
        ],
    },
}

API_TG_KEY = os.getenv('API_KEY')

bot = telebot.TeleBot(API_TG_KEY)
print('start')


'''
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
     bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
'''
name = ''
surname = ''
age = 0
choosen_class = 0
current_message_id = 0

@bot.message_handler(commands=['register', 'auth'])
def choose_class(message):
    question = 'В каком ты классе?'
    bot.send_message(message.from_user.id, text=question, reply_markup=inline_kb.choose_class_inline_keyboard())
   



#@bot.message_handler(commands=['db'])
def db_connect(message):
    choosen_user_class = choosen_class
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    default_notifications = 0
    base = sqlite3.connect('schedule_bot.db')
    cursor = base.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, tg_id INTEGER UNIQUE, user_name varchar(50), class varchar(50), notifications INTEGER DEFAULT 0)')
    
  #  cursor.execute('SELECT * FROM users')
   # users = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM users WHERE tg_id = ?", (user_id,))
    result = cursor.fetchone()
    user_exists = result[0] > 0
    print(f'пользователь_ существует {user_exists}')
    if user_exists:
        cursor.execute("UPDATE users SET class = ? WHERE tg_id = ?", (choosen_user_class, user_id))
    else:
        cursor.execute("INSERT OR REPLACE INTO users (tg_id, user_name, class, notifications) VALUES(?, ?, ?, ?)", (user_id, user_name, choosen_user_class, default_notifications))

    base.commit()
    cursor.close()
    base.close()

#@bot.message_handler(commands=['q'])
def lister(message):
    base = sqlite3.connect('schedule_bot.db')
    cursor = base.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    info = ''
    for el in users:
        info += f'  \n Имя: {el[2]}, id: {el[1]}, ученик {el[3]} класса, уведомления{el[4]}'
    cursor.close()
    base.close()
    print(message.message.chat.id, 'this is chat id', message.from_user.id, 'this is user id')
    bot.send_message(message.from_user.id, info)

def managing_notifications(message):
    question = 'Настройка напоминаний'
    bot.send_message(message.from_user.id, text=question, reply_markup=inline_kb.reminder_keyboard())
   



@bot.message_handler(commands=['start'])
def start(message):
    '''
    markup = types.ReplyKeyboardMarkup()
    show_timetable_btn = types.KeyboardButton('Показать расписание 📅 ')
    markup.row(show_timetable_btn)
    show_bells_btn = types.KeyboardButton('Расписание звонков 🕗')
    show_settings_btn = types.KeyboardButton('Настройки ⚙️')
    markup.row(show_bells_btn, show_settings_btn)
    '''
    
    
    bot.send_message(message.chat.id, 'Выберите нужную функцию', reply_markup=reply_kb.timetable_bells_settings_keyboards())


@bot.message_handler(content_types=['text'])
def show_timetable(message: types.Message):
    if message.text == 'Расписание звонков 🕗':
        bot.send_message(message.chat.id, f'''
            Актуальное расписание звонков:
            \n
            {TIME__LESSONS[0]} \n
            {TIME__LESSONS[1]} \n
            {TIME__LESSONS[2]} \n
            {TIME__LESSONS[3]} \n
            {TIME__LESSONS[4]} \n
            {TIME__LESSONS[5]} \n
            {TIME__LESSONS[6]} \n
            {TIME__LESSONS[7]} \n
        ''')
    elif message.text == 'Показать расписание 📅':
        question = 'Выберите день недели'
        bot.send_message(message.chat.id, text=question, reply_markup=inline_kb.choose_weekday_inline_keyboard())

    elif message.text == 'О школе 🎓':
        info = 'Муниципальное бюджетное общеобразовательное учреждение «Средняя общеобразовательная школа №27 с углубленным изучением отдельных предметов»Нижнекамского муниципального района Республики Татарстан'
        bot.send_message(message.chat.id, text=info, reply_markup=inline_kb.news_keyboard())
    
    elif message.text == 'Настройки ⚙️':
        question = 'Здесь Вы можете изменить класс, а также настроить отправку уведомлений с расписанием'
        chat_id = message.chat.id
        message_id = message.message_id
        print(chat_id, message_id)
        #bot.reply_to(message.chat.id, text=question,  reply_to_message_id=message.message_id, reply_markup=inline_kb.news_keyboard())
        bot.send_message(chat_id, text=question, reply_to_message_id=message_id,  reply_markup=inline_kb.settings_keyboard())

def show_schedule(message):
    # Подключение к БД
    base = sqlite3.connect('schedule_bot.db')
    cursor = base.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall() 

    current_message_id = message.message.message_id
    current_user = message.from_user.id
    weekday = message.data
    current_class = ''

    for user in users:
        if user[1] == current_user:
            current_class = user[3]
            print(current_class)

    if weekday in DAYS:
        weekday_arr = schedule[current_class][weekday]
        title = f' <b> Расписание на {weekday}:</b>'
        info = ''
        #for el in weekday_arr:
        #    info += f' \n {el["time"]}  {el["lesson"]}\n'    
        for index, el in enumerate(weekday_arr, start=1):
            info += f' \n {index}. {el["lesson"]}'
        bot.send_message(message.from_user.id, text=f'{title}\n{info}', parse_mode='html')
        bot.delete_message(message.from_user.id, current_message_id)


'''
def get_age(message):
    global age
    while age == 0: #проверяем что возраст изменился
        try:
             age = int(message.text) #проверяем, что возраст введен корректно
        except Exception:
             bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
             
    keyboard = types.InlineKeyboardMarkup(); #наша клавиатура
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes'); #кнопка «Да»
    keyboard.add(key_yes); #добавляем кнопку в клавиатуру
    key_no= types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)
    question = 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes": #call.data это callback_data, которую мы указали при объявлении кнопки
        
        bot.send_message(call.message.chat.id, 'Запомню : )')
    elif call.data == "no":
        bot.send_message(call.message.chat.id, 'Жаль')
'''

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global choosen_class
    print(call.data)
    if (call.data in DAYS):
        show_schedule(call)

    elif (call.data == 'changing_class'):
        choose_class(call)

    elif (call.data == 'setup_reminder'):
        managing_notifications(call)

    elif (call.data == 'tern_on'):
        tern_on_notification(call.from_user.id)
        bot.send_message(call.from_user.id, text=f' Напоминания успешно {call.data} *ੈ♡⸝⸝🪐༘⋆')

    elif (call.data == 'tern_off'):
       
        bot.send_message(call.from_user.id, text=f' Напоминания успешно {call.data}')
         # Подключение к БД
        base = sqlite3.connect('schedule_bot.db')
        cursor = base.cursor()
        cursor.execute('SELECT * FROM users')
        users = cursor.fetchall() 
        for user in users:
            chat_id = user[1]
            if (user[4] == 1):
                print('this user id', chat_id)
                notification(chat_id)
            '''
        while True:
            what = input('О че напомнить?')
            if what == 'exit':
                break
            else:
                t = input('How match sec?')
                t = int(t) 
                time.sleep(t)
                telegram = get_notifier('telegram')
                print('this user id', call.from_user.id)
                telegram.notify(token='', chat_id=f'{call.from_user.id}', message=what)
    '''

    else:
        choosen_class = call.data
        db_connect(call)
        lister(call)

def notification(chat_id):
    t = 10
    what = 'Напоминаю, что завтра в школу'
    t = int(t) 
    time.sleep(t)
    telegram = get_notifier('telegram')
    telegram.notify(token=API_TG_KEY, chat_id=f'{chat_id}', message=what)

def tern_on_notification(id):
    # Подключение к БД
    base = sqlite3.connect('schedule_bot.db')
    cursor = base.cursor()
    cursor.execute('SELECT * FROM users')
    notifications = 1
    # Меняем значение notifications для пользователя с определенным tg_id
    cursor.execute(f"UPDATE users SET notifications = {notifications} WHERE tg_id = ?", (id,))
    base.commit()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall() 
    print(users)
    cursor.close()
    base.close()

def job_function():
    # Подключение к БД
    base = sqlite3.connect('schedule_bot.db')
    cursor = base.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall() 
    for user in users:
        user_id = user[1]
        user_name = user[2]
        user_class = user[3]
        text = text_notification(user_class, user_name)
        if (user[4] == 1):
            send_notification(user_id, text)

def text_notification(user_class, user_name):
    current_day_of_week = datetime.datetime.today().weekday()
    tomorrow = ''
    if current_day_of_week == 0: # Понедельник
        tomorrow = DAYS[1]
    elif current_day_of_week == 1: # Вторник
        tomorrow = DAYS[2]
    elif current_day_of_week == 2: # Среда
        tomorrow = DAYS[3]
    elif current_day_of_week == 3: # Четверг
        tomorrow = DAYS[4]
    elif current_day_of_week == 4: # Пятница
        tomorrow = DAYS[5]
    else:
        tomorrow = DAYS[0]
    weekday_arr = schedule[user_class][tomorrow]
    info = ''
    for el in weekday_arr:
            info += f''' 
                        {el["time"]}  {el["lesson"]}
                    '''    
    result_text = f'''
                    👋🏫 Пора собираться в школу, {user_name}! 
                    Напоминаю, что расписание занятий на завтра 📚: 
                    {info}
                    Вперед к знаниям💪 Хорошего дня! 🙌🍀✨

                '''
    return result_text


def send_notification(user_id, text):
    bot.send_message(user_id, text=text)

# Инициализация планировщика
scheduler = BackgroundScheduler()
# Задаем временную зону (например, Европейское/Московское время)
scheduler.configure(timezone=timezone('Europe/Moscow'))

# Расписание на будние дни
scheduler.add_job(job_function, 'cron', day_of_week='mon-fri', hour=17, minute=37)
# В этом примере, уведомление будет отправлено каждый будний день в 10:00 по московскому времени

# Запуск планировщика
scheduler.start()


bot.polling(none_stop=True, interval=0)

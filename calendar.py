import datetime
from dates import *


def fa20_calendar():
    startdate = datetime.date(2020, 8, 24)
    enddate = datetime.date(2020, 12, 18)
    delta = enddate - startdate

    weeknum = 0
    for i in range(delta.days):
        t = startdate + datetime.timedelta(days=i)

        fmt = "{W}:: [[%B {S}, %Y]]"
        weekday = dayNameFromWeekday(t.weekday())
        d1 = (
            t.strftime(fmt)
            .replace("{S}", str(t.day) + suffix(t.day))
            .replace("{W}", weekday)
        )

        fmt = "[[%B {S}, %Y]]"
        d2 = t.strftime(fmt).replace("{S}", str(t.day) + suffix(t.day))

        if t.weekday() == 0:
            print(f"[[Fa20 Week {weeknum}]]", "{{[[kanban]]}}")
            weeknum += 1

        print("	", d1)
        print(
            "		",
            "{{[[query]]: {and: [[t]] [[Berkeley]] [[Fa20]] {or: #date #due}",
            d2,
            "{not:{or: #query #depreciated}} } }}",
        )


def get_calendar():
    startdate = datetime.date(2021, 8, 24)
    enddate = datetime.date(2021, 12, 18)
    delta = enddate - startdate

    for i in range(delta.days):
        t = startdate + datetime.timedelta(days=i)
        weekday = t.weekday()
        blanks = weekday * "    "

        fmt = "[[%B {S}, %Y]]"
        d = t.strftime(fmt).replace("{S}", str(t.day) + suffix(t.day))

        # print(blanks + d + "\n" + "test")
        # print(
        #     blanks
        #     + d
        #     + "{{[[query]]: {or: #date #due}"
        #     + d
        #     + "{not:{or: #query #depreciated}} } }}"
        # )


def yearly_calendar(year):
    startdate = datetime.date(year, 1, 1)
    enddate = datetime.date(year, 12, 31)
    delta = enddate - startdate

    for i in range(delta.days):
        fmt = "{W}: [[%B {S}, %Y]]"
        t = startdate + datetime.timedelta(days=i)
        d = custom_strftime(fmt, t)
        print(d)
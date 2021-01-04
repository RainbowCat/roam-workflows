import datetime
from dates import *


def retro_dates():
    today = datetime.date.today()
    retros = [
        custom_strftime("%B {S}, %Y", today - datetime.timedelta(weeks=i))
        for i in [1, 4, 12]
    ]
    retros.append(custom_strftime("%B {S}, %Y", today - datetime.timedelta(days=365)))
    return retros


def academic_calendar(startdate, enddate, semester):
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
            "{{[[query]]: {and: [[t]] [[Berkeley]] "
            + f"[[{semester}]]"
            + " {or: #date #due}",
            d2,
            "{not:{or: #query #depreciated}} } }}",
        )


def fa20_calendar():
    startdate = datetime.date(2020, 8, 24)
    enddate = datetime.date(2020, 12, 18)
    return academic_calendar(startdate, enddate)


def get_calendar(startdate, enddate, with_weekdays):
    fmt = "{W}: [[%B {S}, %Y]]" if with_weekdays else "[[%B {S}, %Y]]"
    delta = enddate - startdate

    for i in range(delta.days):
        t = startdate + datetime.timedelta(days=i)
        d = custom_strftime(fmt, t)
        print(d)


def yearly_calendar(year, with_weekdays):
    fmt = "{W}: [[%B {S}, %Y]]" if with_weekdays else "[[%B {S}, %Y]]"
    startdate = datetime.date(year, 1, 1)
    enddate = datetime.date(year, 12, 31)
    delta = enddate - startdate

    for i in range(delta.days):
        t = startdate + datetime.timedelta(days=i)
        if t.day == 1:
            print(f"[[{t.strftime('%B')}]]")
            print(f"[[Week {t.isocalendar()[1]}]]")  # TODO add indents for Roam?
        elif t.weekday() == 1:
            print(f"[[Week {t.isocalendar()[1]}]]")  # TODO add indents for Roam?
        d = custom_strftime(fmt, t)
        print(d)  # TODO add indents for Roam?

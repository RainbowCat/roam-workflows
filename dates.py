import datetime


def suffix(d):
    return "th" if 11 <= d <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(d % 10, "th")


def custom_strftime(fmt, t):
    weekday = dayNameFromWeekday(t.weekday())
    return (
        t.strftime(fmt)
        .replace("{S}", str(t.day) + suffix(t.day))
        .replace("{W}", weekday)
    )


def dayNameFromWeekday(weekday):
    if weekday == 0:
        return "Mon"
    if weekday == 1:
        return "Tue"
    if weekday == 2:
        return "Wed"
    if weekday == 3:
        return "Thu"
    if weekday == 4:
        return "Fri"
    if weekday == 5:
        return "Sat"
    if weekday == 6:
        return "Sun"


def calculate_retro_dates():
    today = datetime.date.today()
    retros = [
        custom_strftime("%B {S}, %Y", today - datetime.timedelta(weeks=i))
        for i in [1, 4, 12]
    ]
    retros.append(custom_strftime("%B {S}, %Y", today - datetime.timedelta(days=365)))
    return retros


def list_dates_from_today(num, shift=0, with_weekdays=True):
    today = datetime.date.today() + datetime.timedelta(days=shift)
    dates = []
    for i in range(num):
        t = today + datetime.timedelta(days=i)
        if with_weekdays:
            fmt = "{W}:: [[%B {S}, %Y]]"
        else:
            fmt = "[[%B {S}, %Y]]"
        d = custom_strftime(fmt, t)
        dates.append(d)
    return dates

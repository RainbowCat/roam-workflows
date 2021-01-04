import datetime


def suffix(d):
    return "th" if 11 <= d <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(d % 10, "th")


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


def get_dates(startdate, enddate):
    dates = []
    delta = startdate - enddate
    for i in range(delta.days):
        t = startdate + datetime.timedelta(days=i)
        dates.append(t)
    return dates


def get_dates_from_today(shift):
    return get_dates(
        datetime.date.today(), datetime.timedelta(days=shift)
    )  # TODO fix negative shifts


def custom_strftime(fmt, t):
    weekday = dayNameFromWeekday(t.weekday())
    return (
        t.strftime(fmt)
        .replace("{S}", str(t.day) + suffix(t.day))
        .replace("{W}", weekday)
    )
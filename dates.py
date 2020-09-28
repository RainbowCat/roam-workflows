import sys
import datetime

def suffix(d):
    return "th" if 11 <= d <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(d % 10, "th")

def custom_strftime(fmt, t):
	weekday = dayNameFromWeekday(t.weekday())
	return t.strftime(fmt).replace("{S}", str(t.day) + suffix(t.day)).replace("{W}", weekday)

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

def list_dates(num):
	today = datetime.date.today()
	dates = []
	for i in range(num):
		date = today + datetime.timedelta(days=i)
		fmt = "{W}:: [[%B {S}, %Y]]"
		dates.append(custom_strftime(fmt, date))
	return dates

def main():
	num = int(sys.argv[1])
	for date in list_dates(num):
		print(date)

if __name__ == "__main__":
	main()
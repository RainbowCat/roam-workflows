import sys
import datetime

def suffix(d):
    return "th" if 11 <= d <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(d % 10, "th")

def custom_strftime(fmt, t):
	print(fmt)
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

def list_dates(num, with_weekdays=True):
	today = datetime.date.today()
	dates = []
	for i in range(num):
		t = today + datetime.timedelta(days=i)
		if with_weekdays:
			fmt = "{W}:: [[%B {S}, %Y]]"
			weekday = dayNameFromWeekday(t.weekday())
			d = t.strftime(fmt).replace("{S}", str(t.day) + suffix(t.day)).replace("{W}", weekday)
			dates.append(d)
		else:
			fmt = "[[%B {S}, %Y]]"
			d = t.strftime(fmt).replace("{S}", str(t.day) + suffix(t.day))
			dates.append(d)
	return dates

def main():
	num = int(sys.argv[1])
	with_weekdays = True
	if len(sys.argv) == 3:
		with_weekdays = int(sys.argv[2]) != 0
	for date in list_dates(num, with_weekdays):
		print(date)

if __name__ == "__main__":
	main()




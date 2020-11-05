import sys
import datetime
import func


def suffix(d):
    return "th" if 11 <= d <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(d % 10, "th")


def custom_strftime(fmt, t):
    return t.strftime(fmt).replace("{S}", str(t.day) + suffix(t.day))


def calculate_dates(day_shifts):
    today = datetime.date.today()
    dates = [
        custom_strftime("%B {S}, %Y", today - datetime.timedelta(days=i))
        for i in day_shifts
    ]
    return dates


def generate_template():
    day_shifts = [0, -1, -3, -30]
    dates = calculate_dates(day_shifts)
    today, yesterday, three_days, month_ago = dates[0], dates[1], dates[2], dates[3]
    template = """
[[@not done]]
	\{\{[[query]]: \{and: [[TODO]] [[TODAY 😎]] \{not: \{or: #inbox #workflow #waiting #nibble #query\}\} \{between: [[{three_days}]] [[{yesterday}]]\} \} \}\}
	\{\{[[query]]: \{and: [[TODO]] #s \{not: {or: [[TODAY 😎]] #dw [[query]]\}} \{between: [[\{month_ago}]] [[\{yesterday}]]\} \} \}\}
[[@scheduled]]
	\{\{[[query]]: \{and: #s [[{today}]]\} \}\}
[[@priority]]
	\{\{[[query]]: \{and: [[tomorrow's priority]] [[{today}]]\}\}\}
[[TODAY 😎]]
    """.format(
        today=today,
        yesterday=yesterday,
        three_days=three_days,
        month_ago=month_ago,
    )
    return template

if __name__ == "__main__":
	s = generate_template()
	sys.stdout.write(s)
    # day_shifts = [0, 1, 3, 30]
    # dates = calculate_dates(day_shifts)
    # for i in dates:
    # 	print(i)

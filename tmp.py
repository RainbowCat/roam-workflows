import sys
import datetime

def printWeeks():
	for i in range(1, 53):
		print(f"[[Week {i}]]")

def printDays():
	for i in range(1, 32):
		print(f"[[{i}]]")

def suffix(d):
    return "th" if 11 <= d <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(d % 10, "th")


def custom_strftime(fmt, t):
    return t.strftime(fmt).replace("{S}", str(t.day) + suffix(t.day))


def calculate_retro_dates():
    today = datetime.date.today()
    retros = [
        custom_strftime("%B {S}, %Y", today - datetime.timedelta(weeks=i))
        for i in [1, 4, 12]
    ]
    retros.append(custom_strftime("%B {S}, %Y", today - datetime.timedelta(days=365)))
    return retros

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
    tab = "\t"
    nl = "\r"
    a = "and"
    template = r"""
[[@not done]]
	{{[[query]]: {and: [[TODO]] [[TODAY 😎]] {not: {or: #inbox #workflow #waiting #nibble #query}} {between: [[{three_days}]] [[{yesterday}]]\} } }}
	{{[[query]]: {and: [[TODO]] #s {not: {or: [[TODAY 😎]] #dw [[query]]\}} \{between: [[\{month_ago}]] [[\{yesterday}]]\} \} \}\}
[[@scheduled]]
	{{[[query]]: \{and: #s [[{today}]]\} \}\}
[[@priority]]
	\{\{[[query]]: \{and: [[tomorrow's priority]] [[{today}]]\}\}\}
[[TODAY 😎]]
    """.format(
        today=today,
        yesterday=yesterday,
        three_days=three_days,
        month_ago=month_ago,
    )
    template = "[[@not done]]" + nl + tab + f"{{[[query]]: {and: [[TODO]] [[TODAY 😎]] {not: {or: #inbox #workflow #waiting #nibble #query}} {between: [[{three_days}]] [[{yesterday}]]\} } }}"
    return template

def calendar():
	fa20_start = datetime.date(2020, 8, 25)
	fa20_end = datetime.date(2020, 12, 18)
	for 
if __name__ == "__main__":
	s = generate_template()
	sys.stdout.write(s)

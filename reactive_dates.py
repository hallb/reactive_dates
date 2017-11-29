from datetime import timedelta as td


def monthly(day, r):
    return filter(monthlyL(day), daily(r))


def monthlyL(day_of_month=1):
    return lambda dt: dt.day == day_of_month


def onL(day):
    return lambda dt: dt == day


def orL(p1, p2):
    return lambda dt: p1(dt) or p2(dt)


def andL(p1, p2):
    return lambda dt: p1(dt) and p2(dt)


def before(day):
    return lambda dt: dt < day


def after(day):
    return lambda dt: dt > day


def weekly(start_day, r):
    return filter(weeklyL(start_day), daily(r))


def weeklyL(startday):
    return every_x_days(startday, 7)


def annuallyL(startday):
    return every_x_years(startday, 1)


def fortnightlyL(startday):
    return every_x_days(startday, 14)


def every_x_days(startday, x):
    return lambda dt: (dt - startday).days % x == 0


def every_x_years(startday, x):
    return lambda dt: dt.month == startday.month and dt.day == startday.day and (dt.year - startday.year) % x == 0


def daily(r):
    f, t = r
    return [f + td(days=x) for x in range((t - f).days + 1)]

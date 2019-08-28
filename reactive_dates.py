from datetime import timedelta, date
from typing import Callable, Tuple, Iterator

DatePredicate = Callable[[date], bool]
DateIterator = Iterator[date]
DateRange = Tuple[date, date]


def monthly(day: int, r: DateRange) -> DateIterator:
    return filter(monthlyL(day), daily(r))


def monthlyL(day_of_month: int = 1) -> DatePredicate:
    return lambda dt: dt.day == day_of_month


def onL(day: date) -> DatePredicate:
    return lambda dt: dt == day


def orL(p1: DatePredicate, p2: DatePredicate) -> DatePredicate:
    return lambda dt: p1(dt) or p2(dt)


def andL(p1: DatePredicate, p2: DatePredicate) -> DatePredicate:
    return lambda dt: p1(dt) and p2(dt)


def before(day: date) -> DatePredicate:
    return lambda dt: dt < day


def after(day: date) -> DatePredicate:
    return lambda dt: dt > day


def weekly(start_day: date, r) -> DateIterator:
    return filter(weeklyL(start_day), daily(r))


def weeklyL(start_day: date) -> DatePredicate:
    return every_x_days(start_day, 7)


def annuallyL(start_day: date) -> DatePredicate:
    return every_x_years(start_day, 1)


def fortnightlyL(start_day: date) -> DatePredicate:
    return every_x_days(start_day, 14)


def every_x_days(start_day: date, x: int) -> DatePredicate:
    return lambda dt: (dt - start_day).days % x == 0


def every_x_years(start_day: date, x: int) -> DatePredicate:
    return lambda dt: dt.month == start_day.month and dt.day == start_day.day and (dt.year - start_day.year) % x == 0


def daily(date_range: DateRange) -> DateIterator:
    date_from, date_to = date_range
    current_date = date_from + timedelta(-1)
    while current_date < date_to:
        current_date = current_date + timedelta(1)
        yield current_date

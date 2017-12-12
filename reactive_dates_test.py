import reactive_dates
import unittest
from datetime import date as d


class TestDateFunction(unittest.TestCase):

    def test_monthly(self):
        r = (d(2012, 1, 1), d(2013, 1, 1))
        actual = list(reactive_dates.monthly(15, r))
        expected = [
            d(2012, 1, 15),
            d(2012, 2, 15),
            d(2012, 3, 15),
            d(2012, 4, 15),
            d(2012, 5, 15),
            d(2012, 6, 15),
            d(2012, 7, 15),
            d(2012, 8, 15),
            d(2012, 9, 15),
            d(2012, 10, 15),
            d(2012, 11, 15),
            d(2012, 12, 15)]
        self.assertEqual(actual, expected)

    def test_daily(self):
        r = (d(2012, 1, 1), d(2012, 1, 3))
        actual = reactive_dates.daily(r)
        expected = [
            d(2012, 1, 1),
            d(2012, 1, 2),
            d(2012, 1, 3)]
        self.assertEqual(actual, expected)

    def test_weekly(self):
        r = (d(2011, 12, 31), d(2012, 2, 1))
        actual = list(reactive_dates.weekly(d(2012, 1, 1), r))
        expected = [
            d(2012, 1, 1),
            d(2012, 1, 8),
            d(2012, 1, 15),
            d(2012, 1, 22),
            d(2012, 1, 29),
        ]
        self.assertEqual(actual, expected)

    def test_or(self):
        r = (d(2011, 12, 31), d(2012, 1, 14))
        actual_or_p = reactive_dates.orL(
            reactive_dates.weeklyL(d(2012, 1, 1)),
            reactive_dates.weeklyL(d(2012, 1, 3)))
        actual = list(filter(actual_or_p, reactive_dates.daily(r)))
        expected = [
            d(2012, 1, 1),
            d(2012, 1, 3),
            d(2012, 1, 8),
            d(2012, 1, 10)]
        self.assertEqual(actual, expected)

    def test_on(self):
        r = (d(2011, 12, 31), d(2012, 1, 14))
        actual_on_p = reactive_dates.onL(d(2012, 1, 1))
        actual = list(filter(actual_on_p, reactive_dates.daily(r)))
        expected = [d(2012, 1, 1)]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()

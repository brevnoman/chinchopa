import unittest
class Mathematician:

    def __init__(self):
        pass

    @staticmethod
    def square_nums(num_list):
        result = []
        try:
            for i in num_list:
                i = int(i ** 2)
                result.append(i)

        except ValueError:
            return "you can use only nums"
        return f"{result}"

    @staticmethod
    def remove_positives(num_list):
        result = []
        for i in num_list:
            if int(i) < 0:
                result.append(i)
        return f"{result}"

    @staticmethod
    def filter_leaps(num_num_list):
        result = []
        for year in num_num_list:
            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                result.append(year)
        return f"{result}"


years = Mathematician()
print(years.remove_positives([-12, 2000, 1990, 1900, 2002]))
print(years.filter_leaps([-12, 2000, 1990, 1900, 2002]))
print(years.square_nums([-12, 2000, 1990, 1900, 2002]))


class TestMathematician(unittest.TestCase):
    def test_square_nums(self):
        self.assertEqual(years.square_nums([-12, 2000, 1990, 1900, 2002]), "[144, 4000000, 3960100, 3610000, 4008004]")

    def test_remove_positives(self):
        self.assertEqual(years.remove_positives([-12, 2000, 1990, 1900, 2002]), "[-12]")

    def test_filter_leaps(self):
        self.assertEqual(years.filter_leaps([-12, 2000, 1990, 1900, 2002]), "[-12, 2000]")

    def test_square_nums_neg(self):
        self.assertFalse(years.square_nums([-12, 2000, 1990, 1900, 2002]) == "[14, 400000, 396010, 361000, 400800]")

    def test_remove_positives_neg(self):
        self.assertFalse(years.remove_positives([-12, 2000, 1990, 1900, 2002]) == "[2000, 1990, 1900, 2002]")

    def test_filter_leaps_neg(self):
        self.assertFalse(years.filter_leaps([-12, 2000, 1990, 1900, 2002]) == "[1990, 1900, 2002]")
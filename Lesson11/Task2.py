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
        return result

    @staticmethod
    def remove_positives(num_list):
        result = []
        for i in num_list:
            if int(i) < 0:
                result.append(i)
        return result

    @staticmethod
    def filter_leaps(num_num_list):
        result = []
        for year in num_num_list:
            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                result.append(year)
        return result


years = Mathematician()
print(years.remove_positives([-12, 2000, 1990, 1900, 2002]))
print(years.filter_leaps([-12, 2000, 1990, 1900, 2002]))
print(years.square_nums([-12, 2000, 1990, 1900, 2002]))


class Mathematician:

    @staticmethod
    def square_nums(num_list):
        result = []
        try:
            for i in num_list:
                i = i ** 2
                result.append(i)
            return result
        except (ValueError, TypeError):
            print("you can use only nums")
            pass




    @staticmethod
    def remove_positives(num_list):
        result = []
        try:
            for i in num_list:
                if i < 0:
                    result.append(i)
            return result
        except (ValueError, TypeError):
            print("you can use only nums")
            pass
    @staticmethod
    def filter_leaps(num_list):
        result = []
        try:
            for year in num_list:
                if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                    result.append(year)
            return result
        except (ValueError, TypeError):
            print("you can use only nums")
            pass

years = Mathematician()
print(years.remove_positives([-12, 2000, 1990, 1900, 2002]))
print(years.filter_leaps([-12, 2000, 1990, 1900, 2002]))
print(years.square_nums([-12, 2000, 1990, 1900, 2002]))
print(years.remove_positives([-12, 2000, 1990, 1900, "jopa"]))
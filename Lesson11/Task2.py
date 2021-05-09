class Mathematician:

    def __init__(self, list):
        self.list = list

    def square_nums(self):
        result = []
        try:
            for i in self.list:
                i = int(i ** 2)
                result.append(i)

        except ValueError:
            return "you can use only nums"
        print(result)

    def remove_positives(self):
        result = []
        for i in self.list:
            if int(i) < 0:
                result.append(i)
        print(result)

    def filter_leaps(self):
        result = []
        for year in self.list:
            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                result.append(year)
        print(result)


years = Mathematician([-12, 2000, 1990, 1900, 2002])
years.remove_positives()
years.filter_leaps()
years.square_nums()

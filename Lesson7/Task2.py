
def main():
    country = input("name the country\n")
    capital = input(f"name {country} country capital?\n")
    countries = {}
    make_country(country, capital, countries)
    want_out()


def make_country(country, capital, countries):
    countries.setdefault(country, capital)
    if capital != countries[country]:
        while True:
            want_change = input(f"last time you said it was {countries[country]}, do you want to change it?")
            if want_change == "yes":
                countries[country] = capital
                break
            elif want_change == "no":
                print("ok")
                break
            else:
                print('you should choose only from "yes" or "no"')
    print(countries)


def want_out():
    while True:
        choose = input("Want you start over?(yes/no)")
        if choose == 'yes':
            main()
            break
        elif choose == 'no':
            print("bye")
            break
        else:
            print('You can use only "yes" or "no"')


main()

#
# countries={}
#
#
# def make_country(country, capital):
#     upper_country = country[0].upper() + country[1:]
#     upper_capital=capital[0].upper() + capital[1:]
#     countries.setdefault(upper_country, upper_capital)
#     if capital != str(countries[upper_country]).lower():
#         while True:
#             want_change = input(f"last time you said it was {countries[upper_country]}, do you want to change it?")
#             if want_change == "yes":
#                 countries[upper_country] = upper_capital
#                 break
#             elif want_change == "no":
#                 print("ok")
#                 break
#             else:
#                 print('you should choose only from "yes" or "no"')
#
#
# def want_out():
#     while True:
#         choose = input("Want you start over?(yes/no)")
#         if choose == 'yes':
#             main()
#             break
#         elif choose == 'no':
#             print("bye")
#             break
#         else:
#             print('You can use only "yes" or "no"')
#
#
# def main():
#     country = input("name the country\n").lower()
#     capital = input(f"name {country[0].upper() + country[1:]} capital?\n").lower()
#     make_country(country, capital)
#     print(countries)
#     want_out()
#
#
# main()

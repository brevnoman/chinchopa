
countries={}

def make_country():
    country = input("name the country\n")
    capital = input(f"name {country} country capital?\n")
    countries.setdefault(country, capital)
    if capital!= countries[country]:
        while True:
            want_change=input(f"last time you said it was {countries[country]}, do you want to change it?")
            if want_change=="yes":
                countries[country]=capital
                break
            elif want_change=="no":
                print("ok")
                break
            else:
                print('you should choose only from "yes" or "no"')

def want_out():
    while True:
        choise=input("Want you start over?(yes/no)")
        if choise == 'yes':
            main()
            break
        elif choise == 'no':
            print("bye")
            break
        else:
            print('You can use only "yes" or "no"')

def main():
    make_country()
    print(countries)
    want_out()

main()



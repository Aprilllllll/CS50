def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dollars = input("How much was the meal? ")
    dollars = dollars.replace('$','')
    dollars = int(dollars)


def percent_to_float(p):
    int(input("What percentage would you like to tip?))
    # TODO


main()

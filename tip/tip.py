def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    

#def dollars_to_float(d):
    #dollars_input = input("How much was the meal? ")
    #dollars_clean = dollars_input.replace('$','')
    #dollars_to_float = int(dollars_clean)


def percent_to_float(p):
    percent_string = input("What percentage would you like to tip? ")
    percent_string_clean = percent_string.strip('%')
    percent_int = int(percent_string_clean)
    percent_to_float = percent_int/100
    # TODO


main()

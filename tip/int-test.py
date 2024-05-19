percent_string = input("What percentage would you like to tip? ")
percent_string_clean = percent_string.strip('%')
percent_int = int(percent_string_clean)
percent_float = percent_int/100

print(percent_float)

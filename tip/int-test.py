percent_string = input("What percentage would you like to tip? ")
percent_float = percent_string.strip('%')
percent = int("{:.2%}".format(percent))

print(percent)

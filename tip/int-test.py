percent = input("What percentage would you like to tip? ")
percent = percent.replace('%','')
percent = int("{:.0%}".format(percent))

print(percent)

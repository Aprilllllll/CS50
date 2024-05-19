percent = input("What percentage would you like to tip? ")
percent = percent.replace('%','')
percent = int("{:.2%}".format(percent))

print(percent)

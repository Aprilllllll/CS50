#greeting input
user_greeting=input("Greeting?")
#convert to clean string
clean_string=[user_greeting.strip().lower()]

#do match
if clean_string == "hello":
    print("$0")
elif clean_string[0] == "h":
        print("$20")
else:
    print("$100")

#pring result

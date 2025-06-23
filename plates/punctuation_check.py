import string

check_context=input("Pls input string: ")

def punctuation_check(check_context):
    for char in check_context:
        if char in string.punctuation:
            return True
    return False

has_punct = punctuation_check(check_context)

if has_punct:
    print("There is punc")
else:
    print("No punc")


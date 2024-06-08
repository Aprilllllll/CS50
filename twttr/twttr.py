str_input = str(input(""))
remove_vowels = "aeiouAEIOU"

def rm_vowels():
    for a in str_input:
        if a in remove_vowels:
            print('_', end="")
        else:
            print(a, end="")

rm_vowels()

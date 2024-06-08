str_input = str(input(""))
remove_vowels = "aeiouAEIOU"
return_word
def rm_vowels():
    for a in str_input:
        if a in remove_vowels:
            return_word += a
        else:
            print(a, end="")

rm_vowels()

str_input = str(input("Input: "))

def rm_vowels(str_input):
    remove_vowels = "aeiouAEIOU"
    return_word = ""
    for a in str_input:
        if a not in remove_vowels:
            return_word += a
    return return_word

print("Output: " + rm_vowels(str_input))


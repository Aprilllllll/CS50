str_input = input("")

def rm_vowels():
    for a in str(str_input):
        if a in ['a''e''i''o''u''A''E''I''O''U']:
            print('_', end="")
        else:
            print(a, end="")

rm_vowels()

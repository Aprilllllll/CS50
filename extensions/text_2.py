

input_sentence=input("sentence?")
input_symbol=input("symbol?")


def remove_before_symbol(t, s):
    before, sep, after = t.partition(s)
    return before

result=remove_before_symbol(input_sentence,input_symbol)

print(result)

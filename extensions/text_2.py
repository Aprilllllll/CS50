

input_sentence=input("sentence?")
input_symbol=input("symbol?")

result=remove_before_symbol(input_sentence,input_symbol)
def remove_before_symbol(t, s):
    before, sep, after = t.partition(s)
    return before

print(result)

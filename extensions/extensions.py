#clear input to all lowercase string
user_input=input("File name:")



#only leave extension name
clean_string=user_input.strip().lower()

def remove_before_dot(t, s):
    before, sep, after = t.partition(s)
    return after

symbol="."

extension=remove_before_dot(clean_string, ".")

print(extension)
#do match



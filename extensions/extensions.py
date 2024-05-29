#clear input to all lowercase string
user_input=input("File name: ")

#function that take extension name
clean_string=user_input.strip().lower()

def remove_before_dot(t, s):
    before, sep, after = t.partition(s)
    return after

#match extension
extension=remove_before_dot(clean_string, ".")
output_set={'gif', 'jpg', 'jpeg', 'png', 'pdf', 'txt', 'zip'}

if extension in output_set:



    print("supported")
else:
    print("application/octet-stream")



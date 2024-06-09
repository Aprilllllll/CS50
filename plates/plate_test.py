import string

#def main():
#    plate = input("Plate: ")
#    if is_valid(plate):
#        print("Valid")
#    else:
#        print("Invalid")

def is_valid(s):
    result_count = 0
    while result_count < 5:
        if s[0:1].isalpha():
            result_count += 1
            print("start with at least 2 letters")
        if 2 <= len(s) <= 5:
            result_count += 1
            print("correct length")
        #if len(s) > 2:
        if s[1:-1].isalpha():
            result_count += 1
            print("no number in the middle")
        if punctuation_check(s):
            result_count +=1
            print("no punctuation")
    if result_count == 4:
        print(result_count + "All Passed")

def punctuation_check(check_context):
    for char in check_context:
        if char in string.punctuation:
            return True
        
input_plate = input("Plate: ")
is_valid(input_plate)

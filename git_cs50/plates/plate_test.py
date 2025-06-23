#check all condition, even if one of then does not satisfied

import string

#def main():
#    plate = input("Plate: ")
#    if is_valid(plate):
#        print("Valid")
#    else:
#        print("Invalid")

def is_valid(s):
    result_count = 0
    if s[0:2].isalpha():
        result_count += 1
        print("start with at least 2 letters")
    else:
        print("wrong starter")
    if 2 <= len(s) <= 6:
        result_count += 1
        print("correct length")
    else:
        print("wrong length")
    if check_num_location(s):
        result_count +=1
        print("correct number location")
    else:
        print("wrong number location")
    if punctuation_check(s):
        result_count +=1
        print("no punctuation")
    else:
        print("punct found")
    print(str(result_count))
    if result_count == 4:
        return True
    else:
        return False

#function to check number location
def check_num_location(check_context):
    number_started = False
    for char in check_context:
        if not number_started:
            if char == '0':
                return False
        if char.isdigit():
            number_started = True
        if number_started and char.isalpha():
            return False
    return True

#function to check punctuation
def punctuation_check(check_context):
    for char in check_context:
        if char in string.punctuation:
            return False
    else:
        return True

input_plate = input("Plate: ")

if is_valid(input_plate):
    print("Valid plate")
else:
    print("Invalid plate, see above result")

#this is completed

import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    result_count = 0
    while result_count < 5:
        if s[0:1].isalpha():
            result_count += 1
        if 2 <= len(s) <= 5:
            result_count += 1
        if len(s) > 2:
            if s[1:-1].isalpha():
                result_count += 1
        else:
            result_count += 1
        if for char in s:
            char not in string.puncuation:
            result_count +=1
    if result_count == 5:
        return True






main()

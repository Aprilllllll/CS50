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
        if 



main()

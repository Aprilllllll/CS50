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

check_context = input("Pls input plate: ")

if check_num_location(check_context):
    print("Pass!")
else:
    print("Failed!")

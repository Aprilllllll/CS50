menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    _total_ = 0.00
    try:
        while True:
            user_order = input("Item: ")
            insensitive_order = user_order.title()
            if insensitive_order in menu:
                _total_ += menu[insensitive_order]
                print(f"${_total_:.2f}")
    except EOFError:
        print()
main()

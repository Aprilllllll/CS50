grocery = [
    "milk", "mango", "strawberry", "sweet potato", "tortilla", "sugar", "ice cream", "apple", "banana"
]

def main():
    totals = {item: 0 for item in grocery}
    try:
        while True:
            user_input = input().lower()
            if user_input in grocery:
                totals[user_input] += 1
    except EOFError:
        for item, count in totals.items():
            if count > 0:
                print(f"{count} {item.upper()}")

main()


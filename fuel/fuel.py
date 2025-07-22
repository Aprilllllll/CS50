def split(fraction_str):
    numerator, denominator = fraction_str.split("/")
    X = float(numerator)
    Y = float(denominator)
    if not X >= 0:
        raise ValueError
    if not Y >= 0:
        raise ValueError
    if not X.is_integer():
        raise ValueError
    if not Y.is_integer():
        raise ValueError
    if not Y >= X:
        raise ValueError
    return X, Y

def get_fraction(X,Y):
    fraction = X / Y
    guard = round(fraction*100)
    return guard

def main():
    while True:
        fraction_input = input("Please input fraction: ")
        try:
            X, Y = split(fraction_input)
            result = get_fraction(X, Y)
            break
        except (ValueError, ZeroDivisionError):
            continue

    if result >= 99:
        print("F")
    elif result <= 1:
        print("E")
    else:
        print(f"{result}%")

main()

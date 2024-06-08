def coke_machine():
    total_paid = 0
    while total_paid < 50:
      coin = int(input("Insert Coin: "))
      if coin in [5, 15, 20]:
        total_paid += coin
        if total_paid < 50:
            print(f"Amount Due: {50 - total_paid}")
      else:
        print(f"Amount Due: {50 - total_paid}")

    if total_paid > 50:
       print(f"Change Owed: {total_paid - 50}")
coke_machine()

amount_due = 50

while amount_due > 0:
    print(f"Amount Due: {amount_due}")  
    coin = input("Insert Coin: ")

    if coin in ["5", "10", "25"]:
        amount_due -= int(coin)

print(f"Change Owed: {abs(amount_due)}")

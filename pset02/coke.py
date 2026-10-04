# insert coin
# if less then 50 remaining
# if 50 or more amount owed

price = 50
coin = 0
while True:
    if price-coin>0:
        print(f"Amount Due: {price-coin}")
        c = int(input("Insert Coin : "))
        if c==25 or c==10 or c==5:
            coin+=c
    else:
        print(f"Change Owed: {coin-price}")
        break




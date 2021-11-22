nrow = int(input())
food = int(input())
total = int()
amount0 = int()

for i in range(nrow):
    amount = int(input())
    price = int(input())
    if food <= amount:
        total = total + (food - amount0) * price
        break
    else:
        total = total + (amount - amount0) * price
    amount0 = amount

print(total)
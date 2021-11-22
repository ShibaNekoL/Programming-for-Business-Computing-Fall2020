food = int(input())
amount1 = int(input())
price1 = int(input())
amount2 = int(input())
price2 = int(input())
amount3 = int(input())
price3 = int(input())

if food <= amount1:
    total = food * price1
elif amount1 < food <= amount2:
    total = amount1 * price1 + (food - amount1) * price2
elif amount2 < food <= amount3:
    total = amount1 * price1 + (amount2 - amount1) * price2 + (food - amount2) * price3

print(total)
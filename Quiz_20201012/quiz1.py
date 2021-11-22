
# input
p1 = int(input())
p2 = int(input())
d = int(input())

# calculate
price = p1 + p2 - d

# output
if price >= 0:
    print(price)
elif price < 0:
    print(0)
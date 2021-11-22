# input
line1 = input()
line2 = input()


# split to list
ppdn = line1.split(",")
xlist = line2.split(",")

# str to int

for i in range(len(ppdn)):
    ppdn[i] = int(ppdn[i])

for i in range(len(xlist)):
    xlist[i] = int(xlist[i])


# 只買便當不買飲料，則 xi=1；若只買飲料不買便當，則 xi=2；若兩者都買，則 xi=3。

# count
food = xlist.count(1)
drink = xlist.count(2)
both = xlist.count(3)

# price
pfood = ppdn[0]
pdrink = ppdn[1]
pboth = ppdn[0] + ppdn[1] - ppdn[2]

if pboth < 0:
    pboth = 0

price = food * pfood + drink * pdrink + both * pboth


# 輸出便當銷售總個數、飲料銷售總杯數，以及總營業額

totalfood = food + both
totaldrink = drink + both

print(totalfood, totaldrink, price, sep = ",")
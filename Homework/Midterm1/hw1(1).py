# input x1、p1、x2 、p2 、t

stu_num = int(input())
stu_price = int(input())
adult_num = int(input())
adult_price = int(input())
pay = int(input())

price = stu_num * stu_price + adult_num * adult_price

if pay >= price:
    print("$" + str(pay - price))
else:
    print(-1)
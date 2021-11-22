# input x1、p1、x2 、p2 、t

stu_num = int(input())
stu_price = int(input())
adult_num = int(input())
adult_price = int(input())
pay = int(input())
ticket = int(input())

price = stu_num * stu_price + adult_num * adult_price
ticket_buy = stu_num + adult_num

if pay >= price:
    money = "$" + str(pay - price)
else:
    money = -2

if ticket >= ticket_buy:
    ticketleft = ticket - ticket_buy
else:
    ticketleft = -1

print(str(str(ticketleft) + ",") + str(money))
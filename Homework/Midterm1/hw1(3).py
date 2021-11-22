# input x1、p1、x2 、p2 、t

stu_num = int(input())
stu_price = int(input())
adult_num = int(input())
adult_price = int(input())
pay = int(input())
ticket = int(input())

price = stu_num * stu_price + adult_num * adult_price
ticket_buy = stu_num + adult_num

money = int()
ticketleft = int()

if pay >= price:
    money = "$" + str(pay - price)

if ticket >= ticket_buy:
    ticketleft = str(ticket - ticket_buy) + ","

if money != 0:
    if ticketleft != 0:
        print(str(ticketleft) + str(money))
if money == 0:
    if ticketleft != 0:
        print(ticketleft)
if money != 0:
    if ticketleft == 0:
        print(money)
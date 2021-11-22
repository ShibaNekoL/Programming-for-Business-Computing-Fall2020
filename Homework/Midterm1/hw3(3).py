# line 1 input: 級距、購買量
input1 = input()
list_input = input1.split(",")
n = int(list_input[0])
food = int(list_input[1])

# line 2 input: 級距數量、價格
input2 = input()
list_input = input2.split(",")
list_amount = list()
list_price = list()

# 宣告總價、前一級距數量
total = int()
amount0 = int()
amount = int()
price = int()

# 一次跑一個級距
for i in range(n):
    # 讀入list: 級距數量、價格
    amount = int(list_input[i])
    price = int(list_input[i + n])
    # 若購買量<級距數量，則計算最後所剩的價格並跳出迴圈
    if food < amount:
        total = total + (food - amount0) * price
        break
    # 其他情況則計算各級距間價格
    else:
        total = total + (amount - amount0) * price
        amount0 = amount


# 宣告以下迴圈所需變數
list_accamount = list()
list_accprice = list()
accprice = int()
amount0 = int()
amount = int()
price = int()

# 計算各價格之累加總價，若價格非正數，則將總價以及級距數量存入list，因為只有非正數價格才有機會比原先購買量之價格更小
for i in range(n):
    amount = int(list_input[i])
    price = int(list_input[i + n])
    accprice = accprice + (amount - amount0) * price
    amount0 = amount
    if price <= 0 and amount >= food:
        list_accamount.append(amount)
        list_accprice.append(accprice)

# 將原購買價格與數量加到負價格的list裡
list_accprice.append(total)
list_accamount.append(food)

# 排序價格，找出最小值
list_sortedprice = sorted(list_accprice)
minrprice = list_sortedprice[0]

# 用最小價格找出最大購買量所對應之list之順序位置
list_buy = list()
for i in range(len(list_accprice)):
    # 已知最小價格，為了在相同的最小價格中找出最大購買量，故將所有最小價格所對應之購買量存入list_buy
    if minrprice == list_accprice[i]:
        list_buy.append(list_accamount[i])

# 排序購買量，找出最大值
list_realbuy = sorted(list_buy)

# 輸出最大購買量與最小價格，
print(list_realbuy[- 1], minrprice, sep=",")
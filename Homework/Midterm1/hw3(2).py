# input line 1:幾個級距、購買量
input1 = input()
list_input = input1.split(",")
n = int(list_input[0])
food = int(list_input[1])

# input line 2:級距數量、價格
input2 = input()
list_input = input2.split(",")
# 宣告list
list_amount = list()
list_price = list()

# 宣告價格、前一個級距
total = int()
amount0 = int()

# calculate
for i in range(n):

    # 讀入級距數量與價格的list
    amount = int(list_input[i])
    price = int(list_input[i + n])

    # 如果購買量<級距數量->計算購買量與最後一個比購買量小的最大級距數量的價格
    if food <= amount:
        total = total + (food - amount0) * price
        break
    # 其他情況則計算級距數量間價格
    else:
        total = total + (amount - amount0) * price

    # 前一個級距數量
    amount0 = amount

# 輸出價格
print(total)
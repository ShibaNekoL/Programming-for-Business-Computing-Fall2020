# input

line1 = input() # 物品個數與負重上限
line2 = input() # wi 是物品 i 的重量
line3 = input() # vi  是物品 i 的效用
line4 = input() # 是否有帶第 i 個物品

# 物品個數
number = int(line1.split(",")[0])

# 負重上限
limit = int(line1.split(",")[1])

# 重量
list_weight = line2.split(",")
# str to int
for i in range(len(list_weight)):
    list_weight[i] = int(list_weight[i])

# 效用
list_effect = line3.split(",")
# str to int
for i in range(len(list_effect)):
    list_effect[i] = int(list_effect[i])

# 有沒有帶
list_bring = line4.split(",")
# str to int
for i in range(len(list_bring)):
    list_bring[i] = int(list_bring[i])


# 總負重
weight = int()
for i in range(len(list_weight)):
    if list_bring[i] == 1:
        weight = weight + list_weight[i]

# 總效用
effect = int()
for i in range(len(list_effect)):
    if list_bring[i] == 1:
        effect = effect + list_effect[i]

# 判斷是否超過負重 否則印出總負重與總效用 其餘印出-1
if weight <= limit:
    print(weight, effect, sep=",")
else:
    print(-1)
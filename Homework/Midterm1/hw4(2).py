# input

line1 = input() # 物品個數與負重上限
line2 = input() # wi 是物品 i 的重量
line3 = input() # vi  是物品 i 的效用

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

# 計算cp值 r=v/w
list_cp = list()
for i in range(len(list_effect)):
    for j in range(i, i + 1):
        list_cp.append(list_effect[j] / list_weight[i])

# 排序cp值list
list_cp_sort = sorted(list_cp)
list_cp_sort.reverse()

# 把物品編號依照cp值排序
numlist = list()
for i in range(number):
    num = list_cp.index(list_cp_sort[i])
    numlist.append(num)


# 依序檢查能否放入物品
weight = int()
list_number = list()
for i in numlist:
    weight = weight + list_weight[i]
    if weight <= limit:
        list_number.append(i + 1)
    else:
        weight = weight - list_weight[i]


# output
output = str()
list_number.sort()
for i in range(len(list_number)):
    if i == 0:
        output = str(list_number[0])
    elif i < len(list_number):
        output = output + "," + str(list_number[i])
    else:
        output = output + str(list_number[i])
print(output)
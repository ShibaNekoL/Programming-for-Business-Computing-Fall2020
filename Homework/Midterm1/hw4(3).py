# input

line1 = input() # 物品個數與負重上限
line2 = input() # wi 是物品 i 的重量
line3 = input() # vi 是物品 i 的效用

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
# str to int and copy
list_effect3 = list()
for i in range(len(list_effect)):
    list_effect[i] = int(list_effect[i])
    list_effect3.append(list_effect[i])


## 第2題演算法
# 計算cp值 r=v/w
list_cp = list()
for i in range(len(list_effect)):
    for j in range(i, i + 1):
        list_cp.append(list_effect[j] / list_weight[i])

# 排序cp值list
list_cp_sort = sorted(list_cp)
list_cp_sort.reverse()


# 兩樣物品 CP 值相同的話，選比較輕的那個；如果重量還是一樣的話，選編號小的那個

# 把物品編號依照cp值排序
numlist = list()
for i in range(number):
    num = list_cp.index(list_cp_sort[i])
    numlist.append(num)
    list_cp[num] = - 1

# copy 物品編號list以便之後覆寫
newnumlist = list()
for i in numlist:
    newnumlist.append(i)

# 把物品重量依照編號排序
weilist = list()
for i in range(number):
    weilist.append(list_weight[numlist[i]])


# 如果找到兩個一樣cp值的，照重量小sort，如果重量一樣，照編號小sort
samecp_weilist = list()
for i in range(number):
    for j in range(number):
        if i < j and list_cp_sort[i] == list_cp_sort[j]:
            # 把相同cp值的重量抓出來
            samecp_weilist = [weilist[i], weilist[j]]
            if weilist[i] != weilist[j]:
                # sorted比小
                sort_samecp_weilist = sorted(samecp_weilist)
                # 如果和原本的list不同，就要改變照cp值排序的編號順序list
                if sort_samecp_weilist != samecp_weilist:
                    newnumlist[newnumlist.index(numlist[j])] = numlist[i]
                    newnumlist[newnumlist.index(numlist[i])] = numlist[j]
            # 如果重量一樣，照編號sort
            else:
                numbersortedlist = [numlist[i], numlist[j]]
                # sorted比小
                sort_numbersortedlist = sorted(numbersortedlist)
                # 如果和原本的list不同，就要改變照cp值排序的編號順序list
                if sort_numbersortedlist != numbersortedlist:
                    newnumlist[newnumlist.index(numlist[j])] = numlist[i]
                    newnumlist[newnumlist.index(numlist[i])] = numlist[j]


# 依序檢查能否放入物品
weight = int()
list_number = list()
effectnum = list()
for i in newnumlist:
    weight = weight + list_weight[i]
    if weight <= limit:
        list_number.append(i + 1)
        effectnum.append(i)
    else:
        weight = weight - list_weight[i]

# 第2題output
output = str()
list_number.sort()
for i in range(len(list_number)):
    if i == 0:
        output = str(list_number[0])
    elif i < len(list_number):
        output = output + "," + str(list_number[i])
    else:
        output = output + str(list_number[i])


## 第3題演算法
# 當下能讓總效用最大、且不會讓背包過重的物品裝進背包裡
# 兩樣物品效用相同的話，選比較輕的那個；如果重量還是一樣的話，選編號小的那個

# 依照效用大小排序
list_effect_sort = sorted(list_effect)
list_effect_sort.reverse()

# 把物品編號依照效用排序
numlist3 = list()
for i in range(number):
    num = list_effect3.index(list_effect_sort[i])
    numlist3.append(num)
    list_effect3[num] = - 1

# copy 物品編號list以便之後覆寫
newnumlist3 = list()
for i in numlist3:
    newnumlist3.append(i)

# 把物品重量依照編號排序
weilist3 = list()
for i in range(number):
    weilist3.append(list_weight[numlist3[i]])

# 如果找到兩個一樣效用的，照重量小sort，如果重量一樣，照編號小sort
sameeffect_weilist = list()
for i in range(number):
    for j in range(number):
        if i < j and list_effect_sort[i] == list_effect_sort[j]:
            # 把相同效用的重量抓出來
            sameeffect_weilist = [weilist3[i], weilist3[j]]
            if weilist3[i] != weilist3[j]:
                # sorted比小
                sort_sameeffect_weilist = sorted(sameeffect_weilist)
                # 如果和原本的list不同，就要改變照cp值排序的編號順序list
                if sort_sameeffect_weilist != sameeffect_weilist:
                    newnumlist3[newnumlist3.index(numlist3[j])] = numlist3[i]
                    newnumlist3[newnumlist3.index(numlist3[i])] = numlist3[j]

            # 如果重量一樣，照編號sort
            else:
                numbersortedlist3 = [numlist3[i], numlist3[j]]
                # sorted比小
                sort_numbersortedlist3 = sorted(numbersortedlist3)
                # 如果和原本的list不同，就要改變照cp值排序的編號順序list
                if sort_numbersortedlist3 != numbersortedlist3:
                    newnumlist3[newnumlist3.index(numlist3[j])] = numlist3[i]
                    newnumlist3[newnumlist3.index(numlist3[i])] = numlist3[j]

# 依序檢查能否放入物品
weight = int()
list_number3 = list()
effectnum3 = list()
for i in newnumlist3:
    weight = weight + list_weight[i]
    if weight <= limit:
        list_number3.append(i + 1)
        effectnum3.append(i)
    else:
        weight = weight - list_weight[i]

# 第3題output
output3 = str()
list_number3.sort()
for i in range(len(list_number3)):
    if i == 0:
        output3 = str(list_number3[0])
    elif i < len(list_number3):
        output3 = output3 + "," + str(list_number3[i])
    else:
        output3 = output3 + str(list_number3[i])


# 第2題總效用
effect2 = int()
for i in effectnum:
    effect2 += list_effect[i]

# 第3題總效用
effect3 = int()
for i in effectnum3:
    effect3 += list_effect[i]

# output
if effect2 >= effect3:
    print(output)
else:
    print(output3)
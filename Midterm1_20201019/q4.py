line1 = input()

# x  座標上限、y 座標上限,醫院能覆蓋的距離
nmr = line1.split(",")

n = int(nmr[0])
m = int(nmr[1])
r = int(nmr[2])

# 每個位置人口數list
listmn = list()

for i in range(m + 1):
    linem = input()
    listp = linem.split(",")
    for j in range(n + 1):
        listp[j] = int(listp[j])
    listmn.append(listp) # listmn = list[m][n] (y,x)


# 最後所有位置人口數list
plist = list()

# run every position
for u in range(n + 1):
    for v in range(m + 1):
        # 每個位置的人口數
        people = 0
        # calculate every town
        for i in range(n + 1):
            for j in range(m + 1):
                # 若在覆蓋範圍內 計算人口數
                if abs(i - u) + abs(j - v) <= r:
                    people = people + listmn[j][i]
        # 把每個符合的位置的人口數存進plist
        plist.append(people)

print(max(plist))
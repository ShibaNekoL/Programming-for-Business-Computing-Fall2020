import operator

# input
path = input()
word = input()

# inport file
with open(file=path, mode="r", encoding="utf-8") as f:
    lines = f.readlines()

# readlines
linelist = list()
for i in lines:
    # get rid of "\n" and " "
    i = i.strip("\n")
    # 一行分成兩句
    ilist = i.split("\t")
    # 把每句空白去掉
    for i in ilist:
        i = i.strip()
        linelist.append(i)

# 找關鍵字
former = dict()
latter = dict()

for i in linelist:
    S = i
    # find position
    Scut = i

    if i.find(word) != - 1:
        # 一直在同一句找關鍵字 直到找完
        while True:

            # 如果已經找完了(回傳-1) 跳出迴圈
            if Scut.find(word) == - 1:
                break

            else:
                # 找出word字串在S中的絕對位置
                position = (len(S) - len(Scut)) + Scut.find(word) # Scut中的相對位置

                # 前一個字
                # 排除word前面沒字元的情況
                if position != 0:
                    # 找出關鍵字
                    key = i[position - 1]
                    # 關鍵字第一次出現
                    if list(former.keys()).count(key) == 0:
                        former[key] = 1
                    else:
                        # 增加次數
                        former[key] += 1

                # 後一個字
                # 排除word後面沒字元的情況
                if position + len(word) != len(i):
                    # 找出關鍵字
                    key = i[position + len(word)]
                    # 關鍵字第一次出現
                    if list(latter.keys()).count(key) == 0:
                        latter[key] = 1
                    else:
                        # 增加次數
                        latter[key] += 1

                # 把S切掉前面已經找過的部分 但只切掉一個字元而不是整個關鍵字 因為怕關鍵字是有重複的 比如字串娘娘娘 要找 娘娘
                Scut = Scut[Scut.find(word) + 1:]


# sorted

# 前一個字
formerlist = list()
sorted_items = sorted(former.items(), key=operator.itemgetter(1, 0), reverse=True)
# 例外：不足10個字的話
if len(sorted_items) < 10:
    for i in sorted_items:
        formerlist.append(i[0])
# 正常：超過10個字的話
else:
    for i in range(10):
        formerlist.append(sorted_items[i][0])

# 後一個字
latterlist = list()
sorted_items = sorted(latter.items(), key=operator.itemgetter(1, 0), reverse=True)
# 例外：不足10個字的話
if len(sorted_items) < 10:
    for i in sorted_items:
        latterlist.append(i[0])
# 正常：超過10個字的話
else:
    for i in range(10):
        latterlist.append(sorted_items[i][0])


# output
print("熱門前一個字:")
for i in formerlist:
    print(str(i) + "---" + str(word))
print("熱門下一個字:")
for i in latterlist:
    print(str(word) + "---" + str(i))
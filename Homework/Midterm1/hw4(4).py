# input

line1 = input() # 投資標的個數、預算與風險趨避係數
line2 = input() # 投資標的 i 的資金需求
line3 = input() # 投資標的 i 的預期報酬

# 投資標的個數、預算與風險趨避係數
list1 = line1.split(",")
n = int(list1[0]) # number
budget = int(list1[1]) # budget
nn = int(list1[2]) # 風險趨避係數

# 投資標的 i 的資金需求
pay = line2.split(",")
for i in range(len(pay)):
    pay[i] = int(pay[i])

# 投資標的 i 的預期報酬
earn = line3.split(",")
for i in range(len(earn)):
    earn[i] = int(earn[i])

# variance
list_variance = list()
for i in range(n):
    line4 = input()
    var = line4.split(",")
    for j in range(n):
        var[j] = int(var[j])
    list_variance.append(var)

# 如果預算還夠
# 在「當下還沒被挑中，且挑了不會超過預算」的投資標的中，挑選「能最大化目標式 (1)」的那個投資標的，

numlist = list()
numberleft = list(range(n))
moneyleft = int()

# 1st次

# 把每個投資標的目標式存進list_expect
list_expect = list()

for i in range(n):
    expect = earn[i] - nn * list_variance[i][i]
    list_expect.append(expect)

# 找出最大化目標式
sort_list_expect = sorted(list_expect)
sort_list_expect.reverse()
first_expect = sort_list_expect[0] # 最大化目標式

# 判斷投資能夠有獲益，並且開銷累計仍不會大於預算
num = - 1
if first_expect > 0:

    # 找出投資哪一個
    # 沒有重複符合條件的選項
    if sort_list_expect.count(first_expect) == 1:
        num = list_expect.index(first_expect) + 1
        firstpay = pay[num - 1]
    # 如果有數個符合條件的選項，就挑其中資金需求最低的，再平手就挑編號小的。
    else:
        list_num = list()
        list_pay = list()
        # 找出哪幾個符合條件
        for i in range(n):
            if list_expect[i] == first_expect:
                list_num.append(i)
        # 找出pay最低
        for i in list_num:
            list_pay.append(pay[i])
        sort_list_pay = sorted(list_pay)
        firstpay = sort_list_pay[0]

        # 若pay沒平手
        if sort_list_pay.count(firstpay) == 1:
            num = list_num[list_pay.index(firstpay)] + 1
        # 若pay平手，找編號最小
        else:
            num = list_num.sort()[0] + 1

    # 計算剩餘金錢
    moneyleft = budget - firstpay

    # 若剩餘金錢仍大於0
    if moneyleft >= 0 and num >= 0:
        numlist.append(num)
        # 當下還沒被挑中的
        numberleft.remove(num - 1)


# n次

# 把每個投資標的目標式存進n_list_expect

for i in numberleft:
    n_list_expect = list()

    for i in range(n):
        expect = earn[i] - (nn * (list_variance[i][i] + list_variance[i][num - 1] * 2))
        n_list_expect.append(expect)

    # 找出最大化目標式
    sort_list_expect = sorted(n_list_expect)
    sort_list_expect.reverse()
    n_expect = sort_list_expect[0] # 最大化目標式

    # 判斷投資能夠有獲益，並且開銷累計仍不會大於預算
    if n_expect > 0:
        # 找出投資哪一個
        # 沒有重複符合條件的選項
        if sort_list_expect.count(n_expect) == 1:
            num = n_list_expect.index(n_expect) + 1
            firstpay = pay[num - 1]
        # 如果有數個符合條件的選項，就挑其中資金需求最低的，再平手就挑編號小的。
        else:
            list_num = list()
            list_pay = list()
            # 找出哪幾個符合條件
            for i in range(n):
                if n_list_expect[i] == n_expect:
                    list_num.append(i)
            # 找出pay最低
            for i in list_num:
                list_pay.append(pay[i])
            sort_list_pay = sorted(list_pay)
            firstpay = sort_list_pay[0]

            # 若pay沒平手
            if sort_list_pay.count(firstpay) == 1:
                num = list_num[list_pay.index(firstpay)] + 1
            # 若pay平手，找編號最小
            else:
                num = list_num.sort()[0] + 1

        # 計算剩餘金錢
        moneyleft = moneyleft - firstpay

        # 若剩餘金錢仍大於0
        if moneyleft > 0:
            numlist.append(num)
            # 當下還沒被挑中的
            numberleft.remove(num - 1)


numlist.sort()
for i in range(len(numlist)):
    if i == 0:
        output = str(numlist[0])
    elif i < len(numlist):
        output = output + "," + str(numlist[i])
    else:
        output = output + str(numlist[i])

# output
if numlist != []:
    print(output)
else:
    print(0)
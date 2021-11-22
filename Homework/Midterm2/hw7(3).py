import operator

# input
path_title = input()
path_dict = input()
path_cc = input()
line4 = input()

# 有興趣的產業類別 k(category) 、購買的總張數 q 、每輪的購買張數 r
line4 = line4.split(",")
line4_2 = line4[2].split(":")
category = str(line4[0])
q = int(line4[1])
rlist = list()
for i in line4_2:
    rlist.append(int(i))

# import file news_title.txt 新聞標題檔案
with open(file=path_title, mode="r", encoding="utf-8") as f:
    lines_title = f.readlines()
# import file news_dict.txt 關鍵字辭典檔案
with open(file=path_dict, mode="r", encoding="utf-8") as f:
    lines_dict = f.readlines()
# import company_category.txt 公司類別檔案
with open(file=path_cc, mode="r", encoding="utf-8") as f:
    lines_cc = f.readlines()

# readlines
list_title = list()
dict_word = dict()
dict_cc = dict()

# 處理新聞標題檔案
for i in lines_title:
    # get rid of "\n" and " "
    i = i.strip("\n")
    # remove space in title
    title = str()
    for j in i:
        if j != " ":
            title += j
    list_title.append(title)

# 處理關鍵詞辭典檔案
for i in lines_dict:
    # get rid of "\n" and " "
    i = i.strip("\n")
    i = i.split(" ")
    # list to dict
    dict_word[i[0]] = int(i[1])

# 處理公司類別檔案
for i in lines_cc:
    # get rid of "\n" and " "
    i = i.strip("\n")
    i = i.split(" ")
    # list to dict
    dict_cc[i[0]] = i[1]


# 做出關鍵字列表
list_keyword = list(dict_word.keys())
# 做出公司列表
list_company = list(dict_cc.keys())

# 做一個dict儲存公司和分數
company_score = dict()
for i in list_company:
    company_score[i] = int()

# 切關鍵字
# 找出公司
# hw6(3)
for title in list_title:

    # 斷開關鍵字
    # 關鍵字長度較長，優先斷開
    # 長度相同就看哪個關鍵字在重疊的部分中先出現 先出現，所以先斷開

    # 跑每個關鍵字
    position_list = list()
    for i in list_keyword:
        titleposition_list_result = title
        # 一直找關鍵字位置 直到找完
        position_onekeyword_list = list()
        while True:
            # 如果已經找完了(回傳-1) 跳出迴圈
            if titleposition_list_result.find(i) == - 1:
                break
            else:
                # 找出keyword i在title中的絕對位置
                position = (len(title) - len(titleposition_list_result)) + titleposition_list_result.find(i) # Sposition_list_result中的相對位置
                onewordlist = list()
                # 把有關鍵字的每個位置都合成一個list
                for j in range(len(i)):
                    onewordlist.append(position + j)
                # 存進單一關鍵字的list
                position_onekeyword_list.append(onewordlist)
                # 把S切掉前面已經找過的部分 但只切掉一個字元而不是整個關鍵字 因為怕關鍵字是有重複的 比如字串娘娘娘 要找 娘娘
                titleposition_list_result = titleposition_list_result[titleposition_list_result.find(i) + 1:]
        position_list.append(position_onekeyword_list)

    # 把每個關鍵字的每個字元的位置取出
    position_list_expand = list()
    for i in position_list:
        for j in i:
            if j != []:
                position_list_expand.append(j)

    # 照子list長度sort
    length = list()
    # 計算子list長度
    for i in position_list_expand:
        length.append(len(i))
    # sorted
    lengthsort = sorted(length, reverse=True)
    position_list_expand_sort = list()
    for i in range(len(lengthsort)):
        position_list_expand_sort.append(position_list_expand[length.index(lengthsort[i])])
        length[length.index(lengthsort[i])] = - 1

    # create 最後要踢掉哪些關鍵字位置的list
    kick = list()
    # 從長度長的關鍵字開始跑
    for i in range(len(position_list_expand_sort)):
        # 跑每個字元位置看有沒有重疊
        for position in position_list_expand_sort[i]:
            # 檢查其他關鍵字
            for j in range(len(position_list_expand_sort)):
                # 檢查其他關鍵字的每個字元位置
                for position2 in position_list_expand_sort[j]:
                    # 有重疊的話 把其他短的關鍵字刪掉
                    if (i < j) and (position == position2) and (len(position_list_expand_sort[i]) > len(position_list_expand_sort[j])):
                        kick.append(j)
                    # 一樣長的話 看誰先出現
                    if (i < j) and (position == position2) and (len(position_list_expand_sort[i]) == len(position_list_expand_sort[j])):
                        # 若i 先出現，踢掉j
                        if position_list_expand_sort[i][0] < position_list_expand_sort[j][0]:
                            kick.append(j)
                        # 若j 先出現，踢掉i
                        if position_list_expand_sort[i][0] > position_list_expand_sort[j][0]:
                            kick.append(i)

    # creat new list以便之後把短的和後面才出現的剃除
    position_list_result = list()

    # 刪掉不符合條件的位置的關鍵字 (其實是作新list用保留的 因為不知道如何同時刪除)
    for i in range(len(position_list_expand_sort)):
        # 計數器
        count = int()
        for j in kick:
            if i != j:
                count += 1
        # 全部都不符合被剔除的位置才保留此關鍵字
        if count == len(kick):
            position_list_result.append(position_list_expand_sort[i])

    # sorted 讓位置後面的先作 關鍵字比較好切 就不用再考慮整串標題會變長 位置跑掉的問題
    position_list_result.sort(reverse=True)

    # 找出關注公司
    # 重置str_company
    str_company = str()
    list_count = list()
    list_company_exist = list()
    # 把有的company加進list，並計算出現次數
    for c in list_company:
        if c in title:
            list_company_exist.append(c)
            list_count.append(title.count(c))
    # 出現次數的由多至少排序
    list_count_sort = sorted(list_count, reverse=True)
    list_company_exist_sort = list()
    for i in range(len(list_count_sort)):
        # 把公司照出現次數排序
        list_company_exist_sort.append(list_company_exist[list_count.index(list_count_sort[i])])
        # 把值變-1就不會重複找
        list_count[list_count.index(list_count_sort[i])] = - 1
    # 若出現次數相同時，則依照公司集合c的輸入順序由前至後排序
    for i in range(len(list_count_sort)):
        for j in range(len(list_count_sort)):
            if i < j and list_count_sort[i] == list_count_sort[j]:
                # 如果j公司比較早出現，調換位置
                if list_company.index(list_company_exist_sort[i]) > list_company.index(list_company_exist_sort[j]):
                    list_company_exist_sort[i] = list_company[list_company.index(list_company_exist_sort[j])]
                    list_company_exist_sort[j] = list_company[list_company.index(list_company_exist_sort[i])]
    # hw6(3) end

    # 算新聞總分數
    score = int()
    # 跑新聞標題的每個keyword
    for i in position_list_result:
        # 用position_list_result的位置去原title找出關鍵字keyword
        keyword = str()
        for k in i:
            keyword += str(title[k])
        # 跑每個權重 有配對到的關鍵字加分
        for j in dict_word:
            if j == keyword:
                score += dict_word[j]

    # 公司的分數
    for i in list_company_exist_sort:
        company_score[i] += score

# 購買
# 做出產業類別k(category)的公司的list
cklist = list()
for i in dict_cc:
    if dict_cc[i] == category:
        cklist.append(i)

# 如果根本沒此產業的公司
if cklist == []:
    print("NO_MATCH")

else:
    # 全部公司分數排序
    companylist = list()
    sorted_items = sorted(company_score.items(), key=operator.itemgetter(1, 0), reverse=True)

    # 挑出產業類別k中的前len(rlist)個公司 companylist
    # 照sorted過的分數由大到小做
    for j in sorted_items:
        for k in cklist:
            if j[0] == k:
                companylist.append(k)
    # 正常：超過的話
    if len(cklist) > len(rlist):
        companylist = companylist[:len(rlist)]

    # 數輪購買 總張數q
    # 創造公司對應購買量的dict
    buy = dict()
    for i in companylist:
        buy[i] = int()

    while True:
        if q == 0:
            break
        # 每輪重置count=0 -> 從第一家公司開始買
        count = int()
        for i in rlist[0:len(companylist)]:
            # 沒張數後跳出迴圈
            if q == 0:
                break
            if q - i >= 0:
                buy[companylist[count]] += i
                q -= i
            # 剩下的張數少
            else:
                buy[companylist[count]] += q
                q = 0
            count += 1

    # put tuple into dict -> sort buy by company rank
    # 因為原本的buy是dict沒排序 重建一個sortdict 把購買量和公司排名tuple放進去變成dict的value
    sortdict = dict()
    for i in range(len(companylist)):
        for j in buy:
            if j == companylist[i]:
                sortdict[j] = (buy[j], i)

    sorted_items = sorted(sortdict.items(), key=lambda x: x[1][1], reverse=False)

    # 購買數不等於0的公司才印出來
    keep = list()
    for i in sorted_items:
        if i[1][0] != 0:
            keep.append(i)

    output = str()
    for i in keep:
        output = str(i[0]) + "購買" + str(i[1][0]) + "張"
        print(output)
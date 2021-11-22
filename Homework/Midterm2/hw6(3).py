# input
# 公司
line1 = input()
list_company = line1.split(",")

# 關鍵字
line2 = input()
list_keyword = line2.split(",")

# 新聞標題
list_title = list()
while True:
    rawtitle = input()
    if rawtitle == "INPUT_END":
        break
    else:
        # remove space in title
        title = str()
        for i in rawtitle:
            if i != " ":
                title += i
        list_title.append(title)

for title in list_title:
    # 斷開關鍵字
    # 關鍵字長度較長，優先斷開
    # 長度相同就看哪個關鍵字在重疊的部分中先出現 先出現，所以先斷開

    # 跑每個關鍵字
    position_list = list()
    for i in list_keyword:
        titlecut = title
        # 一直找關鍵字位置 直到找完
        position_onekeyword_list = list()
        while True:
            # 如果已經找完了(回傳-1) 跳出迴圈
            if titlecut.find(i) == - 1:
                break
            else:
                # 找出keyword i在title中的絕對位置
                position = (len(title) - len(titlecut)) + titlecut.find(i) # Scut中的相對位置
                onewordlist = list()
                # 把有關鍵字的每個位置都合成一個list
                for j in range(len(i)):
                    onewordlist.append(position + j)
                # 存進單一關鍵字的list
                position_onekeyword_list.append(onewordlist)
                # 把S切掉前面已經找過的部分 但只切掉一個字元而不是整個關鍵字 因為怕關鍵字是有重複的 比如字串娘娘娘 要找 娘娘
                titlecut = titlecut[titlecut.find(i) + 1:]
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

    # 切關鍵字
    # 把要切的位置清理乾淨 (可能有重複的要刪掉)
    cut = list()
    for i in position_list_result:
        if cut.count(i[- 1] + 1) < 1:
            cut.append(i[- 1] + 1)
        if cut.count(i[0]) < 1:
            cut.append(i[0])

    # 把title變成list處理
    titlelist = list()
    for i in title:
        titlelist.append(i)
    for i in cut:
        titlelist.insert(i, "/")
    # 把list變回str
    newtitle = str()
    for i in titlelist:
        newtitle += i
    # 把頭尾/清掉
    if newtitle[- 1] == "/":
        newtitle = newtitle[:- 1]
    if newtitle[0] == "/":
        newtitle = newtitle[1:]

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

    # 輸出符合格式的字串
    if list_company_exist_sort != []:
        str_company = str()
        for i in list_company_exist_sort:
            str_company = str_company + "," + i
        str_company = str_company[1:]
        str_company += ";"

    # 如果有就印出來
    if str_company == "":
        print("NO_MATCH")
    else:
        print(str_company + newtitle)
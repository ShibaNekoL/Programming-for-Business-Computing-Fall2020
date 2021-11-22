path = input()

# import file news_title.txt 新聞標題檔案
with open(file=path, mode="r", encoding="cp950") as f:
    lines_title = f.readlines()

# readlines
list_title = list()

# 處理檔案
for i in lines_title:
    # get rid of "\n"
    i = i.strip("\n")
    titlelist = i.split(",")
    # remove 前後 spaces in titlelist
    news_titlelist = list()
    for j in titlelist:
        news_titlelist.append(j.strip())
    list_title.append(news_titlelist)

# 欄列轉換
flip = list(list(i) for i in zip(*list_title))


# 欄位為 numerical 或 categorical
def TYPE(list_input=flip):
    # index
    index = dict()
    for i in range(len(list_input)):
        for j in list_input[i]:
            try:
                float(j)
                index[i] = "numerical"
            except:
                index[i] = "categorical"
    return index

# 欄位index m
# 每個欄位的最大長度
def MAXLEN(list_input=flip):
    index = dict()
    for i in range(len(list_input)):
        lenlist = list()
        for j in list_input[i]:
            lenlist.append(len(j))
        index[i] = max(lenlist)
    return index



# 欄位的最大數值位數
def MAXNUMLEN(list_input=flip):
    # index
    index = dict()
    for i in range(len(list_input)):
        temp = list()
        for j in range(len(list_input[i])):
            try:
                list_input[i][j] = float(list_input[i][j])
                # +
                if list_input[i][j] >= 0:
                    out = int(list_input[i][j] // 1)
                # negative
                elif list_input[i][j] < 0:
                    out = int( - (list_input[i][j] // 1))
                temp.append(len(str(out)))
            except:
                temp = [0]
        index[i] = max(temp)
    return index


# 欄位的最大小數點後數值位數
def MAXDECPLACE(list_input=flip):
    # index
    index = dict()
    for i in range(len(list_input)):
        temp = list()
        for j in range(len(list_input[i])):
            try:
                # 整數
                if len(list_input[i][j]) == len(str(int(float(list_input[i][j])) // 1)):
                    list_input[i][j] = int(list_input[i][j])
                else:
                    list_input[i][j] = float(list_input[i][j])

                # 把float轉成正字串
                # 原本的float轉成整數
                # +
                if list_input[i][j] >= 0:
                    f = str(list_input[i][j])
                    out = int(list_input[i][j] // 1)
                # negative
                elif list_input[i][j] < 0:
                    f = str(- (list_input[i][j]))
                    out = int( - (list_input[i][j] // 1))
                # 跟整數相減
                if len(str(list_input[i][j])) == len(str(int(float(list_input[i][j])) // 1)):
                    num = len(str(f)) - len(str(out))
                else:
                    num = len(str(f)) - len(str(out)) - 1

                temp.append(num)
            except:
                temp = [0]
        index[i] = max(temp)
    return index



# output

func = input()
if func == "TYPE":
    sorted_items = sorted(TYPE(flip).items(), key=lambda x: (x[0]), reverse=False) 
    for i in sorted_items:
        print(str(i[0]) + ": " + str(i[1]))
if func == "MAXLEN":
    sorted_items = sorted(MAXLEN(flip).items(), key=lambda x: (x[0]), reverse=False) 
    for i in sorted_items:
        print(str(i[0]) + ": " + str(i[1]))
if func == "MAXNUMLEN":
    sorted_items = sorted(MAXNUMLEN(flip).items(), key=lambda x: (x[0]), reverse=False) 
    for i in sorted_items:
        print(str(i[0]) + ": " + str(i[1]))
if func == "MAXDECPLACE":
    sorted_items = sorted(MAXDECPLACE(flip).items(), key=lambda x: (x[0]), reverse=False) 
    for i in sorted_items:
        print(str(i[0]) + ": " + str(i[1]))
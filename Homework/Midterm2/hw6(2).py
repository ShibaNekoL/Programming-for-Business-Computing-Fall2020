# 1st part input
w = int(input()) # 距離<=w: k1結束到k2開始之前中間的字元數

# 2nd part input
keyword1 = input()

# 3rd part input
keyword2 = input()

# 4th part input
# 串接後的字串
S = str()

while True:

    # 原始input單行字串
    s = input().strip()

    if s == "INPUT_END":
        # 停止input
        break
    else:
        # 串接字串
        S = S + " " + s
    # delete the last space
    S = S.strip()


# 儲存絕對位置的list
position_k1_list = list()
position_k2_list = list()

# 一直找關鍵字 直到找完
Scut = S
# 找第一個關鍵字
while True:

    # 如果已經找完了(回傳-1) 跳出迴圈
    if Scut.find(keyword1) == - 1:
        break
    else:
        # 找出keyword字串在S中的絕對位置
        position = (len(S) - len(Scut)) + Scut.find(keyword1) # Scut中的相對位置
        position_k1_list.append(position)
        # 把S切掉前面已經找過的部分 但只切掉一個字元而不是整個關鍵字 因為怕關鍵字是有重複的 比如字串娘娘娘 要找 娘娘
        Scut = Scut[Scut.find(keyword1) + 1:]

Scut = S
# 找第二個關鍵字
while True:

    # 如果已經找完了(回傳-1) 跳出迴圈
    if Scut.find(keyword2) == - 1:
        break
    else:
        # 找出keyword字串在S中的絕對位置
        position = (len(S) - len(Scut)) + Scut.find(keyword2) # Scut中的相對位置
        position_k2_list.append(position)
        # 把S切掉前面已經找過的部分 但只切掉一個字元而不是整個關鍵字 因為怕關鍵字是有重複的 比如字串娘娘娘 要找 娘娘
        Scut = Scut[Scut.find(keyword2) + 1:]

# 判定關鍵字間距離是否小於等於w
position_list = list()
for i in position_k1_list:
    for j in position_k2_list:
        if (i < j) and j - (i + len(keyword1)) <= w:
            position_list.append([i, j])

# 判定是否有找到符合條件的關鍵字
if len(position_list) > 0:
    # output
    # 因為擷取字串不能負的開始 所以用這判斷式從0開始切
    for i in range(len(position_list)):
        if position_list[i][0] - 7 < 0:
            print(S[0:position_list[i][0]] +
                  "**" + S[position_list[i][0]:position_list[i][0] + len(keyword1)] + "**" +
                  S[position_list[i][0] + len(keyword1):position_list[i][1]] +
                  "**" + S[position_list[i][1]:position_list[i][1] + len(keyword2)] + "**" +
                  S[position_list[i][1] + len(keyword2):position_list[i][1] + len(keyword2) + 7])
        else:
            print(S[position_list[i][0] - 7:position_list[i][0]] +
                  "**" + S[position_list[i][0]:position_list[i][0] + len(keyword1)] + "**" +
                  S[position_list[i][0] + len(keyword1):position_list[i][1]] +
                  "**" + S[position_list[i][1]:position_list[i][1] + len(keyword2)] + "**" +
                  S[position_list[i][1] + len(keyword2):position_list[i][1] + len(keyword2) + 7])
else:
# 沒找到就output NO_MATCH
    print("NO_MATCH")
# 1st part input
keyword = input()


# 2nd part input

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


# 判定
Scut = S

if S.find(keyword) != - 1:

    # 一直找關鍵字 直到找完
    while True:

        # 如果已經找完了(回傳-1) 跳出迴圈
        if Scut.find(keyword) == - 1:
            break
        else:
            # 找出keyword字串在S中的絕對位置
            position = (len(S) - len(Scut)) + Scut.find(keyword) # Scut中的相對位置

            # output
            # 因為擷取字串不能負的開始 所以用這判斷式從0開始切
            if position - 7 < 0:
                print(S[0:position] + "**" + S[position:position + len(keyword)] + "**" + S[position + len(keyword):position + len(keyword) + 7])
            else:
                print(S[position - 7:position] + "**" + S[position:position + len(keyword)] + "**" + S[position + len(keyword):position + len(keyword) + 7])

            # 把S切掉前面已經找過的部分 但只切掉一個字元而不是整個關鍵字 因為怕關鍵字是有重複的 比如字串娘娘娘 要找 娘娘
            Scut = Scut[Scut.find(keyword) + 1:]
else:
    # 沒找到就output NO_MATCH
    print("NO_MATCH")
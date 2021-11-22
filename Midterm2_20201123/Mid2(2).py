list_lines = list()
while True:
    line = input()
    # stop input if input LINESTOP
    if line == "INPUTSTOP":
        break
    else:
        # 清理每行

        # 去除頭尾的空白。
        line = line.strip()

        # 將這段文字中成對出現的半形雙引號 " 改成 「 與 」 。每一行中先出現的成對半形雙引號 "，會先被配對成一組，每一行輸入獨立判斷。如果最後有引號無法配對，則保留無法配對的引號，不做任何處理
        # 位置list
        position = list()
        # 找出每個引號位置
        for i in range(len(line)):
            if line[i] == "\"":
                position.append(i)
        # 只處理可以配對的引號
        if len(position) % 2 != 0:
            position = position[:- 1]
        # 上引號位置
        position1 = position[::2]
        # 下引號位置
        position2 = position[1::2]
        # str to list
        linelist = list()
        for i in line:
            linelist.append(i)
        for i in position1:
            linelist[i] = "「"
        for j in position2:
            linelist[j] = "」"

        # 將多個連續空白縮減成一個空白，輸入不會有 tab 字元。
        # 找出空白位置
        kick = set()
        space = list()
        for i in range(len(line)):
            if line[i] == " ":
                space.append(i)
        # 記住要踢掉的位置 有連續的空白
        delete = set()
        # i j 都是位置 數字
        for i in space:
            for j in space:
                if i + 1 == j:
                    delete.add(j)
        # 把kick從大到小sort 踢掉時就不用管位置了
        delete = sorted(list(delete), reverse=True)
        # 踢掉
        for j in delete:
            linelist.pop(j)
        # 把list變回字串
        newline = str()
        for i in linelist:
            newline += i

    # 半形逗點 「,」、冒號 「:」、句號 「.」後面需要有「一個」空白
    # 位置
    spaceadd = list()
    spaceremove = list()
    for i in range(len(newline)):
        if newline[i] == "," or newline[i] == ":" or newline[i] == ".":
            # 但如果這些標點符號出現在某行輸入的行尾，則後面不應有空白。注意: 不論文本內容是否通順或是標點符號使用方式是否正確，你的程式只需依照上述規則處理即可。
            if i != len(newline) - 1:
                # 但如果後面已經有空白就不用了
                if newline[i + 1] != " ":
                    # 因為要加在標點後面
                    spaceadd.append(i + 1)
            # 但如果前面已經沒空白就不用了
            if newline[i - 1] == " ":
                spaceremove.append(i - 1)
    # 行尾空白剛剛刪過了 所以不會出現已經行尾的標點後有空白的情況

    # 把位置從大大小sort 就不擔心插入後list變長位置跑掉
    spaceadd = sorted(spaceadd, reverse=True)
    # 把字串變成list
    newlinelist = list()
    for i in newline:
        newlinelist.append(i)
    # 插入空白
    for j in spaceadd:
        newlinelist.insert(j, " ")

    # 但前面不能有空白。
    spaceremove = sorted(spaceremove, reverse=True)
    # 刪除空白
    for j in spaceremove:
        newlinelist.pop(j)

    final = str()
    for i in newlinelist:
        final += i
    list_lines.append(final)

print(*list_lines, sep="\n")
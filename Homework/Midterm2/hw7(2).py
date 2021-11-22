# input
path_i = input()
path_g = input()
movieid = int(input())

# inport file u.item
with open(file=path_i, mode="r", encoding="ISO-8859-1") as i:
    lines_i = i.readlines()
# inport file u.genre
with open(file=path_g, mode="r", encoding="utf-8") as g:
    lines_g = g.readlines()


# readlines
linelist_i = list()
linelist_g = list()
for i in lines_i:
    # get rid of "\n" and " "
    i = i.strip("\n")
    i = i.split("|")
    linelist_i.append(i)
for i in lines_g:
    # get rid of "\n" and " "
    i = i.strip("\n")
    i = i.split("|")
    linelist_g.append(i)
linelist_g = linelist_g[0:- 1]
for i in linelist_g:
    i[1] = int(i[1])
# list to dict
gdict = dict()
for i in linelist_g:
    gdict[i[1]] = i[0]


# 用movieid找電影在列表內的位置
position = int()
count = int()
for i in range(len(linelist_i)):
    if movieid == int(linelist_i[i][0]):
        position = i
    else:
        count += 1

# 如果有找到電影
genrelist = list()
if count < len(linelist_i):
    # 儲存item是1對應到的genre
    for i in gdict.keys():
        if int(linelist_i[position][5 + i]) == 1:
            genrelist.append(gdict[i])
    # output
    output = str(linelist_i[position][1]) + ": "
    for i in genrelist:
        output += str(i) + str(", ")
    print(output.strip(", "))

# 如果沒找到
elif count == len(linelist_i):
    print("No movie found.")
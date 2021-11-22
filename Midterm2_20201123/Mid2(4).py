line = input()

p = list()
for i in range(len(line)):
    if line[i] != "+" and line[i] !="-" and line[i] != "*" and line[i] !="/" and line[i] !="=":
        p.append(i)

a = list()
for i in p:
    for j in p:
        if i + 1 == j:
            a.append(int(str(line[i]) + str(line[j])))
        elif i < j and a.count(int(line[i])) == 0:
            a.append(int(line[i]))

print(a)


line = line.replace("+", "加")
line = line.replace("-", "減")
line = line.replace("*", "乘")
line = line.replace("/", "除以")
line = line.replace("=", "等於")



line = line.replace("0", "零")
line = line.replace("1", "一")
line = line.replace("2", "二")
line = line.replace("3", "三")
line = line.replace("4", "四")
line = line.replace("5", "五")
line = line.replace("6", "六")
line = line.replace("7", "七")
line = line.replace("8", "八")
line = line.replace("9", "九")
line = line.replace("10", "十")


print(line)
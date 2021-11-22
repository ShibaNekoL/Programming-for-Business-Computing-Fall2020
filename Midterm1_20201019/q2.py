n = int(input())
line2 = input()

listx = line2.split(",")

for i in range(n):
    listx[i] = int(listx[i])

yilist = list()
for i in range(n - 1):
    yilist.append(max(listx[i] - listx[i + 1], 0))

print(min(yilist))

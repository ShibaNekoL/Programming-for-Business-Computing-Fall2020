line1 = input()
line2 = input()

line1 = line1.split(",")

for i in range(len(line1)):
    line1[i] = int(line1[i])

n = line1[0]
b = line1[1]

line2 = line2.split(",")
for i in range(n):
    line2[i] = int(line2[i])

wi = sorted(line2)
wi.reverse()




weightbox = [b]

# every object
for i in range(n):
    j = 0
    # examine each box
    while True:

        if len(weightbox) < j + 1:
            weightbox.append(b)
        # 若wi <= 箱子 : 裝進去
        if wi[i] <= weightbox[j]:
            weightbox[j] = weightbox[j] - wi[i]
            break
        else:
            j = j + 1
            continue
        

print(len(weightbox))

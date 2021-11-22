# input
a = int(input())
b = int(input())
c = int(input())
abc = [a, b, c]

index = 0

# calculate
sumabc = abc[0] + abc[0 + 1]
if abc[0 - 1] == sumabc:
    index = index + 1

sumabc = abc[1] + abc[1 + 1]
if abc[1 - 1] == sumabc:
    index = index + 1

sumabc = abc[2] + abc[0]
if abc[2 - 1] == sumabc:
    index = index + 1

# print
if index != 0:
    print(1)
else:
    print(0)
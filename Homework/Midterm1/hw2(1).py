# input

number = int(input())
numberstr = str()

for i in range(3):

    if 10 <= number < 100:
        number = number * 10
    elif number < 10:
        number = number * 100

    st = int()
    nd = int()
    rd = int()
    st = number // 100
    nd = number % 100 // 10
    rd = number % 10

    maximum = int()
    minimum = int()

    if st >= nd and st >= rd:
        # st, nd, rd
        if nd >= rd:
            maximum = st * 100 + nd * 10 + rd
            minimum = st * 1 + nd * 10 + rd * 100
        # st, rd, nd
        else:
            maximum = st * 100 + rd * 10 + nd
            minimum = st * 1 + rd * 10 + nd * 100

    if nd >= st and nd >= rd:
        # nd, st, rd
        if st >= rd:
            maximum = nd * 100 + st * 10 + rd
            minimum = nd * 1 + st * 10 + rd * 100
        # nd, rd, st
        else:
            maximum = nd * 100 + rd * 10 + st
            minimum = nd * 1 + rd * 10 + st * 100

    if rd >= st and rd >= nd:
        # rd, st, nd
        if st >= nd:
            maximum = rd * 100 + st * 10 + nd
            minimum = rd * 1 + st * 10 + nd * 100
        # rd, nd, st
        else:
            maximum = rd * 100 + nd * 10 + st
            minimum = rd * 1 + nd * 10 + st * 100

    number = maximum - minimum

    if i <= 1:
        numberstr = numberstr + str(number) + ","
    else:
        numberstr = numberstr + str(number)

print(numberstr)
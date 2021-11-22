# input
pm = int(input())
Ta = int(input())
Td = int(input())
v = float(input())

wa = float()
wh = float()
w0 = 0.5
w = float()

if pm <= 35:
    wa = w0 + (100 - pm) * 0.005
else:
    wa = w0 + (45 - pm) * 0.02


RH = 100 - 5 * (Ta - Td)

if RH <= 30:
    wh = w0 / 60 * (110 - RH)
else:
    wh = w0 / 45 * (90 - RH)


if wa < 0:
    w = 0
if wh < 0:
    w = 0

if wa > 1:
    w = 1
if wh > 1:
    w = 1

if wa >= 0:
    if wh >= 0:
        if wa <= 1:
            if wh <= 1:
                w = min(wa, wh)


print('{:.2f}'.format(w))

if w >= v:
    print("Let's go together.")
else:
    print("I wouldn't go out with you.")
nday = int(input())
sumsleep = float()
mday = int()

for i in range(nday):

    sleep = float(input())

    if sleep > 7:
        mday += 1

    sumsleep = sumsleep + sleep

meansleep = sumsleep / nday

# 一張檸檬美白面膜需要 1.5 顆檸檬、4 單位的杏仁油；
# 一張蜜糖修復面膜需要 18 單位的蜂蜜、9 單位的杏仁油；
# 一張蛋白彈潤面膜需要 2 顆雞蛋、6 單位蜂蜜。

# 已知檸檬一顆售價 7 元，只能買整數顆檸檬，買五顆以上（包含）每顆檸檬打 9 折；
# 杏仁油每單位 0.6 元；
# 蜂蜜每單位 1.2 元；
# 雞蛋每盒三顆，每盒 25 元，不拆售。
# 最後結帳時，總金額會進行無條件捨去以整數計算。

# 檸檬美白面膜
lemon = mday * 1.5
oil = mday * 4
if mday % 2 == 1:
    lemon = int(lemon // 1) + 1
# mprice
if lemon >= 5:
    mprice = lemon * 7 * 0.9 + oil * 0.6
else:
    mprice = lemon * 7 + oil * 0.6

# 蜜糖修復面膜
if meansleep <= 6:
    honey = (nday - mday) * 18
    oil = (nday - mday) * 9
    # nmprice
    nmprice = honey * 1.2 + oil * 0.6

# 蛋白保濕面膜
elif meansleep > 6:
    
    egg = (nday - mday) * 2
    honey = (nday - mday) * 6
    # nmprice
    if egg % 3 != 0:
        eggbox = egg // 3 + 1
    else:
        eggbox = egg / 3
    nmprice = eggbox * 25 + honey * 1.2

price = int((mprice + nmprice) // 1)

print(price)

# input
product = int(input()) # 商品種類數
kit = input() # 套組編號
price = input() # 價格
amount = input() # 購買量

# split input
list_kit = kit.split(",")
list_price = price.split(",")
list_amount = amount.split(",")

# convert string in the list into integer
for i in range(len(list_kit)):
    list_kit[i] = int(list_kit[i])

for i in range(product):
    list_price[i] = int(list_price[i])
    list_amount[i] = int(list_amount[i])


# 湊滿套組數
# 將套組之第編號k的購買量存入amount_list，找出最小購買量以得知湊滿套組數
kitamount_list = list()
for k in list_kit:
    kitamount_list.append(list_amount[k - 1])
# 從小排到大，取第一個也就是位置0最小值。找出最小購買量來得知湊滿套組數
min_kit = sorted(kitamount_list)[0]


# 打折
# 湊滿一組套組則該組套組可獲得原價打9折的優惠，每湊滿5組套組則該5組套組可獲得原價打8折的優惠
# 湊滿套組購買量
discount9 = min_kit % 5
discount8 = min_kit // 5 * 5

# 一組套組價格
onekitprice = float()
for k in list_kit:
    onekitprice = onekitprice + list_price[k - 1]

# 所有購買套組打折後省的錢
discountkitprice = onekitprice * discount9 * 0.1 + onekitprice * discount8 * 0.2


# 計算原未打折總價
list_totalprice = list()
# 各商品購買數量 * 價格 = list各元素相乘
for i in range(product):
    for j in range(i, i + 1):
        list_totalprice.append(list_price[i] * list_amount[j])
# 總價
totalprice = float()
for i in range(len(list_totalprice)):
    totalprice = totalprice + list_totalprice[i]
# 實付價格
pay = int((totalprice - discountkitprice) // 1)


# 球員
# 總共為新生們省下了多少錢，每省下 1000元就可以招募到一名正式隊員

member = int(discountkitprice // 1000)


# 若沒有招募到任何球員，則輸出「So sad. I messed up.」
if member == 0:
    print("So sad. I messed up.")
else:
    print(pay, member, sep=",")

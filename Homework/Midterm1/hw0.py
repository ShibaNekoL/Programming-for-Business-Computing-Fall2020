# hw0
"""
你正要去一間美術館看展覽，要買 x1 張全票與 x2 張學生票，而一張全票的售價是 p1 元，
一張學生票則是 p2 元。已知你要付的總金額不超過 t 元，若你拿出 t 元鈔票給櫃臺，請問櫃臺會找你多少錢？

系統會提供一共 10 組測試資料，每組測試資料裝在一個檔案裡。
在每個檔案中會有五列，每列依序裝著一個非負整數 x1、x2、p1 、p2 與 t。已知 p1x1+p2x2≤t、t∈{500,1000}。

請依題目指示在一列中依序印出 t、你所購票券的費用總額，以及櫃臺找錢的金額，兩個整數間用一個逗點隔開。
"""

# input

x1 = int(input())
x2 = int(input())
p1 = int(input())
p2 = int(input())
t = int(input())

# calculate

expense = x1 * p1 + x2 * p2 
left = t - expense

# print

print(str(t) + "," + str(expense) + "," + str(left))
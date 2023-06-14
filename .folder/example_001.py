n = int(input("Введите кол-во монеток"))
count_reshka = 0
count_orel = 0
for i in range(n):
    x = int(input())
    if x == 0:
        count_reshka += 1
    else:
        count_orel += 1
if count_reshka > count_orel:
    print(count_reshka)
else:
    print(count_orel)
x = int(input("Введите число y: "))
y = int(input("Введите число x: "))
for i in range(x):
    for j in range(y):
        if x == i + j and y == i * j:
            print(i, j)
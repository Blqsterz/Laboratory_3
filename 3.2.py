a = float(input("Введите a: "))
b = float(input("Введите b: "))

if a == 0 or b == 0:
    print("Решений нет")
else:
    x = -b / a
    print("x= " + str(x))

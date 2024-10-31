while True:
    try:
        
        a = int(input("Введите первое число (a): "))
        b = int(input("Введите второе число (b): "))
        break  
    except ValueError:
        print("Пожалуйста, вводите только целые числа.")

if a < b:
    for i in range(a + 1, b):
        print(i, end=" ")
elif a > b:
    for i in range(a - 1, b, -1):
        print(i, end=" ")
else:
    print("Нет чисел между a и b.")



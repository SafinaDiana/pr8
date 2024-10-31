summa = 0  

while True:
    user_input = input("Введите число (или 'stop'/'end' для завершения): ")
    
    if user_input.lower() == "stop" or user_input.lower() == "end":
        break

    try:
    
        chislo = float(user_input)
        summa += chislo
    except ValueError:
        
        print("Введите число или команду 'stop'/'end' для завершения.")

print("Сумма введенных чисел:", summa)



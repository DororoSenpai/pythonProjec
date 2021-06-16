what = input("Что выберете?, +, -, *, /: ")

a = float( input("Введите первое число ") )
b = float( input("Введите второе число "))

if what == "+":
    c = a + b
    print("Результат:" + str(c))
elif what == "_":
    c = a - b
    print("Результат:" + str(c))
elif what == "*":
    c = a * b
    print("Результат:" +str(c))
elif what == "/":
    c = a / b
    print("результат:" + str(c))
else:
    print("Выбрана не верная операция")

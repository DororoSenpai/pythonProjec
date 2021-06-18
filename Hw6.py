from random import randrange
number = randrange(20)
print(number)
guess =-1
k=0
while guess !=number:
    guess = int(input("Введи"))
    k+=1
    if guess > number:
        print("Загаданное число тепло")
    elif guess < number:
        print("Загаданное число холодно")
print("Ты отгодал крассава!\Количество попыток",k)

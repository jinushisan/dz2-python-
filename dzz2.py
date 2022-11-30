# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.


x = input('Введите число ')

def summa(x):                            
    if float(x) < 0:                            
        x = float(x) * (-1)
    number = 0

    for i in str(x):
        if i != '.':
            number += int(i)
    return number

   
print(f'Сумма чисел равна {summa(x)}')


# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

N = int(input('Введите число '))

l = 1
for i in range(N):
    i = i + 1
    l = i * l
    
    print(l, end=" ")

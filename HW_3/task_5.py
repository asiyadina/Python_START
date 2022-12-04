#"""
#Задайте целое число N.
#Составьте список чисел Фибоначчи размерность 2N + 1 для отрицательной и положительной части (Негафибоначчи).
#https://ru.wikipedia.org/wiki/Негафибоначчи

#Ввод: значение типа <int>
#Вывод: значение типа <list>

#Пример:
#8
#[-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
#"""

n = int(input('Введите число: '))
negofibonacci = [1,-1]
fibonacci = [1,1]

for i in range(2,n):
    list = fibonacci[i-1]+fibonacci[i-2]
    fibonacci.append(list)
    list2 = negofibonacci[i-2] - negofibonacci[i-1]
    negofibonacci.append(list2)

negofibonacci.reverse()
fibonacci.insert(0, 0)

print(f' Для {n} => {negofibonacci+fibonacci}')

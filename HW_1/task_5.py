#"""
#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#Результат округлить до сотых.

#Ввод: четыре значения типа <int>
#Вывод: значение типа <float>

#Пример:

#4 10
#11 5
#9.22
#"""
ax = float(input('Введите координаты точки a по оси x:'))
ay = float(input('Введите координаты точки a по оси y:'))
bx = float(input('Введите координаты точки b по оси x:'))
by = float(input('Введите координаты точки b по оси y:'))

import math
distans = math.sqrt((ax-bx)**2+(ay-by)**2)
print(f'Растояние между точкой A до точки B = {distans}' )

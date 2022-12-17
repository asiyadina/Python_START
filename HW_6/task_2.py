"""
Задайте список случайных чисел. Выведите:
а) список чисел, которые не повторяются в заданном списке,
б) список повторяемых чисел,
в) список без повторений

Ввод: значение типа <list>
Вывод: три объекта типа <list>

Пример:
[1, 2, 3, 5, 1, 5, 3, 10]
[2, 10]
[1, 3, 5]
[1, 2, 5, 3, 10]
"""

# Представлен список чисел.
# Определить элементы списка, не имеющие повторений
list1 = [9, 1, 5, 9, 4, 2, 7, 2, 9, 5, 3]
list2 = [el for el in list1 if list1.count(el) == 1]
print(list2)

#список повторяемых чисел
#myList = [9, 1, 5, 9, 4, 2, 7, 2, 9, 5, 3] 
#occurrences = [] 

#for item in myList : 
#    count = 0 
#    for x in myList : 
#        if x == item :
#             count += 1
#    occurrences.append(count) 

#duplicates = set() 
#index = 0 
#while index < len(myList) : 
#    if occurrences[index] != 1 : 
#        duplicates.add(myList[index]) 
#    index += 1 

#print(duplicates)


#список без повторений
#myList = [9, 1, 5, 9, 4, 2, 7, 2, 9, 5, 3]
#mySet = set(myList) 
#print(mySet)


"""
Методы и функции по работе со списками
Для управления элементами списки имеют целый ряд методов. Некоторые из них:

append(item): добавляет элемент item в конец списка

insert(index, item): добавляет элемент item в список по индексу index

extend(items): добавляет набор элементов items в конец списка

remove(item): удаляет элемент item. Удаляется только первое вхождение элемента. Если элемент не найден, генерирует исключение ValueError

clear(): удаление всех элементов из списка

index(item): возвращает индекс элемента item. Если элемент не найден, генерирует исключение ValueError

pop([index]): удаляет и возвращает элемент по индексу index. Если индекс не передан, то просто удаляет последний элемент.

count(item): возвращает количество вхождений элемента item в список

sort([key]): сортирует элементы. По умолчанию сортирует по возрастанию. Но с помощью параметра key мы можем передать функцию сортировки.

reverse(): расставляет все элементы в списке в обратном порядке

copy(): копирует список

Кроме того, Python предоставляет ряд встроенных функций для работы со списками:

len(list): возвращает длину списка

sorted(list, [key]): возвращает отсортированный список

min(list): возвращает наименьший элемент списка

max(list): возвращает наибольший элемент списка

"""
def sortList(a):
    return a % 2

list1 = [100, 5, 6, 7, 1000, 9]
print(min(list1))

# list1 = [1, 100, -7, 9]
# max1 = max(list1)
# print(max1)

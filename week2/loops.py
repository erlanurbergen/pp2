# lecture 2
"""
while loops
python list
for loops
arrays
tuple
sets
dictionaries
"""

# while loop
# Циклы позволяют выполнять некоторое действие в зависимости от соблюдения некоторого условия.

# number = 1
# while number < 5 :
#     print(f"number = {number}")
#     number += 1
# print("Работа программы завершена")

# можно также использовать блок else

# number = 1
#
# while number < 5 :
#     print(f"number = {number}")
#     number += 1
# else :
#     print(f"number = {number}. Работа цикла завершена")
# print("Работа программы завершена")


# for loop

# message = "Hello"

# for c in message :
#     print(c)
#
# for i in range(2, 10, 2):
#     print(i)



# message = "Hello"
# for c in message:
#     print(c)
# else:
#     print(f"Последний символ: {c}. Цикл завершен");
# print("Работа программы завершена")

# можно также использовать блок else


# break
# while True:
#     text = input("Insert text: ")
#     if text == "exit":
#         break
#     else:
#         print(text)

# continue
# number = 0
# while number < 5:
#     number += 1
#     if number == 3 :    # если number = 3, переходим к новой итерации цикла
#         continue
#     print(f"number = {number}")
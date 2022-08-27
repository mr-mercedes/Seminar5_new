# Задача 1. Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5.
# Используйте для решения лямбда-функцию.
# 2, 3, 4, 6, 7, 8 -> 6, 7, 8
import random

length = int(input("Введите длину списка: "))
numbers = [random.randint(1, 10) for i in range(length)]
print(f"Начальный массив-->{numbers}<--")
print(f"Отсортированный массив-->{list(filter(lambda x: x > 5, numbers))}<--")

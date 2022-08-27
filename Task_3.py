# Задача 3. Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего совпадающих элементов есть в списке.
# Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают Список уникальных элементов [1, 4, 2, 3, 6, 7]

import random

length = int(input("Введите длину списка: "))
numbers = [random.randint(1, 10) for i in range(length)]
result = list(set(numbers))
different = (len(numbers) - len(result))
print(f"Начальный список-->{numbers}<--")
print(f"Список уникальных элементов -->{result}<-- {different} элемент{'a' if different < 4 else 'ов'} совпадают")

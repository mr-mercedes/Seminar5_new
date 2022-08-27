# Задача 2. Дан список случайных чисел.
# Создайте список, в который попадают числа, описывающие возрастающую последовательность.
# Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] =>[1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

def max_in_list(list_of_numbers):
    max = list_of_numbers[0]
    for i in list_of_numbers:
        if i > max:
            max = i
    return max


new_list_dic = {}
list_input =[1, 5, 2, 3, 4, 6, 1, 7]
index = 0

for n in range(1, len(list_input)):
    for i, item in enumerate(list_input[:-n]):
        new_list = [list_input[i]]
        for j, item_2 in enumerate(list_input[i + n:]):
            if item_2 > max_in_list(new_list):
                new_list.append(item_2)

        if new_list not in new_list_dic.values():
            new_list_dic[index] = new_list
            index += 1

for i in new_list_dic:
    print(f"{i} : \t{new_list_dic[i]}")

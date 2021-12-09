# Дан список размера N. Найти кол-во его промежутков монотонности(т.е. участков, на которых
# его элементы возрастают или убывают.
from random import randint

N = int(input('Введите N: '))
my_list = [randint(-100, 100) for i in range(N)]
# создаем список с рандомными элементами размера N
print(my_list)
count = 1
for i in range(len(my_list) - 2):
    # в цикле считаем экстремумы списка
    if my_list[i] < my_list[i + 1] > my_list[i + 2] or my_list[i] > my_list[i + 1] < my_list[i + 2]:
        count += 1
print(count)

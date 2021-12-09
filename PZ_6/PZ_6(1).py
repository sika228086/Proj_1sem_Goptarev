# Дан список A размера N и целое число K (1 < K < N). Вывести элементы список с порядковыми номерами
# кратными K: Ak, A2*k, A3*k,... Условный оператор не использовать.
from random import randint

N = int(input('Введите N: '))
A = [randint(-100, 100) for i in range(N)]
# создаем список с рандомными числами длиной N
print(A)
K = int(input('Введите K: '))
for i in range(K, len(A), K):
    print(A[i], end=' ')

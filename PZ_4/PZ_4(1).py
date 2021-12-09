# Программе дано целое число N (> 0). Найти сумму N2 + (N + 1)^2 + (N + 2)^2 + ... + (2N)^2

N = input('Введите N(N>0): ')
while type(N) != int or N <= 0:
    # обработка исключений
    try:
        N = int(N)
        if N <= 0:
            print('N <= 0')
            N = input('Введите N снова: ')
    except ValueError:
        print('Вы ввели не число')
        N = input('Введите N снова: ')
# инициализируем переменные
i = N
summa = 0

while i <= 2 * N:
    summa += i ** 2
    i += 1

print(summa)

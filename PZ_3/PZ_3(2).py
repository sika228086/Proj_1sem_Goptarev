# Программе дан номер месяца — целое число в диапазоне 1-12 (1 — январь, 2 — февраль и т. д.).
# Определить количество дней в этом месяце для невисокосного года.

n = input('Введите номер месяца: ')
while type(n) != int or n < 1 or n > 12:
    # обработка исключений
    try:
        n = int(n)
        if n < 1 or n > 12:
            print('Ошибка! Такого месяца нет')
            n = input('Введите номер месяца снова: ')
    except ValueError:
        print('Вы ввели не целое число')
        n = input('Введите номер месяца снова: ')

if n == 1 or n == 3 or n == 5 or n == 7 or n == 8 or n == 10 or n == 12:
    print('В этом месяце 31 день')
elif n == 4 or n == 6 or n == 9 or n == 11:
    print('В этом месяце 30 дней')
elif n == 2:
    print('В этом месяце 28 дней')

# Составить функцию решения задачи: из заданного числа вычли сумму его цифр. Из
# результата вновь вычли сумму его цифр и т.д. Через сколько таких действий получится нуль?

def foo(number):
    def digit_sum(num):
        # вспомогательная функция подсчета суммы цифр числа
        s = 0
        for i in str(num):
            s += int(i)
        return s

    count = 0
    while number != 0:
        number -= digit_sum(number)
        count += 1
    return count


n = int(input('Введите число: '))
print('Результат работы функции: ')
print(foo(n))

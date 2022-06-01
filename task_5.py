from functools import reduce

with open('task5.dat', 'w') as file:
    string = input('Введите числа, разделенные пробелом: ')
    file.write(string)

with open('task5.dat', 'r') as file:
    numbers = file.read().split()
    print('Сумма чисел: ', sum([int(el) for el in numbers]))

with open('task1.dat', 'w', encoding='utf-8') as file:
    print('Введите строку или отправте пустую строку для завершения записи в файл.')

    while string := input('Введите строку: '):
        print(string, file=file)

print('Запить в файл закончена.')

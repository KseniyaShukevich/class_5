with open('task1.dat', 'r', encoding='utf-8') as file:
    content = file.read()
    print('Количество строк в файле: ', content.count('\n'))

    file.seek(0)

    for number, line in enumerate(file.readlines()):
        print('Строка: ', line.replace('\n', ''))
        print(f'В строке {number + 1} число слов: {len(line.split())}')

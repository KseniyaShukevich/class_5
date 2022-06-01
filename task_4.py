my_dict = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}

with open('task4.dat', 'r') as file_1:
    with open('new_task4.dat', 'w', encoding='utf-8') as file_2:
        for line in file_1.readlines():
            word, *number = line.split()
            print(my_dict[word], ' '.join(number), file=file_2)

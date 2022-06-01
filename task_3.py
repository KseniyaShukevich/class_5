from functools import reduce

with open('task3.dat', 'r', encoding='utf-8') as file:
    salaries = []
    min_salary = {}

    for line in file.readlines():
        current_list = line.split()
        salaries.append(float(current_list[1]))

        if float(current_list[1]) < 20000:
            min_salary[current_list[0]] = current_list[1]

    print('С окладом меньше 20 000: ')

    for employee in min_salary.items():
        print(employee[0], employee[1])

    print('Средняя величина дохода сотрудников:', reduce(lambda a, b: a + b, salaries) / len(salaries))

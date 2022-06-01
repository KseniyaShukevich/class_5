with open('task6.dat', 'r', encoding='utf-8') as file:
    my_dict = {}

    for line in file.readlines():
        name, *rest = line.split()

        for item in rest:
            array = item.split('(')

            if array[0].isdigit():
                if not (name in my_dict):
                    my_dict[name] = 0

                my_dict[name] += int(array[0])

    print(my_dict)

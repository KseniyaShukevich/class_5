import json

with open('task7.dat', 'r', encoding='utf-8') as file:
    firms_dict = {}
    total_sum = 0
    count = 0

    for line in file.readlines():
        name, firm_type, revenue, costs = line.split()
        difference = int(revenue) - int(costs)
        firms_dict[name] = difference

        if difference > 0:
            total_sum += difference
            count += 1

    result = [firms_dict, {'average_profit': total_sum / count}]

    with open('new_task7.json', 'w', encoding='utf-8') as new_file:
        json.dump(result, new_file, ensure_ascii=False, indent=2)

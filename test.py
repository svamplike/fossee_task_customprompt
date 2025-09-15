import json

def process_data(filename, filter_key, filter_value, calc_field):
    with open(filename, 'r') as file:
        data = json.load(file)

    filtered_items = []
    for item in data:
        if item[filter_key] == filter_value:
            filtered_items.append(item)

    total = 0
    count = 0
    for item in filtered_items:
        total += item[calc_field]
        count += 1

    if count == 0:
        return 0

    return total / count

result = process_data("data.json", "category", "A", "value")
print(f"The average is: {result}")
import csv

filtered = []
filtered_stone_ids = []
duplicates_in_filtered = []
missing_from_filtered = []

with open('filtered.csv', mode='r') as filtered:
    csv_filtered_reader = csv.DictReader(filtered, delimiter=',')

    line_number = 0
    for row in csv_filtered_reader:
        if line_number == 0:
            print(f'Column names are {", ".join(row)}')
            line_number += 1
        else:
            line_number += 1
            stone_id = row.get("stoneId")
            if stone_id in filtered_stone_ids:
                duplicates_in_filtered.append(row)
                print(f'Duplicate found')
            else:
                filtered_stone_ids.append(stone_id)
                filtered.append(row)

    
with open('unfiltered.csv', mode='r') as unfiltered:
    csv_unfiltered_reader = csv.DictReader(unfiltered, delimiter=',')

    line_number = 0
    for row in csv_unfiltered_reader:
        if line_number == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            line_count += 1
            stone_id = row.get("stoneId")
            if not stone_id in filtered_stone_ids:
                missing_from_filtered.append(stone_id)


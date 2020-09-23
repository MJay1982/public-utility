import csv

filtered_arr = []
filtered_stone_ids = []
duplicates_in_filtered = []
missing_from_filtered = []
missing_from_filtered_ids = []

with open('filtered.csv', mode='r') as filtered:
    fieldnames = ['stoneId', 'color', 'cut', 'dimensions', 'caratWeight', 'isHeated', 'origin', 'usdPerCarat', 'case']
    csv_filtered_reader = csv.DictReader(filtered, fieldnames=fieldnames, delimiter=',')
    

    line_number = 0
    for row in csv_filtered_reader:
        # print(row)
        line_number += 1
        stone_id = row.get('stoneId')
        # print(stone_id)
        if stone_id in filtered_stone_ids:
            # print(stone_id)
            # print(filtered_stone_ids)
            duplicates_in_filtered.append(row)
            # print(f'Column values are {", ".join(row)}')
        else:
            # print(f'In else else')
            filtered_stone_ids.append(stone_id)
            # print(row)
            filtered_arr.append(row)
    # print(line_number)
    print(filtered_stone_ids)
    # print(filtered_arr)
    print(duplicates_in_filtered)
    
with open('unfiltered.csv', mode='r') as unfiltered:
    print(f'In open unfiltered.csv')
    fieldnames = ['stoneId', 'color', 'cut', 'dimensions', 'caratWeight', 'isHeated', 'origin', 'usdPerCarat', 'case']
    csv_unfiltered_reader = csv.DictReader(unfiltered, fieldnames=fieldnames, delimiter=',')

    line_number = 0
    for row in csv_unfiltered_reader:
        line_number += 1
        stone_id = row.get('stoneId')
        if not stone_id in filtered_stone_ids:
            missing_from_filtered_ids.append(stone_id)
            missing_from_filtered.append(row)
    # print(missing_from_filtered)
    print(missing_from_filtered_ids)

# with open('duplicate_stones.csv', mode='w') as duplicates:
#     print(f'In open duplicate_stones.csv')
#     fieldnames = ['stoneId', 'color', 'cut', 'dimensions', 'caratWeight', 'isHeated', 'origin', 'usdPerCarat', 'case']
#     duplicate_writer = csv.DictWriter(duplicates, fieldnames=fieldnames)

#     duplicate_writer.writeheader()
#     duplicate_writer.writerow({'stoneId':'blank', 'color':'blank', 'cut':'blank', 'dimensions':'blank', 'caratWeight':'blank', 'isHeated':'blank', 'origin':'blank', 'usdPerCarat':'blank', 'case':'blank'})
#     for row in duplicates_in_filtered:
#         duplicate_writer.writerow(row)

# with open('missing_stones.csv', mode='w') as missing:
#     print(f'In open missing_stones.csv')
#     fieldnames = ['stoneId', 'color', 'cut', 'dimensions', 'caratWeight', 'isHeated', 'origin', 'usdPerCarat', 'case']
#     missing_writer = csv.DictWriter(missing, fieldnames=fieldnames)

#     missing_writer.writeheader()
#     missing_writer.writerow({'stoneId':'blank', 'color':'blank', 'cut':'blank', 'dimensions':'blank', 'caratWeight':'blank', 'isHeated':'blank', 'origin':'blank', 'usdPerCarat':'blank', 'case':'blank'})
#     for row in missing_from_filtered:
#         missing_writer.writerow(row)
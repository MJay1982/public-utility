import uuid
import csv

appended_stone = []

with open('filtered_clean.csv', mode='r') as filtered:
    fieldnames = ['stoneId', 'color', 'cut', 'dimensions', 'caratWeight', 'isHeated', 'origin', 'usdPerCarat', 'case']
    csv_filtered_reader = csv.DictReader(filtered, fieldnames=fieldnames, delimiter=',')

    line_number = 0
    for row in csv_filtered_reader:
        line_number += 1
        row['id'] = uuid.uuid4()
        appended_stone.append(row)
    
with open('filtered_final.csv', mode='w', newline='') as target:
    fieldnames = ['id','stoneId', 'color', 'cut', 'dimensions', 'caratWeight', 'isHeated', 'origin', 'usdPerCarat', 'case']
    target_writer = csv.DictWriter(target, fieldnames=fieldnames)

    target_writer.writeheader()
    for row in appended_stone:
        target_writer.writerow(row)
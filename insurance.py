import csv

with open('insurance.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    total_age = 0
    row = 1

    for row in csv_reader:
        if line_count != 0:
            total_age += int(row[0])
            line_count += 1
        else:
            line_count += 1

    print("La edad promedio es", total_age/(line_count - 1))

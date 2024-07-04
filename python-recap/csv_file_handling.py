import csv
# with open('data2.csv', mode='r') as csv_file:
#     reader_variable = csv.reader(csv_file)
#     for row in reader_variable:
#         print(row)


with open('data2.csv', mode='w', newline='') as csv_file:
    writer_variable = csv.writer(csv_file)
    writer_variable.writerow([1.4,5457,45])
    writer_variable.writerow([1.4, 5457, 45])
    writer_variable.writerow([1.4, 5457, 45])
    writer_variable.writerow([1.4, 5457, 45])
    writer_variable.writerow([1.4,5457,45])
    writer_variable.writerow([1.4, 5457, 45])



# pliki csv - dane oddzielone znakiem podziału
import csv

row = ['Radek', 'Coe', '3', '0']
fields = ['name', 'branch', 'year', 'cgpa']

zipped_dict = dict(zip(fields, row))
print(zipped_dict)

with open("dane/records.csv", 'w') as csv_f:
    csvwriter = csv.writer(csv_f)
    csvwriter.writerow(row)

with open("dane/records_2.csv", 'w') as csv_f:
    csvwriter = csv.writer(csv_f)
    csvwriter.writerow(fields)
    csvwriter.writerow(row)

with open("dane/records_3.csv", 'w') as csv_f:
    csv_dict_writer = csv.DictWriter(csv_f, fieldnames=fields)
    csv_dict_writer.writeheader()
    csv_dict_writer.writerow(zipped_dict)

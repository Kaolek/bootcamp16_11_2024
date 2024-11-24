import csv

columns = []
rows = []

filename = 'dane/records_records_3.csv'

with open(filename, 'r') as f:
    dialect = csv.Sniffer().sniff(f.read(1024))
    print(dialect.delimiter)
    f.seek(0)
    csvreader = csv.reader(f, delimiter=dialect.delimiter)
    print(csvreader)
    columns = next(csvreader)
    for row in csvreader:
        rows.append(row)
print("Columns", columns)
print("Rows", rows)

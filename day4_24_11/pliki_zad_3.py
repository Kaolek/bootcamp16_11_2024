import pandas

data = pandas.read_csv('dane/records_discount.csv', delimiter=";")
print(data)
print(data.columns)
import csv
with open('example.csv',mode='w',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name','age'])
    writer.writerow(['agrim','19'])

with open('example.cvs', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
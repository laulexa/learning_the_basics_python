import csv

#Read a file
'''with open('products.csv', mode='r') as file:
    cvs_reader = csv.DictReader(file)
    for row in cvs_reader:
        print(row)'''

#show the information by columns
with open('products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(f"Product: {row['name']}, Price: {row['price']}")
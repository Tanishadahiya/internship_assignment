import csv
with open('list.csv','r') as file:
    a=csv.reader(file)
    for lines in a:
        print(lines)

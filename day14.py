import csv

with open("data.csv", 'w+') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['title', 'description'])
    writer.writerow(['row 1', 'some description'])


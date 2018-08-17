import csv

def getCSVData(fileName):
    rows = []
    datFile = open(fileName, "r")
    reader = csv.reader(datFile)
    next(reader)
    for row in reader:
        rows.append(row)
    return rows


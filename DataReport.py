#!/usr/bin/pythgon

import csv

SalesReport2014 = []
SalesReport2015 = []
SalesReport2016 = []

with open('SalesReport2014.csv', 'r') as SalesReport2014:
    SalesReport2014Reader = csv.reader(SalesReport2014)
    for i in (0, 10, 1):
        print(SalesReport2014Reader[i])
       # SalesReport2014.append(row)

with open('SalesReport2015.csv', 'r') as SalesReport2015:
    SalesReport2014Reader = csv.reader(SalesReport2015)
    for i in (0, 10, 1):
        print(SalesReport2015Reader[i])
       # SalesReport2015.append(row)

with open('SalesReport2016.csv', 'r') as SalesReport2016:
    SalesReport2016 = csv.reader(SalesReport2016)
    for i in (0, 10, 1):
        print(SalesReport2016Reader[i])
       # SalesReport2016.append(row)

with open('row_bind.csv', 'w') as rowFile:
    rowFileWriter = csv.writer(rowFile)
    for report14_row in SalesReport2014:
        combined_row = []
        combined_row.extend(report14_row)
        #del report14_row[0]
        #rowFileWriter.writerow(report14_row)
        rowFileWriter.writerow(combined_row)

    for report15_row in SalesReport2015:
        combined_row = []
        combined_row.extend(report15_row)
        #del report15_row[0]
        #rowFileWriter.writerow(report15_row)
        rowFileWriter.writerow(combined_row)

    for report16_row in SalesReport2016:
        combined_row = []
        combined_row.extend(report16_row)
        #del report16_row[0]
        #rowFileWriter.writerow(report16_row)
        rowFileWriter.writerow(combined_row)

outFile = open('outFile.csv', 'w')
outWriter = csv.writer(outFile)

import pandas as pd

import csv

# development_stages = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20', '21', '22', '23', '24', '25','26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40']
dev_stage_array = []

file = open('density2_test.csv')
type(file)

csvreader = csv.reader(file)

header = []
header = next(csvreader)
print("test")


rows = []
for row in csvreader:
        rows.append(row[2])
myset = list(set(rows))
gg = []
for ig in myset:
        gg.append(int(ig))
gg.sort()
print([str(x) for x in gg])

file = open('density2_val.csv')
type(file)

csvreader = csv.reader(file)

header = []
header = next(csvreader)
print("val")


rows = []
for row in csvreader:
        rows.append(row[2])
myset = list(set(rows))
gg = []
for ig in myset:
        gg.append(int(ig))
gg.sort()
print([str(x) for x in gg])

file = open('density2_train.csv')
type(file)

csvreader = csv.reader(file)

header = []
header = next(csvreader)
print("train")


rows = []
for row in csvreader:
        rows.append(row[2])
myset = list(set(rows))
gg = []
for ig in myset:
        gg.append(int(ig))
gg.sort()
print([str(x) for x in gg])


import pandas as pd

import csv

# development_stages = [2, 7, 12, 18, 21, 23, 26, 29, 30, 35, 36, 37, 38, 41, 44, 46, 47, 49, 52, 53, 54, 55, 59, 62, 64, 66, 79, 87, 90, 103, 118, 123, 163]
development_stages = ['d1','d2','d3','d4','d5','d6','d7','d8','d9','d10','d11','d12','d13']

dev_stage_array = []

file = open('official_train.csv')
metadatadomain = open('metadata_domainv2.csv')
type(file)
type(metadatadomain)

csvreader = csv.reader(file)
metareader = csv.reader(metadatadomain)

header = []
header = next(csvreader)
print(header)

headermeta = []
headermeta = next(metareader)
headermeta = headermeta[0].split(";")
print(headermeta)

rows = []
for row in csvreader:
        rows.append(row)

metarows = []
# tlistc = []
for row in metareader:
    newrow = row[0].split(";")
    metarows.append(newrow)

tllarr = []
for imgdata in rows:
    keynum = imgdata[2]
    themetarow = metarows[int(keynum)]
    whDensity = round(int(themetarow[6])/int(themetarow[5]))
    if whDensity not in tllarr :
        tllarr.append(whDensity)
    dval = "temp"
    if(whDensity <10):
        dval = "d1"
    elif(whDensity >=10 and whDensity <20):
        dval = "d2"
    elif(whDensity >=20 and whDensity <30):
        dval = "d3"
    elif(whDensity >=30 and whDensity <40):
        dval = "d4"
    elif(whDensity >=40 and whDensity <50):
        dval = "d5"
    elif(whDensity >=50 and whDensity <60):
        dval = "d6"
    elif(whDensity >=60 and whDensity <70):
        dval = "d7"
    elif(whDensity >=70 and whDensity <80):
        dval = "d8"
    elif(whDensity >=80 and whDensity <90):
        dval = "d9"
    elif(whDensity >=90 and whDensity <100):
        dval = "d10"
    elif(whDensity >=100 and whDensity <110):
        dval = "d11"
    elif(whDensity >=110 and whDensity <120):
        dval = "d12"
    elif(whDensity >=120):
        dval = "d13"
    indexval = development_stages.index(dval)
    imgdata[2] = int(indexval)
    dev_stage_array.append(imgdata)
# list3 = list(set(development_stages + development_stages2 + development_stages3))
# list3.sort()
# print(list3)
print(dev_stage_array[1000])
file.close()
metadatadomain.close()

df2 = pd.DataFrame(dev_stage_array,columns=header)
df2.sort_values(by=['domain'], inplace=True)
df2.to_csv("density2_train.csv",index=False)
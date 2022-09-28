import pandas as pd

import csv

development_stages = ["Spidercam","Gantry","Cart","Handheld","Tractor"]
# development_stages = ["Eschikon","Rothamsted","Gembloux","NMBU","Greoux","VLB","VSC","Mons","Toulouse","Saskatchewan","KSU","Maricopa AZ","Ciudad Obregon","NARO-Tsukuba","NARO-Hokkaido","Kyoto","Baima","Gatton","McAllister","Brookstead","Wad Medani"]
dev_stage_array = []

file = open('official_val.csv')
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
for row in metareader:
    newrow = row[0].split(";")
    metarows.append(newrow)

for imgdata in rows:
    keynum = imgdata[2]
    themetarow = metarows[int(keynum)]
    indexval = development_stages.index(themetarow[4])
    imgdata[2] = int(indexval)
    dev_stage_array.append(imgdata)

print(dev_stage_array[1000])
file.close()
metadatadomain.close()

df2 = pd.DataFrame(dev_stage_array,columns=header)
df2.sort_values(by=['domain'], inplace=True)
df2.to_csv("platform_val.csv",index=False)
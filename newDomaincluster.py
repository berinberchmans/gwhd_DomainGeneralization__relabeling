import pandas as pd

import csv

development_stages = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20', '21', '22', '23', '24', '25','26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40']
dev_stage_array = []

file = open('official_train.csv')
metadatadomain = open('theclusterdomain.csv')
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
metarows2 = []
for row in metareader:
    newrow = row[0].split("\t")
    metarows.append(newrow)
    metarows2.append(newrow[1])
# print(metarows[2])
for imgdata in rows:
    keynum = imgdata[0]
    innewcsvindex = metarows2.index(keynum)
    # print(innewcsvindex)
    # themetarow = metarows[int(keynum)]
    # indexval = development_stages.index(themetarow[3])
    indexval = metarows[innewcsvindex][2]
    imgdata[2] = int(indexval)
    dev_stage_array.append(imgdata)

print(dev_stage_array[1000])
file.close()
metadatadomain.close()

df2 = pd.DataFrame(dev_stage_array,columns=header)
df2.sort_values(by=['domain'], inplace=True)
df2.to_csv("cluster_train.csv",index=False)
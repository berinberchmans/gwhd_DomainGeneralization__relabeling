import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import pandas as pd

import csv


from pathlib import Path


ogdomainfile = open('tempfolder/official_test.csv')
newdomainfile = open('tempfolder/devstage_test.csv')
# densitytest = open('density_test.csv')
# density2test = open('density2_test.csv')
# platformtest = open('platform_test.csv')
# sublocationtest = open('sublocation_test.csv')


ogreader = csv.reader(ogdomainfile)
newreader = csv.reader(newdomainfile)
# densityreader = csv.reader(densitytest)
# density2reader = csv.reader(density2test)
# platformreader = csv.reader(platformtest)
# sublocationreader = csv.reader(sublocationtest)

header = []
header = next(ogreader)

headermeta = []
headermeta = next(newreader)
# headermeta1 = next(densityreader)
# headermeta2 = next(density2reader)
# headermeta3 = next(platformreader)
# headermeta4 = next(sublocationreader)


rows = []
for row in ogreader:
        rows.append(row[0])

rows1 = []
for row in newreader:
        rows1.append(row[0])

# rows2 = []
# for row in densityreader:
#         rows2.append(row[0])

# rows3 = []
# for row in density2reader:
#         rows3.append(row[0])

# rows4 = []
# for row in platformreader:
#         rows4.append(row[0])

# rows5 = []
# for row in sublocationreader:
#         rows5.append(row[0])

# (1278,1450)
for igg in range(0,299):
        imagenumber = igg
        imgaloc = rows1.index(rows1[imagenumber])
        imgb = rows.index(rows1[imagenumber])
        # imgc = rows2.index(rows1[imagenumber])
        # imgd = rows3.index(rows1[imagenumber])
        # imge = rows4.index(rows1[imagenumber])
        # imgf = rows5.index(rows1[imagenumber])
        print(imgaloc,imgb)

        data_folder = Path("predictions/devstage/images/")
        temppath = str(imgaloc) +'.png' 

        imgpath = data_folder / temppath
        img = mpimg.imread(imgpath)


        data_folder2 = Path("predictions/original/collection/")
        # data_folder3 = Path("predictions/density1/images/")
        # data_folder4 = Path("predictions/density2/images/")
        # data_folder5 = Path("predictions/platform/images/")
        # data_folder6 = Path("predictions/locv2/0/")

        temppath2 = str(imgb) +'.png' 

        imgpath2 = data_folder2 / temppath2
        img2 = mpimg.imread(imgpath2)

        # temppath3 = str(imgc) +'.png' 

        # imgpath3 = data_folder3 / temppath3
        # img3 = mpimg.imread(imgpath3)

        # temppath4 = str(imgd) +'.png' 

        # imgpath4 = data_folder4 / temppath4
        # img4 = mpimg.imread(imgpath4)

        # temppath5 = str(imge) +'.png' 

        # imgpath5 = data_folder5 / temppath5
        # img5 = mpimg.imread(imgpath5)

        # temppath6 = str(imgf) +'.png' 

        # imgpath6 = data_folder6 / temppath6
        # img6 = mpimg.imread(imgpath6)

        fig = plt.figure(figsize=(13, 13))
        fig.add_subplot(1, 2, 1)
        imgplot = plt.imshow(img2)
        plt.title("Default Domain")
        fig.add_subplot(1, 2, 2)
        imgplot = plt.imshow(img)
        plt.title("Development Stage Domain")
       
        # fig.add_subplot(2, 3, 3)
        # imgplot = plt.imshow(img3)
        # plt.title("density1")
        # fig.add_subplot(2, 3, 4)
        # imgplot = plt.imshow(img4)
        # plt.title("density2")
        # fig.add_subplot(2, 3, 5)
        # imgplot = plt.imshow(img5)
        # plt.title("location")
        # fig.add_subplot(2, 3, 6)
        # imgplot = plt.imshow(img6)
        # plt.title("platform")



        plt.savefig('comploc/devstage/'+str(imgaloc), bbox_inches='tight')
        # plt.show()




# imagenumber = 357
# imga = rows2.index(rows2[imagenumber])
# imgb = rows.index(rows2[imagenumber])
# print(imga,imgb)
# data_folder = Path("predictions/devstage/images/")
# temppath = str(imga) +'.png' 

# imgpath = data_folder / temppath
# img = mpimg.imread(imgpath)


# data_folder2 = Path("predictions/original/collection/")
# temppath2 = str(imgb) +'.png' 

# imgpath2 = data_folder2 / temppath2
# img2 = mpimg.imread(imgpath2)

# fig = plt.figure(figsize=(10, 10))
# fig.add_subplot(1, 2, 1)
# imgplot = plt.imshow(img)
# plt.title("devstage")
# fig.add_subplot(1, 2, 2)
# imgplot = plt.imshow(img2)
# plt.title("original")
# plt.show()
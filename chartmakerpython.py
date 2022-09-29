import matplotlib.pyplot as plt

thefile = "devstageconsole.txt"
def readDataFile(thefile):
        fileName = thefile
        print("Trying to open file="+str(fileName))
        data = []
        num_lines = 0
        try:
            with open(fileName) as f:
                lines = f.readlines()
                for line in lines:
                    line = line.strip()
                    if line.find("Validation ADA:")==0 and line.find("tensor(")>0:
                        tokens = line.split(' ')
                        newtoken =  tokens[3].split('(')
                        new_string = newtoken[1].replace(',', '')
                        data.append(float(new_string))
                        num_lines += 1
        except Exception as e:
            print("The error raised is: ", e)
        
        return data

splitdata = readDataFile(thefile)
epochs_range=[]
print(splitdata)
for i in range(0,len(splitdata)):
    epochs_range.append(i)
x = len(splitdata)
y = sum(splitdata)
print(y/x,x,y)
plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, splitdata, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Validation Average Domain Accuracy - Development Stage Domain')
plt.show()
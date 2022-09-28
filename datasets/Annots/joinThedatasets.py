import pandas as pd

fl1 = 'D:\FinalProject\domain-generalisation\datasets\Annots\density2_test.csv'
fl2 = 'D:\FinalProject\domain-generalisation\datasets\Annots\density2_train.csv'
fl3 = 'D:\FinalProject\domain-generalisation\datasets\Annots\density2_val.csv'

dataFrame = pd.concat(
   map(pd.read_csv, [fl2, fl3, fl1]), ignore_index=True)
# print(dataFrame)
pd2 = dataFrame['domain'].values.tolist()
pd2= sorted(pd2)
unique = dict(zip(pd2,[pd2.count(i) for i in pd2]))
print("Dictionary : ",unique)
print("count : ",len(unique))
# for i in range(1,5):
#    print(dataFrame[i])
# dataFrame.to_csv("fullLddddist.csv",index=False)


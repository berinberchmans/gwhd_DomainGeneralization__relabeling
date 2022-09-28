import pandas as pd

fl1 = 'D:\FinalProject\domain-generalisation\datasets\Annots\newdomains02\platform_test.csv'
fl2 = 'D:\FinalProject\domain-generalisation\datasets\Annots\newdomains02\platform_train.csv'
fl3 = 'D:\FinalProject\domain-generalisation\datasets\Annots\newdomains02\platform_val.csv'

dataFrame = pd.concat(
   map(pd.read_csv, [fl2, fl3, fl1]), ignore_index=True)
print(dataFrame)

# dataFrame.to_csv("fullList.csv",index=False)


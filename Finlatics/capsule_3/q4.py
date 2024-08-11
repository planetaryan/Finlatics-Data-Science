import pandas as pd

data={"Employee_name":["Arav","Aryan","Raj","Simran","Rajesh"],
      "Income":[12300,45356,45453,87655,76546]}

df=pd.DataFrame(data,index=['a','b','c','d','e'])

print(df)
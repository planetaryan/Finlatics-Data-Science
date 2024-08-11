import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=sns.load_dataset('titanic')

pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)

# print(df.head(10))

# print(df.tail())

# print(df.info())

# print(df.shape)

# print(df.columns)

unique_counts=df.nunique()
# print(unique_counts)

age_unique_values=df['age'].unique()
# print(age_unique_values)

gender_value_counts=df['sex'].value_counts()
# print(gender_value_counts)

grouped_data=df.groupby(['sex','survived'])['survived'].count()
# print(grouped_data)

embarked_class_survival_data=df.groupby(['embark_town','pclass','survived'])['survived'].count()
# print(embarked_class_survival_data)

# sns.countplot(x="sex",hue="survived",data=df)
# plt.xlabel("Gender")
# plt.ylabel("Survival")
# plt.title("Survival by Gender")
# plt.show()

# sns.catplot(x="embark_town",hue="survived",col="pclass",data=df,kind="count",palette="Set2")
# #x=x-axis,y=y-axis,col=no. of subplots to be made based on the number of unique values
# plt.show()

# print(df.describe())
# print(df['embark_town'].describe())# for categorical variable

# print(df['alive'].value_counts())
# print(df['survived'].value_counts())

df.drop(columns=['alive'],inplace=True)
# print(df.columns)

# print(df['embarked'].value_counts())
# print(df['embark_town'].value_counts())

df.drop(columns=['embarked'],inplace=True)

# print(df['class'].value_counts())
# print(df['pclass'].value_counts())

df.drop(columns=['class'],inplace=True)

#========================================================================================

# print(df['adult_male'].value_counts())

df['adult_male'].replace({True:1,False:0},inplace=True)
# print(df['adult_male'].head())

# print(df.isnull().sum())

# sns.boxplot(y='age',data=df)
# plt.show()

df['age']=df['age'].fillna(df['age'].median())

df['deck']=df['deck'].fillna(df['deck'].mode()[0])#mode returns a series...select first element

# print(df['embark_town'].isna().sum())

df.dropna(subset=['embark_town'],inplace=True)

# print(df.isnull().sum())

df.rename(columns={'deck':'cabin'},inplace=True)
# print(df.columns)

# print(df['who'].unique())

# plt.hist(df['who'],color='skyblue',edgecolor='black')
# plt.xlabel('Passenger type')
# plt.ylabel('Frequency')
# plt.show()

# ============================================================================

# numeric_df=df.select_dtypes(include=['int64','float64'])
# corr_matrix=numeric_df.corr()
# plt.figure(figsize=(10,8))
# sns.heatmap(corr_matrix,annot=True,cmap='PuBuGn',fmt='.2f')
# plt.show()



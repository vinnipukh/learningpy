import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

df = pd.read_csv("titanic.csv")
df = df.drop(columns=["PassengerId","Name","Ticket","Cabin"])
print(df["Age"].isnull().sum())

"""
#plotting part

age_counts = df['Age'].value_counts()
plt.style.use("dark_background")
plt.figure(figsize=(10,10))
plt.bar(age_counts.index, age_counts.values,color="Aqua")
plt.title("Age Distribution")
plt.xlabel("Age",fontsize=10)
plt.ylabel("Age Count(how many people are x years old)",fontsize=10)
plt.show()
"""

#training part
df["Age"] = df["Age"].replace(np.nan,df["Age"].median())
df.info()



X_train,X_test,y_train,y_test = train_test_split()





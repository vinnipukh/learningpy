import pandas as pd
import numpy as np

df = pd.read_csv("titanic.csv")
df = df.drop(columns=["PassengerId","Name","Ticket","Cabin"])
print(df["Age"].isnull().sum())
df["Age"] = df["Age"].replace(np.nan,df["Age"].median())
print(df.info())



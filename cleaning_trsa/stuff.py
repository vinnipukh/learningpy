import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'C:\Users\arhan\PycharmProjects\learningpy\cleaning_trsa\merged_semeval.csv')
print("df head :", df.head())
print("df info", df.info())
print("df describe", df.describe())
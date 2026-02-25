import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Social_Network_Ads.csv")
x = df.iloc[:, [2, 3]].values
y = df.iloc[:, 4].values
print(df.head())
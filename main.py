import pandas as pd

df = pd.read_csv("dataset.csv")

df.shape

df.tail()

df.info()

df.dytpes

# Analise dados
import seaborn as sns
import matplotlib.pyplot as plt

#
sns.countplot(data["max_prt"])

#
sns.lineplot(x="date", y="poir", data=df, hue="Leg")
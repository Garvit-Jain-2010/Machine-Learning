import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("penguins")
# sns.lineplot(data=df, x = "bill_depth_mm", y="bill_depth_mm", hue = "island")
# sns.histplot(data=df, x = "bill_length_mm", edgecolor="r", kde=True, rug = True)
# sns.scatterplot(data=df, x = "bill_length_mm", y = "bill_depth_mm", hue="sex")
# sns.heatmap(data=dfttttttttttttttttt)
plt.show()
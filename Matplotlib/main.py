import matplotlib.pyplot as plt 
import pandas as pd

# days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# temperature = [36.6, 37, 37.7, 39, 40.1, 43, 43.4, 45, 45.6, 40.1, 44, 45, 46.8, 47, 47.8]

# plt.title("Gwalior Temperature")
# plt.xlabel("Days", fontsize = 20)
# plt.ylabel("Temperature", fontsize = 20)
# plt.bar(days,temperature, color = "#e67e22", width=0.5)
# plt.show()

# -------------------------------------------------------------

# df = pd.read_excel("E:\Coding\Machine Learning\Pandas\Book2.xlsx")

# plt.xlabel("Product Name", fontsize = 20)
# plt.ylabel("Total Amount", fontsize = 20)
# plt.bar(df["Product Name"],df["Total Amount"], color = "#e67e22", width=0.5, align="edge", edgecolor="black", linewidth = 3, linestyle = "--")
# plt.xticks(rotation = 45)
# plt.yticks(rotation = 45)
# plt.show()

# ------------------------------------------------------------

# x = [10, 20, 30, 40, 50]
# y = [20, 30, 40, 50, 60]
# c = ["red", "green", "blue", "yellow", "magenta"]
# size = [400, 500, 600, 700, 800]

# plt.scatter(x, y, color = c, sizes = size, marker="z")
# plt.show()

# --------------------------------------------

# x = [10, 20, 30, 40, 50]
# y = [20, 30, 40, 50, 60]

# plt.scatter(x, y, c=[10, 20, 30, 40, 50], marker='h', cmap="Accent_r")
# plt.colorbar()
# plt.show()

# -----------------------------------------------

# x = [10, 20, 30, 40]
# y = ["Python", "C++", "Java", "C"]

# plt.pie(x, labels=y, autopct="%0.0f%%", explode=[0.1, 0.1, 0.1, 0.1], shadow=True, radius=1.2)
# plt.legend(loc = "center left")
# plt.show()

# ----------------------------------------------

# x = [1, 2, 3, 4, 5, 6]
# y = [2, 2, 5, 7, 3, 8]

# plt.stem(x, y, linefmt = "-.", markerfmt="m*", basefmt="g", orientation="horizontal")
# plt.show()

# ------------------------------------------

# x = [10, 20, 30, 40]
# plt.boxplot(x, notch = True, widths = 0.4, patch_artist=True, showmeans=True, boxprops=dict(color = "r"), capprops=dict(color = "r"), whiskerprops=dict(color = "red"))
# plt.show()

# ----------------------------------------------

# x = ["Python", "SQL", "C", "C++", "Java"]

# a = [2, 3, 4, 5, 2]
# b = [3, 4, 5, 2, 1]
# c = [5, 3, 2, 6, 3]

# plt.stackplot(x, a, b, c, labels=["A", "B", "C"])
# plt.legend(loc = 1)
# plt.grid()
# plt.show()

# ---------------------------------------------

# a = [2, 3, 4, 5, 2]
# b = [3, 4, 5, 2, 1]

# plt.plot(a)
# plt.plot(b)
# plt.text(2, 5, "Python", fontsize = 15, style = "italic", bbox={"facecolor":"blue"})
# plt.annotate("C++", xy = (2, 1), xytext=(3, 3), arrowprops={"facecolor":"Red"})
# plt.show()

# --------------------------------------------

# x = [1, 2, 3, 4]
# y = [1, 2, 4, 4]
# plt.step(x, y, marker = 'o', ms = 10, mfc="g", label = "Python")
# plt.grid()
# plt.show()

# -------------------------------------------

# no = [49, 45, 54, 16, 31, 56, 28, 33, 18, 48, 54, 21, 53, 43, 30, 23, 48, 33, 54, 47, 22, 34, 59,
    #   55, 44, 54, 35, 18, 24, 37, 53, 19, 42, 14, 26, 43, 13, 37, 25, 28, 63, 34, 40, 45, 64, 29,
    #   52, 25]

# l=[10, 20, 30, 40, 50, 60]

# plt.hist(no, color="yellow", edgecolor = "red", histtype="barstacked", rwidth=0.5, bins=l)
# plt.show()

# --------------------------------------------
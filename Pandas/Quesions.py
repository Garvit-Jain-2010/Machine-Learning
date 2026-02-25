import pandas as pd

data = {"Vikas":{"Hindi":90, "English":89, "Science":95},
        "Rahul":{"Hindi":95, "English":47, "Science":75},
        "Mohit":{"Hindi":67, "English":78, "Science":85},
        "Rohit":{"Hindi":49, "English":69, "Science":35},
        "Garvit":{"Hindi":56, "English":67, "Science":89}}

# 1. Fetch all the marks of mohit
df = pd.DataFrame(data)
print(df["Mohit"])

# 2. Fetch maths and english marks of mohit and rohit
print(df.loc[["English", "Maths"], ["Mohit", "Rohit"]])

# 3. Read a CSV file
df = pd.read_csv("Dataset.csv", sep = ",")
print(df)

# 4. Export the datasent to .txt file
df.to_csv("dataset.txt", sep="\t")

# 5. Delete english marks for rohit and mohit
df = df.loc[:, ["Rohit", "Mohit"]].drop(labels = ["English", "Science"])
print(df)

# 6. Iterate all the rows of dtaframe
for name in df.iterrows():
    print(name)

# 7. add2 series

a = pd.Series([1, 2, 3, 4, 5], index = ["a", "b", "c", "d", "e"])
b = pd.Series([6, 7, 8, 9, 10], index = ["z", "y", "a", "c", "e"])


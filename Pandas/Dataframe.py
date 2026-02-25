import pandas as pd
import numpy as np

# df = pd.DataFrame()
# print(df)

# ------------------------------------------

a = np.array([10, 20, 30])

df = pd.DataFrame(a)
print(df)

# -------------------------------------------

# a = np.array([10, 20, 30])
# b = np.array([40, 50, 60])
# c = np.array([70, 80, 90])

# df = pd.DataFrame([a, b, c])
# print(df)

# df = pd.DataFrame([a, b, c], columns = ["A", "B", "C"])
# print(df)

# df = pd.DataFrame([a, b, c], columns = ["A", "B", "C"], index = ["A", "B", "C"])
# print(df)
# -----------------------------------------

# dict = [{"a":10, "b":20, "c":30}, {"a":40, "b":50, "c":60}]

# df = pd.DataFrame(dict)
# print(df)

# ------------------------------------

# dict = {"State":["Assam", "Delhi", "Kerala"], "GArea":[78438, 1483, 38852], "VDF":[2797, 6.72, 1663]}

# df = pd.DataFrame(dict)
# print(df)
# print(df.T) # T --> Transpose (change the position of rows and coulmns)

# ------------------------------------------------

# x = pd.Series([1, 2, 3, 4, 5], index = ["a", "b", "c", "d", "e"])
# y = pd.Series([6, 7, 8, 9, 10], index = ["a", "b", "c", "d", "e"])
# z = pd.Series([11, 12, 13, 14, 15], index = ["z", "y", "a", "c", "e"])

# df = pd.DataFrame([x, y, z])
# print(df)

# ---------------------------------------------------

# result = {"Arnav": pd.Series([90, 91, 70], index = ["Maths", "Science", "English"]), "Aarav": pd.Series([94, 71, 80], index = ["Maths", "Science", "Hindi"])}

# df = pd.DataFrame(result)
# print(df)

# -----------------------------------------------------

# data = {"Arnav":{"English":80, "Maths":87, "Science":91}, 
        # "Garvit":{"English":90, "Maths":56, "Science":61}, 
        # "Aarush":{"English":71, "Maths":93, "Science":59}}

# df = pd.DataFrame(data)
# print(df)

# -----------------------------------------------------

# data = {"Arnav":pd.Series([90, 91, 70], index = ["Maths", "Science", "English"]), 
        # "Aarav": pd.Series([94, 71, 80], index = ["Maths", "Science", "Hindi"])}

# df = pd.DataFrame(data)
# df["Arnav"] = 90
# print(df["Arnav"])
# print(df[["Arnav", "Aarav"]])

# -----------------------------------------------------------

# data = {"Arnav":pd.Series([90, 91, 70], index = ["Maths", "Science", "English"]), 
        # "Aarav": pd.Series([94, 71, 80], index = ["Maths", "Science", "English"])}

# df = pd.DataFrame(data)
# df = df.rename({"Maths":"Sub1", "Science":"sub2", "English":"Sub3"}, axis = 0)
# print(df)

# ------------------------------------------------------------


# data = {"Arnav":pd.Series([90, 91, 70], index = ["Maths", "Science", "English"]), 
        # "Aarav": pd.Series([94, 71, 80], index = ["Maths", "Science", "English"])}

# df = pd.DataFrame(data)
# print(df.loc[:]>90)
# print(df[:]>90)

# ------------------------------------


# data = {"Arnav":pd.Series([90, 91, 70], index = ["Maths", "Science", "English"]), 
#         "Aarav": pd.Series([94, 71, 80], index = ["Maths", "Science", "English"]),
#         "Malika":pd.Series([90, 91, 70], index = ["Maths", "Science", "English"]), 
#         "Rajni": pd.Series([94, 71, 80], index = ["Maths", "Science", "English"])}

# df = pd.DataFrame(data)
# df.loc['Science', "Arnav":"Rajni":3 ] = 1000
# df['Arnav']['Maths'] = 1000
# print(df)

# ------------------------------------------------

# data = {"Arnav":pd.Series([90, 91, 70], index = ["Maths", "Science", "English"]), 
        # "Aarav": pd.Series([94, 71, 80], index = ["Maths", "Science", "English"]),
        # "Malika":pd.Series([90, 91, 70], index = ["Maths", "Science", "English"]), 
        # "Rajni": pd.Series([94, 71, 80], index = ["Maths", "Science", "English"])}

# df = pd.DataFrame(data)
# print(df.loc[:, [True, False, True, False]])

# -----------------------------------------------

# df = pd.read_csv("Dataset.csv", sep = ",")
# print(df)

# ----------------------------------------------

# data = {"Arnav":{"Maths":78, "Science":89, "Hindi":70},
#         "Radhika":{"Maths":89, "Science":69, "Hindi":72}}

# df = pd.DataFrame(data)
# df.to_csv(path_or_buf="E:\Coding\Machine Learning\Pandas\Data.csv")
# print(df)

# --------------------------------------------------


# data = {"Arnav":{"Maths":78, "Science":89, "Hindi":70},
#         "Radhika":{"Maths":89, "Science":69, "Hindi":72}}

# df = pd.DataFrame(data)
# print(df.info())
# print(df.describe())
# print(df.axes)

# d = df.sort_values("Arnav")
# print(d)

# d = df.sort_index(ascending=False)
# print(d)

# d = df.astype(float)
# print(d)

# ----------------------------------------------

# data = {"Arnav":{"Maths":78, "Science":89, "Hindi":70},
#         "Radhika":{"Maths":89, "Science":69, "Hindi":72}}

# df = pd.DataFrame(data)

# for name, series in df.items():
#     print(name, series)

# for name in df.iterrows():
#     print(name)

# ---------------------------------------------

# data = {"Arnav":{"Maths":-78, "Science":89, "Hindi":70},
        # "Radhika":{"Maths":89, "Science":-69, "Hindi":72}}

# df = pd.DataFrame(data)
# print(df.abs())
# print(df.add(5)) 

# ----------------------------------------------

# data = {"Vikas":{"Hindi":90, "English":89, "Science":95},
#         "Rahul":{"Hindi":95, "English":47, "Science":75},
#         "Mohit":{"Hindi":67, "English":78, "Science":85},
#         "Rohit":{"Hindi":49, "English":69, "Science":35},
#         "Garvit":{"Hindi":56, "English":67, "Science":89}}

# df = pd.DataFrame(data)
# print(df.count(axis = 0))

# -------------------------------------------------

# data = {"Vikas":{"Hindi":90, "English":89, "Science":95},
#         "Rahul":{"Hindi":95, "English":47, "Science":75},
#         "Mohit":{"Hindi":67, "English":78, "Science":85},
#         "Rohit":{"Hindi":49, "English":69, "Science":35},
#         "Garvit":{"Hindi":56, "English":67, "Science":89}}

# df = pd.DataFrame(data)
# df = df.cummax()
# print(df)
# df = df.cummin()
# print(df)
# df = df.cumsum()
# print(df)
# df = df.mean()
# print(df)
# df = df.diff()
# print(df)

# --------------------------------------------------

# df = pd.DataFrame({
#     "A" : [1, 2],
#     "B" : [3, 4]
# })

# s = pd.Series([10, 20], index = ["A", "B"])

# result = df.dot(s)
# print(result)

# ---------------------------------------------------

# data = {"Vikas":{"Hindi":90, "English":89, "Science":95},
        # "Rahul":{"Hindi":95, "English":47, "Science":75},
        # "Mohit":{"Hindi":67, "English":78, "Science":85},
        # "Rohit":{"Hindi":49, "English":69, "Science":35},
        # "Garvit":{"Hindi":56, "English":67, "Science":89}}

# df = pd.DataFrame(data)
# f = df.where(df>90)
# print(f)

# -------------------------------------------------

# data = {
#     "First":["Corey", "Jane", "John"],
#     "Last":["Schafer", "Doe", "Doe"],
#     "Email":["CoreyMSchfer@gmail.com", "JaneDoe@gmail.com", "JohnDoe@gmail.com"]
# }

# df = pd.DataFrame(data)
# filt = (df["Last"] == "Doe") & (df["First"] == "John")
# a = df.loc[filt, "Email"]
# print(a)
# a = df.loc[~filt, "Email"]
# print(a)

# --------------------------------------------

# data = {
#     "First":["Corey", "Jane", "John"],
#     "Last":["Schafer", "Doe", "Doe"],
#     "Email":["CoreyMSchfer@gmail.com", "JaneDoe@gmail.com", "JohnDoe@gmail.com"]
# }

# df = pd.DataFrame(data)

# filt = (df["First"].isin(["Jane"])) & (df["Last"].isin(["Doe"]))
# print(df.loc[filt, "Email"])

# filt = df["First"].srt.uppercase()  # Can call any srting function like this
# print(filt)

# ---------------------------------------------

# data = {
#     "First":["Corey", "Jane", "John"],
#     "Last":["Schafer", "Doe", "Doe"],
#     "Email":["CoreyMSchfer@gmail.com", "JaneDoe@gmail.com", "JohnDoe@gmail.com"]
# }

# df = pd.DataFrame(data)
# idx = df.coulmns.rename(column={"First", "1st"})
# print(idx)

# ---------------------------------------------------

customers = pd.read_excel("Book1.xlsx")
orders = pd.read_excel("Book2.xlsx")

# print(customers)
# print(orders)

df = pd.merge(left=orders, right=customers, left_on="Customer ID", right_on="Customer ID", how = "inner")
print(df)
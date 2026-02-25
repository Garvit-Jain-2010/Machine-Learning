import pandas as pd
import re

df = pd.read_csv("IMDB Dataset.csv")
# print(df.shape)
# print(df.head())
# print(df.tail())
# df["review"] = df["review"].str.lower()
# print(df)

def remove_html_tag(text):
    pattern = re.compile("<.*?>")
    return pattern.sub(r'', text)

# text = '<html><body><p>Movie 1</p><p> Actor - Amir Khan</p><p> Click Here to <a href = "http://google.com">download</a></p></body><html>'

# print(remove_html_tag(text))

# df["review"]=df["review"].apply(remove_html_tag)
# print(df)

def remove_url(text):
    pattern = re.compile(r'https?://\S+|www\.\S+')
    return pattern.sub(r'', text)
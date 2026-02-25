import pandas as pd
import requests

# df = pd.read_json("solar_system.json")
# print(df)

url = "https://dummyjson.com/users"

response = requests.get(url)
data = response.json()

dg = pd.DataFrame(data)
print(dg.head(5))
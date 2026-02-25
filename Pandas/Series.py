import pandas as pd
import numpy as np

# j = pd.Series([2, 3, 4], index = ["Feb", "March", "April"])
# print(j["March"])

# k = pd.Series(["New Delhi", "WashingtonDC", "London", "Paris"], index = ["India", "U.S.A.", "U.K", "France"])
# print(k["India"])

# l = [10, 20, 30]
# s = pd.Series(l, index=["Python", "C", "Java"])
# a = pd.Series(np.arange(1, 6, 1), index = ['a', 'b', 'c', 'd', 'e'])
# s[1:-2] = 69
# s[[0, 1]] = 67, 78
# print(s)
# print(s[["Python", "C"]])
# print(s[[0, 1]])
# print(s[0:2])
# print(s[0:-1])
# print(s[::])
# print(s[::-1]) # Reverse the series

# s = pd.Series(["rg", "wg", "rh", "kh"], index = ["gh", "jb", "fs", "lk"])
# s.name = "Capitals"
# print(s)

# s.index.name = "Counties"
# print(s)

# print(s.values)
# print(s.size)
# print(s.empty)
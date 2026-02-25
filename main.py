import re

# text = "I love learning Python. My birthday is on 454545 and contack number is @(#*$&@O#"

# matches = re.findall("[0-9a-zA-Z]", text)
# print(matches)
# matches = re.findall("[^0-9a-zA-Z]", text)   # ------> For not and rest except
# print(matches)

# Character Classes
# \s  -------> space character
# \S  -------> except space character
# \w  -------> any digit
# \W  -------> except digit
# \d  -------> any [a-zA-Z0-9]
# \D  -------> except [a-zA-Z0-9]


# text = "python is too easy"
# s = input("Enter the text: ")

# result = re.match('o', text)

# if result != None:
#     print("The string started from given alphabate")
# else:
#     print("Match is not found");

# result = re.fullmatch(s, text)

# if result != None:
    # print("The given string is fully matched")
# else:
    # print("Match is not found");

# result = re.search(s, text)

# if result != None:
    # print(f"The given string is matched and index is {result.start()} to {result.end()}")
# else:
    # print("Match is not found")

# ---------------------------------------------------

# text = "Hello I am Garvit Raj Jain"

# a = input("Enter what u want to replace: ")
# b = input("Enter the replacement: ")

# result = re.sub(a, b, text)
# result = re.subn(a, b, text) # ----> will give the final output and number of words replaced

# print(result)

# ---------------------------------------------------

# text = "ram,shyam,rohan,mohan,kishan"

# result = re.split(",",text)
# print(result)

# ---------------------------------------------------


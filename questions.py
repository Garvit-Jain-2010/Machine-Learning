import re

# Email Checker
email = input("Enter your email: ")

pattern = r'^\w+@\w+\.\w+$'

if re.match(pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")

# Word Replacer
text = "Hello I am Garvit Raj Jain"

a = input("Enter what u want to replace: ")
b = input("Enter the replacement: ")

result = re.sub(a, b, text)
print(result)

# Vowel Counter
text = input("Enter a sentence: ")

vowels = re.findall(r'[aeiouAEIOU]', text)

count = 0
v = "aeiou"
for i in v:
    for j in vowels:
        if i == j:
            count+=1
    print(f"{i} = {count}")
    count = 0
import re
x = input("enter your string")
y = len(x)
if re.findall("^(a)b*c(a+b)", x):
    print("string is accepted")
else:
    print("not accepted")


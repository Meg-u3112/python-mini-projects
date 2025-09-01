
a="  HELLO, MEGU!  "

print(a.upper())
print(a.lower())
print(a.replace("L","O"))
print(a.strip())
print(a.split(","))

b="this is  \bMegu"
print(b)
b="this is  \rMegu"
print(b)

b="this is  \nMegu"
print(b)
b="this is  \\Megu"
print(b)
b="this is  \tMegu"
print(b)
b="\123\110"
print(b)


c=a+b
print(c)

price=45
txt=f"this is {price}"
print(txt)
txxt=f"this is {price:.2f}"
print(txxt)
res=f"this is {2*12}"
print(res)



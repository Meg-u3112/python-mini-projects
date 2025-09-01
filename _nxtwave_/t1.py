x = int(input("Enter base (x): "))
n = int(input("Enter exponent (n): "))

pd = 1
i = 1

while i <= n:
    pd *= x
    i += 1

print(pd)
print("-------")
h=3
c=1
sum=0
while(c<=h):
    sum=c*c
    c=c+1
print(sum)    
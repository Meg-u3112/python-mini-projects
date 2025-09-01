x ="python" #python
for i in x:
    print(i)
print("--------")    
c="query"
first_char=c[0]
for i in range(len(c)):

    print(first_char)
print("--------")    
d="megu"
for i in d:
    print(i)
print("--------")   
f=5
i=1
while i<=f:
    print(i)
    i+=1
print("--------")   
o=6
i=1
sum=0
while i<=o:
#    sum=i+sum
    sum=o*(o+1)//2

    i+=1
print(sum) 
print("--------")   
u=8
i=1
while i<=8:
    sum=u*(u+1)//2
    i+=1
print(sum/u)    
print("--------")   
y=3
i=1
cube=0
while i in range(y+1):
    prd=i*i*i
    cube +=prd
    i+=1
    print(prd )    
    print(cube )
print("--------")   
#t = 3
#for i in range(t):
   # y = int(input())
#print("--------") 
qq1=3
prd2=1
for i in range(1,qq1+1):
    prd2*=i
    print(prd2)
print("--------")  
star = 4
for i in range (1,star+1):
    print("*"*i)  
    i+=1
print("--------")
f= "MEgu"
print("-".join(f))
var=f[0]
for i in range(1,len(f)):
    var=var+"-"+f[i]
print(var)
print("--------")
p = 789
total = 0
p_str = str(p)

for i in range(len(p_str)):
    total += int(p_str[i])

print(total)
print("--------")
re = 2
uo = 4
Me = 0

for i in range(re, uo + 1):
    Me += i ** 2 
    i+=1

print(Me)
print("--------")
a=9
sum=0
for i in range(a+1):
    if i%2==0 :
        sum+=i

print(sum)
print("---------")
b=1
cc=9
sum=0
for i in range(b,cc+1):
    if i%2!=0 :
        sum+=i

print(sum)
print("---------")
n=int (input())
li=[]
i=1
for i in range(n):
    li.append(int(input()))
print(f"max -> -> {max(li)}")   
print("---------")













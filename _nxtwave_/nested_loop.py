n="megu"
v=len(n)
p=[1,2,3,1]
for i in p:

    res=n[i]
    print(res)
print("---------------------")
n="kolathur"
res=""
for i in n:
    res=res+i
    print(res)
print("---------------------")
n=4
for i in range(n):
    for j in range(n):
        print(i,end=" ")
    print()
print("---------------------")
s=5
n=4
for i in range(0,n):
    for j in range(s,s+n):
        print(j,end=" ")
    print()        
print("---------------------")
f=10300800
s=str(f)
count=""
for i in s:
    if(i=="0"):
        count+=i
c=len(count)
if(c>3):
    print("yes! its > than 3")
else:
    print("nope")    
print("---------------------")
p=1456789876543
c=0
for i in str(p):
    if int(j)%2==0:
        c+=1
if c>2:
    print("count of even is >2")
else:
    print("noppe")        
print("---------------------")
u=7
fact=0
for i in range(2,u):
    if n%i==0:
        fact+=1
if fact==0:
    print("prime")        
else:
    print("💰")
print("---------------------")
o=5
for i in range (1,o+1):
    print("* "*(o-i))
print("---------------------")
n=5

for i in range (1,n+3):
    o=("   ")*n
    f=(" - ")*n
    if i==1 or i==n+2:
        print("+" + f + "+" )
    else:
        print("|" + o + "|" )    


print("---------------------")
n1="AToyStory"
n2=n1.upper()
result=""
for i in n1:
    for j in n2:
        if(i==j):
            print(i)
            result=i+"-"
print(result)        
print("---------------------")
n=5
for i in range (1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()    
print("---------------------")
n=4
for i in range (n+1,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()    
print("---------------------")
n=3
m=15

for i in range (n,m+1):
    co=0
    for j in range(1,i+1):
        if i%j==0:
            co+=1
    if co == 2:
        print(i)    
print("---------------------")
u=2
res=6
for i in range(1,n+1):
    for j in range(1,n+1):
        res+=1
        print(res,end=" ")
    print()
print("---------------------")
s=6
n=3
for i in range(1,n+1):
    res=""
    for j in range(i): # ---> i*2 will be multiple of 2 tables  
        res+=str(s)+" "
        s=s+1
    print(res)
print("---------------------")
s=3
n=4
k=s*n
for i in range(1,s+1):
    res=""
    for j in range(1,n+1): 
        res+=str(k)+" "
        k-=1
    print(res)
print("---------------------")
col = 2
res=0
for i in range (1,col+1):
    for j in range(1,col+1):   
        res+=1
        
        print(res,end=" ")
    print()
print("---------------------")
n=4
for i in range(1,n+1):
    res=""
    for j in range(1,i+1):
        res+=str(j)+" "
    for k in range(1,i):
        res+=str(k)+" "
    print(res)
print("---------------------")
row=6
start_no=16
res=start_no
for i in range(1,row+1):
    for j in range(1,i+1):
        print(res,end=" ")
        res+=1
    print()
print("---------------------")
row = 5
st_no = 15
res=st_no
for i in range(1,row+1):
        sp=("-")*i
        res=st_no*i
        print(sp+str(res))
        res-=1
print("---------------------")
n=5
count=0
for tot in range(1,n+1):
    count+=tot   # ------>>>>> count=n*(n+1)//2
print(count)
for i in range(1,n+1):
    print("--"*2*(i-1),end="")
    for j in range(i,n+1):
        print(f"{count:2}",end="``")
        count-=1
    print()       
print("---------------------")
row=3
column=4
k=row*column
for i in range(1,row+1):
    for j in range(1,column+1):
        print(str(k),end=" ")
        k-=1
    print()
print("---------------------")
n=10
count=0
for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            if i<j<k and i+j+k==n:
                count+=1
print(count)

print("---------------------")
n=5
start_no=10
countt= n * ( n + 1 ) // 2
print(countt)
res=""
for i in range(1,n+1):
    res= str(countt)
    start_no-=1
    print(res,end=" ")
print()   
print("---------------------")
n=4
for i in range (1,n+1):
        space=("-")*(n-i)
        print(space,end="")
        for j in range(1,i+1):
            res= str(i)
            print(res,end="")
            i-=1
        print()
print("---------prime-no--------")
n=10
for i in range (2,n+1):
    fact =0
    for j in range (2,i):
        if i%j==0:
            fact += i
    if fact==0:
        print(i)

print("---------------------")
r=2
c=3
res=0
for i in range (1,r+1):
    for j in range (1,c+1):
        res+=1
        print(str(res),end ="")
    print()
print("---------------------")
n=4
res=0
for i in range (1,n+1):
    for j in range (1,n+1):
        if i==n or i==1 :
            res+=1
            print(res,end=" ")
        elif j==1 or j==n:
            res+=1
            
            print(res,end=" ")
        else:
            print(" "*(n-2),end="")    
    print()
print("---------------------")
n=5
for i in range (1,n+1):
    for j in range (1,n+1):
        if i==n:
            print("* ",end="")
        else:
            l_sp="-"*(n-i)
            hallow="--"*(i-2)
            if i>1:
                print(l_sp+"* "+hallow+"* ",end=" ")
                break
            else:
                print(l_sp+"* ",end=" ")
                break
    print()

  

print("---------------------")
n=5 
for i in range (1,n+1):
    for j in range (1,n+1):
        if i == n:
            print(str(j),end=" ")
          
        else:
            l_sp=(" ")*(n-i)
            hal=(" ")*2*(i-2)
            if i>1:
                print(l_sp+str(1)+" "+hal+str(i),end=" ")
                break
            else:
                print(l_sp+str(1),end=" ")    
                break

    print()  
      
print("---------------------")
n=6
start_num=1 


for i in range(1,n+1):
    for j in range (1,n-i+2):
        if i ==1 or j==1 or j==n-i+1:
            print(start_num,end=" ")
        else:
            print(" ",end=" ")
        start_num+=1 
    print()      
print("---------------------")
n=5
for i in range(1,n+1):
    v=" *"*(i)
    print(v)
for k in range(n-1,0,-1):
    v=" *"*(i)
    print(v)
    k-=1
    


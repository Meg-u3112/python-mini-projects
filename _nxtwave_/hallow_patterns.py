u=4
for i in range(1,u+1):
    if(i==1):
        res=str(i)
    else:
        star=str(i)    
        hallow=(" ")*(i-1)
        res=str(i)+hallow+str(i)
    print(res)    
for i in range(u-1,0,-1):
    if(i==1):
        res=str(i)
    else:
        star=str(i)    
        hallow=(" ")*(i-1)
        res=str(i)+hallow+str(i)
    print(res)    
print("--------------------------")
o=5
for i in range(1,o+1):
    if i==1 :
        star=("* ")*(o)
        res=star
    elif i==5:
        star=("* ")*(o-i+1)
        res=star    
    else:
        star=("* ")
        space=(" ")*2*((o-i)-1)
        res=star+space+star

    print(res)                
print("--------------------------")
t=5
for i in range(1,t+1):
    if i==1:
        space=("- ")*(t-i)
        star=("* ")
        res=space+star

    elif i==5:
        star=("* ")*i
        res=star

    else:
        star=("* ")
        space=("- ")*(t-i)
        hallow=("- ")*((t-i))
        res=space+star+hallow+star    
    print(res)    
print("--------------------------")
o=5
for i in range(1,o+1):
    if i==1:print("* "*(o))
    elif i==o: 
        space=("  ")*(i-1)
        star=("* ")
        print(space+star)

    else: 
        space=("  ")*(i-1)
        star=("* ")
        mid=("- ")*((o-i)-1)
        
        print(space+star+mid+star)        
print("--------------------------")
u=5
for i in range(1,u+1):
    if i==1:
        l_space=("- ")*(u-1)
        star=("* ")*i
        res=l_space+star
    else:
        l_space=("- ")*(u-i)
        star=("* ")*((u-i)+1)
        res=l_space+star   
    print(res) 
print("--------------------------")
n=6
for i in range(1,n+1):
    if i==1:
        space=("- ")*(n-i)
        star=str(i)
        res=space+star
        print(res)
    else:    
        space=("- ")*(n-i)
        star=str(i)
        mid_space= ("  ")*((i-2))   
        print(space+star+mid_space+" "+star)
for i in range(n-1,0,-1):
    if i==1:
        space=("- ")*(n-i)
        star=str(i)
        res=space+star
        print(res)
    else:    
        space=("- ")*(n-i)
        star=str(i)
        mid_space= ("  ")*((i-2))   
        print(space+star+mid_space+" "+star)
print("--------------------------")
n=4
for i in range (1,n+1):
    if i ==1:
        star=("*")
        mid_space=("  ")*(n+1)
        res=star+mid_space+star
    elif i==n:
        star=("*")
        hallow=("  ")*(n-2)
        res=star+hallow+star+star+hallow+star

    else:    
        star=("*")
        hallow=(" ")*(i-1)
        mid_space=("  ")*((n-i)+1)
        res=star+hallow+star+mid_space+star+hallow+star
    print(res)
for i in range (n,0,-1):
    if i ==1:
        star=("*")
        mid_space=("  ")*(n+1)
        res=star+mid_space+star
    elif i==n:
        star=("*")
        hallow=("  ")*(n-2)
        res=star+hallow+star+star+hallow+star    
    else:    
        star=("*")
        hallow=(" ")*(i-1)
        mid_space=("  ")*((n-i)+1)
        res=star+hallow+star+mid_space+star+hallow+star
    print(res)    
print("-------------------")
n=9
m=100
count=0
for i in range (n,m+1):
        if i**0.5==int(i**0.5):
            count+=1
print(count)    
print("-------------------")
u=5
for i in range(1,u+1):
    if i==1:
        space=(" ")*(u-i)
        star=("* ")
        res=space+star
    else:
        space=(" ")*(u-i)
        star=("* ")
        hallow=(" ")*()
        res=space+star+hallow+star+space
        



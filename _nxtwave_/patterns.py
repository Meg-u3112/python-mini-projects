print("----------------------")
w=5
for i in range(w+1):
    space=" "*(w-i)
    star="* "*i
    print(space+star)
print("----------------------")
r=5
for i in range(r+1):

    space =" "*(r-i)
    if(i==5):
        star=("# "*i)
    else:
        star="* "*i
    print(space+star)
print("----------------------") 
r=5
for i in range (r+1):
    space=" "* (r-i)
    num=str(i)*i
    star=""
    print(space+star+num)
print("----------------------") 
n = 5
for i in range(n):

    space = ("- ")*(n-i-1)

    num=(str(i+1)+" ")*((2*(i))+1) 
    # ---> str > num to be printed * 2 denotes times to print  
    print(space+num)
print("----------------------") 
e=5
for i in range(e):
    space=("* ")*(r-i)
    star=("  ")*i
    
    
    print(star+space)
    
print("----------------------") 
r=5
for i in range(r):
    star=("*")*(2*(n-i)-1)
    space=("")*i
    print(space+star)
#   print(space+star)
print("----------------------") 
n = 5
# Top Half
for i in range(1, n + 1):
    spaces = " " * (n - i)
    stars = "* " * i
    print(spaces + stars)

# Bottom Half
for i in range(n - 1, 0, -1):
    spaces = " " * (n - i)
    stars = "* " * i
    print(spaces + stars)
print("----------------------")
n = 5

# Top Half
for i in range(1, n + 1):
    print("* " * i)

# Bottom Half
for i in range(n - 1, 0, -1):
    print("* " * i)
print("----------------------")

n = 5

# Top Half
for i in range(1, n + 1):
    #print("* " * i)
    print(str(i)*i)

# Bottom Half
for i in range(n - 1, 0, -1):
    #print("* " * i)
    print(str(i)*i)
print("----------------------")
u=5
for i in range(1,u):
    space="-" *(u-i)
    star=(str(i)+" ")*i
    print(space+star)
print("----------------------")
y=8
for i in range(y-1,0,-1):
    print(" " * (y-i),end = "")
    print("* " * i)
print("------------------")
o=5
for i in range(n):
    space=(" ")*(i)
    #star=("S ")*(n-i)
    #star=(str(i)*(n-i))*2
    star=(str(i)+" ")*(n-i)
    plus=("M ")*(n-i)
    if(i==0): print(plus)
    else: print(space+star)
print("---------------------")     
y=5
for i in range(y):
    space=("-")*(y-i)
    star=(("* ")*i)
    mid_sp=("-")*2*(y-i)
    print(space+star+mid_sp+star)
print("---------------------")     
row=3
for j in range(2):
    for i in range(1,row+1):

#        space=("  ")*(row-i)
#        star=("* ")*i
#        print(star+space)
#        for i in range(1,row+1):
#          print(" * "*i) 
          print((str(i))*i)   

print("---------------------")     
y=5
for i in range (y):
    space=(" ")*(y-i) 
#    star=("*")*i
    star=(str(i))*i
    mid_sp=("-")*2*(y-i)
    
    print(space+star+mid_sp+star)
print("---------------------")     
n = 5
alph = 65
for i in range(0, n):
    print("-" * (n-i),end=" ")
    for j in range(0, i+1):

        print(chr(alph),end=" ")
        alph += 1
    alph = 65
    print()
print("---------------------")     
h=5
for i in range (h):
   
    space=("* ")*(h-i)
    star=("-")*i
    mid=("-")*2*(i)
    print(star+space+mid+space)

print("---------------------")   
n=6
print(("* " )*n)
for i in range(2,n+1):
    space=("  ")*(n-i)
    fir=("|")
    sec=("/ ")
    print(fir+space+sec)
print("---------------------")   
p=4
for i in range(1,p+1):
    if(i==1 or i==4):
        print(("* ")*p)
    else:
        space=(("  ")*2)    
        print("* "+space+"* ")
print("---------------------")   




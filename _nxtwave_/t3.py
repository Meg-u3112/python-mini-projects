
u = 6
sum = 0

for i in range(1, u):
    if u % i == 0:
        sum += i
print(sum)
if sum == u:
    print("-Perf-no-")
else:
    print("-no-perf")
print('-----------')
o=6
p=23
count=0
st=[]
for i in range(o,p+1):
    if(i%6==0):
        count = count+1
        #st=st+str(i)+" "
        st.append(i)

print(st)
print("-----------")
#count of vowels > than 2 then print "String has more than 2 vowels"
h="megeue"
count =""
for i in h:
    if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u" ):
        count = count + str(i)+" "
cur=len(count)
if(cur>2):
    print("yes")
print("------------")
y=24
for i in range(2,9):
    if(y%i==0):
        print(i)
print("-----even-no------")
a=5
b=12
for i in range(a,b):
    if(i%2==0):
        print(i)
print("----odd-no-prd----")     
a=2
b=7
prd=1
for i in range(a,b+1):
    if(i%2!=0):
        prd=prd*i 
print(prd)        
print("---multiplication-table--")     
a=3
for i in range(1,10+1):
    res=a*i
    print( str(a)+"x"+str(i)+"="+str(res))
print("--vowels---")
a="Megu"
for i in  a:
    if(i=="a" or i=="e" or  i=="i" or i=="o" or i=="u" ):
        print(i)
print("--reverse-string--")        
a="kolathur"
rev=''
for i in a:
    rev=i+rev
print(rev)        
print("--pwd-input")
a=24753
s=str(a)
length=len(s)
sum=0
for i in  s:
        pwd=int(i)**length
        
        sum=sum+pwd
print(sum)        
print("---amstrong-no---")
a=164
s=str(a)
leng = len(s)
sum_eq =0
 #1634 --> 1^4 6^4  3^4  4^4  == 1634 ??
res = 1
for i in s:
    res = int(i)**leng
    sum_eq=sum_eq+res
if(sum_eq==a):    
    
    print("U made it man!!! 🥹 🥹 ")
else:
    print("whst wrong with u??  🤨 🤨 ")    
print("--factors--")    
a=12
b=3
if(a%b==0):
    print("its is a factor")
print("-3-inpts-divider-2-ranges-")
divi_no=2
a=5
b=9
sum=0
for m in range (a,b+1):
       if(m%divi_no==0):
           sum = sum+m
print(sum)           
print("-count-of-the-divisible-no-")
n=12
t=3
count=0
for i in range(1,12+1):
    if(i%t==0):
        count=count+1
print(count)
print("---------------------")





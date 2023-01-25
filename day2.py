"""
li=[1,2,3,4,5]
r=li.pop()
print(r)
print(li)
t1=(1,2,3,"abc",3,2,3)
res=t1.count(3)
print(res)
t=(1,2,3,4,2,3,2)
print(t.index(2))
SET METHODS
s1={1,2,3,4,5}
s2={3,4,5,78,9}
intrsctn=s1.intersection(s2)
unn=s1.union(s2)
dfrnce=s1.difference(s2)
print(intrsctn)
print(unn)
print(dfrnce)
print(s1)
dfrnceup=s1.difference_update(s2)
print(dfrnceup)
print(s1)
print(s2)

#conditional statements
if 7<0:
   print("true")
else:
    print("false")


n=int(input("enter number"))
if n%2==0:
    print("Even")
else:%
    print("Odd")


# condition? Truepart: Falsepart = terenary operator syntax
n=int(input())
print("Even")if n%2==0 else print("Odd")# truepart if condition else falsepart

#if-elif-else
day=int(input())
if day==1:
    print("Monday")
elif day==2:
    print("Tuesday")
elif day==3:
    print("Wednesday")
elif day==4:
    print("Thursday")
elif day==5:
    print("Friday")
elif day==6:
    print("saturday")
elif day==7:
    print("Sunday")
else:
    print("Invalid input")
    
#if input number>0 and less than 20.if even weird if not normal.2)>=20 and <30 normal.3)>=30 if odd normal.else weird.
num=int(input("enter number"))
if(0<num and num<20):
    if(num%2==0):
        print("Weird")
    else:
        print("normal number")
elif(num>=20 and num<30):
    print("normal number")
else:
    if(num%2!=0):
        print("weird")
    else:
        print("normal number")

        
#Dictionaries

dict1={"key1":20,"key2":30,"key3":30}
print(dict1["key2"])

d={}
d.update({"key1":"value 1"})
d.update({"key2":"value 2"})
d.update({"key3":"value 3"})
print(d)
print(d.get("key2"))


#looping statements

print(list(range(1,10,2)))
#range syntax---range(start,end,step_size)

for i in range():
    print(i,end="  ")



li=[9,45,847,651,3,54]
for i in li:
    print(i**2, end="  ")


num=int(input("enter number"))
li=[1,3,4,6,79,32,4,65]
for i in range(0,len(li)):
      if num==li[i]:
           print(i)
           break
        
li=[]
for i in range(10):
    li.append(i)
print(li)

#list comprehensions

li=[i*i for i in range(10)]
print(li)

li=[num for num in range(10) if num%2==0]

print(li)


li=[i for i in range(1,101) if i%7==0 and i%11==0]
print(li)

li1=[1,2,3,4,5,6]
li2=[]
for i in range(len(li1),0,-1)

"""
li=input().split( )
l2=list(map(int,li))
sum1,sum2=0,0
for i in l2:
    if(i<0):
        sum1+=i
    else:
        sum2+=i
print(sum1+sum2)





































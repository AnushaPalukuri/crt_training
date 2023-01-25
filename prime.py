"""def is_prime(num):
    c=0
    for i in range(2,num//2):
        if num%i==0:
            c+=1
    if c==0:
        print("prime")
    else:
        print("not a prime")
num=int(input())
is_prime(num)"""

 #another method
def is_prime(num):
    c=0
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            c+=1
    if c==0:
        print("prime")
    else:
        print("not a prime")
num=int(input())
is_prime(num)

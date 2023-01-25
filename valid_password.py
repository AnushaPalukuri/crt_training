n=int(input())
l=[]
for i in range(n):
    pswrd=input()
    l.append(pswrd)
for i in l:
    if len(i)>=8 and len(i)<=16:
        if i[0].lower() in "qwertyuiopasdfghjklzxcvbnm":
            for k in i:
                if k.upper()==True:
                    break
                    for x in i:
                        if x.lower()==True:
                            break
                            for a in i:
                                if a in "!@#$%^&*":
                                    break
                                    for b in i:
                                        if b in"123456789":
                                            print("True")

    else:
        print("False")
    

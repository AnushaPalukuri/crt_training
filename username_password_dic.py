db=[{'abc@example.com':'abc'},
    {'xyz@example.com':'123'},
    {'a123@example.com':'quertyuiop'},
    {'zxcv@example.com':'1234567890'}
    ]
print(db)
username=input()
password=input()
temp={username:password}
"""for i in db:
    if i[username]==password:
        print("matched")
    else:
        print("not matched")
"""
if temp in db:
    print("matched")
else:
    print("not matched")
    

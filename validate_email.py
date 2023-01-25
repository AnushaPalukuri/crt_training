mail=input()
if mail[0].lower() in "abcdefghijklmnopqrstuvwxyz":
    if "@" in mail:
        if mail[-1:-5:-1]=="moc.":
            print("valid mail")
        else:
             print(".com is missed")
    else:
        print("@ is not found")
else:
    print("digits and special characters are not allowed in first place")


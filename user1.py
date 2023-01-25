from User import UserClass
class login:
    __db=[]
    def __init__(self):
        self.print_menu()
    def print_menu(self):
        print("welcome User")
        print("1.Register")
        print("2.Login")
        print("3.Exit")
    def create_user(self,name,email,password):
        new_user=UserClass(name,email,password)
        self.__db.append(new_user)
        print(Self.__db)
        return True
    def validate_user(self,email,password):
        temp=self.__db.copy()
        for user_obj in temp:
            if email==user_obj.email:
                if password==user_obj.get_user_password:
                    print("login success")
                else:
                    print("Wrong password")
            else:
                print("email doesn't exits")
    obj=Login()
    while True:
        option=input("Enter your choice:")
        if option=='1':
            name=input("Enter your full name:")
            email=input("Enter email:")
            password=input("create new password:")
            res=obj.create_user(name,email,password)
            if res==True:
                print("User created successfully")
        elif option=='2':
            email=input("Enter email:")
            password=input("Enter password:")
            result=obj.validate_user
            elif option=='3'













            

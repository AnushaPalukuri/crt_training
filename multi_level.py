class Student:
    num=""
    attendence=50
    def __init__(self,num):
        self.num=num
        self.attendence=attendence
    def view_att(self,num):
        return(self.attendence)
class Faculty(Student):
    num=""
    rating=4
    def __init__(self,num):
        self.num=num
        self.rating=rating
    def view_rat(self,num):
        return(self.rating)
class Principal(Faculty):
    rating=3
    def __init__(self):
        self.rating=rating
    def view_ratt(self):
        return(self.rating)
p=Principal()
num=int(input())
print(p.Student(num))
print(p.view_att(num))
print(p.view_rat(num))
print(p.view_ratt())
        
    

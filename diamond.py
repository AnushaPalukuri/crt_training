"""
when child class try to access a method present in both the parent classes then Diamond problem occurs.
this problem occurs in multiple inheritance"""
class P1:
    def m1(self):
        print("in parent class 1")
class P2:
    def m1(self):
        print("in parent class 2")
class c(P2,P1):
    pass
obj=c()
obj.m1()

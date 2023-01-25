class A:
    name="anusha"
    age=19
    
class B(A):
    name="anu"
    age=16
class C(B):
    age=9
b=C()
print(b.age)
print(b.name)

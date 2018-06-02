class A:
    def method(self):
        print("This method belong to class A")

class B(A):
    def method(self):
        print("This method belong to class B")

        
class C(A):
    def method(self):
        print("This method belong to class C")

class D(B,C):
    pass

d=D()
d.method()                      #Calls class B first (Method resolution order)

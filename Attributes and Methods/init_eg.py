#An attribute is a property that further defines a class

#A method is a function within a class which can access all the attributes of a
#class and perform a specific task

#Class attributes are sttributes that are shared across all instances of a class
#They are created either as a part of the class or by using className.attributeName

#Instance attributes are attributes that are specific to each instance of a class

#They are created using objectName.attributeName

#The method call objectName.methodName() is interpreted as className.methodName(objectName)
#and this parameter is referred to as 'self' in method definition

#Instance method has the default parameter as the object are static methods. They are
#used to modify the instance attributes of a class

#Static methods are methods that do not modify the instance attributes of a class are
#They can still be used to modify class attributes

#init method is the constructor method for python


class Employee:

    def __init__(self,name):
        self.name=name

    def displayEmployeeDetails(self):
        print(self.name)


employee = Employee("Mark")
employeeTwo = Employee("Matthew")
employee.displayEmployeeDetails()
employeeTwo.displayEmployeeDetails()

#Understanding self parameter

class Employee:       
    def employeeDetails(self):
        self.name = "Matthew"
        print("Name = ",self.name)
        age=30
        print("Age = ",age)             #Without using self, no error.
    def printEmployeeDetails(self):
        print("Printing in another method")
        print("Name: ", self.name)
        print("Age: ", age)             #Gives error, age cannot be accessed within this method

#employee.employeeDetails       #Will give error, 0 positional argument but 1 was given

#Employee.employee.Details(employee) << Method call by Python

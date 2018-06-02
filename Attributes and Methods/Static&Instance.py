class Employee:
    def employeeDetails(self):
        self.name = "Ben"

    @staticmethod                   #Make Python understand that this method is static, no parameters should be given    
    def welcomeMessage():           #static method, do not take self parameter
        print("Welcome to our organization!")

employee = Employee()
employee.employeeDetails()
print(employee.name)
employee.welcomeMessage()

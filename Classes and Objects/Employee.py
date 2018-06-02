#Everything in Python is an object!
#Create an Employee class

class Employee:
    numberofWorkingHours = 40               #Number of Hours worked for employee in company
    def hasAchievedTarget(self):
        if self.salesMadeThisWeek >= 5:
            print("Target has been achieved")
        else:
            print("Target has not been achieved")

            
#Program first checks for instance attributes >> Followed by class attributes

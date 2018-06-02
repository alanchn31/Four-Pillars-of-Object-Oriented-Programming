from random import randint


class Bank:

    #Initialize with a dictionary, with clients' names as indices, to access account numbers and balances
    #Under clients information, there is balance amount and account number
    #structure: clients' name >> saving accounts >> balance in each account
    def __init__(self,clientsinfo):
        self.clientsinfo = clientsinfo                      #Initialize a dictionary containing clients' information


    def addAccount(self,name,deposit):
        accnum = randint(10000, 99999)
        self.clientsinfo[name][accnum] = {}
        self.clientsinfo[name][accnum]["balances"] = deposit
        print("New account created, account number: {}".format(accnum))
        
    def accessAccount(self, name, accountnum):
        if name in list(self.clientsinfo.keys()):
            if accountnum in list(self.clientsinfo[name].keys()):
                while True:
                    print("Welcome! Please select one of the follow options:")
                    print("For Withdrawal, input 1")
                    print("For Deposit, input 2")
                    print("To display available balance, input 3")
                    print("To exit, input 4")
                    x = int(input())

                    if x == 1:                                                          #Client chooses to withdraw
                        while True:
                            print("Input withdrawal amount: ")
                            y = int(input())
                            if self.clientsinfo[name][accountnum]["balances"] < y:
                                print("Insufficient balance, please try again.")
                            else:
                                self.clientsinfo[name][accountnum]["balances"] -= y
                                return(y)
                                break

                    elif x == 2:                                                          #Client chooses to deposit
                        while True:
                            print("Input deposit amount: ")
                            y = int(input())
                            if y < 0:
                                print("Sorry but negative input not allowed, please try again.")
                            else:
                                self.clientsinfo[name][accountnum]["balances"] += y
                                print("$" + str(y) + "has been deposited")
                                print("Balance: " + str(self.clientsinfo[name][accountnum]["balances"]))
                                break

                    elif x==3:
                        while True:                                                     #Client choose to display available balance
                            print("Balance: " + str(self.clientsinfo[name][accountnum]["balances"]))
                            break

                    elif x==4:
                        break





#Test Case:
clientsinfo = {"Adam" : {10000: {"balances": 10000} } , "Becky" : {10001 : {"balances": 9999}}}
boa = Bank(clientsinfo)
boa.accessAccount("Adam",10000)                     #Access Adam's Bank account with account number: 10000
#input 1,2, 3 or 4 to test



class OperatingSystem:
    multitasking = True
    name = "Mac OS"

class Apple:
    website = "www.apple.com"
    name = "Apple"

class MacBook(OperatingSystem, Apple):      #Name of OS was adopted instead due to order of args
    def __init__(self):
        if self.multitasking is True:
            print("This is a multi tasking system. Visit {} for more details".format(self.website))

macBook = MacBook()

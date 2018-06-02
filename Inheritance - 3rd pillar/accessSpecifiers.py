#Public => memberName
#Protected => _memberName
#Private => __memberName

class Car:
    numberOfWheels = 4              #Public Attribute
    _color = "Black"                #Protected Attribute, as good practice, should not be used outside family of classes
    __yearOfManufacture = 2017      #Private Attribute, should not be used outside class
                                    

class Bmw(Car):
    def __init__(self):
        print("Protected attribute color: ", self._color)


car = Car()
print("Public attribute numberOfWheels: ",car.numberOfWheels)
bmw = Bmw()
print("Private attribute yearOfManufacture: ",car.__yearOfManufacture)

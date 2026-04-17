# Classes & Objects

# class Student: # Creating class
#     name = "Yash"

# s1 = Student() #Creating object
# print(s1.name)

# class Car:
#     color = "Black"
#     brand = "BMW"

# car = Car()
# print(car.color)
# print(car.brand)

# __init__ Function or constructor

class Student():

    #Default constructor
    def __init__(self):
        pass

    #Parameterized constructor
    def __init__(self, fullName):
        self.name = fullName
        print("Adding new student in database")

    
s1 = Student("Yash Bansode")
print(s1.name)
s2 = Student("Sakshi Bansode")
print(s2.name)


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

# class Student():

#     #Default constructor
#     def __init__(self):
#         pass

#     #Parameterized constructor
#     def __init__(self, fullName):
#         self.name = fullName
#         print("Adding new student in database")

    
# s1 = Student("Yash Bansode")
# print(s1.name)
# s2 = Student("Sakshi Bansode")
# print(s2.name)

# Class & Instance attribute

# class Student():
#     college = "ABC College"

#     #Parameterized constructor
#     def __init__(self, fullName):
#         self.name = fullName
#         print("Adding new student in database")

    
# s1 = Student("Yash Bansode")
# print(s1.name)
# # print(Student.college)
# print(s1.college)

#Methods

# class Student():
#     college = "ABC College"

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
    
#     def welcome(self):
#         print(f"Welcome student, {self.name}")

#     def get_marks(self):
#         return self.marks

    
# s1 = Student("Yash Bansode", 97)
# s1.welcome()
# print(s1.get_marks())

#Question

# class Student:
    
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print(f"Hello {self.name} your avg marks is: {sum/3}%")

    
# s1 = Student("Yash", [99,98,97])
# s1.get_avg()

#Static Methods: this methods don't use the self parameter (wrok at class level)

class Student:
    @staticmethod
    def hello():
        print("Hello")

s1 = Student()
s1.hello()

        


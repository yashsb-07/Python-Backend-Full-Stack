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

# class Student:
#     @staticmethod
#     def hello():
#         print("Hello")

# s1 = Student()
# s1.hello()

#Abstraction

# class Car:
#     def __init__(self):
#         self.accl = False
#         self.brk = False
#         self.clutch = False

#     def start(self):
#         self.clutch = True
#         self.brk = True
#         print("Car started..")

    
# car = Car()
# car.start()

#Encapsulation

class Account:
    def __init__(self, balance, acc_no):
        self.balance = balance
        self.acc_no = acc_no

    def debit(self, amt):
        self.balance -= amt
        print(f"Rs. {amt} was debited")
        print(f"Total balance: {self.get_balance()}")

    def credit(self, amt):
        self.balance += amt
        print(f"Rs. {amt} was credited")
        print(f"Total balance: {self.get_balance()}")

    def get_balance(self):
        return self.balance
    
acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)


        

        


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

# class Account:
#     def __init__(self, balance, acc_no):
#         self.balance = balance
#         self.acc_no = acc_no

#     def debit(self, amt):
#         self.balance -= amt
#         print(f"Rs. {amt} was debited")
#         print(f"Total balance: {self.get_balance()}")

#     def credit(self, amt):
#         self.balance += amt
#         print(f"Rs. {amt} was credited")
#         print(f"Total balance: {self.get_balance()}")

#     def get_balance(self):
#         return self.balance
    
# acc1 = Account(10000, 12345)
# acc1.debit(1000)
# acc1.credit(500)

#del Keayword

# class Student:
    
#     def __init__(self, name):
#         self.name = name

# s1 = Student("Yash")
# print(s1.name)
# del s1.name
# print(s1.name)

#Private Attribute and methods

# class Person:

#     __name = "Yash"

#     def __hello(self):
#         print("Hello yash")

#     def welcome(self):
#         self.__hello()

# p1 = Person()
# print(p1.welcome())


#Inheritance

# class Car:

#     color = "black"
#     @staticmethod
#     def start():
#         print("Car started..")

#     def stop():
#         print("Car stopped.")

# class ToyotaCar(Car):

#     def __init__(self, brand):
#         self.brand = brand

# class Fortuner(ToyotaCar):
#     def __init__(self, type):
#         self.type = type

# car1 = ToyotaCar("Fortuner")
# print(car1.name, car1.start())
# print(car1.color)
        
# car2 = Fortuner("Petrol")
# car2.start()
# print(car2.type)

# class A:
#     varA = "Welcome to class A"

# class B:
#     varB = "Welcome to class B"

# class C(A, B):
#     varC= "Welcome to class C"

# c1 = C()
# print(c1.varA)
# print(c1.varB)
# print(c1.varC)

#Super Method

# class Car:
#     def __init__(self,type):
#         self.type = type
       
#     @staticmethod
#     def start():
#         print("Car started..")

#     def stop():
#         print("Car stopped.")

# class ToyotaCar(Car):

#     def __init__(self, name, type):
#         super().__init__(type)
#         self.name = name
#         super().start()

# car1 = ToyotaCar("Fortuner", "Petrol")
# print(car1.name, car1.type)

#Class Method

# class Person:
#     name = "anonymous"


#     # def changeName(self, name):
#     #     self.name = name

#     @classmethod
#     def changeName(cls, name):
#         cls.name = name

# p1 = Person()
# p1.changeName("Yash Bansode")
# print(p1.name)
# print(Person.name)

#Property Decorator

# class Student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math

#     @property
#     def percentage(self):
#         return str((self.phy + self.chem + self.math)/3) + "%"

# s1 = Student(98, 97, 99)
# print(s1.percentage)

# s1.phy = 86
# print(s1.percentage)
        
#Polymorphism

# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def showNumber(self):
#         print(self.real, "i +", self.img, "j")

#     def __add__(self, num2):
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return Complex(newReal, newImg)

# num1 = Complex(1, 2)
# num1.showNumber()

# num2 = Complex(3, 4)
# num2.showNumber()

# num3 = num1 + num2
# num3.showNumber()
        
#Question1    

# class Circle():

#     def __init__(self, radius):
#         self.radius = radius
    
#     def area(self):
#         return 3.14 * self.radius ** 2
    
#     def perimeter(self):
#         return 2 * 3.14 * self.radius
    
# c1 = Circle(21)           
# print(c1.area())
# print(c1.perimeter())

#Question2

# class Employee:
#     def __init__(self, role, dept, salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary

#     def showDetails(self):
#         print("Role: ", self.role)
#         print("Dept: ", self.dept)
#         print("Salary: ", self.salary)

 
# class Engineer(Employee):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__("SDE", "IT", "1,00,000")

        

# emp = Employee("SDE", "IT", "1,00,000") 
# emp.showDetails()

# eng = Engineer("Yash", 22)
# eng.showDetails()
        
#Project 1: Bank System

# class BankAccount:
#     def __init__(self, name, acc_no, balance):
#         self.name = name
#         self.account_no = acc_no
#         self.__balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Rs. {amount} deposited successfully!")
#         else:
#             print("Invalid amount")

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Rs. {amount} withdrawn successfully!")
#         else:
#             print("Insufficient fund.")

#     def get_balance(self):
#         return self.__balance

#     def display(self):
#         print(f"Name: {self.name}")
#         print(f"Account Number: {self.account_no}")
#         print(f"Balance: {self.__balance}")
    

# acc1 = BankAccount("Yash Bansode", 1234567, 100000)
# acc1.deposit(100)
# print(acc1.get_balance())
# acc1.withdraw(1000)
# print(acc1.get_balance())
# acc1.display()

    
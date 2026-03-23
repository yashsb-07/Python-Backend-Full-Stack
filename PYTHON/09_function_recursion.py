#Functions

# def cal_sum(a, b):
#     sum = a + b
#     print(sum)

# cal_sum(5, 10)

# def cal_avg(a, b, c):
#     sum = a + b + c
#     avg = sum / 3
#     print(avg)

# cal_avg(98, 78, 90)

# def printHello():
#     print("Hello")

# printHello()
# printHello()
# printHello()
# printHello()
# printHello()

#Recursion

# def show(n):
#     if n == 0: #Base Case
#         return
#     print(n)
#     show(n-1)

# show(5)

# def fact(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return n * fact(n-1)

# print(fact(6))

#Q1

# def cal_sum(n):
#     if n == 0:
#         return 0
#     return cal_sum(n-1) + n
    
# sum = cal_sum(10)
# print(sum)

#Q2

def print_list(list, idx=0):
    if idx == len(list):
        return
    print(list[idx])
    print_list(list, idx + 1)

cities = ["Pune", "Mumbai", "Banglore", "Chennai", "Hydrabad"]
print_list(cities)
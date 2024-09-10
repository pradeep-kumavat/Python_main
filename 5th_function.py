def sum(a,b):
    return a+b

def subt(a,b):
    return a-b

def mul(a,b):
    return a*b

# num1 = int(input("enter the no1:"))
# num2 = int(input("enter the no2:"))
# print("the sum is ",sum(num1,num2))
# print("the subt is ",subt(num1,num2))
# print("the mul is ",mul(num1,num2))

#arbitrary arguments:passing array in function as ndirect numbers
def add(*num):
    sum = 0
    for i in num:
        sum+=i
    return sum

# print("the sum is ", add(1,2,3,4,5))

#**kwargs
def student(**num):
    sum = 0
    for i,j in num.items():
        print(i ,"is", j)

# one way
stud={
    "name1" :"ria",
    "name2" :"tia",
    "name3" :"mia",
    "name4" :"sia"
}
# student(**stud)
        
# second way
# student(name1 ="ria",name2 ="tia", name3 ="mia", name4 ="sia")

#pass by value = apply to immutable objects: string, integer, float, tuple
#pass by reference = apply to mutable objects: list , dictionary

# recursion-----------------

def fact(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n* fact(n-1)

    
def fibb(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibb(n-2) + fibb(n-1)

no = int(input("enter the number:"))
print("the factorial is ", fact(no))
print("the fibbanacci is ", fibb(no))
for i in range(1, no+1):
    print(fibb(i))

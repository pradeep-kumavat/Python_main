a = int(input("enter the no1:"))
b = int(input("enter the no2:"))

try:
    result= a/b
    print(result)
except ZeroDivisionError:
    result= None
    print("error cannot divide by zero")
finally:
    print("division operation completed")
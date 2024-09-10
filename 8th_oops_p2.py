#inheritance

#single inheritance --------------------------
# class parent:
#     def __init__(self):
#         print("this is parent class")
#         self.attribut= True

# class child(parent):
#     def __init__(self):
#         super().__init__()
#         print("this is child class")
#         print(self.attribut)



# child1 = child()

#polimorphism --------------------------

# class animal:
#     def speak(self): #abstract method which will be overwritten
#         pass


# class dog(animal):
#     def speak(self):
#         print("bhow")

# class cat(animal):
#     def speak(self):
#         print("meow")

# class cow(animal):
#     def speak(self):
#         print("mooo")

# dog = dog()
# dog.speak()

# cat = cat()
# cat.speak()

# cow = cow()
# cow.speak()

# compile time polimorphism: function overloading & operator overloading 
#this is operator overloading
class complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def __add__(self, other):
        return complex(self.real + other.real , self.img + other.img)
    
c1 = complex(1,2)
c2 = complex(3,5)
c3 = c1 + c2
print(c3.real , "+ i",c3.img)

# class student:
#     def set_name(self,name):
#         self.name= name
#     def get_name(self):
#         return self.name

# student1 = student()

# student1.set_name("Pradeep")
# print(student1.name)
# print(student1.get_name())

# student2 = student()
# student2.set_name("Kumavat")
# print(student2.name)
# print(student2.get_name())

# class rect:
#     def set_dim(self, hie,wid):
#         self.hie = hie
#         self.wid = wid

#     def area(self):
#         return self.hie * self.wid
    
# rect1 = rect()
# rect1.set_dim(4,5)
# print("the  area is ",rect1.area())

#using constructor

# class rect:
#     def __init__(self, hie,wid):
#         self.hie = hie
#         self.wid = wid

#     def area(self):
#         return self.hie * self.wid
    
# rect1 = rect(4,6)
# # rect1.set_dim(4,5)
# print("the  area is ",rect1.area())


# access modifier: 
#by default public modifier is applied

# class abc:
#     def __init__(self):
#         self.public_attribute =10
#     def public_function():
#         pass

# obj1 = abc()
# print(obj1.public_attribute)

# to make private function or variables : simply add __ (two underscore)

# class abc:
#     def __init__(self):
#         self.__private_attribute =10
#     def __private_function():
#         pass

# obj1 = abc()
# obj1.__private_attribute()

# to make protected function or variables : simply add _ (one underscore)

# protected modifier 
class abc:
    def __init__(self):
        self._prptected_attribute =10
    def _protected_function():
        pass

# class Book():
#     def __init__(self,title,author,pages):
#         self.title=title
#         self.author=author
#         self.pages=pages
#     def __str__(self):
#         return "Title: {}, Author: {}, pages: {}".format(self.title,self.author,self.pages)
#     def __len__(self):
#         return self.pages
#     def __del__(self):
#         print("a book is destroyed!")        

# b=Book("Python","jose",200)
# print(b) 
# print(len(b))
# del b       












# class Animal():
#     def __init__(self):
#         print("Animal Created!")
#     def whoami(self):
#         print("Animal")
#     def eat(self):
#         print("Eating")        

# class Dog(Animal):
#     def __init__(self):
#         # Animal.__init__(self)
#         print("Dog Created")
#     def bark(self):
#         print("Woof")
#     def eat(self): # overriding
#         print("I ain't eating ntn")        

# mya=Animal()
# mya.whoami()
# mya.eat()
# mydog=Dog()
# mydog.whoami()
# mydog.eat()
# mydog.bark()




# class Circle:
#     pi=3.14
#     def __init__(self,radius=1):
#         self.radius=radius
#     def area(self):
#          return self.radius*self.radius*Circle.pi  
#     def set_radius(self,new_r):
#         self.radius=new_r      
# myc=Circle(4)
# myc.set_radius(12)
# print(myc.area())       



# class Dog():
#     species='mammal'
#     def __init__(self,breed,name):
#         self.breed=breed
#         self.name=name
# mydog=Dog("Lab","You")
# print(mydog.breed)
# print(mydog.name)
# print(mydog.species)



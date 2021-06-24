# x=25
# def my_func():
#     x=50
#     return x
# my_func()
# print(x)

# Local
# lambda x: x**2

# Enclosing function locals a function inside a function
# name="This is a global name!"
# def greet():
#     name="sammy"
#     def hello():
#         print("hello " + name)
#     hello()    
# greet() 


# to change x inside a function
x=50
def func():
    # global x
    x=1000
    return x
   
x=func() 
print(x)    
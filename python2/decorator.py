# Decorator
def new_decorator(func):
    def wrap_func():
        print("CODE HERE BEFORE EXECUTING FUNCTION")
        func()
        print("FUNC() HAS BEEN CALLED")
    return wrap_func
@new_decorator    
def func_needs_decorators():
    print("THIS FUNCTION IS IN NEED OF THE DECORATOR!")        
# func_needs_decorators = new_decorator(func_needs_decorators)



func_needs_decorators()





# function as argument
# def hello():
#     return "Hi JOSE!"
# def other(func):
#     print("HELLO")
#     print(func())

# other(hello)        



# def hello(name="jose"):
#     print("THE HELLO() FUNCTION HAS BEEN RUN!")
#     def greet():
#         return "THIS STRING IS INSIDE GREET()"
#     def welcome():
#         return "THIS STRING IS INSIDE WELCOME!"
#     if name == "jose":
#         return greet
#     else:
#         return welcome        
# x=hello()
# print(x())    









# def hello(name="Jose"):
#     return "hello "+name
# print(hello()) 

# mynewgreet=hello #setting it equal to the function not what it returns

# print(mynewgreet())
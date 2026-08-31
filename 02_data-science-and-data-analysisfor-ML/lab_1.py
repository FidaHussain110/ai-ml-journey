print(3*"\n")
print('Hello! Welcome to the Data Science and Data Analysis for Machine Learning Lab 1.\n\n')

# position of arguments while calling the function does not matter
def greet_with_positional_args(name,age):
    print("\nHello from Position argument function\n")
    print(f"Hello, {name}! You are {age} years old.")

# position of arguments while calling the function does not matter
def greet_with_keyword_args(name, age):
    print("\nHello from Keyword argument function\n")
    print(f"Hello, {name}! You are {age} years old.")



# *args accepts variable number of positional arguments
def greet_with_args(*nums):
    print("\nHello from varaible pisitional argument function\n")
    print(nums)


# **kewargs accepts variable number of keyword arguments
def greet_with_kewarg(**kwargs):
    print("\nHello from varaible Keyword argument function\n")

    for k,v in kwargs.items():
        print(k,":  ",v)


name = input("Enter your name: ")
age = int(input("Enter your age: "))
university = input("Enter your uni name: ")

greet_with_positional_args(name, age)   
greet_with_keyword_args(age = age, name = name)
greet_with_args(name,age,university)
greet_with_kewarg(name = name,age = age , university = university)






print(3*"\n")
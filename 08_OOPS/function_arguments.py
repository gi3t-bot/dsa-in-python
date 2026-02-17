name = "Prajjwal Dobriyal"
age = 10
gender = "male"


print(f"My name is {name}")
print(f"My name is {name}, I am {age} yrs old, my Gender is {gender}")


def addition(n1, n2):
    print(f"N1 is {n1}")
    print(f"N2 is {n2}")
    # print(f"The total is {n1 + n2}")
    print(f"The total is {n1 + n2}")


addition(False, False)

False == 0
True == 1

# def fun(n1, n2, n3, n4, n5):


def func1():
    return 10


def func2():
    return 30


def func():
    a = func1()
    b = func2()
    print(a + b)


func()


def total_marks(maths, hindi, english, science):
    total = maths + hindi + english + science
    print(maths)
    print(hindi)
    print(english)
    print(science)
    print(total)


# we call this Named arguments
total_marks(56, 76, 66, 76)
# total_marks(hindi=56, maths=76, english=66, science=76)


# *----------------------------------------------------------------------------*
# args and kwargs

# like if we dont know about the number of arguments that has to be given....then we use args

# why the * then ??
# the * tells the Python, take all possible arguments and pack them into one variable, It packs all the values into a tuple


def total(*args):
    # print(args)
    print(sum(args))


total([1, 2], 3, (5, 2))
# total(56, 76, 66, 76)
# total(4, 3, 5, 3, 3, 2, 2, 4, 3, 5, 4, 5)
# total(211, 43)


# **kwargs means keyword arguments
# **kwargs will take the arguments and make this into a dictionary
def total(**kwargs):
    print(kwargs)


total([1, 2], 3, (5, 2))

total(name="Prajjwal", age=24, gender="male")


# *----------------------------------------------------------------------------*
# lambda is an anonymous function- because we dont have to create function inorder to use it


# why?? like why do we use it??
# lambda function allows us to write full funtions for the small logic


def add_numbers(n1, n2, n3):
    return n1 + n2 + n3


result = add_numbers(10, 20, 30)
print(result)


# lambda parameters : returning statement
y = lambda n1, n2, n3: n1 + n2 + n3

x = lambda x: x**2

# print(y(10, 20, 30))

print(x(10))

even_odd = lambda num: num % 2 == 0

print(even_odd(23))


# *----------------------------------------------------------------------------*
# Annotations -> they are the notes about the data types, they are not strict but are used just to tell the user about the data type to be used in arguments.
def add(num1: int, num2: int):
    print(num1 + num2)


add("10", "30")



# OOPS - Object Oriented Programming Language
# OOPS helps us in converting the large size real life problem into multiple smaller problems

# The Features of OOPS are:
#     Classes
#     Objects
#     Encapsulation
#     Inheritance
#     Polymorphism
#     Abstraction


# Classes = Blueprint, They are single (or unique)
# like incase of Students
# Students -> Id, Name, PhoneNo, Gender etc etc...

# If there are 20 students, then I have to personally add all these ID, Name columns for every one of them....
# which is a really bigger problem...
# so instead of doing all this , what we can do is....
# We can create a CLASS Students which have these columns ....
# and I will use it for the students....that way I dont have to personally add all the columns for every student


class Student:
    # the variables that are made in the class....are known as Attributes
    # id = 0
    # name = ""
    # age = 0
    # phn_no = 0
    # sex = ""

    # we can also make functions inside the class
    # The functions that are inside the class are known as Methods
    # but when defining the function inside the class, we have to write "self" inside the function as a parameter
    # self is like the reference Python uses to connect a method call (info) to the correct object (student_1).
    # self is like a connecting wire for the python that tells the python that s1 is Prajjwal...s2 is Aman

    # Python do not stores “s1 is Rahul” permanently inside self.
    # self temporarily refers to object that is calling the method at that time...

    # for example : When someone says "I am going".....that "I" tells us who is speaking....
    # and "I" changes based on "Who says it".. or in other words "Who use it"

    def info(self):
        print(f"Name = {self.name}")
        print(f"Id = {self.id}")
        print(f"Age = {self.age}")
        print(f"Phone No = {self.phn_no}")
        print(f"Sex = {self.sex}")

    def set_info(self):
        self.name = input("Enter the name: ")
        self.id = int(input("Enter the id: "))
        self.age = int(input("Enter the age: "))
        self.phn_no = int(input("Enter the phone number: "))
        self.sex = input("Enter the gender: ")
        
        
student_1 = Student()
student_2 = Student()

# if I have to print the values for any object, I will write:    object_name.class_property
# for example If I want to print the phone number of Student 1....I will write it as -> student_1.phn_no

# if I have to insert the values for any object, I will write :    object_name.class_property = "value to insert"
# for example If I want to insert the name of Student 1....I will write it as -> student_1.name = "Prajjwal"


# student_1.name = "Prajjwal"
# student_1.id = 121
# student_1.sex = "Male"
# student_1.phn_no = 9045
# student_1.age = 24

student_1.set_info()
# student_1.info()
# print()

# student_2.name = "Akash"
# student_2.id = 12
# student_2.sex = "Male"
# student_2.phn_no = 6402
# student_2.age = 21

student_2.set_info()
# student_2.info()


# so what is happening that I have to manually insert the lines or moethods that I want my data to insert
# so instead of writing it again and again....
# what we can do, we can just make a function (method) that will help me inorder to take inputs from the user


# so instead of writing this whole line....I can just make a function set_info() that will help me reducing this task

# student_1.name = "Prajjwal"
# student_1.id = 121
# student_1.sex = "Male"
# student_1.phn_no = 9045746402
# student_1.age = 24 


student_1.info()
student_2.info()

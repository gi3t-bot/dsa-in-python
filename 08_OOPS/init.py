# So what I am doing initially is that I am calling the specific function to enter the data
# which can ultimately result in me forgetting to call the function to enter the data...which will result in the code not being able to work

# so I can do one thing...
# I can create a special method (also known as Constructor) that will execute automatically whenever I will create an object..
# that Constructor is known as "__init__ function" or method

# the "__init__" function will execute automatically as soon as the object is created
# so rather than using the function set_info() I can put the values to be inserted inside the __init__ function


class Student:
    def __init__(self):
        self.name = input("Enter the name: ")
        self.id = int(input("Enter the id: "))
        self.age = int(input("Enter the age: "))
        self.phn_no = int(input("Enter the phone number: "))
        self.sex = input("Enter the gender: ")       

    def info(self):
        print(f"Name = {self.name}")
        print(f"Id = {self.id}")
        print(f"Age = {self.age}")
        print(f"Phone No = {self.phn_no}")
        print(f"Sex = {self.sex}")

    # def set_info(self):
    #     self.name = input("Enter the name: ")
    #     self.id = int(input("Enter the id: "))
    #     self.age = int(input("Enter the age: "))
    #     self.phn_no = int(input("Enter the phone number: "))
    #     self.sex = input("Enter the gender: ")


student_1 = Student()
student_2 = Student()


student_1.info()
student_2.info()


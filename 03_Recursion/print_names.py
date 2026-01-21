# Head Recursion 
count = 0

def print_names():
    global count  # declaring that the count is a global variable
    if count == 4:
        return 
    
    print("Prajjwal")
    count += 1
    print_names()
    
print_names()


# Tail Recursion or Backtracking
count = 0

def print_names():
    global count  # declaring that the count is a global variable
    if count == 4:
        return 
    
    count += 1
    print_names()
    print("Prajjwal")
     
print_names()



# another example of tail recursion 
def print_name(count):
    if count <= 0:
        return 
    
    print("Prajjwal")
    return print_name(count-1)
    
print_name(5)
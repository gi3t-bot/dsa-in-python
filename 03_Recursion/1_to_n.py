# without using parameters
count = 1
def func():
    global count
    if count > 5:
        return 
    
    print(count)
    count += 1
    func()
    
func()


# using parameters
def func(i, n):
    if i > n:
        return
    
    print(i)
    func(i+1, n)
       
func(1, 8)


# Tail recursion 

def func(i, n):
    if n < i:
        return
    
    func(i+1, n)
    print(i)
    
func(1, 7)

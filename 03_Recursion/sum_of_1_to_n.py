# parameterised recursion 
def func(sum, i , n):
    if i > n:
        print(sum)
        return

    func(sum+i, i+1, n)
    
func(0,1,10)


# functional recursion 

def func(n):
    if n == 1:
        return 1
    
    return n + func(n-1)

func(10)
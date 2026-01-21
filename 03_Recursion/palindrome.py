# using looping (reversing the string and then checking)
def palindrome(str1):
    l = 0
    r = len(str1) - 1
    
    temp = list(str1)
    
    while l < r:
        temp[l], temp[r] = temp[r], temp[l]
        
        l += 1
        r -= 1
    
    reversed_str = "".join(temp)
    return "Palindrome" if str1 == reversed_str else "Not Palindrome"


palindrome("Nitin")




# using looping (checking positions of left and right)
def palindrome(str1):
    l = 0 
    r = len(str1) - 1
    
    while l < r:
        if str1[l] == str1[r]:
            l += 1
            r -= 1
        else:
            return "Not Palindrome"
           
    return "Palindrome" 

palindrome("ANBCDDCBNA")

         
# using recursion (checking positions of left and right)

def lr(str1):
    l = 0
    r = len(str1) - 1
    
    return palindrome(str1, l , r)
    
    
def palindrome(str1, l , r):
    if l >= r:
        return "Palindrome"
    
    if str1[l] == str1[r]:
        return palindrome(str1, l + 1, r - 1)
    
    else:
        return "Not Palindrome"
        
lr("ANBCDDCBNA")
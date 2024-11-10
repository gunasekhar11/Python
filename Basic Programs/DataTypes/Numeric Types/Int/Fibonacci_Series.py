def Fibonacci_Series_Recursive(n):
    if(n<0):
        return f"Less Than 0 Is Not Accepted For Fibonacci Series"
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return Fibonacci_Series_Recursive(n-1) + Fibonacci_Series_Recursive(n-2)
    
def Fibonacci_Series_Iterative(n):
    temp = [0,1]
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        temp_number = 0
        for _ in range(0,n):
            temp.append(temp_number)
            temp_number=temp[-2]+temp[-1]
        return temp_number
    
def Fibonacci_Series_Swapping(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        a,b = 0,1
        for _ in range(2,n+1):
            a,b = b,a+b
        return b
    
for i in range(0,10):
    print(Fibonacci_Series_Swapping(i))
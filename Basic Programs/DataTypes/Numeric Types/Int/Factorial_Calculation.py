def Factorial_Calculation(num):
    if(num < 0):
        return f"{num} is a Negative Number"
    fact = 1
    for i in range(1,num+1):
        fact = fact * i
    return f"Factorial of {num} is {fact}"

print(Factorial_Calculation(5))
print(Factorial_Calculation(4))
print(Factorial_Calculation(-10))
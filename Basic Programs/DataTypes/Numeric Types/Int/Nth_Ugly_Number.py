def Nth_Ugly_Number(n):
    ugly_numbers = [1]
    iterable = 1 
    while len(ugly_numbers) < n:
        if(iterable%2==0 or iterable%3==0 or iterable%5==0):
            ugly_numbers.append(iterable)
        iterable +=1
    return ugly_numbers[-1]

print(Nth_Ugly_Number(56))
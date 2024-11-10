def Prime_Number(num):
    if (num < 2):
        return f"{num} is Not a Prime Number"
    else:
        for i in range(2,int(num**0.5)+1):
            if (num%i==0):
                return f"{num} is not a Prime Number"
        return f"{num} is Prime Number" 
    
for i in range(1,100):
    print(Prime_Number(i))
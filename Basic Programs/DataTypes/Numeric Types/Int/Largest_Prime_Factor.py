def isPrime(num):
    if(num < 2):
        return 0
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return 0
    return 1

def primeFactors(num):
    arr = []
    for i in range(num+1):
        if isPrime(i) and num%i == 0:
            arr.append(i)
    return arr
            

def Largest_Prime_Factor(num):
    prime_factors = primeFactors(num)
    return max(prime_factors)

print(Largest_Prime_Factor(97))

def Prime_Factors(num):
    factors = []
    divisor = 2
    while num > 1:
        while num % divisor == 0:
            factors.append(divisor)
            num = num//divisor
        divisor= divisor + 1
    return factors

print(Prime_Factors(60))
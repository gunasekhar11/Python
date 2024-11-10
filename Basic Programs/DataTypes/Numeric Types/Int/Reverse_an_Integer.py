def Reverse_an_Integer(n):
    reversed = 0
    while n>0:
        last_digit = n%10
        reversed = reversed*10 + last_digit 
        n = n//10
    return reversed

def Reverse_an_Integer(n):
    reversed = 0
    while n>0:
        digits = int("1"+("0"*(len(str(n))-1)))
        reversed += n%10 * digits
        n = n//10
    return reversed

print(Reverse_an_Integer(1234))

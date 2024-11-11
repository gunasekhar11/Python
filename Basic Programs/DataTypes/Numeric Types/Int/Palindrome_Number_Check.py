def Palindrome_Number_Check(n):
    temp = n
    reversed = 0
    while temp>0:
        last_digit = temp%10
        reversed = reversed * 10 + last_digit
        temp = temp//10
    return f"{n} is Palindrome" if n == reversed else f"{n} is not Palindrome"

print(Palindrome_Number_Check(12321))
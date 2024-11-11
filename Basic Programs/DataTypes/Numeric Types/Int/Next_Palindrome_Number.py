def Palindrome_Number_Check(n):
    temp = n
    reversed = 0
    while temp>0:
        last_digit = temp%10
        reversed = reversed * 10 + last_digit
        temp = temp//10
    return 1 if n == reversed else 0

def Next_Largest_Palindrome(n):
    temp = n + 1
    while True:
        if(Palindrome_Number_Check(temp)):
            return f'{temp} is a Next Palindrome After {n}'
        else:
            temp+=1

print(Next_Largest_Palindrome(112))
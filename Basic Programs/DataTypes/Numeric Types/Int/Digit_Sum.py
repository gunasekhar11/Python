def Digit_Sum(num:int):
    Sum = 0
    while(num>0):
        temp = num%10
        Sum+=temp
        num = num//10
    return Sum

def Digit_Sum_2(num: int):
    total = 0
    while num > 0:
        num, remainder = divmod(num, 10)
        total += remainder
    return total

print(Digit_Sum_2(124634))
print(Digit_Sum(124634))
def Divisibility_Check(num:int):
    if(num % 3 == 0 and num % 5 == 0):
        return "Both"
    elif(num % 3 == 0 and num % 5 != 0):
        return "Three Only"
    elif(num % 3 != 0 and num % 5 == 0):
        return "Five Only"
    else:
        return "Not Divisible By any"
    

print(Divisibility_Check(3))
print(Divisibility_Check(5))
print(Divisibility_Check(15))
print(Divisibility_Check(16))
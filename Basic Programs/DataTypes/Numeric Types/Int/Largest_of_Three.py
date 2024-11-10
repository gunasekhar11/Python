def Largest_of_Three(num1,num2,num3):
    if num1 == num2 == num3:
        return "All numbers are equal"
    elif(num1 > num2 and num1 > num3):
        return f"{num1} is Greater"
    elif(num2 > num1 and num2 > num3):
        return f"{num2} is Greater"
    else:
        return f"{num3} is Greater"
    
print(Largest_of_Three(1,233,34))
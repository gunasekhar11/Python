def Positive_Or_Negative(num:int):
    if(num<0):
        return "Negative"
    elif(num>0):
        return "Positive"
    else:
        return "Zero"
    
print(Positive_Or_Negative(-20))
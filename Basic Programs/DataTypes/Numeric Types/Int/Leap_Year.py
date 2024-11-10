def Leap_Year(year):
    if((year % 4 == 0) or (year % 400 == 0 and year % 100 != 0)):
        return "Leap"
    else:
        return "Leap Year"
    
print(Leap_Year(2100))

def Perfect_Number(num):
    temp = []
    for i in range(1,num):
        if (num%i==0):
            temp.append(i)
    return f"{num} is a Perfect Number" if sum(temp) == num  else f"{num} is not a Perfect Number"

print(Perfect_Number(8))
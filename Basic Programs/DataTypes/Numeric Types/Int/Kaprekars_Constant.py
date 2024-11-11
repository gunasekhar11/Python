
def Kaprekars_Constant(num):
    steps = 0
    if(num == 6174):
        return f"{steps} steps to get 6174 from {num}"
    temp = num
    for i in range(0,7):
        arr = list(str(temp).zfill(4))
        num_arr = [int(i) for i in arr]
        num_arr.sort()
        max_num = ""
        min_num = ""
        for i in num_arr:
            min_num+=str(i)
        num_arr.sort(reverse=True)
        for i in num_arr:
            max_num+=str(i)
        if temp == 6174:
            return f"{steps} steps to get 6174 from {num}"
        temp = int(max_num) - int(min_num)
        steps+=1
    return f"max no.of steps exceeded to get 6174 from {num}"


print(Kaprekars_Constant(2111))
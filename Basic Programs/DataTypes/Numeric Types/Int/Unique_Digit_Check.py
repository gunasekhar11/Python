def Unique_Digit_Check(num):
    arr = [int(i) for i in list(str(num))]
    empty_arr = []
    for i in arr:
        if i in empty_arr:
            return False
        else:
            empty_arr.append(i)
    return True

print(Unique_Digit_Check(1224))
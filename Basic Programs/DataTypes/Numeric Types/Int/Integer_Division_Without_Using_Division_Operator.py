def Integer_Division_Without_Using_Division_Operator(divident,divisor):
    count = 0
    temp = divident
    while temp>=divisor:
        temp = temp - divisor
        count +=1
    return f"{divident} / {divisor} = {count} & Remainder {temp}"


print(Integer_Division_Without_Using_Division_Operator(11,5))
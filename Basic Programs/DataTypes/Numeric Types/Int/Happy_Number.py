def Happy_Number(num):
    already_checked = []
    while num!=1 and num not in already_checked:
        already_checked.append(num)
        arr = [int(i)*int(i) for i in list(str(num))]
        num = sum(arr)

    if num == 1:
        return True
    else:
        return False 



print(Happy_Number(19))
        
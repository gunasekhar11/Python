def Armstrong_Number(num):
    num_str = str(num)
    digits = len(num_str)
    sum_of_digits = 0
    for i in num_str:
        sum_of_digits += int(i)**digits

    return f"{num} is a Armstrong Number" if sum_of_digits == num else f"{num} is not a Armstrong Number"

print(Armstrong_Number(153))
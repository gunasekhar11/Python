def Sum_of_Even_And_Odd(n):
    even_sum = 0
    odd_sum = 0
    for i in range (n):
        if(i%2==0):
            even_sum+=i
        else:
            odd_sum+=i
    return f"evensum {even_sum} , oddsum {odd_sum}"

print(Sum_of_Even_And_Odd(10))
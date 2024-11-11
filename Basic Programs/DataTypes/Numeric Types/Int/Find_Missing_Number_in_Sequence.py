def Find_Missing_Number_in_Sequence(arr):
    n = arr[-1]
    total_sum = (n*(n+1))//2
    return total_sum-sum(arr)

print(Find_Missing_Number_in_Sequence([1,2,3,4,5,7]))
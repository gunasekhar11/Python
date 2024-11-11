def Integer_Square_Root(n):
    start = 0
    end = n
    while start<=end:
        mid = (start+end) // 2
        if(mid*mid == n):
            return mid
        elif(mid*mid > n):
            end = mid - 1
        else:
            start = mid + 1
    return -1

print(Integer_Square_Root(64))
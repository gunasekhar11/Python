def Integer_to_Binary(n):
    if(n==0):
        return "0"
    binary_str = ""
    while n>0:
        remainder = n%2
        binary_str = str(remainder) + binary_str
        n=n//2
    return binary_str

for i in range(100):
    print(Integer_to_Binary(i)) 
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

num1 = 12
num2 = 18

print("GCD:", gcd(num1, num2))
print("LCM:", lcm(num1, num2))
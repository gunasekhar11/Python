int_to_romans = {
    1000: "M", 
    900: "CM", 
    500: "D", 
    400: "CD", 
    100: "C", 
    90: "XC", 
    50: "L", 
    40: "XL", 
    10: "X", 
    9: "IX", 
    5: "V", 
    4: "IV", 
    1: "I"
}

romans_to_int = {
    "I": 1, 
    "V": 5, 
    "X": 10, 
    "L": 50, 
    "C": 100, 
    "D": 500, 
    "M": 1000
}


def Integer_to_Roman(num):
    roman_str = ""
    for value,symbol in int_to_romans.items():
        while num>=value:
            roman_str+=symbol
            num -=value
    return roman_str

def Roman_to_Integer(roman):
    total = 0
    length = len(roman)  
    for i in range(length):
        current_value = romans_to_int[roman[i]]
        if( i+1 < length and current_value < romans_to_int[roman[i+1]]):
            total -= current_value
        else:
            total += current_value

    return total

print(Roman_to_Integer("MXIV"))
print(Integer_to_Roman(Roman_to_Integer("MXIV")))
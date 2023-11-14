def IntToRoman(num: int) -> str:
    num_map = {
        1:"I",
        5: "V",    4: "IV",
        10: "X",   9: "IX",
        50: "L",   40: "XL",
        100: "C",  90: "XC",
        500: "D",  400: "CD",
        1000: "M", 900: "CM",
    }

    r = ''

    for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
            # If n in list then add the roman value to result variable
        while n <= num:
            r += num_map[n]
            num-=n
    return r    

num = 1999
print(IntToRoman(num))

def RomanToInteger(s: str) -> int:
    num_map = {"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000}
    num = 0
    s = s.replace("IV", "IIII").replace("IX", "VIIII")
    s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
    for char in s:
        num += num_map[char]
    return num

    # decimal = 0
    # prev_value = 0
    # dict1 ={"I": 1,"V":5,"X":10,"L":50,"C":100, "D":500, "M" :1000}
    # lenght= len(s)
    # for x in reversed(s) :
    #     value = dict1.get(x, 0)

    #     if value < prev_value:
            
    #         decimal -= value
    #     else:
    #         decimal += value

    #     prev_value = value
    # return decimal
s = "MCMXCIV"
print((reversed(s)))


# Example 2:
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

# Example 3:
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


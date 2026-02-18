import math

def is_armstrong_number(number):
    #digits = int(math.log10(number)) + 1
    digits_str = str(number)
    num_digits = len(digits_str)
    return number == sum(int(digit)**num_digits for digit in digits_str)

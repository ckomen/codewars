def narcissistic(value):
    
    digits = str(value)
    num_digits = len(digits)
    
    
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)
    
    
    return sum_of_powers == value
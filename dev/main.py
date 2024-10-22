def convert_base(num1, b1, b2):
    # Check if num1 is valid in base b1
    try:
        int(num1, b1)
    except ValueError:
        return f"Invalid number '{num1}' for base {b1}"
    
    # Convert num1 from base b1 to base 10
    base_10_num = int(num1, b1)
    
    # Convert the base 10 number to the new base b2
    def from_base_10(n, base):
        if n == 0:
            return '0'
        digits = []
        while n:
            digits.append(int(n % base))
            n //= base
        return ''.join(str(x) for x in digits[::-1])
    
    return from_base_10(base_10_num, b2)

# Example usage:
print("1011(2) to b10")
print(convert_base("1011", 2, 10))  # Output: 11
print(convert_base("A2", 16, 2))    # Output: 10100010
print(convert_base("19", 10, 2))    # Output: 10011
print(convert_base("101", 2, 16))   # Output: 5
print(convert_base("123", 5, 10))   # Output: Invalid number '123' for base 5


number = int(input("Enter \#: "))
base1 = int(input("Enter b1: "))
base2 = int(input("Enter b2: "))
print(convert_base(number, base1, base2))

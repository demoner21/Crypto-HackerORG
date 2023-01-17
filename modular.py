def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

# Example usage
a = 12
b = 8
print(gcd(a, b))

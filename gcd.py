def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

# Example usage
a = 52920
b = 66528
print(gcd(a, b))  # output: 4

# Example usage
a = 52920
b = 66528
print(gcd(a, b))

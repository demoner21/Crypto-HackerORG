def extended_euclidean(a: int, b: int) -> tuple[int, int]:
    if b == 0:
        return (1, 0)
    else:
        q, r = divmod(a, b)
        s, t = extended_euclidean(b, r)
        return (t, s - q * t)

# Example usage
p = 26513
q = 32321
gcd, u, v = extended_euclidean(p, q)
print(gcd)
print(u)
print(v)

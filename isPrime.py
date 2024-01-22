import math

def fibonacci(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")

    if n < 0:
        raise ValueError("Input must be a non-negative integer")

    sqrt5 = math.sqrt(5)
    phi = (1 + sqrt5) / 2

    is_even = n % 2 == 0
    is_positive = n > 0

    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif is_even and is_positive:
        return round((phi**n - (-1/phi)**n) / sqrt5)
    elif not is_even and is_positive:
        return round((phi**(n-1) - (-1/phi)**(n-1)) / sqrt5) + round((phi**(n-2) - (-1/phi)**(n-2)) / sqrt5)
    elif is_even and not is_positive:
        return round((-1)**n * (phi**(-n) - (-1/phi)**(-n)) / sqrt5)
    elif not is_even and not is_positive:
        return round((-1)**n * (phi**(-n) - (-1/phi)**(-n)) / sqrt5)

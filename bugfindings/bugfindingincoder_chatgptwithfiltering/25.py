from typing import List


def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    import math
    fact = []
    i = 0
    while i <= int(math.sqrt(n) + 1):
        if n % i == 0:
            fact.append(i)
            n //= i
        else:
            i += 1

    if n > 1:
        fact.append(n)
    return fact
assert factorize(8) == [2, 2, 2]
assert factorize(10) == [2, 5]
assert factorize(27) == [3, 3, 3]
assert factorize(6) == [2, 3]
assert factorize(2) == [2]
assert factorize(100) == [2, 2, 5, 5]
assert factorize(4) == [2, 2]
assert factorize(3) == [3]
assert factorize(3) == [3,]
assert factorize(9) == [3, 3]
assert factorize(12) == [2,2,3]

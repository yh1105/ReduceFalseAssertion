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
assert factorize(1000) == [2, 2, 2, 5, 5, 5]
assert factorize(20) == [2, 2, 5]
assert factorize(6) == [2, 3]
assert factorize(12) == [2, 2, 3]
assert factorize(27) == [3, 3, 3]
assert factorize(64) == [2, 2, 2, 2, 2, 2]
assert factorize(2) == [2]
assert factorize(3) == [3]
assert factorize(5) == [5]
assert factorize(7) == [7]
assert factorize(11) == [11]
assert factorize(4) == [2, 2]
assert factorize(9) == [3, 3]
assert factorize(25) == [5, 5]
assert factorize(36) == [2, 2, 3, 3]
assert factorize(100) == [2, 2, 5, 5]
assert factorize(10) == [2, 5]
assert factorize(54) == [2, 3, 3, 3]
assert factorize(18) == [2, 3, 3]
assert factorize(13) == [13]
assert factorize(7**7) == [7, 7, 7, 7, 7, 7, 7]
assert factorize(13**13) == [13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13]
assert factorize(8) == [2, 2, 2]
assert factorize(56) == [2, 2, 2, 7]
assert factorize(70) == [2, 5, 7]
assert factorize(15) == [3, 5]
assert factorize(16) == [2, 2, 2, 2]
assert factorize(999) == [3, 3, 3, 37]
assert factorize(1009) == [1009]
assert factorize(1013) == [1013]
assert factorize(1000000) == [2, 2, 2, 2, 2, 2, 5, 5, 5, 5, 5, 5]
assert factorize(126) == [2, 3, 3, 7]
assert factorize(1001) == [7, 11, 13]
assert factorize(500) == [2, 2, 5, 5, 5]
assert factorize(60) == [2, 2, 3, 5]
assert factorize(42) == [2, 3, 7]
assert factorize(111) == [3, 37]
assert factorize(9699690) == [2, 3, 5, 7, 11, 13, 17, 19]
assert factorize(81) == [3, 3, 3, 3]
assert factorize(1024) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
assert factorize(144) == [2, 2, 2, 2, 3, 3]
assert factorize(102) == [2, 3, 17]
assert factorize(14) == [2, 7]
assert factorize(28) == [2, 2, 7]
assert factorize(101) == [101]
assert factorize(2 * 3 * 3 * 5 * 5 * 7 * 7 * 11 * 11 * 13) == [2, 3, 3, 5, 5, 7, 7, 11, 11, 13]
assert factorize(17) == [17]
assert factorize(240) == [2, 2, 2, 2, 3, 5]
assert factorize(356) == [2, 2, 89]
assert factorize(89) == [89]
assert [2, 5] == factorize(10)
assert [2, 7] == factorize(14)
assert [2, 2, 89] == factorize(356)
assert [89] == factorize(89)
assert [2, 2, 2, 5, 5, 5] == factorize(1000)
assert factorize(150) == [2, 3, 5, 5]
assert factorize(45) == [3, 3, 5]
assert factorize(72) == [2, 2, 2, 3, 3]
assert factorize(21) == [3, 7]
assert factorize(22) == [2, 11]
assert factorize(24) == [2, 2, 2, 3]
assert factorize(180) == [2, 2, 3, 3, 5]
assert factorize(2*3*3*5*7*7*7*11*11*11*13) == [2, 3, 3, 5, 7, 7, 7, 11, 11, 11, 13]
assert factorize(2*2*2*5*5*5*5*5*5*5*5*5*5*5*5*13) == [2, 2, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 13]
assert factorize(19) == [19]
assert factorize(23) == [23]
assert factorize(96) == [2, 2, 2, 2, 2, 3]
assert factorize(97) == [97]
assert factorize(29) == [29]
assert factorize(30) == [2, 3, 5]
assert factorize(31) == [31]
assert factorize(2*2*3*3*3*7*7*11*13) == [2, 2, 3, 3, 3, 7, 7, 11, 13]
assert list(factorize(3)) == [3]
assert list(factorize(10)) == [2, 5]
assert list(factorize(12)) == [2, 2, 3]
assert list(factorize(14)) == [2, 7]
assert factorize(2*2) == [2, 2]
assert factorize(2*3) == [2, 3]
assert factorize(3*3) == [3, 3]
assert factorize(2*2*2) == [2, 2, 2]
assert factorize(2*2*3) == [2, 2, 3]
assert factorize(2*2*2*2) == [2, 2, 2, 2]
assert factorize(2*2*2*3) == [2, 2, 2, 3]
assert factorize(3*3*3) == [3, 3, 3]
assert factorize(5*5*5*5) == [5, 5, 5, 5]
assert factorize(2*2*2*2*3) == [2, 2, 2, 2, 3]
assert factorize(2*2*2*2*2) == [2, 2, 2, 2, 2]
assert factorize(2*2*2*2*3*3) == [2, 2, 2, 2, 3, 3]
assert factorize(121) == [11, 11]
assert factorize(123456789) == [3, 3, 3607, 3803]
assert factorize(2 * 3 * 3 * 5 * 7 * 11 * 11 * 13) == [2, 3, 3, 5, 7, 11, 11, 13]
assert factorize(48) == [2, 2, 2, 2, 3]
assert factorize(10000000000) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
assert factorize(3 ** 5 * 11 ** 2) == [3, 3, 3, 3, 3, 11, 11]
assert factorize(2 ** 2 * 7 ** 2 * 41) == [2, 2, 7, 7, 41]
assert factorize(35) == [5, 7]
assert factorize(99) == [3, 3, 11]
assert factorize(625) == [5, 5, 5, 5]
assert factorize(901255) == [5, 17, 23, 461]
assert factorize(93819012551) == [11, 9539, 894119]
assert factorize(2*2*2*2*3*3*3*3*3*7*7*7*11*11*13*13*19) == [2, 2, 2, 2, 3, 3, 3, 3, 3, 7, 7, 7, 11, 11, 13, 13, 19]
assert factorize(354) == [2, 3, 59]
assert factorize(13**3) == [13, 13, 13]
assert factorize(17**4) == [17, 17, 17, 17]
assert factorize(2039) == [2039]
assert factorize(200) == [2, 2, 2, 5, 5]
assert factorize(3 * 5 * 7 * 11 * 11 * 13 * 17) == [3, 5, 7, 11, 11, 13, 17]
assert factorize(37) == [37]
assert factorize(17*19) == [17, 19]
assert factorize(19*17) == [17, 19]
assert factorize(864) == [2, 2, 2, 2, 2, 3, 3, 3]
assert factorize(103) == [103]
assert factorize(1324) == [2, 2, 331]
assert factorize(2222) == [2, 11, 101]
assert factorize(50) == [2, 5, 5]
assert factorize(123) == [3, 41]
assert factorize(120) == [2, 2, 2, 3, 5]
assert factorize(192) == [2, 2, 2, 2, 2, 2, 3]
assert factorize(47) == [47]
assert factorize(98) == [2, 7, 7]
assert factorize(77) == [7, 11]
assert factorize(147) == [3, 7, 7]
assert factorize(7901) == [7901]
assert factorize(132) == [2, 2, 3, 11]
assert factorize(2**3) == [2, 2, 2]
assert factorize(2**5) == [2, 2, 2, 2, 2]
assert factorize(2**10) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
assert factorize(2**7*3**2*5) == [2, 2, 2, 2, 2, 2, 2, 3, 3, 5]
assert factorize(212) == [2, 2, 53]
assert factorize(5040) == [2, 2, 2, 2, 3, 3, 5, 7]
assert factorize(2 ** 2) == [2, 2]
assert factorize(3 ** 4) == [3, 3, 3, 3]
assert factorize(2 ** 3 * 3 ** 3 * 5 ** 2) == [2, 2, 2, 3, 3, 3, 5, 5]
assert factorize(1234) == [2, 617]
assert factorize(1234567) == [127, 9721]
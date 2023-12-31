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
assert factorize(2) == [2]
assert factorize(4) == [2, 2]
assert factorize(12) == [2, 2, 3]
assert factorize(30) == [2, 3, 5]
assert factorize(100) == [2, 2, 5, 5]
assert factorize(120) == [2, 2, 2, 3, 5]
assert factorize(6) == [2, 3]
assert factorize(15) == [3, 5]
assert factorize(36) == [2, 2, 3, 3]
assert factorize(3) == [3]
assert factorize(8) == [2, 2, 2]
assert factorize(9) == [3, 3]
assert factorize(10) == [2, 5]
assert factorize(16) == [2, 2, 2, 2]
assert factorize(18) == [2, 3, 3]
assert factorize(20) == [2, 2, 5]
assert factorize(21) == [3, 7]
assert factorize(22) == [2, 11]
assert factorize(24) == [2, 2, 2, 3]
assert factorize(25) == [5, 5]
assert factorize(26) == [2, 13]
assert factorize(27) == [3, 3, 3]
assert factorize(28) == [2, 2, 7]
assert factorize(5) == [5]
assert factorize(7) == [7]
assert factorize(11) == [11]
assert factorize(13) == [13]
assert factorize(14) == [2, 7]
assert factorize(17) == [17]
assert factorize(19) == [19]
assert factorize(23) == [23]
assert factorize(32) == [2, 2, 2, 2, 2]
assert factorize(33) == [3, 11]
assert factorize(34) == [2, 17]
assert factorize(35) == [5, 7]
assert factorize(37) == [37]
assert factorize(38) == [2, 19]
assert factorize(39) == [3, 13]
assert factorize(40) == [2, 2, 2, 5]
assert factorize(42) == [2, 3, 7]
assert factorize(43) == [43]
assert factorize(44) == [2, 2, 11]
assert factorize(45) == [3, 3, 5]
assert factorize(46) == [2, 23]
assert factorize(47) == [47]
assert factorize(48) == [2, 2, 2, 2, 3]
assert factorize(49) == [7, 7]
assert factorize(51) == [3, 17]
assert factorize(52) == [2, 2, 13]
assert factorize(53) == [53]
assert factorize(54) == [2, 3, 3, 3]
assert factorize(55) == [5, 11]
assert factorize(56) == [2, 2, 2, 7]
assert factorize(57) == [3, 19]
assert factorize(58) == [2, 29]
assert factorize(59) == [59]
assert factorize(60) == [2, 2, 3, 5]
assert factorize(29) == [29]
assert factorize(31) == [31]
assert factorize(41) == [41]
assert factorize(61) == [61]
assert factorize(62) == [2, 31]
assert factorize(63) == [3, 3, 7]
assert factorize(64) == [2, 2, 2, 2, 2, 2]
assert factorize(65) == [5, 13]
assert factorize(66) == [2, 3, 11]
assert factorize(67) == [67]
assert factorize(68) == [2, 2, 17]
assert factorize(69) == [3, 23]
assert factorize(70) == [2, 5, 7]
assert factorize(71) == [71]
assert factorize(72) == [2, 2, 2, 3, 3]
assert factorize(73) == [73]
assert factorize(74) == [2, 37]
assert factorize(75) == [3, 5, 5]
assert factorize(76) == [2, 2, 19]
assert factorize(77) == [7, 11]
assert factorize(78) == [2, 3, 13]
assert factorize(79) == [79]
assert factorize(80) == [2, 2, 2, 2, 5]
assert factorize(50) == [2, 5, 5]
assert factorize(90) == [2, 3, 3, 5]
assert factorize(144) == [2, 2, 2, 2, 3, 3]
assert factorize(160) == [2, 2, 2, 2, 2, 5]
assert factorize(180) == [2, 2, 3, 3, 5]
assert factorize(200) == [2, 2, 2, 5, 5]
assert factorize(210) == [2, 3, 5, 7]
assert factorize(240) == [2, 2, 2, 2, 3, 5]
assert factorize(280) == [2, 2, 2, 5, 7]
assert factorize(320) == [2, 2, 2, 2, 2, 2, 5]
assert factorize(360) == [2, 2, 2, 3, 3, 5]
assert factorize(400) == [2, 2, 2, 2, 5, 5]
assert factorize(420) == [2, 2, 3, 5, 7]
assert factorize(480) == [2, 2, 2, 2, 2, 3, 5]
assert factorize(540) == [2, 2, 3, 3, 3, 5]
assert factorize(600) == [2, 2, 2, 3, 5, 5]
assert factorize(840) == [2, 2, 2, 3, 5, 7]
assert factorize(1080) == [2, 2, 2, 3, 3, 3, 5]
assert factorize(1200) == [2, 2, 2, 2, 3, 5, 5]
assert factorize(1440) == [2, 2, 2, 2, 2, 3, 3, 5]
assert factorize(1680) == [2, 2, 2, 2, 3, 5, 7]
assert factorize(84) == [2, 2, 3, 7]
assert factorize(96) == [2, 2, 2, 2, 2, 3]
assert factorize(108) == [2, 2, 3, 3, 3]
assert factorize(132) == [2, 2, 3, 11]
assert factorize(156) == [2, 2, 3, 13]
assert factorize(168) == [2, 2, 2, 3, 7]
assert factorize(192) == [2, 2, 2, 2, 2, 2, 3]
assert factorize(204) == [2, 2, 3, 17]
assert factorize(216) == [2, 2, 2, 3, 3, 3]
assert factorize(228) == [2, 2, 3, 19]
assert factorize(252) == [2, 2, 3, 3, 7]
assert factorize(264) == [2, 2, 2, 3, 11]
assert factorize(276) == [2, 2, 3, 23]
assert factorize(288) == [2, 2, 2, 2, 2, 3, 3]
assert factorize(300) == [2, 2, 3, 5, 5]
assert factorize(312) == [2, 2, 2, 3, 13]
assert factorize(324) == [2, 2, 3, 3, 3, 3]
assert factorize(336) == [2, 2, 2, 2, 3, 7]
assert factorize(348) == [2, 2, 3, 29]
assert factorize(372) == [2, 2, 3, 31]
assert factorize(384) == [2, 2, 2, 2, 2, 2, 2, 3]
assert factorize(396) == [2, 2, 3, 3, 11]
assert factorize(408) == [2, 2, 2, 3, 17]
assert factorize(432) == [2, 2, 2, 2, 3, 3, 3]
assert factorize(444) == [2, 2, 3, 37]
assert factorize(81) == [3, 3, 3, 3]
assert factorize(82) == [2, 41]
assert factorize(456) == [2, 2, 2, 3, 19]
assert factorize(468) == [2, 2, 3, 3, 13]
assert factorize(492) == [2, 2, 3, 41]
assert factorize(450) == [2, 3, 3, 5, 5]
assert factorize(500) == [2, 2, 5, 5, 5]
assert factorize(720) == [2, 2, 2, 2, 3, 3, 5]
assert factorize(150) == [2, 3, 5, 5]
assert factorize(700) == [2, 2, 5, 5, 7]
assert factorize(800) == [2, 2, 2, 2, 2, 5, 5]
assert factorize(900) == [2, 2, 3, 3, 5, 5]
assert factorize(1000) == [2, 2, 2, 5, 5, 5]
assert factorize(130) == [2, 5, 13]
assert factorize(140) == [2, 2, 5, 7]
assert factorize(170) == [2, 5, 17]
assert factorize(190) == [2, 5, 19]
assert factorize(128) == [2, 2, 2, 2, 2, 2, 2]
assert factorize(256) == [2, 2, 2, 2, 2, 2, 2, 2]
assert factorize(270) == [2, 3, 3, 3, 5]
assert factorize(660) == [2, 2, 3, 5, 11]
assert factorize(780) == [2, 2, 3, 5, 13]
assert factorize(960) == [2, 2, 2, 2, 2, 2, 3, 5]
assert factorize(1020) == [2, 2, 3, 5, 17]
assert factorize(1140) == [2, 2, 3, 5, 19]
assert factorize(1260) == [2, 2, 3, 3, 5, 7]
assert factorize(1320) == [2, 2, 2, 3, 5, 11]
assert factorize(1380) == [2, 2, 3, 5, 23]
assert factorize(1234567890) == [2, 3, 3, 5, 3607, 3803]

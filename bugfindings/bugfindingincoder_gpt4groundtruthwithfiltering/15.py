

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return ' '.join([str(x) for x in range(n)])
assert string_sequence(9) == '0 1 2 3 4 5 6 7 8 9'
assert string_sequence(1) == "0 1"
assert string_sequence(2) == "0 1 2"
assert string_sequence(3) == "0 1 2 3"
assert string_sequence(4) == "0 1 2 3 4"
assert string_sequence(5) == "0 1 2 3 4 5"
assert string_sequence(6) == "0 1 2 3 4 5 6"
assert string_sequence(7) == "0 1 2 3 4 5 6 7"
assert string_sequence(8) == "0 1 2 3 4 5 6 7 8"
assert string_sequence(9) == "0 1 2 3 4 5 6 7 8 9"
assert string_sequence(1) == '0 1'
assert string_sequence(2) == '0 1 2'
assert string_sequence(3) == '0 1 2 3'
assert string_sequence(4) == '0 1 2 3 4'
assert string_sequence(5) == '0 1 2 3 4 5'
assert string_sequence(6) == '0 1 2 3 4 5 6'
assert string_sequence(7) == '0 1 2 3 4 5 6 7'
assert string_sequence(8) == '0 1 2 3 4 5 6 7 8'
assert string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10'
assert string_sequence(11) == '0 1 2 3 4 5 6 7 8 9 10 11'
assert string_sequence(12) == '0 1 2 3 4 5 6 7 8 9 10 11 12'
assert string_sequence(13) == '0 1 2 3 4 5 6 7 8 9 10 11 12 13'
assert string_sequence(14) == '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14'
assert string_sequence(15) == '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15'
assert string_sequence(16) == '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16'
assert string_sequence(100) == "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100"
assert string_sequence(0) == "0"
assert string_sequence(0) == '0'
assert string_sequence(20) == "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20"
assert string_sequence(20) == '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20'
assert string_sequence(10) == "0 1 2 3 4 5 6 7 8 9 10"
assert string_sequence(-1) == ""

from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not numbers:
        return []

    result = []

    for n in numbers[:-1]:
        result.append(n)
        result.append(delimeter)

    return result
assert intersperse([1, 2, 3, 4], 0) == [1, 0, 2, 0, 3, 0, 4]
assert intersperse([5, 6, 7, 8], 9) == [5, 9, 6, 9, 7, 9, 8]
assert intersperse([1], 2) == [1]
assert intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]
assert intersperse([5, 6, 7], 1) == [5, 1, 6, 1, 7]
assert intersperse([10], 2) == [10]
assert intersperse([4, 5, 6], 9) == [4, 9, 5, 9, 6]
assert intersperse([7], 3) == [7]
assert intersperse([1, 2, 3, 4, 5], 6) == [1, 6, 2, 6, 3, 6, 4, 6, 5]
assert intersperse([7, 8, 9], 1) == [7, 1, 8, 1, 9]
assert intersperse([10, 11, 12], 5) == [10, 5, 11, 5, 12]
assert intersperse([13, 14, 15], 7) == [13, 7, 14, 7, 15]
assert intersperse([8], 7) == [8]
assert intersperse([9, 10], 7) == [9, 7, 10]
assert intersperse([13, 14, 15], 2) == [13, 2, 14, 2, 15]
assert intersperse([4, 5, 6], -1) == [4, -1, 5, -1, 6]
assert intersperse([7, 8, 9], 100) == [7, 100, 8, 100, 9]
assert intersperse([7, 8, 9], 10) == [7, 10, 8, 10, 9]
assert intersperse([10, 11, 12], 13) == [10, 13, 11, 13, 12]
assert intersperse([13, 14, 15], 16) == [13, 16, 14, 16, 15]
assert intersperse([1, 2, 3, 4], 5) == [1, 5, 2, 5, 3, 5, 4]
assert intersperse([1, 2, 3, 4], 9) == [1, 9, 2, 9, 3, 9, 4]
assert intersperse([1, 2, 3, 4], -1) == [1, -1, 2, -1, 3, -1, 4]
assert intersperse([7, 8, 9], 2) == [7, 2, 8, 2, 9]
assert intersperse([8, 9, 10], 11) == [8, 11, 9, 11, 10]
assert intersperse([12], 13) == [12]
assert intersperse([1, 2, 3, 4], 10) == [1, 10, 2, 10, 3, 10, 4]
assert intersperse([1], 0) == [1]
assert intersperse([10, 11, 12], 2) == [10, 2, 11, 2, 12]
assert intersperse([8], 3) == [8]
assert intersperse([9, 10], 2) == [9, 2, 10]
assert intersperse([1, 2, 3, 4], 100) == [1, 100, 2, 100, 3, 100, 4]
assert intersperse([4, 5, 6], 1) == [4, 1, 5, 1, 6]
assert intersperse([10], 4) == [10]
assert intersperse([7], 8) == [7]
assert intersperse([7, 8, 9], -1) == [7, -1, 8, -1, 9]
assert intersperse([10, 11, 12], 100) == [10, 100, 11, 100, 12]
assert intersperse([9, 10], 11) == [9, 11, 10]
assert intersperse([5, 6, 7, 8], -1) == [5, -1, 6, -1, 7, -1, 8]
assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]
assert intersperse([10], 3) == [10]
assert intersperse([10, 11, 12], 3) == [10, 3, 11, 3, 12]
assert intersperse([7], 2) == [7]
assert intersperse([8], 2) == [8]
assert intersperse([9, 10], 3) == [9, 3, 10]
assert intersperse([5, 6, 7], 9) == [5, 9, 6, 9, 7]
assert intersperse([8], 1) == [8]
assert intersperse([1, 2, 3], 9) == [1, 9, 2, 9, 3]
assert intersperse([1, 2, 3], 5) == [1, 5, 2, 5, 3]
assert intersperse([1], 5) == [1]
assert intersperse([1, 2], 0) == [1, 0, 2]
assert intersperse([1, 2], 5) == [1, 5, 2]
assert intersperse([9], 8) == [9]
assert intersperse([10, 11], 12) == [10, 12, 11]
assert intersperse([8, 9], 1) == [8, 1, 9]
assert intersperse([4, 5, 6, 7], -1) == [4, -1, 5, -1, 6, -1, 7]
assert intersperse([1, 2, 3, 4, 5], 9) == [1, 9, 2, 9, 3, 9, 4, 9, 5]
assert intersperse([2, 3, 4, 5], 1) == [2, 1, 3, 1, 4, 1, 5]

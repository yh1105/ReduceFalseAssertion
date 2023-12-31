

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(l)
assert unique([1, 2, 1, 3, 2, 5]) == [1, 2, 3, 5]
assert unique([1,1,1,1,1]) == [1]
assert unique([1,1,2,2,3,3,4,4,5,5]) == [1,2,3,4,5]
assert unique(['b','o','b','a','d','i','l','a']) == ['a','b','d','i','l','o']
assert unique(['b','o','b','b','b','b','a','a','a','a','a','d','i','l','a']) == ['a','b','d','i','l','o']
assert unique([]) == []
assert unique([1, 1, 1, 1, 1]) == [1]
assert unique([1, 2, 3, 1, 2, 3, 4]) == [1, 2, 3, 4]
assert unique([5, 0, 1, 2, 3, 1, 2, 3, 4]) == [0, 1, 2, 3, 4, 5]
assert unique([1, 2, 3, 3, 3, 3]) == [1, 2, 3]
assert unique([1, 2, 3, 2, 1, 2, 3]) == [1, 2, 3]
assert unique([1, 2, 3, 2, 3, 1, 3, 2, 1]) == [1, 2, 3]
assert unique([1, 1, 2, 3, 2, 5, 2, 4, 2, 5, 7, 8, 8, 10]) == [1, 2, 3, 4, 5, 7, 8, 10]
assert unique([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert unique([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert unique([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert unique([1, 2, 3]) == [1, 2, 3]
assert unique([1, 2, 1, 3, 2]) == [1, 2, 3]
assert unique([1]) == [1]
assert unique([1, 2, 3, 4]) == [1, 2, 3, 4]
assert unique([1, 1, 1, 1]) == [1]
assert unique([1, 2, 2, 3, 2, 1]) == [1, 2, 3]
assert unique([1, 2, 1, 2, 3, 2, 1]) == [1, 2, 3]
assert unique([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert unique([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
assert unique([1, 2, 1, 2, 3]) == [1, 2, 3]
assert unique([1, 1, 2, 3, 1, 4, 5, 3, 2, 4, 5]) == [1, 2, 3, 4, 5]
assert unique([1, 4, 2, 2, 3, 4, 8]) == [1, 2, 3, 4, 8]
assert unique([1, 1, 2, 3]) == [1, 2, 3]
assert unique([1, 1, 2, 3, 3]) == [1, 2, 3]
assert unique([1, 1, 2, 3, 3, 2]) == [1, 2, 3]
assert unique([1, 1, 2, 3, 3, 2, 1]) == [1, 2, 3]
assert unique([1, 1, 2, 3, 3, 2, 1, 2]) == [1, 2, 3]
assert unique([1, 1, 2, 3, 3, 2, 1, 2, 2]) == [1, 2, 3]
assert unique([1, 1, 2, 3, 3, 2, 1, 2, 2, 1]) == [1, 2, 3]
assert unique([1, 1, 2, 3, 3, 2, 1, 2, 2, 1, 1]) == [1, 2, 3]
assert unique([0, 0, 0, 0, 0]) == [0]
assert unique([4, 3, 4, 3, 2, 1, 1, 5, 5]) == [1, 2, 3, 4, 5]
assert unique([1, 1]) == [1]
assert unique([1, 1, 1]) == [1]
assert unique([1, 2, 1, 2, 1, 2, 1]) == [1, 2]
assert unique([1, 2, 3, 1, 2, 3, 1, 2, 3]) == [1, 2, 3]
assert unique([1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1]
assert unique([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1]
assert unique([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert unique([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert unique([1, 1, 2, 2, 2, 1, 1]) == [1, 2]
assert unique([1, 3, 2, 3, 2, 1, 2, 1, 2, 1]) == [1, 2, 3]
assert unique([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1]
assert unique([1, 1, 1, 1, 1, 1]) == [1]
assert unique([1, 5, 2, 0]) == [0, 1, 2, 5]
assert unique([5,2,1,3]) == [1,2,3,5]
assert unique([2, 3, 4, 5, 6, 7, 7, 7, 8, 8, 9, 3, 3, 1, 1, 1, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == list(range(10))
assert unique([1, 4, 2, 1, 4, 4]) == [1, 2, 4]
assert unique([2, 1, 2, 3, 1, 3, 4, 3, 2, 1]) == [1, 2, 3, 4]
assert unique([1, 2, 1, 1, 2, 3]) == [1, 2, 3]
assert unique([1, 1, 2, 2, 3]) == [1, 2, 3]
assert unique([1, 2, 3, 1, 2, 3]) == [1, 2, 3]
assert unique([3, 2, 1, 3, 2, 1]) == [1, 2, 3]
assert unique([3, 2, 1, 3, 2, 1, 3, 2, 1]) == [1, 2, 3]
assert unique([1, 1, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert unique([1, 1, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 10, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert unique([3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1]) == [1,2,3]
assert unique([2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,1,1,1,1,1,1,1,1,1,1]) == [1,2,3]
assert unique([1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3]) == [1,2,3]
assert unique([5, 2, 3, 1, 4, 2, 6, 2]) == [1, 2, 3, 4, 5, 6]
assert unique([1,1,1,1,1,1]) == [1]
assert unique([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1]
assert unique([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == [1, 2]
assert unique([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2]) == [1, 2]
assert unique([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2]) == [1, 2]
assert unique([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2]) == [1, 2]
assert unique([1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]) == [1, 2]
assert unique([3, 2, 1]) == [1, 2, 3]
assert unique([1, 2, 1, 2, 1]) == [1, 2]
assert unique([1, 2, 3, 2, 1]) == [1, 2, 3]
assert unique([1, 2, 2, 1]) == [1, 2]
assert unique([1, 2, 3, 2, 1, 4, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
assert unique([1, 2, 4, 2, 1]) == [1, 2, 4]
assert unique([1, 4, 2, 2, 4, 4, 4, 1]) == [1, 2, 4]
assert unique([1, 2, 3, 3]) == [1, 2, 3]
assert unique([1, 1, 2, 3, 4, 4, 5, 5, 6, 6, 6, 7, 7, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert unique([1, 1, 1, 1, 1, 5]) == [1, 5]
assert unique([1, 1, 1, 1, 1, 1, 5]) == [1, 5]
assert unique([1, 1, 1, 1, 1, 1, 5, 5]) == [1, 5]
assert unique([1, 1, 1, 1, 1, 1, 5, 5, 6]) == [1, 5, 6]
assert unique([1, 1, 1, 1, 1, 1, 5, 5, 6, 6]) == [1, 5, 6]
assert unique([1, 1, 1, 1, 1, 1, 5, 5, 6, 6, 6]) == [1, 5, 6]
assert unique([1, 1, 1, 1, 1, 1, 5, 5, 6, 6, 6, 6]) == [1, 5, 6]
assert unique([1, 1, 1, 1, 1, 1, 5, 5, 6, 6, 6, 6, 7]) == [1, 5, 6, 7]
assert unique([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1]
assert unique([2, 3, 3, 3, 5, 6, 8, 9, 9]) == [2, 3, 5, 6, 8, 9]
assert unique([1, 1, 1, 1, 1, 1, 1, 2, 3]) == [1, 2, 3]
assert unique([2, 1, 2, 3, 2, 1]) == [1, 2, 3]
assert unique([1, 2, 1, 1, 3, 2, 1]) == [1, 2, 3]
assert unique([0]) == [0]
assert unique([1, 0]) == [0, 1]
assert unique([1, 0, 1]) == [0, 1]
assert unique([1, 0, 1, 0]) == [0, 1]
assert unique([2, 1, 0, 1, 0]) == [0, 1, 2]
assert unique([1,1,1,1,1,1,1]) == [1]
assert unique(list(range(1000000))) == list(range(1000000))

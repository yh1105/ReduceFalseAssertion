

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(l)
assert unique([5, 5, 5]) == [5]
assert unique([1, 1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert unique([1,2,2,3]) == [1,2,3]
assert unique([1,2,2,3,3]) == [1,2,3]
assert unique([1,1,2,2,3]) == [1,2,3]
assert unique([1,1,2,2,3,3]) == [1,2,3]
assert unique([1,1,2,3,3,3,3]) == [1,2,3]
assert unique([2, 3, 4, 5]) == [2, 3, 4, 5]
assert unique([3, 5]) == [3, 5]
assert unique([1, 3, 5]) == [1, 3, 5]
assert unique([5]) == [5]
assert unique([6]) == [6]
assert unique([7, 11]) == [7, 11]
assert unique([7, 9, 11]) == [7, 9, 11]
assert unique([7, 10, 11]) == [7, 10, 11]
assert unique([7, 11, 13]) == [7, 11, 13]
assert unique([7, 9, 11, 13]) == [7, 9, 11, 13]
assert unique([7, 10, 11, 13]) == [7, 10, 11, 13]
assert unique([7, 11, 13, 15]) == [7, 11, 13, 15]
assert unique([7, 9, 11, 13, 15]) == [7, 9, 11, 13, 15]
assert unique([7, 10, 11, 13, 15]) == [7, 10, 11, 13, 15]
assert unique([1, 1, 3]) == [1, 3]
assert unique([1, 3, 3]) == [1, 3]
assert unique([3]) == [3]
assert unique([3, 3]) == [3]
assert unique([3, 3, 3]) == [3]
assert unique([1, 2, 2, 1]) == [1, 2]
assert unique([3, 3, 3, 3, 3]) == [3]
assert unique(['foo', 'foo', 'foo']) == ['foo']
assert unique(['foo', 'foo']) == ['foo']
assert unique([1,2,3,4,5,6,7,8]) == [1,2,3,4,5,6,7,8]
assert unique([1,3,5,6,7,8,9]) == [1,3,5,6,7,8,9]
assert unique([2,3,5,6,7,8,9]) == [2,3,5,6,7,8,9]
assert unique([3,4,5,6,7,8,9]) == [3,4,5,6,7,8,9]
assert unique([1]) == [1]
assert unique([10, 10, 20, 20, 30]) == [10, 20, 30]
assert unique([10, 10, 10, 20, 30, 40, 50, 60, 70, 80]) == [10, 20, 30, 40, 50, 60, 70, 80]
assert unique([10, 10, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
assert unique([1, 2, 3, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert unique([5, 5]) == [5]
assert unique([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert unique([1, 2, 1]) == [1, 2]
assert unique([1, 2]) == [1, 2]
assert unique([2, 1]) == [1, 2]
assert unique([2]) == [2]
assert unique([1, 2, 3]) == [1, 2, 3]
assert unique([1,2]) == [1,2]
assert unique([2, 1, 3, 2]) == [1, 2, 3]
assert unique([2, 1, 2, 3, 1, 3]) == [1, 2, 3]
assert unique([3, 1, 2, 1, 3, 2]) == [1, 2, 3]
assert unique([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]) == [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
assert unique([1, 2, 3, 5]) == [1, 2, 3, 5]
assert unique([0, 1, 2]) == [0, 1, 2]
assert unique([-1, -2, -3]) == [-3, -2, -1]
assert unique(['A', 'B', 'C']) == ['A', 'B', 'C']
assert unique([('A', 'B'), ('C', 'A')]) == [('A', 'B'), ('C', 'A')]
assert unique([True, 1, True]) == [True]
assert unique([1, 1, 2, 3, 3, 5, 6]) == [1, 2, 3, 5, 6]
assert unique([False]) == [False]
assert unique([10, 10, 20, 30, 40]) == [10, 20, 30, 40]
assert unique([1, 2, 3, 1]) == [1, 2, 3]
assert unique([1, 2, 3, 4]) == [1, 2, 3, 4]
assert unique([1, 1, 2]) == [1, 2]
assert sorted(list(unique(['a', 'b', 'c', 'b']))) == ['a', 'b', 'c']
assert unique([1, 2, 3, 1, 2, 3]) == [1, 2, 3]
assert unique([7, 7]) == [7]
assert unique([1, 3, 1]) == [1, 3]
assert unique([1, 2, 2, 3]) == [1, 2, 3]
assert unique([2, 2, 2]) == [2]
assert unique([1, 1, 2, 2]) == [1, 2]
assert unique([1, 2, 2, 3, 3, 3]) == [1, 2, 3]
assert unique([]) == []
assert unique([1, 1, 1]) == [1]
assert unique([2, 2, 1, 2, 1]) == [1, 2]
assert unique([2, 2, 1, 2, 3]) == [1, 2, 3]
assert unique([1,2,3,2,2,2,3]) == [1,2,3]
assert unique([1, 2, 2, 3, 3, 5]) == [1, 2, 3, 5]
assert unique([1,2,2,2,3,3,3]) == [1,2,3]
assert unique([1,1,1,2]) == [1,2]
assert unique([1, 2, 2]) == [1, 2]
assert unique([1,2,3,4,5]) == [1,2,3,4,5]
assert unique([1, 3, 5, 5, 6]) == [1, 3, 5, 6]
assert unique([1,5,5,3,5]) == [1,3,5]
assert unique([2, 2, 3]) == [2, 3]

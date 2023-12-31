
def pluck(arr):
    """
    "Given an array representing a branch of a tree that has non-negative integer nodes
    your task is to pluck one of the nodes and return it.
    The plucked node should be the node with the smallest even value.
    If multiple nodes with the same smallest even value are found return the node that has smallest index.

    The plucked node should be returned in a list, [ smalest_value, its index ],
    If there are no even values or the given array is empty, return [].

    Example 1:
        Input: [4,2,3]
        Output: [2, 1]
        Explanation: 2 has the smallest even value, and 2 has the smallest index.

    Example 2:
        Input: [1,2,3]
        Output: [2, 1]
        Explanation: 2 has the smallest even value, and 2 has the smallest index. 

    Example 3:
        Input: []
        Output: []
    
    Example 4:
        Input: [5, 0, 3, 0, 4, 2]
        Output: [0, 1]
        Explanation: 0 is the smallest value, but  there are two zeros,
                     so we will choose the first zero, which has the smallest index.

    Constraints:
        * 1 <= nodes.length <= 10000
        * 0 <= node.value
    """
    if(len(arr) == 0): return []
    evens = list(filter(lambda x: x%2 == 0, arr))
    if(evens == []): return []
    return [arr.index(min(evens)), min(evens)]
assert pluck([1, 3, 5, 7]) == []
assert pluck([2, 4, 6, 8]) == [2, 0]
assert pluck([1, 2, 3, 4, 5, 6, 7, 8]) == [2, 1]
assert pluck([1, 2, 3, 4, 5, 6]) == [2, 1]
assert pluck([1, 3, 5, 7, 9]) == []
assert pluck([2, 4, 6, 8, 10]) == [2, 0]
assert pluck([2, 4, 6, 8, 10, 2, 4, 6, 8, 10]) == [2, 0]
assert pluck([]) == []
assert pluck([1, 3, 5]) == []
assert pluck([2, 3, 5]) == [2, 0]
assert pluck([2, 4, 5, 6]) == [2, 0]
assert pluck([6, 4, 5, 2]) == [2, 3]
assert pluck([4, 2, 6, 8]) == [2, 1]
assert pluck([2, 4, 6]) == [2, 0]
assert pluck([2, 4, 6, 2, 4, 6]) == [2, 0]
assert pluck([3, 5, 7, 2, 4, 6]) == [2, 3]
assert pluck([3, 5, 7, 2, 4, 6, 2, 4, 6]) == [2, 3]
assert pluck([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [0, 9]
assert pluck([2, 4, 6, 8, 2, 4, 6, 8]) == [2, 0]
assert pluck([1, 3, 5, 7, 2, 4, 6, 8]) == [2, 4]
assert pluck([1, 3, 5, 7, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == [2, 4]
assert pluck([2, 4, 6, 2]) == [2, 0]
assert pluck([1, 3, 5, 7, 9, 2, 4, 6, 8]) == [2, 5]
assert pluck([6, 4, 2]) == [2, 2]
assert pluck([1, 2, 2, 4, 5]) == [2, 1]
assert pluck([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == [2, 0]
assert pluck([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [2, 1]
assert pluck([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [2, 8]
assert pluck([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == [0, 0]
assert pluck([2, 4, 6, 8, 10, 2]) == [2, 0]
assert pluck([2, 4, 6, 8, 10, 12]) == [2, 0]
assert pluck([4, 2, 6, 8, 10, 12]) == [2, 1]
assert pluck([4, 6, 8, 10, 12, 2]) == [2, 5]
assert pluck([3, 2, 4, 6, 8, 10, 12]) == [2, 1]
assert pluck([3, 2, 4, 6, 8, 10, 12, 2]) == [2, 1]
assert pluck([3, 4, 2, 6, 8, 10, 12, 2]) == [2, 2]
assert pluck([3, 4, 6, 2, 8, 10, 12, 2]) == [2, 3]
assert pluck([3, 4, 6, 8, 2, 10, 12, 2]) == [2, 4]
assert pluck([3, 4, 6, 8, 10, 2, 12, 2]) == [2, 5]
assert pluck([3, 4, 6, 8, 10, 12, 2, 2]) == [2, 6]
assert pluck([3, 4, 6, 8, 10, 12, 2, 2, 2]) == [2, 6]
assert pluck([3, 4, 6, 8, 10, 12, 2, 2, 2, 2]) == [2, 6]
assert pluck([3, 4, 6, 8, 10, 12, 2, 2, 2, 2, 2]) == [2, 6]
assert pluck([3, 4, 6, 8, 10, 12, 2, 2, 2, 2, 2, 2]) == [2, 6]
assert pluck([3, 4, 6, 8, 10, 12, 2, 2, 2, 2, 2, 2, 2]) == [2, 6]
assert pluck([3, 4, 6, 8, 10, 12, 2, 2, 2, 2, 2, 2, 2, 2]) == [2, 6]
assert pluck([3, 4, 6, 8, 10, 12, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == [2, 6]
assert pluck([3, 4, 6, 8, 10, 12, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == [2, 6]
assert pluck([3, 4, 6, 8, 10, 12, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == [2, 6]
assert pluck([3, 4, 6, 8, 10, 12, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == [2, 6]
assert pluck([2, 2, 2, 2, 2, 2]) == [2, 0]
assert pluck([0, 1, 2, 3, 4, 5, 6, 7, 8]) == [0, 0]
assert pluck([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [2, 1]
assert pluck([1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == [2, 5]
assert pluck([2, 4, 1, 6, 8, 10]) == [2, 0]
assert pluck([1, 3, 5, 7, 9, 2, 4, 6, 8, 10, 12]) == [2, 5]
assert pluck([1, 3, 5, 7, 9, 2, 4, 6, 8, 10, 12, 14]) == [2, 5]
assert pluck([2, 4, 6, 8, 10, 12, 14, 16]) == [2, 0]
assert pluck([1, 3, 5, 7, 9, 11, 13, 15]) == []
assert pluck([6, 8, 10, 12, 2, 4]) == [2, 4]
assert pluck([1, 2, 3, 4, 5, 6, 2, 4, 6, 8, 10]) == [2, 1]
assert pluck([2, 1, 4, 3, 6, 5]) == [2, 0]
assert pluck([6, 5, 4, 3, 2, 1]) == [2, 4]
assert pluck([1, 3, 5, 2, 4, 6]) == [2, 3]
assert pluck([2, 4, 6, 8, 10, 12, 14]) == [2, 0]
assert pluck([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == [2, 0]
assert pluck([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == []
assert pluck([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == [2, 0]
assert pluck([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [2, 1]
assert pluck([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]) == [2, 0]
assert pluck([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]) == []
assert pluck([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60]) == [2, 0]
assert pluck([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == [2, 1]
assert pluck([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80]) == [2, 0]
assert pluck([2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == [2, 0]
assert pluck([2, 4, 3, 6, 8, 10]) == [2, 0]
assert pluck([4, 2, 6, 8, 10]) == [2, 1]
assert pluck([4, 2, 6, 8, 10, 12, 14, 16]) == [2, 1]
assert pluck([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]) == [2, 0]
assert pluck([4, 2, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]) == [2, 1]
assert pluck([2, 2, 2, 2, 2]) == [2, 0]
assert pluck([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2]) == [2, 1]
assert pluck([1, 3, 5, 7, 9, 2]) == [2, 5]
assert pluck([5, 4, 3, 2, 1]) == [2, 3]
assert pluck([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 4, 6, 8, 10]) == [2, 1]
assert pluck([3, 2, 4, 6, 8]) == [2, 1]
assert pluck([2, 3, 4, 6, 8]) == [2, 0]
assert pluck([2, 4, 6, 8, 2]) == [2, 0]
assert pluck([2, 4, 6, 8, 10, 12, 14, 16, 18]) == [2, 0]
assert pluck([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]) == [2, 0]
assert pluck([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]) == [2, 0]
assert pluck([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26]) == [2, 0]
assert pluck([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]) == [2, 0]
assert pluck([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32]) == [2, 0]
assert pluck([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34]) == [2, 0]
assert pluck([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]) == [2, 0]
assert pluck([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]) == [2, 0]
assert pluck([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42]) == [2, 0]
assert pluck([4, 2, 6]) == [2, 1]
assert pluck([10, 8, 6, 4, 2]) == [2, 4]
assert pluck([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 0]
assert pluck([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 1, 3, 5, 7, 9]) == [2, 0]
assert pluck([8, 6, 4, 2]) == [2, 3]
assert pluck([1, 2, 3, 4, 5, 6, 7, 8, 2, 4, 6, 8]) == [2, 1]
assert pluck([5, 4, 3, 2, 1, 0]) == [0, 5]
assert pluck([0, 1, 2, 3, 4, 5]) == [0, 0]
assert pluck([1, 2, 3, 4, 5, 6, 0]) == [0, 6]
assert pluck([1, 2, 2, 2, 2]) == [2, 1]
assert pluck([1, 3, 5, 7, 8, 9]) == [8, 4]
assert pluck([1, 3, 5, 7, 9, 2, 4, 6, 8, 10, 0]) == [0, 10]
assert pluck([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [0, 10]
assert pluck([2, 2, 2, 2]) == [2, 0]
assert pluck([4, 2, 6, 2]) == [2, 1]
assert pluck([4, 6, 2, 2]) == [2, 2]
assert pluck([4, 6, 8, 2]) == [2, 3]
assert pluck([4, 2, 6, 8, 2]) == [2, 1]
assert pluck([4, 6, 2, 2, 2]) == [2, 2]
assert pluck([4, 6, 8, 2, 2]) == [2, 3]
assert pluck([4, 6, 8, 10, 2]) == [2, 4]
assert pluck([2, 4, 1, 3, 5]) == [2, 0]
assert pluck([3, 2, 1, 4, 5, 6, 7, 8, 9]) == [2, 1]
assert pluck([2, 4, 6, 8, 2, 4, 6, 8, 2, 4, 6, 8]) == [2, 0]
assert pluck([2, 4, 6, 8, 2, 4, 6, 8, 2, 4, 6, 8, 2, 4, 6, 8]) == [2, 0]
assert pluck([2, 4, 6, 8, 2, 4, 6, 8, 2, 4, 6, 8, 2, 4, 6, 8, 2, 4, 6, 8]) == [2, 0]
assert pluck([1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 4, 6, 8]) == [2, 1]
assert pluck([1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 4, 6, 8, 2, 4, 6, 8]) == [2, 1]
assert pluck([1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 4, 6, 8, 2, 4, 6, 8, 2, 4, 6, 8]) == [2, 1]
assert pluck([1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 4, 6, 8, 2, 4, 6, 8, 2, 4, 6, 8, 2, 4, 6, 8]) == [2, 1]
assert pluck([1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 4, 6, 8, 2, 4, 6, 8, 2, 4, 6, 8, 2, 4, 6, 8, 2, 4, 6, 8]) == [2, 1]
assert pluck([1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 4, 6, 8, 2, 4, 6, 8, 2, 4, 6, 8, 2, 4, 6, 8, 2, 4, 6, 8, 2, 4, 6, 8]) == [2, 1]
assert pluck([1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 4, 6, 8, 2, 4, 6, 8, 2, 4, 6, 8, 2, 4, 6, 8, 2, 4, 6, 8, 2, 4, 6, 8, 2, 4, 6, 8, 2, 4, 6, 8]) == [2, 1]
assert pluck([1, 2, 3, 4, 5]) == [2, 1]
assert pluck([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == []
assert pluck([2]) == [2, 0]
assert pluck([1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == [2, 9]
assert pluck([2, 1, 4, 3, 6, 5, 8, 7, 10, 9]) == [2, 0]
assert pluck([1, 3, 5, 7, 9, 2, 4, 6, 8, 10, 2, 4, 6, 8, 10]) == [2, 5]
assert pluck([2, 4, 6, 1, 8, 10]) == [2, 0]
assert pluck([2, 4, 6, 8, 10, 2, 4, 6, 8, 10, 2, 4, 6, 8, 10]) == [2, 0]
assert pluck([1, 3, 5, 7, 9]) == [], "Test case 2 failed"
assert pluck([]) == [], "Test case 3 failed"
assert pluck([2, 4, 6, 8, 10]) == [2, 0], "Test case 4 failed"
assert pluck([1, 2, 2, 3, 4, 5, 6, 6]) == [2, 1], "Test case 5 failed"
assert pluck([1, 2, 4, 6, 8]) == [2, 1]
assert pluck([2, 4, 6, 8, 10, 1, 3, 5, 7]) == [2, 0]
assert pluck([1, 3, 5, 7, 2, 4, 6, 8, 10]) == [2, 4]
assert pluck([10, 8, 6, 4, 2, 1, 3, 5, 7]) == [2, 4]
assert pluck([1, 3, 5, 7, 2, 4, 6, 8, 10, 1, 3, 5, 7]) == [2, 4]
assert pluck([2, 3, 4, 5, 6, 7, 8, 9, 10]) == [2, 0]
assert pluck([2, 2, 2, 2, 2, 2, 2, 2, 2]) == [2, 0]
assert pluck([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 4, 6, 8]) == [2, 1]
assert pluck([2, 3, 4, 5, 6, 7, 8]) == [2, 0]
assert pluck([2, 4, 6, 8, 2, 4, 6, 8, 10]) == [2, 0]
assert pluck([10, 8, 6, 4, 2, 8, 6, 4, 2]) == [2, 4]
assert pluck([10, 8, 6, 4, 2, 8, 6, 4, 2, 10]) == [2, 4]
assert pluck([10, 8, 6, 4, 2, 8, 6, 4, 2, 10, 12]) == [2, 4]
assert pluck([1, 2, 2, 4, 5, 6]) == [2, 1]
assert pluck([1, 2, 3, 4, 5, 6, 2, 4, 6]) == [2, 1]
assert pluck([1, 2, 3, 4, 5, 6, 7]) == [2, 1]
assert pluck([3, 2, 4, 6, 8, 10]) == [2, 1]
assert pluck([1, 1, 1, 1, 2, 2, 2, 2]) == [2, 4]
assert pluck([9, 7, 5, 3, 1]) == []

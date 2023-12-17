
def exchange(lst1, lst2):
    """In this problem, you will implement a function that takes two lists of numbers,
    and determines whether it is possible to perform an exchange of elements
    between them to make lst1 a list of only even numbers.
    There is no limit on the number of exchanged elements between lst1 and lst2.
    If it is possible to exchange elements between the lst1 and lst2 to make
    all the elements of lst1 to be even, return "YES".
    Otherwise, return "NO".
    For example:
    exchange([1, 2, 3, 4], [1, 2, 3, 4]) => "YES"
    exchange([1, 2, 3, 4], [1, 5, 3, 4]) => "NO"
    It is assumed that the input lists will be non-empty.
    """
    odd = 0
    even = 0
    for i in lst1:
        if i%2 == 1:
            even -= 1
    for i in lst2:
        if i%2 == 0:
            odd += 1
    if even >= odd:
        return "YES"
    return "NO"
            
assert exchange([2, 3, 4, 5], [1, 5, 5, 8]) == "NO"
assert exchange([2, 3, 4, 5], []) == "NO"
assert exchange([1, 4, 5], [7, 3, 5]) == "NO"
assert exchange([5, 4, 9], [1, 3, 7]) == "NO"
assert exchange([1, 1, 2], [1, 1, 2]) == "NO"
assert exchange([1, 2, 3], [1, 2, 3]) == "NO"
assert exchange([1, 2, 3], [4, 5, 7]) == "NO"
assert exchange([4, 5, 3], [3, 2, 1]) == "NO"
assert exchange([1, 2, 3], [3, 4, 5]) == "NO"
assert exchange([1, 3, 4], [3, 4, 5]) == "NO"
assert exchange([1, 2, 3], [1, 4, 5]) == "NO"
assert exchange([2, 2, 2], [4, 5, 6]) == "YES"
assert exchange([1, 2, 3], [1, 5, 6]) == "NO"
assert exchange([2, 3, 4, 5], [1, 7, 12, 13]) == "NO"
assert exchange([2, 3, 3], [3, 1, 1]) == "NO"
assert exchange([1, 2, 3], [1, 3, 5]) == "NO"
assert exchange([1, 2, 3], [5, 3, 1]) == "NO"
assert exchange([1, 2, 3], [1, 5, 3]) == "NO"
assert exchange([1, 2, 3], [3, 2, 1]) == "NO"
assert exchange([1, 2, 3], [3, 1, 2]) == "NO"
assert exchange([1, 2, 3], [3, 1, 5]) == "NO"
assert exchange([1, 2, 3], [5, 1, 3]) == "NO"
assert exchange([0], []) == "YES"
assert exchange([1], []) == "NO"
assert exchange([2], []) == "YES"
assert exchange([1, 3], []) == "NO"
assert exchange([1, 3, 4], []) == "NO"
assert exchange([1, 3, 4, 5], []) == "NO"
assert exchange([1, 3, 4, 5, 6], []) == "NO"
assert exchange([1, 3, 4, 5, 6, 7], []) == "NO"
assert exchange([1, 3, 5, 6], [4, 5, 8, 9]) == "NO"
assert exchange([1, 4, 5], [3, 2, 1]) == "NO"
assert exchange([1, 2, 3], []) == "NO"
assert exchange([2, 4, 6], [2, 4, 6]) == "YES"
assert exchange([2, 4, 6], [2, 4, 8]) == "YES"
assert exchange([3, 5, 7], [1, 4, 6]) == "NO"
assert exchange([2, 2, 2], [2, 2, 2]) == "YES"
assert exchange([1, 3, 5], [4, 5, 6]) == "NO"
assert exchange([1, 2, 3], [5, 5, 5]) == "NO"
assert exchange([3, 5, 7], [4, 5, 6]) == "NO"
assert exchange([2, 2, 2], [4, 4, 4]) == "YES"
assert exchange([1, 1, 1], [1, 1, 1]) == "NO"
assert exchange([0, 0, 0], [4, 4, 4]) == "YES"
assert exchange([4, 4, 4], [4, 4, 4]) == "YES"
assert exchange([1, 2, 3], [3, 4, 7]) == "NO"
assert exchange([1, 2, 3], [4, 5, 5]) == "NO"
assert exchange([2, 2, 2, 2], [5, 1, 4, 6]) == "YES"
assert exchange([2, 3, 5, 7], [3, 5, 7, 9]) == "NO"
assert exchange([1,3,5,7], [8,9,10,11]) == "NO"
assert exchange([2, 3, 5, 7], [1, 10, 4, 9]) == "NO"
assert exchange([3, 1, 7], [1, 4, 6]) == "NO"
assert exchange([1, 2, 5], [1, 2, 5]) == "NO"
assert exchange([], [1, 2, 3]) == "YES"
assert exchange([2, 3, 4, 7], [1, 5, 7, 4]) == "NO"
assert exchange([5, 5, 5, 5], [5, 5, 5, 5]) == "NO"
assert exchange([2, 5, 5, 5], [5, 5, 5, 2]) == "NO"
assert exchange([2, 4, 6], [1, 3, 5]) == "YES"
assert exchange([2, 3, 4], [1, 5, 7]) == "NO"
assert exchange([1, 2, 3], [7, 8, 9]) == "NO"
assert exchange([1, 2, 3], [2, 3, 5]) == "NO"
assert exchange([4, 1, 2, 3], [2, 3, 5]) == "NO"
assert exchange([6, 5, 13, 16], [3, 4, 1, 15]) == "NO"
assert exchange([1, 1, 1, 3], [1, 1, 1, 2]) == "NO"
assert exchange([3, 5, 4, 1], [8, 6, 7, 9]) == "NO"
assert exchange([2, 2, 2], [2, 4, 6]) == "YES"
assert exchange([1, 1, 1], []) == "NO"
assert exchange([2, 2, 4], [2, 3, 4]) == "YES"
assert exchange([1, 2, 3], [5, 6, 7]) == "NO"
assert exchange([2, 2, 2], [3, 3, 3]) == "YES"
assert exchange([2, 2, 2], [3, 3, 3, 5]) == "YES"
assert exchange([2, 4, 6, 8], [1, 3, 5]) == "YES"
assert exchange([1, 2, 3], [2, 1, 3]) == "NO"
assert exchange([], []) == "YES"
assert exchange([2, 4, 6], [8, 8, 8]) == "YES"
assert exchange([2, 4, 6], [8, 8, 8, 8]) == "YES"
assert exchange([2, 4, 6], [8, 8, 8, 8, 10]) == "YES"
assert exchange([1, 2, 3, 5], [3, 4, 5, 6]) == "NO"
assert exchange([5, 1, 2, 3, 4], [1, 3, 4, 5, 6]) == "NO"
assert exchange([3, 5, 7], [1, 1, 1]) == "NO"
assert exchange([1, 2, 3], [3, 4, 1]) == "NO"
assert exchange([1, 3, 5], [6, 7, 8]) == "NO"
assert exchange([2, 2, 2, 2], [1, 1, 1, 1]) == "YES"
assert exchange([2, 2, 2, 2], [1, 2, 1, 2]) == "YES"
assert exchange([1, 3, 2, 4], [6, 5]) == "NO"
assert exchange([1, 2, 3], [1, 3, 4]) == "NO"
assert exchange([1, 2, 3], [1, 2, 5]) == "NO"
assert exchange([1, 2, 3], [7, 5, 6]) == "NO"
assert exchange([1, 2, 3], [7, 5, 6, 7]) == "NO"
assert exchange([1, 3, 5], [7, 6, 5]) == "NO"
assert exchange([1, 3, 5], [8, 7, 6]) == "NO"
assert exchange([5, 3, 1], [10, 8, 7]) == "NO"
assert exchange([1, 3, 5], [1, 4, 6]) == "NO"
assert exchange([2, 6, 4, 8], [1, 5, 7, 9]) == "YES"
assert exchange([6, 2, 8, 4], [1, 5, 7, 9]) == "YES"
assert exchange([1, 3, 5], [4, 8, 9]) == "NO"
assert exchange([5, 5, 2, 1], [3, 7, 4, 3]) == "NO"
assert exchange([5, 5, 2, 3], [3, 7, 4, 1]) == "NO"
assert exchange([2, 4, 6, 8], [1, 3, 5, 7]) == "YES"
assert exchange([1, 3, 5], [1, 2, 4]) == "NO"
assert exchange([1, 2, 3], [1, 4, 3, 5, 7]) == "NO"
assert exchange([1, 2, 3], [1, 4, 3, 7]) == "NO"
assert exchange([2, 4, 6, 8], [1, 3, 5, 6]) == "YES"
assert exchange([2, 3, 4, 5], [1, 3, 5, 7]) == "NO"
assert exchange([1, 4, 5, 7], []) == "NO"
assert exchange([1, 2, 3, 5], [1, 2, 3, 5]) == "NO"
assert exchange([1,2,3], [4,5,7]) == "NO"
assert exchange([1,1,2,3], [4,5,7,8]) == "NO"
assert exchange([1,1,2,3], [4,5,7,8,9]) == "NO"
assert exchange([1, 2, 1], [1, 2, 1]) == "NO"
assert exchange([1, 2, 3], [1, 1, 1]) == "NO"
assert exchange([1, 2, 1], [1, 1, 1]) == "NO"
assert exchange([1, 9, 5, 2], [3, 9, 5, 2]) == "NO"
assert exchange([2, 4, 6, 8], [1, 3, 5, 7, 9]) == "YES"
assert exchange([2, 3, 4], [1, 3, 5]) == "NO"
assert exchange([1, 1, 2], [1, 1, 1]) == "NO"
assert exchange([2, 3, 4], [1, 1, 5]) == "NO"
assert exchange([3, 4, 5], [1, 2, 3]) == "NO"
assert exchange([3, 4, 6, 8], [1, 7, 5, 9]) == "NO"
assert exchange([2, 3, 5, 7], [1, 9, 5, 3]) == "NO"
assert exchange([1, 3, 5, 2], [1, 3, 5, 2]) == "NO"
assert exchange([3, 4, 6, 7], [1, 2, 3, 5]) == "NO"
assert exchange([2, 4, 6, 8], [1, 2, 3, 5]) == "YES"
assert exchange([1, 0, 1, 3], [4, 5, 6, 7]) == "NO"
assert exchange([2, 3, 1], [1, 5, 6]) == "NO"
assert exchange([7, 1, 5], [1, 4, 2]) == "NO"
assert exchange([1, 7, 5], [4, 2, 3]) == "NO"
assert exchange([2, 2, 2], [1, 1, 1]) == "YES"
assert exchange([1, 3, 2], [3, 2, 3]) == "NO"
assert exchange([1, 2, 1], [2, 1, 1]) == "NO"
assert exchange([3, 5, 7], [1, 2, 6]) == "NO"
assert exchange([3, 3, 3], [3, 3, 3]) == "NO"
assert exchange([3, 5, 2], [1, 7, 5]) == "NO"
assert exchange([2, 2, 1], [1, 1, 1]) == "NO"
assert exchange([2, 2, 1], [3, 3, 3]) == "NO"
assert exchange([1, 1, 1], [3, 3, 3]) == "NO"
assert exchange([1, 3, 5], [3, 4, 6]) == "NO"
assert exchange([1, 3, 5], [4, 2, 7]) == "NO"
assert exchange([5, 5, 5, 9, 9], [5, 5, 5, 9, 9]) == "NO"
assert exchange([1, 3, 5], [5, 7, 9]) == "NO"
assert exchange([1, 3, 3], [4, 5, 6]) == "NO"
assert exchange([2, 5, 7, 8], [1, 3, 5, 7]) == "NO"
assert exchange([4, 4, 4, 4], [4, 4, 4, 4]) == "YES"



def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l = sorted(l)
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        return (l[len(l) - 1 // 2] + l[len(l) // 2]) / 2.0
assert median([1, 2, 3]) == 2.0
assert median([1, 2, 3, 4, 5, 6]) == 3.5
assert median([1, 2, 3, 4, 5, 6, 7]) == 4.0
assert median([5, 2, 7, 4, 1, 6, 3]) == 4.0
assert median([1, 2, 3, 4, 5, 6, 7, 8]) == 4.5
assert median([8, 6, 7, 5, 3, 0, 9]) == 6.0
assert median([1, 2, 3, 4]) == 2.5
assert median([1, 1, 2, 3, 4]) == 2
assert median([1, 1, 2, 3, 4, 5]) == 2.5
assert median([1]) == 1
assert median([1, 2, 3, 4, 5]) == 3
assert median([5, 4, 3, 2, 1]) == 3
assert median([1, 3, 2, 5, 4]) == 3
assert median([1, 2, 3, 4]) == 2.5, "Test case 2 failed"
assert median([5, 4, 3, 2, 1]) == 3, "Test case 3 failed"
assert median([1, 3, 5, 2, 4]) == 3, "Test case 4 failed"
assert median([1, 1, 1, 1, 1]) == 1, "Test case 5 failed"
assert median([1, 2, 3, 4, 5, 6]) == 3.5, "Test case 2 failed"
assert median([1, 2, 3, 4, 5, 6, 7]) == 4, "Test case 3 failed"
assert median([5, 2, 8, 1, 9]) == 5, "Test case 4 failed"
assert median([3, 6, 1, 2, 8, 4, 5]) == 4, "Test case 5 failed"
assert median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5.5
assert median([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 5.0
assert median([1]) == 1.0
assert median([1, 3, 2, 4, 5]) == 3, "Test case 3 failed"
assert median([5, 4, 3, 2, 1]) == 3, "Test case 4 failed"
assert median([1, 2, 3, 4, 5, 6]) == 3.5, "Test case 5 failed"
assert median([1, 2, 3, 4, 5, 6, 7]) == 4, "Test case 6 failed"
assert median([1, 2, 3, 4, 5, 6, 7, 8]) == 4.5, "Test case 4 failed"
assert median([1]) == 1, "Test case 5 failed"
assert median([1, 2]) == 1.5, "Test case 6 failed"
assert median([2, 1]) == 1.5, "Test case 7 failed"
assert median([5, 4, 3, 2, 1]) == 3, "Test case 8 failed"
assert median([6, 5, 4, 3, 2, 1]) == 3.5, "Test case 4 failed"
assert median([1, 1, 1, 1]) == 1, "Test case 5 failed"
assert median([1, 1, 1, 2]) == 1, "Test case 6 failed"
assert median([1, 2, 3, 4, 5, 6, 7]) == 4
assert median([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 5
assert median([1, 2, 3, 4]) == 2.5, 'Test Case 2 Failed'
assert median([5, 2, 8, 1, 9]) == 5, 'Test Case 3 Failed'
assert median([3, 1, 4, 2]) == 2.5, 'Test Case 4 Failed'
assert median([1, 1, 1, 1, 1, 1]) == 1, 'Test Case 5 Failed'
assert median([1, 2, 3, 4, 5, 6, 7]) == 4.0, "Test case 3 failed"
assert median([1, 3, 5, 7, 9]) == 5.0, "Test case 4 failed"
assert median([2, 4, 6, 8, 10]) == 6.0, "Test case 5 failed"
assert median([1]) == 1.0, "Test case 6 failed"
assert median([1, 3]) == 2.0, "Test case 7 failed"
assert median([2, 4]) == 3.0, "Test case 8 failed"
assert median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5.5, "Test case 9 failed"
assert median([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 5.5, "Test case 10 failed"
assert median([4, 5, 6, 7]) == 5.5, "Test case 2 failed"
assert median([1, 2, 3, 4, 5]) == 3, "Test case 3 failed"
assert median([1]) == 1, "Test case 4 failed"
assert median([10, 20, 30, 40, 50]) == 30, "Test case 3 failed"
assert median([1, 1, 1, 1, 1, 1, 1]) == 1, "Test case 4 failed"
assert median([2, 4, 6, 8, 10]) == 6, "Test case 5 failed"
assert median([10, 20, 30, 40, 50]) == 30.0
assert median([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 11.0
assert median([1, 3, 5]) == 3, "Test case 3 failed"
assert median([2, 4, 6, 8]) == 5, "Test case 4 failed"
assert median([1, 2, 3, 4, 5, 6]) == 3.5, "Error: Test Case 2"
assert median([1]) == 1, "Error: Test Case 3"
assert median([4, 5, 6, 7]) == 5.5, "Error: Test Case 2"
assert median([8, 9, 10, 11, 12]) == 10, "Error: Test Case 3"
assert median([13, 14, 15, 16, 17, 18]) == 15.5, "Error: Test Case 4"
assert median([19, 20, 21, 22, 23, 24, 25]) == 22, "Error: Test Case 5"
assert median([1, 3, 2]) == 2
assert median([2, 1, 3]) == 2
assert median([3, 1, 2]) == 2
assert median([2, 3, 1]) == 2
assert median([1, 2, 3, 4]) == 2.5, "Test case 5 failed"
assert median([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 5, "Test case 5 failed"
assert median([10, 20, 30, 40]) == 25.0
assert median([1, 2]) == 1.5
assert median([5, 2, 9, 1, 7]) == 5
assert median([1, 1, 1, 1, 1, 1]) == 1
assert median([3, 1, 4, 2, 5]) == 3, "Test case 3 failed"
assert median([1, 3, 2, 4, 5]) == 3, "Test case 5 failed"
assert median([1]) == 1, "Test case 6 failed"
assert median([1, 2]) == 1.5, "Test case 7 failed"
assert median([2, 1]) == 1.5, "Test case 8 failed"
assert median([1, 2, 3, 4, 5, 6]) == 3.5, "Test case 9 failed"
assert median([6, 5, 4, 3, 2, 1]) == 3.5, "Test case 10 failed"
assert median([4, 2, 1, 3]) == 2.5
assert median([1, 1, 1, 1]) == 1
assert median([1, 2, 3, 4, 5, 6, 7]) == 4, "Error: Test Case 3"
assert median([1, 3, 5, 7, 9]) == 5, "Error: Test Case 4"
assert median([2, 4, 6, 8, 10]) == 6, "Error: Test Case 5"
assert median([1, 2, 3, 4, 5, 6]) == 3.5, 'Test Case 2 Failed'
assert median([1, 2, 3, 4, 5, 6, 7]) == 4, 'Test Case 3 Failed'
assert median([1, 2, 3, 4, 5, 6, 7, 8]) == 4.5, 'Test Case 4 Failed'
assert median([5]) == 5, 'Test Case 5 Failed'
assert median([1]) == 1, "Test case 3 failed"
assert median([2, 4, 6, 8, 10]) == 6, "Test case 4 failed"
assert median([3, 1, 4, 2]) == 2.5, "Test case 5 failed"
assert median([5, 4, 3, 2, 1]) == 3, "Error: Test case 2 failed"
assert median([1, 3, 2, 5, 4]) == 3, "Error: Test case 3 failed"
assert median([1, 2, 3, 4]) == 2.5, "Error: Test case 4 failed"
assert median([4, 3, 2, 1]) == 2.5, "Error: Test case 5 failed"
assert median([1, 2, 3]) == 2, "Error: Test case 6 failed"
assert median([3, 2, 1]) == 2, "Error: Test case 7 failed"
assert median([1]) == 1, "Error: Test case 8 failed"
assert median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5.5, "Test case 5 failed"
assert median([5, 2, 7, 3, 8]) == 5, "Test case 3 failed"
assert median([4, 5, 6, 7]) == 5.5, 'Test Case 2 Failed'
assert median([1, 2, 3, 4, 5]) == 3, 'Test Case 3 Failed'
assert median([1]) == 1, 'Test Case 4 Failed'
assert median([1, 2, 3, 4]) == 2.5, "Test case 3 failed"
assert median([10, 20, 30, 40, 50]) == 30, 'Test Case 3 Failed'
assert median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5.5, 'Test Case 4 Failed'
assert median([1, 2, 3]) == 2
assert median([1, 1, 1, 1]) == 1, "Test case 4 failed"
assert median([1, 1, 1, 1, 1]) == 1.0
assert median([1, 1, 1, 2, 2, 2]) == 1.5
assert median([1]) == 1, 'Test Case 3 Failed'
assert median([2, 4, 6, 8, 10]) == 6, 'Test Case 4 Failed'
assert median([5, 5, 5, 5, 5]) == 5, 'Test Case 5 Failed'
assert median([1, 3, 5, 7, 9]) == 5, "Test case 3 failed"
assert median([2, 4, 6, 8, 10, 12]) == 7, "Test case 4 failed"
assert median([1, 3, 5, 2, 4]) == 3
assert median([5]) == 5.0
assert median([1, 3, 5, 7, 9]) == 5.0, "Test case 3 failed"
assert median([2, 4, 6, 8, 10]) == 6.0, "Test case 4 failed"
assert median([1, 3, 2]) == 2, "Test case 5 failed"
assert median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5.5, "Test case 6 failed"
assert median([1, 2, 3]) == 2, "Test case 3 failed"
assert median([1, 2]) == 1.5, "Test case 4 failed"


def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    odd_digit_elements = []
    for j, i in enumerate(x):
        if all (int(c) % 2 == 1 for c in str(i)):
            odd_digit_elements.append(i)
            odd_digit_elements.append(j)
    return sorted(odd_digit_elements)
assert 	unique_digits([]) == []
assert unique_digits([1, 3, 5, 7, 9]) == [1, 3, 5, 7, 9]
assert unique_digits([]) == []
assert unique_digits([1, 3, 4, 5, 6, 7, 8, 9, 0]) == [1, 3, 5, 7, 9]
assert 	unique_digits([1,3,5,7,9]) == [1,3,5,7,9]
assert unique_digits([3, 7, 4, 10, 9, 1]) == [1, 3, 7, 9]

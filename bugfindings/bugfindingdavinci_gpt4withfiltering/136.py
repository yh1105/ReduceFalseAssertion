
def largest_smallest_integers(lst):
    '''
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    '''
    smallest = list(filter(lambda x: x < 0, lst))
    largest = list(filter(lambda x: x > 0, lst))
    largest = list(filter(lambda x: x > 0, smallest))
    smallest = list(filter(lambda x: x > 0, largest))
    return (max(smallest) if smallest else None, min(largest) if largest else None)
assert largest_smallest_integers([]) == (None, None)
assert largest_smallest_integers([1, 3, 5]) == (None, 1)
assert largest_smallest_integers([4, -7, 8, 2, 0, 2]) == (-7, 2)
assert largest_smallest_integers([1, -1, -1, -1, -1, 1]) == (-1, 1)
assert largest_smallest_integers([-1, 0, 1]) == (-1, 1)
assert largest_smallest_integers([0, 1]) == (None, 1)
assert largest_smallest_integers([-1, 0]) == (-1, None)
assert largest_smallest_integers([0]) == (None, None)
assert largest_smallest_integers([0, -1, 1]) == (-1, 1)
assert largest_smallest_integers([0, 0, 0]) == (None, None)
assert largest_smallest_integers([-2, 0, 1, 2, 3, 10]) == (-2, 1)
assert largest_smallest_integers([1, 2, 3, 10]) == (None, 1)
assert largest_smallest_integers([1, 1, 1, 1, 2, 2]) == (None, 1)
assert largest_smallest_integers([-2, -2, -2, -2, -2]) == (-2, None)
assert largest_smallest_integers([0, 0, 0, 0, 0]) == (None, None)
assert largest_smallest_integers([1, 1, 1, 1, 1, 1, 1, 1, 1]) == (None, 1)
assert largest_smallest_integers([0, 0, 0, 0, 0, 0, 0, 0, 0]) == (None, None)
assert largest_smallest_integers([0,0,0,0]) == (None, None)
assert largest_smallest_integers([-1,0,1,2]) == (-1, 1)
assert largest_smallest_integers([1,2,3,4,5]) == (None, 1)
assert largest_smallest_integers([5, 6, 7, 8, 9]) == (None, 5)
assert largest_smallest_integers([0, 1, 2]) == (None, 1)
assert largest_smallest_integers([0,0,-1,0]) == (-1, None)
assert largest_smallest_integers([2]) == (None, 2)
assert largest_smallest_integers([-1]) == (-1, None)
assert largest_smallest_integers([-1,0,1]) == (-1, 1)
assert largest_smallest_integers([0,0,0]) == (None, None)
assert largest_smallest_integers([0, -1, 0]) == (-1, None)
assert largest_smallest_integers([-1, -1, -1]) == (-1, None)
assert largest_smallest_integers([1, 1, 1]) == (None, 1)
assert largest_smallest_integers([1, 2, 3, 4, 5, 3, 8, 9, 10]) == (None, 1)
assert largest_smallest_integers([2, 3, 4, 5, 6]) == (None, 2)
assert largest_smallest_integers([0, 0, 0, 0, 0, 0]) == (None, None)
assert largest_smallest_integers([2, 5, 1, 9, 7, 3]) == (None, 1)
assert largest_smallest_integers([1, 2, 3]) == (None, 1)
assert largest_smallest_integers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == (None, 1)
assert largest_smallest_integers([10, 11, 8, 2, 6, 8, 12, 0]) == (None, 2)
assert largest_smallest_integers([10, 2, 1, 7, 1, 5, 8, 10, 5]) == (None, 1)
assert largest_smallest_integers([1, 2, 3, 4, 5]) == (None, 1)
assert largest_smallest_integers([1, 2, 3, 4, 5, 0]) == (None, 1)
assert largest_smallest_integers([-2, -2, -2, -2, -2, -2, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2]) == (-2, 2)
assert largest_smallest_integers([0, 0, 0, 0, 0, 0, 0]) == (None, None)
assert largest_smallest_integers([0, 1, 2, 3, 4, 5]) == (None, 1)
assert largest_smallest_integers([-1, 0, 1, 2, 3, 4, 5]) == (-1, 1)
assert largest_smallest_integers([8, 10, 12, 2, 4, 6, 3]) == (None, 2)
assert largest_smallest_integers([10, 20, 30]) == (None, 10)
assert largest_smallest_integers([-1, -1, -1, -1, -1]) == (-1, None)
assert largest_smallest_integers([1, 1, 1, 1, 1]) == (None, 1)
assert largest_smallest_integers([-2,-2,-2,-2,-2]) == (-2, None)
assert largest_smallest_integers([0, 1, 2, 3]) == (None, 1)
assert largest_smallest_integers([0, 0, 5, 3, 6]) == (None, 3)
assert largest_smallest_integers([-1, -1, -1, -1]) == (-1, None)
assert largest_smallest_integers([1, 1, 1, 1]) == (None, 1)
assert largest_smallest_integers([0, 1, 2, 3, 4]) == (None, 1)
assert largest_smallest_integers([-1, 2, -1, 3, 1]) == (-1, 1)
assert largest_smallest_integers([-1, 1]) == (-1, 1)
assert largest_smallest_integers([1]) == (None, 1)
assert largest_smallest_integers([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == (None, 1)
assert largest_smallest_integers([4, 6, 8, 10]) == (None, 4)
assert largest_smallest_integers([10, 8, 6, 4, 2]) == (None, 2)
assert largest_smallest_integers([1, 1, 1, -1, -1, 1]) == (-1, 1)
assert largest_smallest_integers([1, 1, 1, 1, 1, 1, 1]) == (None, 1)
assert largest_smallest_integers([-1, -1, -1, -1, -1, -1, -1]) == (-1, None)
assert largest_smallest_integers([2, 3, 4, 1, 5, 6, 7]) == (None, 1)
assert largest_smallest_integers([-1, -1, -1, -1, -1, -1, 1]) == (-1, 1)
assert largest_smallest_integers([-1, -1, -1, -1, -1, 1, 1]) == (-1, 1)
assert largest_smallest_integers([-1, -1, -1, -1, 1, 1, 1]) == (-1, 1)
assert largest_smallest_integers([-1, -1, -1, 1, 1, 1, 1]) == (-1, 1)
assert largest_smallest_integers([-4, -4, -4, -4]) == (-4, None)
assert largest_smallest_integers([4, 4, 4, 4]) == (None, 4)
assert largest_smallest_integers([0, 1, 0, 1, 0, 1]) == (None, 1)

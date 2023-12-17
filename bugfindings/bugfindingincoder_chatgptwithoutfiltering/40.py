

def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triples_sum_to_zero([1, 3, 5, 0])
    False
    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """
    for i in range(1, len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                if l[i] + l[j] + l[k] == 0:
                    return True
    return False
assert triples_sum_to_zero([1, -1, 0]) is True
assert triples_sum_to_zero([-7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == True
assert triples_sum_to_zero([3, -1, -2, -4, -5]) == True
assert triples_sum_to_zero([-1, 5, -3, 4]) is True
assert triples_sum_to_zero([0, 1, -1]) is True
assert triples_sum_to_zero([-2, 0, 2]) == True
assert triples_sum_to_zero([0, -3, 2, 1]) == True
assert triples_sum_to_zero([1, 2, -3, -4, 10, -6, 12])
assert triples_sum_to_zero([4, -2, 2, 5, -3]) is True
assert triples_sum_to_zero([5, 1, 2, 3, -3]) is True
assert triples_sum_to_zero([-1, 5, -6, -7, 8, -4, -5, -9, -8]) == True
assert triples_sum_to_zero([-1, -3, -4, -6, 8, -5, -7, -9, 10]) == True

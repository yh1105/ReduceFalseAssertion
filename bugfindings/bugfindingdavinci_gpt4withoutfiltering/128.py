
def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    """
    if not arr: return None
    prod = 0 if 0 in arr else (-1) ** 2 * len(list(filter(lambda x: x < 0, arr)))
    return prod * sum([abs(i) for i in arr])
assert (prod_signs([]) == None), "prod_signs failed"
assert prod_signs([]) is None
assert prod_signs([]) == None
assert prod_signs([]) is None, "Wrong answer"
assert prod_signs([]) == None, "Return value for an empty array incorrect"
assert prod_signs([]) is None, 'error2'

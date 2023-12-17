
def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    def digits_sum(n):
        neg = 1
        if n < 0: n, neg = -1 * n, -1 + n 
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg
        return sum(n)
    return sorted(nums, key=digits_sum)
assert order_by_points([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert order_by_points([1, 2, 3, 4, 5, 6, 7]) == [1, 2, 3, 4, 5, 6, 7]
assert order_by_points([1, 3]) == [1, 3]
assert order_by_points([1, 3, 3, 3]) == [1, 3, 3, 3]
assert order_by_points([2, 3, 4, 5]) == [2, 3, 4, 5]
assert order_by_points([1]) == [1]
assert order_by_points([12, 3, 6]) == [12, 3, 6]
assert order_by_points([10, 20, 30, 40, 50]) == [10, 20, 30, 40, 50]
assert order_by_points([100, 200, 300]) == [100, 200, 300]
assert order_by_points([100, 200, 300, 500, 600, 700, 800]) == [100, 200, 300, 500, 600, 700, 800]
assert order_by_points([100, 200, 300, 500, 600, 700, 800, 900]) == [100, 200, 300, 500, 600, 700, 800, 900]
assert order_by_points([1, 12, 31, 32, 34]) == [1, 12, 31, 32, 34]
assert order_by_points([1, 12, 31, 33, 34]) == [1, 12, 31, 33, 34]
assert order_by_points([1, 12, 31, 33, 34, 35]) == [1, 12, 31, 33, 34, 35]
assert order_by_points([1, 1, 12, 31, 33, 34, 35]) == [1, 1, 12, 31, 33, 34, 35]
assert order_by_points([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
assert order_by_points([1, 2, 3, 4]) == [1, 2, 3, 4]
assert order_by_points([1, 2, 3, 4, 5, 6, 7, 8]) == [1, 2, 3, 4, 5, 6, 7, 8]
assert order_by_points([1, 1, 1]) == [1, 1, 1]
assert order_by_points([13]) == [13]
assert order_by_points([9]) == [9]
assert order_by_points([12]) == [12]
assert order_by_points([7, 7, 7, 7, 7]) == [7, 7, 7, 7, 7]
assert order_by_points([10, 11, 12, 13, 14, 15]) == [10, 11, 12, 13, 14, 15]
assert order_by_points([1, 3, 5]) == [1, 3, 5]
assert order_by_points([1, 3, 4]) == [1, 3, 4]
assert order_by_points([9, 9, 9, 9]) == [9, 9, 9, 9]
assert order_by_points([5]) == [5]
assert order_by_points([7]) == [7]
assert order_by_points([11, 11, 11, 11, 11, 11, 11, 11, 11]) == [11, 11, 11, 11, 11, 11, 11, 11, 11]
assert order_by_points([5, 5]) == [5, 5]
assert order_by_points([1,3,5]) == [1,3,5]
assert order_by_points([1, 2, 3]) == [1, 2, 3]
assert order_by_points([10, 10, 10, 10, 10, 10, 10]) == [10, 10, 10, 10, 10, 10, 10]
assert order_by_points([10, 10, 10, 10, 10]) == [10, 10, 10, 10, 10]
assert order_by_points([10, 10]) == [10, 10]
assert order_by_points([1, 9, 9, 9, 9]) == [1, 9, 9, 9, 9]
assert order_by_points([18]) == [18]
assert order_by_points([]) == []
assert order_by_points([99]) == [99]

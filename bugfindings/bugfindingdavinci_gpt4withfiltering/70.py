
def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''
    res, switch = [], False
    while lst:
        res.append(min(lst) if switch else max(lst))
        lst.remove(res[-1])
        switch = not switch
    return res
assert strange_sort_list([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]
assert strange_sort_list([2, 5, 3, 1, 9, 4]) == [1, 9, 2, 5, 3, 4]
assert strange_sort_list([1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]
assert strange_sort_list([]) == []
assert strange_sort_list([4, 5, 3, 1, 2]) == [1, 5, 2, 4, 3]
assert strange_sort_list([1,2,3,4,5]) == [1,5,2,4,3]
assert strange_sort_list([1, 3, 5, 4, 2]) == [1, 5, 2, 4, 3]
assert strange_sort_list([1, 3, 2, 4, 5]) == [1, 5, 2, 4, 3]
assert strange_sort_list([1, 2, 3, 4, 5, 6]) == [1, 6, 2, 5, 3, 4]
assert strange_sort_list([5, 2, 6, 9, 3, 1, 8, 10, 4, 7]) == [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
assert strange_sort_list([5, 2, 6, 9, 3, 1, 8, 10, 7, 4]) == [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
assert strange_sort_list([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 9, 2, 8, 3, 7, 4, 6, 5]
assert strange_sort_list([5, 3, 1, 4, 2]) == [1, 5, 2, 4, 3]
assert strange_sort_list([5, 4, 3, 2, 1]) == [1, 5, 2, 4, 3]
assert strange_sort_list([3, 2, 1]) == [1, 3, 2]
assert strange_sort_list([2, 1]) == [1, 2]
assert strange_sort_list([0, 1]) == [0, 1]
assert strange_sort_list([1, 0]) == [0, 1]
assert strange_sort_list([1, 2, 0]) == [0, 2, 1]
assert strange_sort_list([6, 2, 5, 1, 4, 0, 3]) == [0, 6, 1, 5, 2, 4, 3]
assert strange_sort_list([-5, -3, -1, 0, 1, 3, 5]) == [-5, 5, -3, 3, -1, 1, 0]
assert strange_sort_list([-10, -10, 0, 10, 10]) == [-10, 10, -10, 10, 0]
assert strange_sort_list([-5, -3, -1, 0, 1, 3, 5, -10, -10, 0, 10, 10]) == [-10, 10, -10, 10, -5, 5, -3, 3, -1, 1, 0, 0]
assert strange_sort_list([5, 4, 3, 1, 2]) == [1, 5, 2, 4, 3]
assert strange_sort_list([3, 2, 2, 1]) == [1, 3, 2, 2]
assert strange_sort_list([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [0, 9, 1, 8, 2, 7, 3, 6, 4, 5]
assert strange_sort_list([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5]
assert strange_sort_list([4, 2, 3, 1, 8, 6, 5, 7]) == [1, 8, 2, 7, 3, 6, 4, 5]
assert strange_sort_list([8, 2, 7, 4, 1, 6, 5, 3]) == [1, 8, 2, 7, 3, 6, 4, 5]
assert strange_sort_list([5, 6, 4, 3, 7, 2, 1]) == [1, 7, 2, 6, 3, 5, 4]
assert strange_sort_list([2, 3, 5, 4, 1]) == [1, 5, 2, 4, 3]
assert strange_sort_list([1, 1, 2, 2, 2, 1, 2, 1]) == [1, 2, 1, 2, 1, 2, 1, 2]
assert strange_sort_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
assert strange_sort_list([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
assert strange_sort_list([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
assert strange_sort_list([1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
assert strange_sort_list([4, 1, 3, 2, 5]) == [1, 5, 2, 4, 3]
assert strange_sort_list([4, 1, 3, 5, 2]) == [1, 5, 2, 4, 3]
assert strange_sort_list([4, 3, 1, 5, 2]) == [1, 5, 2, 4, 3]
assert strange_sort_list([4, 3, 1, 2, 5]) == [1, 5, 2, 4, 3]
assert strange_sort_list([1, 5, 2, 4, 3, 6]) == [1, 6, 2, 5, 3, 4]
assert strange_sort_list([1, 5, 2, 6, 3, 4]) == [1, 6, 2, 5, 3, 4]
assert strange_sort_list([10, 4, 15, 12, 9, 5, 6, 8, 7, 1, 3, 14, 2, 11, 13]) == [1, 15, 2, 14, 3, 13, 4, 12, 5, 11, 6, 10, 7, 9, 8]
assert strange_sort_list([4, 5, 1, 6, 3, 8, 2, 7]) == [1, 8, 2, 7, 3, 6, 4, 5]
assert strange_sort_list([3, 2, 4, 5, 1, 6, 7, 8]) == [1, 8, 2, 7, 3, 6, 4, 5]
assert strange_sort_list([1, 2, 3, 4, 5, 6, 7, 8]) == [1, 8, 2, 7, 3, 6, 4, 5]
assert strange_sort_list([8, 7, 6, 5, 4, 3, 2, 1]) == [1, 8, 2, 7, 3, 6, 4, 5]
assert strange_sort_list([9, 5, 8, 3, 4, 6, 7, 1, 2]) == [1, 9, 2, 8, 3, 7, 4, 6, 5]
assert strange_sort_list([1, 3, 5, 7, 9, 2, 4, 6, 8]) == [1, 9, 2, 8, 3, 7, 4, 6, 5]
assert strange_sort_list([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 9, 2, 8, 3, 7, 4, 6, 5]
assert strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
assert strange_sort_list([1, 2, 3, 3, 3, 4]) == [1, 4, 2, 3, 3, 3]
assert strange_sort_list([1, 2, 1, 2, 1, 2, 1, 2]) == [1, 2, 1, 2, 1, 2, 1, 2]
assert strange_sort_list([1, 2, 1, 2, 1, 2, 1, 2, 1]) == [1, 2, 1, 2, 1, 2, 1, 2, 1]
assert strange_sort_list([1,5,2,4,3]) == [1,5,2,4,3]
assert strange_sort_list([10, 4, 8, 2, 6, 3, 4, 7, 4, 0, 9, 1, 5]) == [0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 4, 5, 4]
assert strange_sort_list([4, 2, 3, 1, 0]) == [0, 4, 1, 3, 2]
assert strange_sort_list([4, 0, 1, 3, 2]) == [0, 4, 1, 3, 2]
assert strange_sort_list([1, 2, 2, 3, 2, 4, 2, 5]) == [1, 5, 2, 4, 2, 3, 2, 2]
assert strange_sort_list([5, 2, 7, 1, 4]) == [1, 7, 2, 5, 4]
assert strange_sort_list([5, 2, 2, 1, 4]) == [1, 5, 2, 4, 2]
assert strange_sort_list([2, 1, 3]) == [1, 3, 2]
assert strange_sort_list([9, 0, 1, 7, 2, 5, 6, 4, 3, 8]) == [0, 9, 1, 8, 2, 7, 3, 6, 4, 5]
assert strange_sort_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == [0, 9, 1, 8, 2, 7, 3, 6, 4, 5]
assert strange_sort_list([1, 4, 3, 2, 5]) == [1, 5, 2, 4, 3]
assert strange_sort_list([4, 4, 4, 4, 4]) == [4, 4, 4, 4, 4]
assert strange_sort_list([4, 8, 7, 6, 1, 5, 2, 3]) == [1, 8, 2, 7, 3, 6, 4, 5]
assert strange_sort_list([19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 19, 2, 18, 3, 17, 4, 16, 5, 15, 6, 14, 7, 13, 8, 12, 9, 11, 10]
assert strange_sort_list([8, 5, 7, 1, 6, 2, 4, 3]) == [1, 8, 2, 7, 3, 6, 4, 5]
assert strange_sort_list([1, 2, 3, 4, 5, 6, 7]) == [1, 7, 2, 6, 3, 5, 4]
assert strange_sort_list([1, 2, 3, 5, 4]) == [1, 5, 2, 4, 3]
assert strange_sort_list([3, 4, 2, 1, 5]) == [1, 5, 2, 4, 3]
assert strange_sort_list([1, 2, 3, 5, 4, 6]) == [1, 6, 2, 5, 3, 4]
assert strange_sort_list([4, 3, 2, 1, 5]) == [1, 5, 2, 4, 3]
assert strange_sort_list([5, 4, 1, 2, 3]) == [1, 5, 2, 4, 3]
assert strange_sort_list([3, 2, 1, 4, 5]) == [1, 5, 2, 4, 3]
assert strange_sort_list([1, 5, 4, 3, 2]) == [1, 5, 2, 4, 3]
assert strange_sort_list([3, 8, 2, 1, 7, 4, 6, 5]) == [1, 8, 2, 7, 3, 6, 4, 5]
assert strange_sort_list([1, 3, 5, 2, 4]) == [1, 5, 2, 4, 3]
assert strange_sort_list([-1, -1, -1, -1, -1]) == [-1, -1, -1, -1, -1]
assert strange_sort_list([1,1,1,1,1]) == [1,1,1,1,1]
assert strange_sort_list([2, 7, 3, 1, 0, 4, 6, 5]) == [0, 7, 1, 6, 2, 5, 3, 4]
assert strange_sort_list([4, 6, 2, 1, 7, 5, 3]) == [1, 7, 2, 6, 3, 5, 4]
assert strange_sort_list([2, 3, 1, 4, 7, 6, 5]) == [1, 7, 2, 6, 3, 5, 4]
assert strange_sort_list([1, 2, 4, 5, 6, 7, 3]) == [1, 7, 2, 6, 3, 5, 4]
assert strange_sort_list([7, 6, 5, 4, 3, 2, 1]) == [1, 7, 2, 6, 3, 5, 4]
assert strange_sort_list([7, 6, 4, 5, 3, 2, 1]) == [1, 7, 2, 6, 3, 5, 4]
assert strange_sort_list([5, 1, 2, 4, 3]) == [1, 5, 2, 4, 3]
assert strange_sort_list([9,8,7,6,5,4,3,2,1]) == [1,9,2,8,3,7,4,6,5]
assert strange_sort_list([1,1,1,1,1,1,1,1,1]) == [1,1,1,1,1,1,1,1,1]
assert strange_sort_list([9, 9, 9, 9, 9]) == [9, 9, 9, 9, 9]
assert strange_sort_list([3, 5, 7, 9, 1]) == [1, 9, 3, 7, 5]
assert strange_sort_list([4, 6, 2, 1, 9, 10, 8, 5, 7, 3]) == [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
assert strange_sort_list([3, 3, 2, 1, 4]) == [1, 4, 2, 3, 3]
assert strange_sort_list([8, 4, 0, 9, 1, 5, 2, 7, 3, 6]) == [0, 9, 1, 8, 2, 7, 3, 6, 4, 5]
assert strange_sort_list([9, 7, 4, 5, 1, 2, 6, 3, 8]) == [1, 9, 2, 8, 3, 7, 4, 6, 5]
assert strange_sort_list([-100, -100, -100, -100, -100, -100, -100, -100, -100]) == [-100, -100, -100, -100, -100, -100, -100, -100, -100]
assert strange_sort_list([3, 5, 4, 2, 1]) == [1, 5, 2, 4, 3]
assert strange_sort_list([7, 4, 5, 6, 3, 1, 2, 8, 9, 10]) == [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
assert strange_sort_list([9, 3, 8, 1, 7, 2, 6, 4, 5]) == [1, 9, 2, 8, 3, 7, 4, 6, 5]
assert strange_sort_list([1,2,3,4,5,6,7,8,9]) == [1,9,2,8,3,7,4,6,5]
assert strange_sort_list([1, 3, 5, 7, 9]) == [1, 9, 3, 7, 5]
assert strange_sort_list([1, 4, 8, 12, 16]) == [1, 16, 4, 12, 8]

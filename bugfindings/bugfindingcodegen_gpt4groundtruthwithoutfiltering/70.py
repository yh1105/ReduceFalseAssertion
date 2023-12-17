
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
assert 	strange_sort_list([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
assert 	strange_sort_list([]) == [], "Empty list"
assert 	strange_sort_list([]) == []
assert 	strange_sort_list([1, 1, 1]) == [1, 1, 1]
assert 	strange_sort_list([1, 1, 1, 1]) == [1, 1, 1, 1]
assert 	strange_sort_list([1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]

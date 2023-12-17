
def sorted_list_sum(lst):
    """Write a function that accepts a list of strings as a parameter,
    deletes the strings that have odd lengths from it,
    and returns the resulted list with a sorted order,
    The list is always a list of strings and never an array of numbers,
    and it may contain duplicates.
    The order of the list should be ascending by length of each word, and you
    should return the list sorted by that rule.
    If two words have the same length, sort the list alphabetically.
    The function should return a list of strings in sorted order.
    You may assume that all words will have the same length.
    For example:
    assert list_sort(["aa", "a", "aaa"]) => ["aa"]
    assert list_sort(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]
    """
    lst.sort()
    new_lst = []
    for i in lst:
        if len(i)%2 == 0:
            new_lst.append(i)
    return new_lst
assert sorted_list_sum([]) == []
assert sorted_list_sum([""]) == [""]
assert sorted_list_sum(["", ""]) == ["", ""]
assert sorted_list_sum(['test']) == ['test']
assert sorted_list_sum([])  == []
assert sorted_list_sum(['k']) == []
assert sorted_list_sum(['ab', 'bc', 'ca', 'da']) == ['ab', 'bc', 'ca', 'da']
assert sorted_list_sum(['ab', 'cd', 'ef']) == ['ab', 'cd', 'ef']
assert sorted_list_sum([]) == [], 'incorrect list sum'


def get_row(lst, x):
    """
    You are given a 2 dimensional data, as a nested lists,
    which is similar to matrix, however, unlike matrices,
    each row may contain a different number of columns.
    Given lst, and integer x, find integers x in the list,
    and return list of tuples, [(x1, y1), (x2, y2) ...] such that
    each tuple is a coordinate - (row, columns), starting with 0.
    Sort coordinates initially by rows in ascending order.
    Also, sort coordinates of the row by columns in descending order.
    
    Examples:
    get_row([
      [1,2,3,4,5,6],
      [1,2,3,4,1,6],
      [1,2,3,4,5,1]
    ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
    get_row([], 1) == []
    get_row([[], [1], [1, 2, 3]], 3) == [(2, 2)]
    """
    coords = [(j, i) for i in range(len(lst)) for j in range(len(lst[i])) if lst[i][j] == x]
    return sorted(sorted(coords, key=lambda x: x[1], reverse=True), key=lambda x: x[0])
assert get_row([[1, 2, 3], [4, 5], [6, 7, 8, 9]], 5) == [(1, 1)]
assert get_row([[1, 2, 3], [4, 5], [6, 7, 8, 9]], 7) == [(2, 1)]
assert get_row([[1, 2, 3], [4, 5], [6, 7, 8, 9]], 9) == [(2, 3)]
assert get_row([[1, 2, 3], [4, 5], [6, 7, 8, 9]], 10) == []
assert get_row([[1, 2, 3], [4, 5], [6, 7, 8, 9]], 9) == [(2, 3)], 'Test Case 2 Failed'
assert get_row([[1, 2, 3], [4, 5], [6, 7, 8, 9]], 1) == [(0, 0)], 'Test Case 3 Failed'
assert get_row([[1, 2, 3], [4, 5], [6, 7, 8, 9]], 10) == [], 'Test Case 4 Failed'
assert get_row([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 9) == [(2, 2)]
assert get_row([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 10) == []
assert get_row([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 7) == [(2, 0)]
assert get_row([[1,2,3],[4,5,6],[7,8,9]], 10) == []
assert get_row([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5) == [(1, 1)]
assert get_row([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 4) == [(1, 0)]
assert get_row([[1, 2, 3], [4, 5], [6, 7, 8, 9]], 4) == [(1, 0)]
assert get_row([[1, 2, 3], [4, 5], [6, 7, 8, 9]], 2) == [(0, 1)]
assert get_row([[1, 2, 3], [4, 5], [6, 7, 8, 9]], 1) == [(0, 0)]
assert get_row([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], 6) == [(1, 2)]
assert get_row([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], 11) == [(3, 1)]
assert get_row([[1, 2], [4, 5, 6], [7, 8, 9]], 2) == [(0, 1)]
assert get_row([[1, 2, 3], [4, 5], [6, 7, 8, 9]], 0) == []
assert get_row([[1,2,3],[4,5],[6,7,8,9]], 9) == [(2,3)]
assert get_row([[1,2,3],[4,5],[6,7,8,9]], 10) == []
assert get_row([[1, 2, 3], [4, 5], [6, 7, 8, 9]], 6) == [(2, 0)]
assert get_row([[1,2,3],[4,5],[6,7,8,9]], 9) == [(2, 3)]
assert get_row([[1,2,3],[4,5],[6,7,8,9]], 2) == [(0, 1)]
assert get_row([[1,2,3],[4,5],[6,7,8,9]], 6) == [(2, 0)]
assert get_row([[1,2,3],[4,5],[6,7,8,9]], 1) == [(0, 0)]
assert get_row([[1, 2], [3, 4, 5], [6, 7, 8, 9]], 7) == [(2, 1)]
assert get_row([[1, 2, 3], [4, 5], [6, 7, 8, 9]], 3) == [(0, 2)]
assert get_row([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 8) == [(2, 1)]
assert get_row([[1,2,3],[4,5,6],[7,8,9]], 7) == [(2,0)]
assert get_row([[1, 2, 3], [4, 5], [6, 7, 8, 9]], 9) == [(2, 3)], "Test case 2 failed"
assert get_row([[1, 2, 3], [4, 5], [6, 7, 8, 9]], 10) == [], "Test case 3 failed"
assert get_row([[1, 2, 3], [4, 5], [6, 7, 8, 9]], 6) == [(2, 0)], "Test case 5 failed"
assert get_row([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3) == [(0, 2)]
assert get_row([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1) == [(0, 0)]


def minPath(grid, k):
    """
    Given a grid with N rows and N columns (N >= 2) and a positive integer k, 
    each cell of the grid contains a value. Every integer in the range [1, N * N]
    inclusive appears exactly once on the cells of the grid.

    You have to find the minimum path of length k in the grid. You can start
    from any cell, and in each step you can move to any of the neighbor cells,
    in other words, you can go to cells which share an edge with you current
    cell.
    Please note that a path of length k means visiting exactly k cells (not
    necessarily distinct).
    You CANNOT go off the grid.
    A path A (of length k) is considered less than a path B (of length k) if
    after making the ordered lists of the values on the cells that A and B go
    through (let's call them lst_A and lst_B), lst_A is lexicographically less
    than lst_B, in other words, there exist an integer index i (1 <= i <= k)
    such that lst_A[i] < lst_B[i] and for any j (1 <= j < i) we have
    lst_A[j] = lst_B[j].
    It is guaranteed that the answer is unique.
    Return an ordered list of the values on the cells that the minimum path go through.

    Examples:

        Input: grid = [ [1,2,3], [4,5,6], [7,8,9]], k = 3
        Output: [1, 2, 1]

        Input: grid = [ [5,9,3], [4,1,6], [7,8,2]], k = 1
        Output: [1]
    """
    n = len(grid)
    val = n * n + 1
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                temp = []
                if i != 0:
                    temp.append(grid[i][j])

                if j != 0:
                    temp.append(grid[i][j])

                if i != n - 1:
                    temp.append(grid[i][j])

                if j != n - 1:
                    temp.append(grid[i][j])

                val = min(temp)

    ans = []
    for i in range(k):
        if i % 2 == 0:
            ans.append(1)
        else:
            ans.append(val)
    return ans
assert minPath([[1,2,3],[2,3,4],[3,4,5]], 2) == [1,2]
assert minPath([[1,1,1],[1,1,1],[1,1,1]], 5) == [1,1,1,1,1]
assert minPath([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 4) == [1, 1, 1, 1], '2'
assert minPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2) == [1, 2]
assert minPath([[1,2,3],[4,5,6],[7,8,9]], 2) == [1,2]
assert minPath([[1,2,3],[4,5,6],[7,8,9]], 1) == [1]
assert (minPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1) == [1])
assert minPath([[3,2,1], [4,5,6], [7,8,9]], 2) == [1,2]
assert minPath([[1,1,1], [1,1,1], [1,1,1]], 5) == [1,1,1,1,1]
assert minPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1) == [1]
assert minPath([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 9) == [1, 1, 1, 1, 1, 1, 1, 1, 1]
assert minPath([[1,2,3],[4,5,6],[7,8,9]], 2) == [1,2], 'not correct'
assert minPath([[1,2,3],[4,5,6],[7,8,9]], 1) == [1], 'not correct'
assert minPath([[1, 2, 3], [3, 2, 1], [2, 1, 3]], 1) == [1]
assert minPath([[1, 2, 3], [3, 2, 6], [2, 1, 8]], 4) == [1, 2, 1, 2]
assert (minPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2) == [1, 2])
assert minPath([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 2) == [1, 1]
assert minPath([[1, 2, 2], [1, 1, 1], [2, 1, 1]], 6) == [1, 1, 1, 1, 1, 1]
assert minPath([[1, 2, 3], [3, 4, 5], [5, 6, 7]], 1) == [1]
assert minPath([[1, 2, 3], [3, 4, 5], [5, 6, 7]], 2) == [1, 2]
assert minPath([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 5) == [1, 1, 1, 1, 1]
assert minPath([[1, 2, 3], [2, 3, 4], [3, 4, 5]], 2) == [1, 2]
assert minPath([[1, 2, 3], [2, 3, 4], [3, 4, 5]], 1) == [1]
assert minPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0) == []
assert minPath([[9,8,7],[6,5,4],[3,2,1]], 1) == [1]
assert minPath([[9,8,7],[6,5,4],[3,2,1]], 2) == [1,2]
assert (minPath([[1, 2, 3], [2, 3, 4], [3, 4, 5]], 2) == [1, 2])
assert (minPath([[1, 2, 3], [2, 3, 4], [3, 4, 5]], 1) == [1])
assert (minPath([[8, 4, 7], [6, 5, 9]], 0) == [])
assert minPath([[1, 4, 7], [2, 5, 8], [3, 6, 9]], 1) == [1]
assert minPath([[1, 4, 7], [2, 5, 8], [3, 6, 9]], 2) == [1, 2]
assert minPath([[1, 2, 3], [2, 3, 4], [5, 6, 7]], 2) == [1, 2]
assert minPath([[1, 2, 3], [2, 3, 4], [5, 6, 7]], 1) == [1]

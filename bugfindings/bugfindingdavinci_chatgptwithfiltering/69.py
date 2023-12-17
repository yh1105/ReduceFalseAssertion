
def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    '''
    frq = [0] * (max(lst) + 1)
    for i in lst:
        frq[i] += 1;

    ans = 0
    for i in range(1, len(frq)):
        if frq[i] >= i:
            ans = i
    
    return ans
assert search([0, 1, 2, 3, 4, 4, 4, 4, 2, 2, 2, 1, 1, 1, 0, 0, 0]) == 4
assert search([1, 2, 3, 2, 1, 2, 3, 2, 3]) == 3
assert search([1, 2, 2, 2, 2, 2, 2, 2, 2]) == 2
assert search([1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
assert search([1,1,1,1,4,4,4,4,4,4]) == 4
assert search([1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3]) == 3
assert search([1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4]) == 4
assert search([4,4,4,4,4,4,4,4,4,4]) == 4
assert search([1,2,2,2,2,2,2,2,2,2]) == 2
assert search([1,1,1,1,1,1,1,1,1,1]) == 1
assert search([1,2,3,3,3,3,3,3,3,3]) == 3
assert search([1,1,1,1,1,1,1,1,1,4,4,4,4,4,4,4,4,4,4]) == 4
assert search([3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]) == 3
assert search([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
assert search([1, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5]) == 5
assert search([2,2,2,2,2,2,2,2,2,2]) == 2
assert search([9,9,9,9,9,9,9,9,9,9]) == 9
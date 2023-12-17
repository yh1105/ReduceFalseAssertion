

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l = sorted(l)
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        return (l[len(l) - 1 // 2] + l[len(l) // 2]) / 2.0
assert median([1, 2, 3, 5, 7]) == 3
assert median([3, 1, 2, 5, 7]) == 3
assert median([1, 2, 3, 5, 7, 9]) == 4
assert median([3, 1, 2, 5, 3]) == 3
assert median([1, 300, 2, 200, 1]) == 2
assert median([3, 6, 20, 99, 10, 15]) == 12.5
assert median([1, 1, 2, 4, 5]) == 2
assert median([1, 1, 2, 3, 4, 5, 5]) == 3
assert median([1, 1, 1, 1, 1]) == 1
assert median([1,1,1,1,1]) == 1
assert median([1]) == 1
assert median([1, 2]) == 1.5
assert median([2, 1]) == 1.5
assert median([1, 2, 3]) == 2
assert median([1, 2, 3, 4]) == 2.5
assert median([1, 2, 3, 4, 5]) == 3
assert median([3, 2, 4, 1, 5]) == 3
assert median([2, 3, 1, 4, 5]) == 3
assert median([5, 2, 3, 4, 1]) == 3
assert median([4, 2, 3, 1, 5]) == 3
assert median([1, 2, 3, 4, 5, 6]) == 3.5
assert median([3, 2, 4, 1, 5, 6]) == 3.5
assert median([2, 3, 1, 4, 5, 6]) == 3.5
assert median([5, 2, 3, 4, 1, 6]) == 3.5
assert median([4, 2, 3, 1, 5, 6]) == 3.5
assert median([1, 2, 3, 4, 5, 6, 7]) == 4
assert median([3, 2, 4, 1, 5, 6, 7]) == 4
assert median([2, 3, 1, 4, 5, 6, 7]) == 4
assert median([5, 2, 3, 4, 1, 6, 7]) == 4
assert median([4, 2, 3, 1, 5, 6, 7]) == 4
assert median([2, 2, 1, 2, 4, 6, 0]) == 2
assert median([1, 2, 3, 4, 5, 6, 7, 8]) == 4.5
assert median([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 5
assert median([1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 5, 9]) == 3
assert median([1, 1, 2, 3, 3, 3, 3, 5, 9, 11]) == 3
assert median([0, 1, 2, 3, 4, 5, 6]) == 3
assert median([1, 2, 3, 4, 5, 6, 6]) == 4
assert median([2, 2, 1]) == 2
assert median([2, 2, 1, 1]) == 1.5
assert median([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]) == 3.5
assert median([1, 5, 3, 4, 2]) == 3
assert median([1, 5, 3, 4, 2, 3]) == 3
assert median([4, 3, 2, 1]) == 2.5
assert median([5, 4, 3, 2, 1]) == 3
assert median([-1, 0, 1, 2, 3, 4, 5]) == 2.0
assert (median([1, 2, 3, 4, 5, 6]) == 3.5)
assert (median([1, 2, 3, 4, 5, 6, 7]) == 4)
assert median([1, 2, 3, 4, 5]) == 3, "Wrong Answer"
assert median([1, 2, 3, 4, 5, 6]) == 3.5, "Wrong Answer"
assert median([0,1,2,3,4,5,6]) == 3
assert median([1,2,2,2,2,2,2]) == 2
assert median([1,1,1,1,1,1,1]) == 1
assert median([2, 3, 1, 6, 4]) == 3
assert median([-5, -4, -3, -2, -1]) == -3
assert median([2, 3, 4, 5, 6, 7, 8]) == 5
assert median([10,0,1,2,3,4,5,6,7,8,9]) == 5
assert median([10,9,8,7,6,5,4,3,2,1,0]) == 5
assert median([10]) == 10
assert median([0]) == 0
assert median([1, 0]) == 0.5
assert median([1, 1, 0]) == 1
assert median([3, 3, 4, 4, 5, 5, 6, 6]) == 4.5
assert median([1, 1, 4, 4, 4, 4, 6, 8, 9, 10]) == 4
assert median([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]) == -1
assert median([1, 2, 4, 5]) == 3
assert median([1, 3, 4, 5]) == 3.5
assert median([2, 3, 4, 5]) == 3.5
assert median([-1, 0, 1]) == 0
assert median([1, 1, 1, 1]) == 1
assert median([1, 2, 3, 4, 5, 5, 7]) == 4
assert median([1, 2, 2, 3, 4, 5]) == 2.5
assert median([1, 2, 2, 3, 4, 5, 5]) == 3
assert median([1, 2, 2, 3, 4, 5, 5, 6]) == 3.5
assert median([1, 4, 5, 2, 3]) == 3
assert median([3, 1, 4, 5, 2]) == 3
assert median([4, 1, 3, 5, 2]) == 3
assert median([1,2,3,4,5,6]) == 3.5
assert median([1,2,3,4,5,6,7]) == 4
assert median([1,2,3,4,5,6,7,8]) == 4.5
assert median([1,2,3,4,5,6,7,8,9]) == 5
assert median([1, 2, 5, 4, 3]) == 3
assert median([2, 3, 5, 4, 1]) == 3
assert median([2, 3, 4, 5, 1]) == 3
assert median([3, 2, 1]) == 2
assert median([5, 2, 1, 4, 3]) == 3
assert median([6, 2, 1, 4, 3, 5]) == 3.5
assert median([1, 4, 2, 3, 0]) == 2
assert median([1, 4, 2, 3, 0, 5]) == 2.5
assert median([1, 5, 2, 4, 3]) == 3
assert median([3, 2, 1, 4, 5]) == 3
assert median([1, 1, 2, 3, 4]) == 2
assert median([3, 4, 1, 2, 1]) == 2
assert median([1, 4, 3, 2, 1]) == 2
assert median([1, 2, 3, 1, 4]) == 2
assert median([1, 1, 2, 2, 3]) == 2
assert median([1, 1, 2, 3, 2]) == 2
assert median([1, 2, 1, 2, 3]) == 2
assert median([1, 2, 3, 2, 1]) == 2
assert median([3, 2, 1, 2, 1]) == 2
assert median([3, 1, 2, 1, 2]) == 2
assert median([3, 1, 2, 2, 1]) == 2
assert median([1, 1, 2, 2, 2]) == 2
assert median([2, 1, 1, 2, 2]) == 2
assert median([2, 2, 1, 1, 2]) == 2
assert median([3, 4, 2, 1, 5]) == 3
assert median([1, 1, 3, 4, 5, 6]) == 3.5
assert median([-3, -1, 0, 1, 3]) == 0
assert median([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == 0
assert median([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6]) == 0.5
assert median([3]) == 3
assert median([3, 1]) == 2
assert median([3, 1, 2]) == 2
assert median([2, 3, 1]) == 2
assert median([1, 3, 2]) == 2
assert median([1, 2, 3, 4, 5, 6]) == 3.5, 'Error in median'
assert median([1, 2, 3, 4]) == 2.5, 'Error in median'
assert median([1, 1, 2, 2, 3, 3]) == 2, 'Error in median'
assert median([4,4,4,4,4]) == 4
assert median([5,5,5,5,5,5,5,5,5,5,5,5,5,6]) == 5
assert median([6,5,5,5,5,5,5,5,5,5,5,5,5,5]) == 5
assert median([5,5,5,5,5,5,5,5,5,5,5,5,5,4]) == 5
assert median([2, 1, 3]) == 2
assert median([2, 3, 3]) == 3
assert median([2, 3, 4]) == 3
assert median([0, -10, 100]) == 0
assert median([1, 3, 5, 7, 9]) == 5
assert median([1, 2, 2, 2, 2]) == 2
assert median([-1, 0, 1, 2, 3]) == 1
assert median([1, 1, 2, 3, 5]) == 2
assert median([0,1,2,4,5]) == 2
assert median([1,1,1,1,1,1]) == 1
assert median([5,3,4,2,1]) == 3
assert median([5,3,4,1,2]) == 3
assert median([4, 6, 5]) == 5
assert median([4, 6, 5, 6]) == 5.5
assert median([5, 3, 8, 1]) == 4
assert median([1, 3, 5, 4, 2]) == 3
assert median([6, 5, 4, 3, 2, 1]) == 3.5
assert median([7, 6, 5, 4, 3, 2, 1]) == 4
assert median([8, 7, 6, 5, 4, 3, 2, 1]) == 4.5
assert median([3, 2, 3, 3, 3, 3, 3, 3]) == 3
assert median([3, 3, 3, 3, 3, 3, 3, 3]) == 3
assert median([-2, -1, 0, 1, 2]) == 0
assert median([-1, -10, -100]) == -10
assert median([-10, -100, 100]) == -10
assert median([0, 100, -100]) == 0
assert median([1,2,4,4,5]) == 4
assert median([1,2,4,4,5,7]) == 4
assert median([6, 4, 3, 2, 1]) == 3
assert median([4, 7, 2, 6, 8, 9]) == 6.5
assert median([9, 8, 7, 6, 5, 4, 3, 2, 1]) == 5
assert median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5.5
assert median([1, 3, 2, 4, 5]) == 3
assert median([1, 4, 2, 3, 5]) == 3
assert median([1, 3, 4, 2, 5]) == 3
assert median([1, 3, 4, 5, 2]) == 3
assert median([2, 4, 1, 3, 5]) == 3
assert median([2, 4, 3, 1, 5]) == 3
assert median([2, 4, 3, 5, 1]) == 3
assert median([3, 4, 1, 2, 5]) == 3
assert median([3, 4, 2, 5, 1]) == 3
assert median([3, 4, 5, 1, 2]) == 3
assert median([3, 4, 5, 2, 1]) == 3
assert median([4, 3, 2, 1, 5]) == 3
assert median([4, 5, 2, 1, 3]) == 3
assert median([4, 5, 2, 3, 1]) == 3
assert median([4, 5, 6, 5]) == 5, 'test #2 failed'
assert median([2, 6, 3, 4, 5]) == 4
assert median([-1, -2, -3, -4, -5]) == -3
assert median([-5, -2, -3, -4, -1]) == -3
assert median([1, 1, 2, 3, 4, 5]) == 2.5
assert median([-1, -1, -2, -3, -4, -5]) == -2.5
assert median([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 3
assert median([-1, -1, -2, -2, -3, -3, -4, -4, -5, -5]) == -3
assert median([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]) == 3
assert median([-1, -1, -1, -2, -2, -2, -3, -3, -3, -4, -4, -4, -5, -5, -5]) == -3
assert median([1, 3, 5, 7, 10]) == 5
assert median([2, 4, 6, 8, 10]) == 6
assert median([3, 5, 6, 11, 20]) == 6
assert median([1,2,3,4,5]) == 3
assert median([-1,2,3,4,5,6,7]) == 4
assert median([-1,0,1,2,3,4,5,6,7,8]) == 3.5
assert median([-1,0,1,2,3,4,5,6,7,8,9]) == 4
assert median([1, 2, 3, 4, 5, 6]) == 3.5, "2"
assert median([6, 5, 4, 3, 2, 1]) == 3.5, "4"
assert median([1, 2, 3, 4, 5, 6, 7]) == 4, "5"
assert median([6, 2, 4, 1, 5, 3]) == 3.5
assert median([6, 2, 4, 1, 5, 3, 7]) == 4
assert median([6, 2, 4, 1, 5, 3, 7, 8]) == 4.5
assert median([1, 2, 2, 3]) == 2
assert median([3, 4, 5, 7, 8, 9, 10]) == 7
assert median([-1, -2, 0, 2, 4, 6, 8, 10]) == 3
assert median([-1, -2, 0, 2, 4, 6, 8, 10, 12]) == 4
assert median([2, 3, 1, 5, 4]) == 3
assert median([5, 2, 3, 1, 4]) == 3
assert median([0]) == 0, "Median of [0] should be 0"
assert median([5,5,5]) == 5, "Median of [5,5,5] should be 5"
assert median([1,2,3,4,5]) == 3, "Median of [1,2,3,4,5] should be 3"
assert median([1, 0, 3, 2]) == 1.5, 'incorrect'
assert median([2, 0, 3, 1]) == 1.5, 'incorrect'
assert median([2, 1, 3, 0]) == 1.5, 'incorrect'
assert median([0, 1, 2, 3]) == 1.5, 'incorrect'
assert median([3, 0, 1, 2]) == 1.5, 'incorrect'
assert median([3, 2, 1, 0]) == 1.5, 'incorrect'
assert median([3, 2, 0, 1]) == 1.5, 'incorrect'
assert median([1, 0, 2, 3]) == 1.5, 'incorrect'
assert median([2, 1, 0, 3]) == 1.5, 'incorrect'
assert median([3, 1, 0, 2]) == 1.5, 'incorrect'
assert median([2, 3, 0, 1]) == 1.5, 'incorrect'
assert median([1, 2, 0, 3]) == 1.5, 'incorrect'
assert median([1, 3, 0, 2]) == 1.5, 'incorrect'
assert median([6, 8, 11, 2, 1]) == 6
assert median([2, 3, 4, 5, 6]) == 4
assert median([3, 4, 6, 9]) == 5
assert median([3,1,2,5,3]) == 3
assert median([1,300,2,200,1]) == 2
assert median([3,6,20,99,10,15]) == 12.5
assert median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 6
assert median([1,2,3,4,5,6,7,8,9,10]) == 5.5
assert median([-1, 0, 1, 2, 3, 4, 5, 6]) == 2.5
assert median([1, 2, 3, 4, 5, -1, -2, -3, -4, -5, -6]) == -1
assert median([1, 2, 3, 4, 5, -1, -2, -3, -4, -5, -6, -7]) == -1.5
assert median([1, 2, 3, 4, 5, -1, -2, -3, -4, -5, -6, -7, -8]) == -2
assert median([2, 3, 4, 5, 7, 15]) == 4.5
assert median([2, 2, 2, 2, 2]) == 2

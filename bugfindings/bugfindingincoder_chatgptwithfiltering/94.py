

def skjkasdkd(lst):
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.

    Examples:
    For lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3] the output should be 10
    For lst = [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1] the output should be 25
    For lst = [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3] the output should be 13
    For lst = [0,724,32,71,99,32,6,0,5,91,83,0,5,6] the output should be 11
    For lst = [0,81,12,3,1,21] the output should be 3
    For lst = [0,8,1,2,1,7] the output should be 7
    """
    def isPrime(n):
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return True

        return False
    maxx = 0
    i = 0
    while i < len(lst):
        if(lst[i] > maxx and isPrime(lst[i])):
            maxx = lst[i]
        i+=1
    result = sum(int(digit) for digit in str(maxx))
    return result

assert skjkasdkd([1]) == 1
assert skjkasdkd([5]) == 5
assert skjkasdkd([16, 4, 6, 10, 2, 3]) == 3
assert skjkasdkd([7, 7, 7, 7, 7]) == 7
assert skjkasdkd([3, 3, 3]) == 3, "Second"
assert skjkasdkd([5, 6]) == 5, "Fourth"
assert skjkasdkd([6, 6, 3]) == 3, "Third"
assert skjkasdkd([5, 5]) == 5, "Fifth"
assert skjkasdkd([4, -2, 1, 3, -6, 8, -10, -5, -4, 0]) == 3
assert skjkasdkd([3, -2, 0, -1, -6, 8, -10, -5, -4, 0]) == 3
assert skjkasdkd([1, 3, 5]) == 5
assert skjkasdkd([5, 3, 5]) == 5
assert skjkasdkd([10, 11, 12, 13, 14, 15, 16, 18, 19, 22, 24]) == 10
assert skjkasdkd([0]) == 0
assert skjkasdkd([2, 3, 1, 5]) == 5
assert skjkasdkd([2, 3, 1, 7]) == 7
assert skjkasdkd([2, 2]) == 2
assert skjkasdkd([7, 1, 3]) == 7
assert skjkasdkd([4, 5, 1, 2, 3]) == 5
assert skjkasdkd([2]) == 2
assert skjkasdkd([2,3]) == 3
assert skjkasdkd([5, 3]) == 5
assert skjkasdkd([2, 3, 5]) == 5
assert skjkasdkd([9, 7, 3]) == 7
assert skjkasdkd([4, 2]) == 2

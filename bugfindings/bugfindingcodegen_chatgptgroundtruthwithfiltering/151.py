
def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
   
    If the input list is empty, return 0.
    '''
    return sum([i**2 for i in lst if i > 0 and "." not in str(i)])
assert 	double_the_difference([]) == 	0
assert 	double_the_difference([0]) == 	0
assert double_the_difference([]) == 0
assert 	double_the_difference([]) == 0, "wrong result for []"
assert 	double_the_difference([]) == 0, "Wrong answer"
assert 	double_the_difference([]) == 0
assert 	double_the_difference([-1, -2]) == 0
assert 	double_the_difference([0]) 	== 0
assert 	double_the_difference([7]) 	== 49
assert 	double_the_difference([9]) 	== 81
assert 	double_the_difference([11]) 	== 121
assert 	double_the_difference([13]) 	== 169
assert 	double_the_difference([15]) 	== 225

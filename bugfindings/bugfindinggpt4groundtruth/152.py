
def compare(game,guess):
    """I think we all remember that feeling when the result of some long-awaited
    event is finally known. The feelings and thoughts you have at that moment are
    definitely worth noting down and comparing.
    Your task is to determine if a person correctly guessed the results of a number of matches.
    You are given two arrays of scores and guesses of equal length, where each index shows a match. 
    Return an array of the same length denoting how far off each guess was. If they have guessed correctly,
    the value is 0, and if not, the value is the absolute difference between the guess and the score.
    
    
    example:

    compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) -> [0,0,0,0,3,3]
    compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) -> [4,4,1,0,0,6]
    """
    return [abs(x-y)+abs(y-x) for x,y in zip(game,guess)]
assert 	compare([1,1,1], [1,1,1]) == [0,0,0]
assert 	compare([1,2,3], [1,1,1]) == [0,1,2]
assert 	compare(game = [10,15,15,15,20], guess = [15,15,15,15,15])
assert 	compare([0, 2, 9], [0, 2, 9]) == [0, 0, 0]
assert 	compare([0, 4, 9], [0, 4, 9]) == [0, 0, 0]
assert 	compare([0, 5, 9], [0, 5, 9]) == [0, 0, 0]
assert 	compare([0, 6, 9], [0, 6, 9]) == [0, 0, 0]
assert 	compare([0, 7, 9], [0, 7, 9]) == [0, 0, 0]
assert 	compare([0, 8, 9], [0, 8, 9]) == [0, 0, 0]
assert 	compare([0, 9, 9], [0, 9, 9]) == [0, 0, 0]
assert 	compare([7, 7, 7, 7], [7, 7, 7, 7]) == [0, 0, 0, 0], "compare error"
assert 	compare([1,2,3], [1,2,3]) == [0,0,0]
assert 	(compare([1, 2, 3], [2, 1, 3]) == [1, 1, 0])
assert 	(compare([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == [0, 0, 0, 0, 0])
assert 	(compare([1, 1, 1], [1, 1, 1]) == [0, 0, 0])
assert 	(compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0])

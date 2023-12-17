
def check_dict_case(dict):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    Examples:
    check_dict_case({"a":"apple", "b":"banana"}) should return True.
    check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) should return False.
    check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) should return False.
    check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) should return False.
    check_dict_case({"STATE":"NC", "ZIP":"12345" }) should return True.
    """
    if len(dict.keys()) == 0:
        return False
    else:
        state = "start"
        for key in dict.keys():

            if isinstance(key, str) == False:
                state = "mixed"
                break
            if state == "start":
                if key.isupper():
                    state = "upper"
                elif key.islower():
                    state = "lower"
                else:
                    break
            elif (state == "upper" and not key.isupper()) and (state == "lower" and not key.islower()):
                    state = "mixed"
                    break
            else:
                break
        return state == "upper" or state == "lower" 
assert check_dict_case({'A': 1, 'B': 2}) == True
assert check_dict_case({'a': 1, 'b': 2}) == True
assert check_dict_case({'A': 1, 'B': 2, 'C': 3}) == True
assert check_dict_case({'a': 1, 'b': 2, 'c': 3}) == True
assert check_dict_case({'A': 'a', 'B': 'b'}) == True
assert check_dict_case({'A': 'a', 'B': 'b', 'C': 'c'}) == True
assert check_dict_case({'a': 'A', 'b': 'B', 'c': 'C'}) == True
assert check_dict_case({'a':2}) == True
assert check_dict_case({'a':2, 'b':3}) == True
assert check_dict_case({'A':1}) == True
assert check_dict_case({'a':1}) == True
assert check_dict_case({'a':1, 'b':2}) == True
assert check_dict_case({'a':1, 'b':2, 'c':3}) == True
assert check_dict_case({'A':1, 'B':2, 'C':3}) == True
assert check_dict_case({'A':1,'B':2,'C':3}) == True
assert True == check_dict_case({'a':1})
assert True == check_dict_case({'A':1})
assert True == check_dict_case({'a':1, 'b':2})
assert True == check_dict_case({'A':1, 'B':2})
assert True == check_dict_case({'A': 'a', 'B': 'b', 'C': 'c'})
assert True == check_dict_case({'a': 'a', 'b': 'b'})
assert True == check_dict_case({'a': 'a', 'b': 'b', 'c': 'c'})
assert True == check_dict_case({'a': 0, 'b': 1})
assert True == check_dict_case({'A': 0, 'B': 1})
assert True == check_dict_case({'TEST': 'TEST'})
assert True == check_dict_case({'test': 'test'})
assert check_dict_case({"LOWER": 1, "LOWER": 2}) == True, "Test 6 Failed"
assert check_dict_case({"lower": 1, "lower": 2}) == True, "Test 7 Failed"
assert check_dict_case({"lower": 1, "lower": 2, "lower_case": 3}) == True, "Test 8 Failed"
assert check_dict_case({"lower": 1, "lower": 2, "lower_case": 3, "lower_case": 4}) == True, "Test 9 Failed"
assert check_dict_case({'A':1, 'B':2}) == True
assert check_dict_case({'A':1, 'B':2}) == True, 'Upper case'
assert check_dict_case({'a':1, 'b':2}) == True, 'Lower case'
assert check_dict_case({'A':1, 'B':2, 'C':3}) == True, 'Upper case'
assert check_dict_case({'a':1, 'b':2, 'c':3}) == True, 'Lower case'
assert check_dict_case({'A':1,'B':2})
assert check_dict_case({'name': 'Jennifer'}) == True
assert check_dict_case({'name': 'Jennifer', 'age': 20}) == True
assert check_dict_case({'NAME': 'Jennifer', 'AGE': 20}) == True
assert check_dict_case({'hello':'world'}) == True
assert check_dict_case({"A": 1, "B": 2}) == True, "failed upper case"
assert check_dict_case({"a": 1, "b": 2}) == True, "failed lower case"
assert check_dict_case({'a':1, 'a':2}) == True
assert check_dict_case({'a':1, 'b':2}) == True, 'Two lower case keys should pass'
assert check_dict_case({'A':1, 'B':2}) == True, 'Two upper case keys should pass'
assert check_dict_case({'A':1, 'B':2, 'C':3}) == True, 'Three upper case keys should pass'
assert check_dict_case({'FOO':1, 'BAR':2}) == True
assert check_dict_case({'A':1, 'B':1}) == True
assert True == check_dict_case({'X':1, 'Y':2})
assert check_dict_case({'abc': 1, 'def': 2})
assert True == check_dict_case({'a': 1, 'b': 2})
assert True == check_dict_case({'A': 1, 'B': 2})
assert check_dict_case({'a':1, 'b':2}) == True, 'Invalid check_dict_case'
assert check_dict_case({'A':1, 'B':2}) == True, 'Invalid check_dict_case'
assert check_dict_case({'A':1, 'B':2, 'C':2}) == True, 'Invalid check_dict_case'
assert check_dict_case({'foo': 123}) == True
assert True == check_dict_case({'ONE': 1, 'TWO': 2, 'THREE': 3})
assert True == check_dict_case({'one': 1, 'two': 2, 'three': 3})
assert check_dict_case({'A':1, 'B':2, 'C':3})
assert check_dict_case({'lower':1}) == True
assert check_dict_case({'LOWER':1, 'LOWER':2}) == True
assert check_dict_case({'ab':'Ab', 'cd':'Cd'}) == True, 'Test 2'
assert check_dict_case({'A':'a', 'B':'b'}) == True
assert check_dict_case({'a':'a'}) == True
assert check_dict_case({'a':'a', 'b':'b'}) == True
assert check_dict_case({'hello': 1, 'world': 2}) == True
assert check_dict_case({'a': 2, 'b': 5}) == True
assert check_dict_case({'A': 2, 'B': 5}) == True
assert check_dict_case({'a':'b'}) == True
assert check_dict_case({'A':'b'}) == True
assert check_dict_case({'A':'b', 'B':'b'}) == True
assert check_dict_case({'a':'b', 'b':'b'}) == True
assert check_dict_case({'A':2,'B':1}) == True
assert check_dict_case({'hi': 1, 'this': 2}) == True
assert check_dict_case({'HI': 1, 'THIS': 2}) == True
assert True == check_dict_case({'A': 1, 'B': 2, 'C': 3})
assert check_dict_case({'a': 'a', 'b': 'b'}) == True
assert check_dict_case({'a': 1}) == True
assert check_dict_case({'A':1, 'B':2, 'C':3, 'D':4}) == True
assert check_dict_case({'A': 0, 'B': 1}) == True
assert check_dict_case({'a': 0, 'b': 1}) == True
assert check_dict_case({'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6}) == True
assert check_dict_case({'A':1, 'B':2, 'C': 3}) == True
assert check_dict_case({'A':1,'B':2,'C':3})
assert check_dict_case({'A':1}) == True, 'incorrect'
assert check_dict_case({'A':1, 'B':2}) == True, 'incorrect'
assert check_dict_case({'a':1, 'b':2}) == True, 'incorrect'
assert check_dict_case({'a':1, 'b':2, 'c':3}) == True, 'incorrect'
assert check_dict_case({'A':1, 'B':2, 'C':3}) == True, 'incorrect'
assert check_dict_case({"A": 1, "B": 2}) == True, "Test Failed"
assert check_dict_case({"a": 1, "b": 2, "c": 3}) == True, "Test Failed"
assert check_dict_case({'x': 1, 'y': 2}) == True
assert check_dict_case({'X': 1, 'Y': 2}) == True
assert check_dict_case({'FOO':'BAR'}) == True
assert check_dict_case({'A': 1, 'B': 2, 'C': 3, 'D':4, 'E':5}) == True
assert check_dict_case({'A': 1, 'B': 2, 'C': 3, 'D':4, 'E':5, 'F':6, 'G':7}) == True
assert check_dict_case({'ONE': 1, 'TWO': 2, 'THREE': 3}) == True

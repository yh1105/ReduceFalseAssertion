from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    current_string = []
    current_depth = 0

    for c in paren_string:
        if c == '(':
            current_depth += 1
            current_string.append(c)
        elif c == ')':
            current_depth -= 1
            current_string.append(c)

            if current_depth < 0:
                result.append(''.join(current_string))
                current_string.clear()

    return result
assert separate_paren_groups("()") == ["()"]
assert separate_paren_groups("()()") == ["()", "()"]
assert separate_paren_groups("(())") == ["(())"]
assert separate_paren_groups("()()()") == ["()", "()", "()"]
assert separate_paren_groups("()()()()") == ["()", "()", "()", "()"]
assert separate_paren_groups("(())(())") == ["(())", "(())"]
assert separate_paren_groups("((()))") == ["((()))"]
assert separate_paren_groups("()()()()()()") == ["()", "()", "()", "()", "()", "()"]
assert separate_paren_groups("(())(())(())") == ["(())", "(())", "(())"]
assert separate_paren_groups("()()()()()") == ["()", "()", "()", "()", "()"]
assert separate_paren_groups("()()()()()()()") == ["()", "()", "()", "()", "()", "()", "()"]
assert separate_paren_groups("()()()()()()()()") == ["()", "()", "()", "()", "()", "()", "()", "()"]
assert separate_paren_groups("()()()()()()()()()") == ["()", "()", "()", "()", "()", "()", "()", "()", "()"]
assert separate_paren_groups("()()()()()()()()()()") == ["()", "()", "()", "()", "()", "()", "()", "()", "()", "()"]
assert separate_paren_groups("(())(())(())(())(())(())(())(())(())(())") == ["(())", "(())", "(())", "(())", "(())", "(())", "(())", "(())", "(())", "(())"]
assert separate_paren_groups("((((()))))((((()))))((((()))))((((()))))((((()))))((((()))))((((()))))((((()))))((((()))))") == ["((((()))))", "((((()))))", "((((()))))", "((((()))))", "((((()))))", "((((()))))", "((((()))))", "((((()))))", "((((()))))"]
assert separate_paren_groups("") == []
assert separate_paren_groups("(())()") == ["(())", "()"]
assert separate_paren_groups("((())())") == ["((())())"]
assert separate_paren_groups("()((())())") == ["()", "((())())"]
assert separate_paren_groups("((())())()") == ["((())())", "()"]
assert separate_paren_groups("((())())()()") == ["((())())", "()", "()"]
assert separate_paren_groups("()((())())()()") == ["()", "((())())", "()", "()"]
assert separate_paren_groups("((()))()") == ["((()))", "()"]
assert separate_paren_groups("((()))(())") == ["((()))", "(())"]
assert separate_paren_groups("((()))(())()") == ["((()))", "(())", "()"]
assert separate_paren_groups("((()))(())()()") == ["((()))", "(())", "()", "()"]
assert separate_paren_groups("((()))(())()()()") == ["((()))", "(())", "()", "()", "()"]
assert separate_paren_groups("()(()())") == ["()", "(()())"]
assert separate_paren_groups("()(()())()") == ["()", "(()())", "()"]
assert separate_paren_groups("()(()())()()") == ["()", "(()())", "()", "()"]
assert separate_paren_groups("((()))()()") == ["((()))", "()", "()"]
assert separate_paren_groups("((()))()()()") == ["((()))", "()", "()", "()"]
assert separate_paren_groups("((()))()()()()") == ["((()))", "()", "()", "()", "()"]
assert separate_paren_groups("((()))()()()()()") == ["((()))", "()", "()", "()", "()", "()"]
assert separate_paren_groups("(()())") == ["(()())"]
assert separate_paren_groups("((()())())") == ["((()())())"]
assert separate_paren_groups("(())()()()") == ["(())", "()", "()", "()"]
assert separate_paren_groups("((()()))()") == ["((()()))", "()"]
assert separate_paren_groups("((()())())()") == ["((()())())", "()"]
assert separate_paren_groups("(((())))()") == ["(((())))", "()"]
assert separate_paren_groups("(((()())))") == ["(((()())))"]
assert separate_paren_groups("(((()()))())") == ["(((()()))())"]
assert separate_paren_groups("(((()()))())(())") == ["(((()()))())", "(())"]
assert separate_paren_groups("(((()()))())(())()") == ["(((()()))())", "(())", "()"]
assert separate_paren_groups("(((()()))())(())()()") == ["(((()()))())", "(())", "()", "()"]
assert separate_paren_groups("(((()()))())(())()()()") == ["(((()()))())", "(())", "()", "()", "()"]
assert separate_paren_groups("(((()()))())(())()()()()") == ["(((()()))())", "(())", "()", "()", "()", "()"]
assert separate_paren_groups("()((()))()()()") == ["()", "((()))", "()", "()", "()"]
assert separate_paren_groups("()((()))()()()()") == ["()", "((()))", "()", "()", "()", "()"]
assert separate_paren_groups("()((()))()()()()()") == ["()", "((()))", "()", "()", "()", "()", "()"]
assert separate_paren_groups("()((()))") == ["()", "((()))"]
assert separate_paren_groups("()((()))()") == ["()", "((()))", "()"]
assert separate_paren_groups("((())())((()))") == ["((())())", "((()))"]
assert separate_paren_groups("((())())((()))()") == ["((())())", "((()))", "()"]
assert separate_paren_groups("((()))((()))") == ["((()))", "((()))"]
assert separate_paren_groups("((()))((()))((()))") == ["((()))", "((()))", "((()))"]
assert separate_paren_groups("()(()())()()()") == ["()", "(()())", "()", "()", "()"]
assert separate_paren_groups("()()()()()()()()()()()()") == ["()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()"]
assert separate_paren_groups("()()()()()()()()()()()()()") == ["()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()"]
assert separate_paren_groups("()()()()()()()()()()()()()()") == ["()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()"]
assert separate_paren_groups("()()()()((()))") == ["()", "()", "()", "()", "((()))"]
assert separate_paren_groups("()()()()((()))()()()()") == ["()", "()", "()", "()", "((()))", "()", "()", "()", "()"]
assert separate_paren_groups("(())(())(())(())(())(())(())(())") == ["(())", "(())", "(())", "(())", "(())", "(())", "(())", "(())"]
assert separate_paren_groups('(())') == ['(())']
assert separate_paren_groups('()()') == ['()', '()']
assert separate_paren_groups('()()()') == ['()', '()', '()']
assert separate_paren_groups('((()))') == ['((()))']
assert separate_paren_groups('()()()()') == ['()', '()', '()', '()']
assert separate_paren_groups('()()()()()') == ['()', '()', '()', '()', '()']
assert separate_paren_groups('()()()()()()') == ['()', '()', '()', '()', '()', '()']
assert separate_paren_groups('((())())') == ['((())())']
assert separate_paren_groups('((())())()()') == ['((())())', '()', '()']
assert separate_paren_groups('((())())()()()') == ['((())())', '()', '()', '()']
assert separate_paren_groups('((())())()()()()') == ['((())())', '()', '()', '()', '()']
assert separate_paren_groups('((())())()()()()()') == ['((())())', '()', '()', '()', '()', '()']
assert separate_paren_groups('((())())()()()()()()') == ['((())())', '()', '()', '()', '()', '()', '()']
assert separate_paren_groups('((())())()()()()()()()') == ['((())())', '()', '()', '()', '()', '()', '()', '()']
assert separate_paren_groups('((())())()()()()()()()()') == ['((())())', '()', '()', '()', '()', '()', '()', '()', '()']
assert separate_paren_groups('((())())()()()()()()()()()') == ['((())())', '()', '()', '()', '()', '()', '()', '()', '()', '()']
assert separate_paren_groups('((())())()()()()()()()()()()') == ['((())())', '()', '()', '()', '()', '()', '()', '()', '()', '()', '()']
assert separate_paren_groups('((())())()()()()()()()()()()()') == ['((())())', '()', '()', '()', '()', '()', '()', '()', '()', '()', '()', '()']
assert separate_paren_groups('((())())()()()()()()()()()()()()') == ['((())())', '()', '()', '()', '()', '()', '()', '()', '()', '()', '()', '()', '()']
assert separate_paren_groups('((())())()()()()()()()()()()()()()') == ['((())())', '()', '()', '()', '()', '()', '()', '()', '()', '()', '()', '()', '()', '()']
assert separate_paren_groups('((())())()()()()()()()()()()()()()()') == ['((())())', '()', '()', '()', '()', '()', '()', '()', '()', '()', '()', '()', '()', '()', '()']
assert separate_paren_groups('((())())()()()()()()()()()()()()()()()') == ['((())())', '()', '()', '()', '()', '()', '()', '()', '()', '()', '()', '()', '()', '()', '()', '()']
assert separate_paren_groups('((())())()()()()()()()()()()()()()()()()') == ['((())())', '()', '()', '()', '()', '()', '()', '()', '()', '()', '()', '()', '()', '()', '()', '()', '()']
assert separate_paren_groups('((())())()()()()()()()()()()()()()()()()()') == ['((())())', '()', '()', '()', '()', '()', '()', '()', '()', '()', '()', '()', '()', '()', '()', '()', '()', '()']
assert separate_paren_groups('((())())()()()()()()()()()()()()()()()()()()') == ['((())())', '()', '()', '()', '()', '()', '()', '()', '()', '()', '()', '()', '()', '()', '()', '()', '()', '()', '()']
assert separate_paren_groups("((())) ()") == ["((()))", "()"]
assert separate_paren_groups("((()))() ()") == ["((()))", "()", "()"]
assert separate_paren_groups("((()))() (())") == ["((()))", "()", "(())"]
assert separate_paren_groups("((()))() (()) ()") == ["((()))", "()", "(())", "()"]
assert separate_paren_groups("((()))() (()) () ()") == ["((()))", "()", "(())", "()", "()"]
assert separate_paren_groups("()()(()())()") == ["()", "()", "(()())", "()"]
assert separate_paren_groups("()()(()())()()") == ["()", "()", "(()())", "()", "()"]
assert separate_paren_groups("()()(()())()()()()") == ["()", "()", "(()())", "()", "()", "()", "()"]
assert separate_paren_groups("((())())(())") == ["((())())", "(())"]
assert separate_paren_groups("((()())(()))") == ["((()())(()))"]
assert separate_paren_groups("(())((()))") == ["(())", "((()))"]
assert separate_paren_groups("((()())) ()") == ["((()()))", "()"]
assert separate_paren_groups("((())((())()))()()()") == ["((())((())()))", "()", "()", "()"]
assert separate_paren_groups("((())) () ()") == ["((()))", "()", "()"]
assert separate_paren_groups("((())) () (())") == ["((()))", "()", "(())"]
assert separate_paren_groups("((())) () (()) ()") == ["((()))", "()", "(())", "()"]
assert separate_paren_groups("((())) () (()) () ()") == ["((()))", "()", "(())", "()", "()"]
assert separate_paren_groups("((()()))") == ["((()()))"]
assert separate_paren_groups("((()())(()))()()") == ["((()())(()))", "()", "()"]
assert separate_paren_groups("((()())(()))()()()") == ["((()())(()))", "()", "()", "()"]
assert separate_paren_groups("((()())(()))()()()()") == ["((()())(()))", "()", "()", "()", "()"]
assert separate_paren_groups("(())(())(())(())") == ["(())", "(())", "(())", "(())"]
assert separate_paren_groups("(())()()") == ["(())", "()", "()"]
assert separate_paren_groups("() ()") == ["()", "()"]
assert separate_paren_groups("() () ()") == ["()", "()", "()"]
assert separate_paren_groups("()()()()()()()()()()()") == ["()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()"]
assert separate_paren_groups("()()()()()()()()()()()()()()()") == ["()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()"]
assert separate_paren_groups("()()()()()()()()()()()()()()()()") == ["()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()"]
assert separate_paren_groups("()()()()()()()()()()()()()()()()()") == ["()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()"]
assert separate_paren_groups("()()()()()()()()()()()()()()()()()()") == ["()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()"]
assert separate_paren_groups("()()()()()()()()()()()()()()()()()()()") == ["()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()"]
assert separate_paren_groups("()()()()()()()()()()()()()()()()()()()()") == ["()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()"]
assert separate_paren_groups("((())())((())())") == ["((())())", "((())())"]
assert separate_paren_groups("((())())((())())((())())") == ["((())())", "((())())", "((())())"]
assert separate_paren_groups("(((())())((())()))") == ["(((())())((())()))"]
assert separate_paren_groups("((())())((())())((())())((())())") == ["((())())", "((())())", "((())())", "((())())"]
assert separate_paren_groups("((())())((())())((())())((())())((())())") == ["((())())", "((())())", "((())())", "((())())", "((())())"]
assert separate_paren_groups('((()))()') == ['((()))', '()']
assert separate_paren_groups('()((()))()') == ['()', '((()))', '()']
assert separate_paren_groups('()()((()))()()') == ['()', '()', '((()))', '()', '()']
assert separate_paren_groups('(())(())') == ['(())', '(())']
assert separate_paren_groups('(())(())(())') == ['(())', '(())', '(())']
assert separate_paren_groups('()()()()()()()()()()') == ['()', '()', '()', '()', '()', '()', '()', '()', '()', '()']
assert separate_paren_groups('(())(())(())(())(())(())(())(())(())(())') == ['(())', '(())', '(())', '(())', '(())', '(())', '(())', '(())', '(())', '(())']
assert separate_paren_groups("() (()) ()") == ["()", "(())", "()"]
assert separate_paren_groups("((())())()()()") == ["((())())", "()", "()", "()"]
assert separate_paren_groups("((())())()()()()") == ["((())())", "()", "()", "()", "()"]
assert separate_paren_groups("((())())()()()()()") == ["((())())", "()", "()", "()", "()", "()"]
assert separate_paren_groups("((())())()()()()()()") == ["((())())", "()", "()", "()", "()", "()", "()"]
assert separate_paren_groups("((())())()()()()()()()") == ["((())())", "()", "()", "()", "()", "()", "()", "()"]
assert separate_paren_groups("((())())()()()()()()()()") == ["((())())", "()", "()", "()", "()", "()", "()", "()", "()"]
assert separate_paren_groups("(())()") == ["(())","()"]
assert separate_paren_groups("()()()()()()") == ["()","()","()","()","()","()"]
assert separate_paren_groups("()()()()()") == ["()","()","()","()","()"]
assert separate_paren_groups("()()()()") == ["()","()","()","()"]
assert separate_paren_groups("()()()") == ["()","()","()"]
assert separate_paren_groups("()()") == ["()","()"]
assert separate_paren_groups("((()()))(())") == ["((()()))", "(())"]
assert separate_paren_groups("((()()))(())()") == ["((()()))", "(())", "()"]
assert separate_paren_groups("((()())())((()))") == ["((()())())", "((()))"]
assert separate_paren_groups("((()())())((()))()") == ["((()())())", "((()))", "()"]
assert separate_paren_groups("(((())))") == ["(((())))"]
assert separate_paren_groups("((()(())))") == ["((()(())))"]
assert separate_paren_groups("() (()) ()") == ["()","(())","()"]
assert separate_paren_groups("(()) (()) (())") == ["(())","(())","(())"]
assert separate_paren_groups("()()((()))") == ["()", "()", "((()))"]
assert separate_paren_groups("((()))()()((()))") == ["((()))", "()", "()", "((()))"]
assert separate_paren_groups('(()())') == ['(()())']
assert separate_paren_groups('()((()))') == ['()', '((()))']
assert separate_paren_groups("((()))()(()())") == ["((()))", "()", "(()())"]
assert separate_paren_groups("()()()") == ["()", "()", "()"], "Test case 2 failed"
assert separate_paren_groups("((())) () ()") == ["((()))", "()", "()"], "Test case 3 failed"
assert separate_paren_groups("() () ()") == ["()", "()", "()"], "Test case 4 failed"
assert separate_paren_groups("((())) () () ()") == ["((()))", "()", "()", "()"], "Test case 5 failed"
assert separate_paren_groups("() () () ()") == ["()", "()", "()", "()"], "Test case 6 failed"
assert separate_paren_groups("((())) () () () ()") == ["((()))", "()", "()", "()", "()"], "Test case 7 failed"
assert separate_paren_groups("() () () () ()") == ["()", "()", "()", "()", "()"], "Test case 8 failed"
assert separate_paren_groups("") == [], "Test case 9 failed"
assert separate_paren_groups("()") == ["()"], "Test case 10 failed"
assert separate_paren_groups("()()()()()") == ["()", "()", "()", "()", "()"], "Test case 11 failed"
assert separate_paren_groups("((()))((()))") == ["((()))", "((()))"], "Test case 12 failed"
assert separate_paren_groups("((()))()()()()()()()()()()") == ["((()))", "()", "()", "()", "()", "()", "()", "()", "()", "()", "()"]
assert separate_paren_groups("((())(()))") == ["((())(()))"]
assert separate_paren_groups("((())(())())") == ["((())(())())"]
assert separate_paren_groups("() (())") == ["()", "(())"]
assert separate_paren_groups("((())()())") == ["((())()())"]
assert separate_paren_groups("((()()()()))()") == ["((()()()()))", "()"]
assert separate_paren_groups("()()()((()))") == ["()", "()", "()", "((()))"]
assert separate_paren_groups("()()()((()))()") == ["()", "()", "()", "((()))", "()"]
assert separate_paren_groups("((()))()()((()))(())") == ["((()))", "()", "()", "((()))", "(())"]
assert separate_paren_groups("()()(()())") == ["()", "()", "(()())"]
assert separate_paren_groups("()()((()))()()") == ["()", "()", "((()))", "()", "()"]
assert separate_paren_groups("()()((()))()()()") == ["()", "()", "((()))", "()", "()", "()"]
assert separate_paren_groups("()()((()))()()()()") == ["()", "()", "((()))", "()", "()", "()", "()"]
assert separate_paren_groups("()((())())()") == ["()", "((())())", "()"]
assert separate_paren_groups('((()())(()())())') == ['((()())(()())())']
assert separate_paren_groups('((()())((())()))') == ['((()())((())()))']
assert separate_paren_groups("(()())()") == ["(()())", "()"]
assert separate_paren_groups("()()()(()())") == ["()", "()", "()", "(()())"]
assert separate_paren_groups("((()())(()))()") == ["((()())(()))", "()"]
assert separate_paren_groups("(())(())(())(())(())") == ["(())", "(())", "(())", "(())", "(())"]
assert separate_paren_groups("(())(())(())(())(())(())") == ["(())", "(())", "(())", "(())", "(())", "(())"]
assert separate_paren_groups("()((()))()()") == ["()", "((()))", "()", "()"]
assert separate_paren_groups('()(()())') == ['()', '(()())']
assert separate_paren_groups("(()) ()") == ["(())", "()"]
assert separate_paren_groups("(()) (())") == ["(())", "(())"]
assert separate_paren_groups("() ()()") == ["()", "()", "()"]
assert separate_paren_groups("(()) ()()") == ["(())", "()", "()"]
assert separate_paren_groups("() (())()") == ["()", "(())", "()"]
assert separate_paren_groups("(()) (())()") == ["(())", "(())", "()"]
assert separate_paren_groups("()() ()()") == ["()", "()", "()", "()"]
assert separate_paren_groups("() ()() ()()") == ["()", "()", "()", "()", "()"]
assert separate_paren_groups("(()) ()() ()()") == ["(())", "()", "()", "()", "()"]
assert separate_paren_groups("() (())() ()()") == ["()", "(())", "()", "()", "()"]
assert separate_paren_groups("(()) (())() ()()") == ["(())", "(())", "()", "()", "()"]
assert separate_paren_groups("(())(())(())(())(())(())(())") == ["(())", "(())", "(())", "(())", "(())", "(())", "(())"]

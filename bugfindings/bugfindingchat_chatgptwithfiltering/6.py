from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def parse_paren_group(s):
        depth = 0
        max_depth = 0
        for c in s:
            if c == '(':
                depth += 1
                max_depth = max(depth, max_depth)
            else:
                max_depth -= 1

        return max_depth

    return [parse_paren_group(x) for x in paren_string.split(' ') if x]
assert parse_nested_parens("()") == [1]
assert parse_nested_parens("() ()") == [1, 1]
assert parse_nested_parens("() () ()") == [1, 1, 1]
assert parse_nested_parens("() () () ()") == [1, 1, 1, 1]
assert parse_nested_parens("() () () () ()") == [1, 1, 1, 1, 1]
assert parse_nested_parens("() () () () () ()") == [1, 1, 1, 1, 1, 1]
assert parse_nested_parens("((()))") == [3]
assert parse_nested_parens("((())) ()") == [3, 1]
assert parse_nested_parens("((())) () ()") == [3, 1, 1]
assert parse_nested_parens("() (((())))") == [1, 4]
assert parse_nested_parens("() () (((())))") == [1, 1, 4]
assert parse_nested_parens("() () () (((())))") == [1, 1, 1, 4]
assert parse_nested_parens("() () () () (((())))") == [1, 1, 1, 1, 4]
assert parse_nested_parens("() () () () () (((())))") == [1, 1, 1, 1, 1, 4]
assert parse_nested_parens("() () () () () () (((())))") == [1, 1, 1, 1, 1, 1, 4]
assert parse_nested_parens("()()() ()()()") == [1, 1]
assert parse_nested_parens("(())") == [2]
assert parse_nested_parens("() ((()))") == [1, 3]
assert parse_nested_parens("() ((())) ()") == [1, 3, 1]
assert parse_nested_parens("() ((())) () ()") == [1, 3, 1, 1]
assert parse_nested_parens("() () ((()))") == [1, 1, 3]
assert parse_nested_parens("() () ((())) ()") == [1, 1, 3, 1]
assert parse_nested_parens("() () ((())) () ()") == [1, 1, 3, 1, 1]
assert parse_nested_parens("() () () ((()))") == [1, 1, 1, 3]
assert parse_nested_parens("() () () ((())) ()") == [1, 1, 1, 3, 1]
assert parse_nested_parens("() () () ((())) () ()") == [1, 1, 1, 3, 1, 1]
assert parse_nested_parens("() (())") == [1, 2]
assert parse_nested_parens("() (()) ()") == [1, 2, 1]
assert parse_nested_parens("() (()) ((()))") == [1, 2, 3]
assert parse_nested_parens("() (()) ((())) ()") == [1, 2, 3, 1]
assert parse_nested_parens("(()())") == [2]
assert parse_nested_parens('() ()') == [1, 1]
assert parse_nested_parens('(()())') == [2]
assert parse_nested_parens('(()()) ()') == [2, 1]
assert parse_nested_parens('(()()) ((()))') == [2, 3]
assert parse_nested_parens('() () ()') == [1, 1, 1]
assert parse_nested_parens("") == []
assert parse_nested_parens("()()") == [1]
assert parse_nested_parens("() (()) (())") == [1, 2, 2]
assert parse_nested_parens("() (()) (()) (())") == [1, 2, 2, 2]
assert parse_nested_parens("() (()) (()) (()) (())") == [1, 2, 2, 2, 2]
assert parse_nested_parens("() (()) (()) (()) (()) (())") == [1, 2, 2, 2, 2, 2]
assert parse_nested_parens("() (()) (()) (()) (()) (()) (())") == [1, 2, 2, 2, 2, 2, 2]
assert parse_nested_parens("() (()) (()) (()) (()) (()) (()) (())") == [1, 2, 2, 2, 2, 2, 2, 2]
assert parse_nested_parens("() (()) (()) (()) (()) (()) (()) (()) (())") == [1, 2, 2, 2, 2, 2, 2, 2, 2]
assert parse_nested_parens("() (()) (()) (()) (()) (()) (()) (()) (()) (())") == [1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
assert parse_nested_parens("(((())))") == [4]
assert parse_nested_parens('(()) ()') == [2, 1]
assert parse_nested_parens('((())) ()') == [3, 1]
assert parse_nested_parens('((())) () ()') == [3, 1, 1]
assert parse_nested_parens('((())) (())') == [3, 2]
assert parse_nested_parens('((())) (()) ()') == [3, 2, 1]
assert parse_nested_parens("((())) ()() ((()))") == [3, 1, 3], "Test case 2 failed"
assert parse_nested_parens("()()() ()() ()()()") == [1, 1, 1], "Test case 3 failed"
assert parse_nested_parens("(()) ((())) ()()") == [2, 3, 1], "Test case 4 failed"
assert parse_nested_parens("() () ()") == [1, 1, 1], "Test case 5 failed"
assert parse_nested_parens("((())) ((()))") == [3, 3]
assert parse_nested_parens("((())) ((())) ()") == [3, 3, 1]
assert parse_nested_parens("() ((())) ((()))") == [1, 3, 3]
assert parse_nested_parens("() ((())) ((())) ()") == [1, 3, 3, 1]
assert parse_nested_parens('() (()) ()') == [1, 2, 1]
assert parse_nested_parens('() ((())) ()') == [1, 3, 1]
assert parse_nested_parens('() (((()))) ()') == [1, 4, 1]
assert parse_nested_parens('() (((()))) () ((()))') == [1, 4, 1, 3]
assert parse_nested_parens('() (((()))) () ((())) ()') == [1, 4, 1, 3, 1]
assert parse_nested_parens("() () () () () () ()") == [1, 1, 1, 1, 1, 1, 1]
assert parse_nested_parens("() () () () () () () ()") == [1, 1, 1, 1, 1, 1, 1, 1]
assert parse_nested_parens("() () () () () () () () ()") == [1, 1, 1, 1, 1, 1, 1, 1, 1]
assert parse_nested_parens("() () () () () () () () () ()") == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
assert parse_nested_parens("() () () () () () () () () () ()") == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
assert parse_nested_parens("() ((())) () (())") == [1, 3, 1, 2]
assert parse_nested_parens("() ((())) () (()) ()") == [1, 3, 1, 2, 1]
assert parse_nested_parens("() () () () () () () () () () () ()") == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
assert parse_nested_parens("() () () () () () () () () () () () ()") == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
assert parse_nested_parens("() () () () () () () () () () () () () ()") == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
assert parse_nested_parens("() () () () () () () () () () () () () () ()") == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
assert parse_nested_parens("() () () () () () () () () () () () () () () ()") == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
assert parse_nested_parens("() () () () () () () () () () () () () () () () ()") == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
assert parse_nested_parens("() () () () () () () () () () () () () () () () () ()") == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
assert parse_nested_parens("() () () () () () () () () () () () () () () () () () ()") == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
assert parse_nested_parens("(()()) ()") == [2, 1]
assert parse_nested_parens("(()()) (())") == [2, 2]
assert parse_nested_parens("(()()) () ()") == [2, 1, 1]
assert parse_nested_parens("((())) (())") == [3, 2]
assert parse_nested_parens("((())) ((())) (())") == [3, 3, 2]
assert parse_nested_parens("((())) ((())) () ()") == [3, 3, 1, 1]
assert parse_nested_parens("(()()) (()())") == [2, 2]
assert parse_nested_parens("(()()) (()()) (()())") == [2, 2, 2]
assert parse_nested_parens("((())) ((())) ((()))") == [3, 3, 3]
assert parse_nested_parens("((()(())))") == [4]
assert parse_nested_parens("((())) (()) ()") == [3, 2, 1]
assert parse_nested_parens("((()()()(())))") == [4]
assert parse_nested_parens("((()()()(()))) ()") == [4, 1]
assert parse_nested_parens("((())())") == [3]
assert parse_nested_parens("(()()) ((()))") == [2, 3]
assert parse_nested_parens("((())) (()())") == [3, 2]
assert parse_nested_parens("(((()))) (()())") == [4, 2]
assert parse_nested_parens("((())) (()) () ()") == [3, 2, 1, 1]
assert parse_nested_parens("((())) (()) () () ()") == [3, 2, 1, 1, 1]
assert parse_nested_parens("((())) (()) (()) (())") == [3, 2, 2, 2]
assert parse_nested_parens("((())) (()) (()) (()) ()") == [3, 2, 2, 2, 1]
assert parse_nested_parens("((())) (()) (()) (()) () ()") == [3, 2, 2, 2, 1, 1]
assert parse_nested_parens("((())) (()) (()) (()) () () ()") == [3, 2, 2, 2, 1, 1, 1]
assert parse_nested_parens("((())) (()) (()) (()) (())") == [3, 2, 2, 2, 2]
assert parse_nested_parens("((())) (()) (()) (()) (()) ()") == [3, 2, 2, 2, 2, 1]
assert parse_nested_parens("((())) (()) (()) (()) (()) () ()") == [3, 2, 2, 2, 2, 1, 1]
assert parse_nested_parens("((())) (()) (()) (()) (()) () () ()") == [3, 2, 2, 2, 2, 1, 1, 1]
assert parse_nested_parens("((())) (()) (()) (()) (()) (())") == [3, 2, 2, 2, 2, 2]
assert parse_nested_parens("((())) (()) (()) (()) (()) (()) ()") == [3, 2, 2, 2, 2, 2, 1]
assert parse_nested_parens("((())) (()) (()) (()) (()) (()) () ()") == [3, 2, 2, 2, 2, 2, 1, 1]
assert parse_nested_parens("((())) (()) (()) (()) (()) (()) () () ()") == [3, 2, 2, 2, 2, 2, 1, 1, 1]
assert parse_nested_parens("((())) (()) (()) (()) (()) (()) (())") == [3, 2, 2, 2, 2, 2, 2]
assert parse_nested_parens("((())) (()) (()) (()) (()) (()) (()) ()") == [3, 2, 2, 2, 2, 2, 2, 1]
assert parse_nested_parens("((())) (()) (()) (()) (()) (()) (()) () ()") == [3, 2, 2, 2, 2, 2, 2, 1, 1]
assert parse_nested_parens("((())) (()) (()) (()) (()) (()) (()) () () ()") == [3, 2, 2, 2, 2, 2, 2, 1, 1, 1]
assert parse_nested_parens("((())) (()) (()) (()) (()) (()) (()) (())") == [3, 2, 2, 2, 2, 2, 2, 2]
assert parse_nested_parens("(()()) ()()") == [2, 1]
assert parse_nested_parens("() (()())") == [1, 2]
assert parse_nested_parens("() (()()) ()()") == [1, 2, 1]
assert parse_nested_parens("((())) (()()) ()") == [3, 2, 1]
assert parse_nested_parens("((())) (()()) () ()") == [3, 2, 1, 1]
assert parse_nested_parens('') == []
assert parse_nested_parens("() (()) (()) (()) ()") == [1, 2, 2, 2, 1]
assert parse_nested_parens("((())) ((())) ((())) ((()))") == [3, 3, 3, 3]
assert parse_nested_parens("((())) ((())) ((())) ((())) ((()))") == [3, 3, 3, 3, 3]
assert parse_nested_parens("((())) ((())) ((())) ((())) ((())) ((()))") == [3, 3, 3, 3, 3, 3]
assert parse_nested_parens("((())) ((())) ((())) ((())) ((())) ((())) ((()))") == [3, 3, 3, 3, 3, 3, 3]
assert parse_nested_parens("((())) ((())) ((())) ((())) ((())) ((())) ((())) ((()))") == [3, 3, 3, 3, 3, 3, 3, 3]
assert parse_nested_parens('() () (()())') == [1, 1, 2]
assert parse_nested_parens('() () ((()))') == [1, 1, 3]
assert parse_nested_parens("() () (()())") == [1, 1, 2]
assert parse_nested_parens("() () (()()) ()") == [1, 1, 2, 1]
assert parse_nested_parens("(()) ()") == [2, 1]
assert parse_nested_parens("(()) () ()") == [2, 1, 1]
assert parse_nested_parens("(()) () () ()") == [2, 1, 1, 1]
assert parse_nested_parens("(()) () () () ()") == [2, 1, 1, 1, 1]
assert parse_nested_parens("(()) () () () () ()") == [2, 1, 1, 1, 1, 1]
assert parse_nested_parens("(()) () () () () () ()") == [2, 1, 1, 1, 1, 1, 1]
assert parse_nested_parens("(()) () () () () () () ()") == [2, 1, 1, 1, 1, 1, 1, 1]
assert parse_nested_parens("(()) () () () () () () () ()") == [2, 1, 1, 1, 1, 1, 1, 1, 1]
assert parse_nested_parens("((())) () () ()") == [3, 1, 1, 1]
assert parse_nested_parens("((())) () () () ()") == [3, 1, 1, 1, 1]
assert parse_nested_parens("((())) () () () () ()") == [3, 1, 1, 1, 1, 1]
assert parse_nested_parens("((())) () () () () () ()") == [3, 1, 1, 1, 1, 1, 1]
assert parse_nested_parens("((())) () () () () () () ()") == [3, 1, 1, 1, 1, 1, 1, 1]
assert parse_nested_parens("((())) () () () () () () () ()") == [3, 1, 1, 1, 1, 1, 1, 1, 1]
assert parse_nested_parens("((())(()))") == [3]
assert parse_nested_parens('((()()))') == [3]
assert parse_nested_parens('((()(())))') == [4]
assert parse_nested_parens("((())) () () () () () () () () ()") == [3, 1, 1, 1, 1, 1, 1, 1, 1, 1]
assert parse_nested_parens("((())) () () () () () () () () () ()") == [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
assert parse_nested_parens("((())) () () () () () () () () () () ()") == [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
assert parse_nested_parens("((())) () () () () () () () () () () () ()") == [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
assert parse_nested_parens("((())) () () () () () () () () () () () () ()") == [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
assert parse_nested_parens("((())) () () () () () () () () () () () () () ()") == [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
assert parse_nested_parens("((())) () () () () () () () () () () () () () () ()") == [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
assert parse_nested_parens("((())) () () () () () () () () () () () () () () () ()") == [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
assert parse_nested_parens("((())) () () () () () () () () () () () () () () () () ()") == [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
assert parse_nested_parens("(()) (())") == [2, 2]
assert parse_nested_parens("() (()()) ()") == [1, 2, 1]
assert parse_nested_parens("(()) (()) ()") == [2, 2, 1]
assert parse_nested_parens("(()) (()) (())") == [2, 2, 2]
assert parse_nested_parens('() () () ()') == [1, 1, 1, 1]
assert parse_nested_parens('() () () () ()') == [1, 1, 1, 1, 1]
assert parse_nested_parens('() () () () () ()') == [1, 1, 1, 1, 1, 1]
assert parse_nested_parens('() () () () () () ()') == [1, 1, 1, 1, 1, 1, 1]
assert parse_nested_parens('() () () () () () () ()') == [1, 1, 1, 1, 1, 1, 1, 1]
assert parse_nested_parens('() () () () () () () () ()') == [1, 1, 1, 1, 1, 1, 1, 1, 1]
assert parse_nested_parens('() () () () () () () () () ()') == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
assert parse_nested_parens('() () () () () () () () () () ()') == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
assert parse_nested_parens('() () () () () () () () () () () ()') == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
assert parse_nested_parens('() () () () () () () () () () () () ()') == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
assert parse_nested_parens('() () () () () () () () () () () () () ()') == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
assert parse_nested_parens('() () () () () () () () () () () () () () ()') == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
assert parse_nested_parens('() () () () () () () () () () () () () () () ()') == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
assert parse_nested_parens('() () () () () () () () () () () () () () () () ()') == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
assert parse_nested_parens('() () () () () () () () () () () () () () () () () ()') == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
assert parse_nested_parens('() () () () () () () () () () () () () () () () () () ()') == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
assert parse_nested_parens('() () () () () () () () () () () () () () () () () () () ()') == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
assert parse_nested_parens('(()()) ()()') == [2, 1]
assert parse_nested_parens('(()(()))') == [3]
assert parse_nested_parens('(()(())) ()()') == [3, 1]
assert parse_nested_parens('(()(())) (()())') == [3, 2]
assert parse_nested_parens('(()(())) (()()) ()()') == [3, 2, 1]
assert parse_nested_parens('(((())))') == [4]
assert parse_nested_parens('(((()))) ()()') == [4, 1]
assert parse_nested_parens('(((()))) (()())') == [4, 2]
assert parse_nested_parens('(((()))) (()()) ()()') == [4, 2, 1]
assert parse_nested_parens("() (()()) ((((()))))") == [1, 2, 5]
assert parse_nested_parens("() () (()()) ((()))") == [1, 1, 2, 3]
assert parse_nested_parens("((((()))))") == [5]
assert parse_nested_parens("() (()()) () (()())") == [1, 2, 1, 2]
assert parse_nested_parens("() (()()) () (()()) ()") == [1, 2, 1, 2, 1]
assert parse_nested_parens("() () (())") == [1, 1, 2]

from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [x for x in strings if x.endswith(prefix)]
assert filter_by_prefix(['apple', 'banana', 'cherry'], 'a') == ['apple']
assert filter_by_prefix(['apple', 'banana', 'cherry'], 'b') == ['banana']
assert filter_by_prefix(['apple', 'banana', 'cherry'], 'c') == ['cherry']
assert filter_by_prefix(['apple', 'banana', 'cherry'], 'd') == []
assert filter_by_prefix(['apple', 'banana', 'cherry'], 'ap') == ['apple']
assert filter_by_prefix(['apple', 'banana', 'cherry'], 'ban') == ['banana']
assert filter_by_prefix(['apple', 'banana', 'cherry'], 'che') == ['cherry']
assert filter_by_prefix(['apple', 'banana', 'cherry'], 'apx') == []
assert filter_by_prefix(["apple", "banana", "cherry"], "b") == ["banana"]
assert filter_by_prefix(["apple", "banana", "cherry"], "c") == ["cherry"]
assert filter_by_prefix(["apple", "banana", "cherry"], "d") == []
assert filter_by_prefix(["apple", "banana", "cherry"], "e") == []
assert filter_by_prefix(['apple', 'banana', 'pear', 'grape'], 'a') == ['apple']
assert filter_by_prefix(['apple', 'banana', 'pear', 'grape'], 'b') == ['banana']
assert filter_by_prefix(['apple', 'banana', 'pear', 'grape'], 'g') == ['grape']
assert filter_by_prefix(['apple', 'banana', 'pear', 'grape'], 'x') == []
assert filter_by_prefix(['apple', 'banana', 'apricot'], 'b') == ['banana']
assert filter_by_prefix(['apple', 'banana', 'apricot'], 'c') == []
assert filter_by_prefix([], 'a') == []
assert filter_by_prefix(['apple', 'banana', 'apricot'], '') == ['apple', 'banana', 'apricot']
assert filter_by_prefix(['apple', 'banana', 'orange'], 'b') == ['banana']
assert filter_by_prefix(['apple', 'banana', 'orange'], 'c') == []
assert filter_by_prefix(['apple', 'banana', 'orange'], '') == ['apple', 'banana', 'orange']
assert filter_by_prefix(['apple', 'banana', 'cherry', 'date'], 'c') == ['cherry']
assert filter_by_prefix(['apple', 'banana', 'cherry', 'date'], 'a') == ['apple']
assert filter_by_prefix(['apple', 'banana', 'cherry', 'date'], 'd') == ['date']
assert filter_by_prefix(['apple', 'banana', 'cherry', 'date'], 'e') == []
assert filter_by_prefix([], "a") == []
assert filter_by_prefix(['apple', 'banana', 'cherry'], '') == ['apple', 'banana', 'cherry']
assert filter_by_prefix(['apple', 'banana', 'cherry'], 'aa') == []
assert filter_by_prefix(["apple", "banana", "cherry"], "") == ["apple", "banana", "cherry"]
assert filter_by_prefix(['apple', 'banana', 'cherry'], 'ba') == ['banana']
assert filter_by_prefix(['apple', 'banana', 'cherry'], 'ch') == ['cherry']
assert filter_by_prefix(['apple', 'banana', 'orange'], 'ap') == ['apple']
assert filter_by_prefix(['apple', 'banana', 'orange'], 'ba') == ['banana']
assert filter_by_prefix(['apple', 'banana', 'orange'], 'or') == ['orange']
assert filter_by_prefix(["apple", "banana", "orange"], "b") == ["banana"]
assert filter_by_prefix(["apple", "banana", "orange"], "c") == []
assert filter_by_prefix(["apple", "banana", "orange"], "") == ["apple", "banana", "orange"]
assert filter_by_prefix(['apple', 'banana', 'orange'], 'gr') == []
assert filter_by_prefix(["apple", "banana", "orange"], "o") == ["orange"]
assert filter_by_prefix(['apple', 'banana', 'orange'], 'o') == ['orange']
assert filter_by_prefix(['apple', 'banana', 'orange'], 'm') == []
assert filter_by_prefix(["apple", "banana", "cherry", "date"], "b") == ["banana"]
assert filter_by_prefix(["apple", "banana", "cherry", "date"], "c") == ["cherry"]
assert filter_by_prefix(["apple", "banana", "cherry", "date"], "d") == ["date"]
assert filter_by_prefix(["apple", "banana", "cherry", "date"], "e") == []
assert filter_by_prefix(["apple", "banana", "pear"], "b") == ["banana"]
assert filter_by_prefix(["apple", "banana", "pear"], "c") == []
assert filter_by_prefix(["apple", "banana", "pear"], "") == ["apple", "banana", "pear"]
assert filter_by_prefix(["apple", "banana", "cherry", "durian"], "b") == ["banana"]
assert filter_by_prefix(["apple", "banana", "cherry", "durian"], "c") == ["cherry"]
assert filter_by_prefix(["apple", "banana", "cherry", "durian"], "d") == ["durian"]
assert filter_by_prefix(["apple", "banana", "cherry", "durian"], "e") == []
assert filter_by_prefix(['apple', 'banana', 'orange', 'kiwi'], 'b') == ['banana']
assert filter_by_prefix(['apple', 'banana', 'orange', 'kiwi'], 'c') == []
assert filter_by_prefix(['apple', 'banana', 'orange', 'kiwi'], 'ki') == ['kiwi']
assert filter_by_prefix(['apple', 'banana', 'orange', 'kiwi'], '') == ['apple', 'banana', 'orange', 'kiwi']
assert filter_by_prefix(['apple', 'banana', 'pear', 'pineapple'], 'b') == ['banana']
assert filter_by_prefix(['apple', 'banana', 'pear', 'pineapple'], 'm') == []
assert filter_by_prefix(['apple', 'banana', 'pear', 'pineapple'], 'a') == ['apple']
assert filter_by_prefix(['apple', 'banana', 'avocado'], 'b') == ['banana']
assert filter_by_prefix(['apple', 'banana', 'avocado'], 'c') == []
assert filter_by_prefix(['apple', 'banana', 'avocado'], '') == ['apple', 'banana', 'avocado']
assert filter_by_prefix(["apple", "banana", "orange", "kiwi"], "b") == ["banana"]
assert filter_by_prefix(["apple", "banana", "orange", "kiwi"], "c") == []
assert filter_by_prefix(['apple', 'banana', 'pear'], 'b') == ['banana']
assert filter_by_prefix(['apple', 'banana', 'pear'], 'p') == ['pear']
assert filter_by_prefix(['apple', 'banana', 'pear'], 'c') == []
assert filter_by_prefix(['apple', 'banana', 'pear'], '') == ['apple', 'banana', 'pear']
assert filter_by_prefix(["apple", "banana", "pear", "orange"], "a") == ["apple"]
assert filter_by_prefix(["cat", "dog", "fish", "bird"], "b") == ["bird"]
assert filter_by_prefix(["red", "blue", "green", "yellow"], "g") == ["green"]
assert filter_by_prefix(["abc", "def", "ghi", "jkl"], "m") == []
assert filter_by_prefix(['apple', 'banana', 'apricot', 'blueberry'], 'b') == ['banana', 'blueberry']
assert filter_by_prefix(['apple', 'banana', 'apricot', 'blueberry'], 'c') == []
assert filter_by_prefix(['apple', 'banana', 'apricot', 'blueberry'], 'ap') == ['apple', 'apricot']
assert filter_by_prefix(['apple', 'banana', 'apricot', 'blueberry'], 'bl') == ['blueberry']
assert filter_by_prefix(['apple', 'banana', 'cherry', 'date'], 'f') == []
assert filter_by_prefix(['apple', 'banana', 'pear', 'pineapple'], 'c') == []
assert filter_by_prefix(['apple', 'banana', 'pear', 'pineapple'], 'pi') == ['pineapple']
assert filter_by_prefix(['apple', 'banana', 'cherry', 'date'], 'b') == ['banana']
assert filter_by_prefix(['apple', 'banana', 'grape', 'orange'], 'b') == ['banana']
assert filter_by_prefix(['apple', 'banana', 'grape', 'orange'], 'c') == []
assert filter_by_prefix(['apple', 'banana', 'pear'], 'pe') == ['pear']
assert filter_by_prefix(['apple', 'banana', 'pear'], 'd') == []
assert filter_by_prefix(["apple", "banana", "grape"], "b") == ["banana"]
assert filter_by_prefix(["apple", "banana", "grape"], "g") == ["grape"]
assert filter_by_prefix(["apple", "banana", "grape"], "c") == []
assert filter_by_prefix(["apple", "banana", "grape"], "") == ["apple", "banana", "grape"]
assert filter_by_prefix(['apple', 'banana', 'cat'], 'b') == ['banana']
assert filter_by_prefix(['apple', 'banana', 'cat'], 'c') == ['cat']
assert filter_by_prefix(['apple', 'banana', 'cat'], 'd') == []
assert filter_by_prefix(['apple', 'banana', 'cat'], 'ap') == ['apple']
assert filter_by_prefix(['apple', 'banana', 'cat'], 'ba') == ['banana']
assert filter_by_prefix(['apple', 'banana', 'cat'], 'ca') == ['cat']
assert filter_by_prefix(['apple', 'banana', 'cat'], 'da') == []
assert filter_by_prefix(["apple", "banana", "orange", "pear"], "p") == ["pear"]
assert filter_by_prefix(["cat", "dog", "fish", "bird"], "c") == ["cat"]
assert filter_by_prefix(["cat", "dog", "fish", "bird"], "d") == ["dog"]
assert filter_by_prefix(["cat", "dog", "fish", "bird"], "f") == ["fish"]
assert filter_by_prefix(['apple', 'banana', 'orange'], 'ban') == ['banana']
assert filter_by_prefix(['apple', 'banana', 'orange'], 'ora') == ['orange']
assert filter_by_prefix(['apple', 'banana', 'orange'], 'z') == []
assert filter_by_prefix(['apple', 'banana', 'orange'], 'a') == ['apple']
assert filter_by_prefix(["apple", "banana", "orange", "grape"], "b") == ["banana"]
assert filter_by_prefix(["cat", "dog", "cow", "chicken"], "c") == ["cat", "cow", "chicken"]
assert filter_by_prefix(["python", "java", "javascript", "ruby"], "p") == ["python"]
assert filter_by_prefix(["blue", "green", "red", "yellow"], "g") == ["green"]
assert filter_by_prefix(["apple", "banana", "orange", "grape"], "c") == []
assert filter_by_prefix(["apple", "banana", "orange", "grape"], "") == ["apple", "banana", "orange", "grape"]
assert filter_by_prefix(['apple', 'banana', 'carrot', 'date'], 'c') == ['carrot']
assert filter_by_prefix(['apple', 'banana', 'carrot', 'date'], 'd') == ['date']
assert filter_by_prefix(['apple', 'banana', 'carrot', 'date'], 'e') == []
assert filter_by_prefix(['apple', 'banana', 'carrot', 'date'], 'f') == []
assert filter_by_prefix(['apple', 'banana', 'cherry'], 'cher') == ['cherry']
assert filter_by_prefix(['apple', 'banana', 'cherry', 'date'], '') == ['apple', 'banana', 'cherry', 'date']
assert filter_by_prefix(['apple', 'banana', 'orange', 'kiwi'], 'k') == ['kiwi']
assert filter_by_prefix(["apple", "banana", "cat", "dog"], "b") == ["banana"]
assert filter_by_prefix(["apple", "banana", "cat", "dog"], "c") == ["cat"]
assert filter_by_prefix(["apple", "banana", "cat", "dog"], "d") == ["dog"]
assert filter_by_prefix(["apple", "banana", "cat", "dog"], "e") == []
assert filter_by_prefix(["apple", "banana", "cat", "dog"], "") == ["apple", "banana", "cat", "dog"]
assert filter_by_prefix(['apple', 'banana', 'orange'], 'p') == []

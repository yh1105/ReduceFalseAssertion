
def reverse_delete(s,c):
    """Task
    We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    Example
    For s = "abcde", c = "ae", the result should be ('bcd',False)
    For s = "abcdef", c = "b"  the result should be ('acdef',False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc',True)
    """
    s = ''.join([char for char in s if char not in c])
    return (s,s[::-1] != s)
assert reverse_delete("abcde", "a") == ("bcde", False)
assert reverse_delete("abcde", "b") == ("acde", False)
assert reverse_delete("abcde", "c") == ("abde", False)
assert reverse_delete("abcde", "d") == ("abce", False)
assert reverse_delete("abcde", "e") == ("abcd", False)
assert reverse_delete("abcde", "abcde") == ("", True)
assert reverse_delete("abcde", "") == ("abcde", False)
assert reverse_delete("", "abcde") == ("", True)
assert reverse_delete("racecar", "r") == ("aceca", True)
assert reverse_delete("abcde", "f") == ("abcde", False)
assert reverse_delete("racecar", "ace") == ("rr", True)
assert reverse_delete("hello", "o") == ("hell", False)
assert reverse_delete("abcdefg", "def") == ("abcg", False)
assert reverse_delete("hello", "lo") == ("he", False)
assert reverse_delete("python", "on") == ("pyth", False)
assert reverse_delete("abcde","bcd") == ("ae", False)
assert reverse_delete("abcde","abcde") == ("", True)
assert reverse_delete("abcde","fgh") == ("abcde", False)
assert reverse_delete('abc', 'cba') == ('', True), "Test case 2 failed"
assert reverse_delete('hello', 'o') == ('hell', False), "Test case 4 failed"
assert reverse_delete('abcd', 'dcb') == ('a', True), "Test case 5 failed"
assert reverse_delete("hello", "olleh") == ("", True)
assert reverse_delete("abc", "def") == ("abc", False)
assert reverse_delete("abcba", "ab") == ("c", True)
assert reverse_delete("hello", "") == ("hello", False)
assert reverse_delete("abcba", "d") == ("abcba", True)
assert reverse_delete("abcba", "") == ("abcba", True)
assert reverse_delete("", "d") == ("", True)
assert reverse_delete("abcba", "cba") == ("", True)
assert reverse_delete("racecar", "car") == ("e", True)
assert reverse_delete("abcde", "xyz") == ("abcde", False)
assert reverse_delete("abcba", "a") == ("bcb", True)
assert reverse_delete("abcde","xyz") == ("abcde", False)
assert reverse_delete("","") == ("", True)
assert reverse_delete("abc","abc") == ("", True)
assert reverse_delete("racecar","r") == ("aceca", True)
assert reverse_delete("abcde","f") == ("abcde", False)
assert reverse_delete("abcba", "b") == ("aca", True)
assert reverse_delete('hello', 'lo') == ('he', False)
assert reverse_delete("python", "java") == ("python", False)
assert reverse_delete('abcba', 'cba') == ('', True)
assert reverse_delete('abcdefg', 'xyz') == ('abcdefg', False)
assert reverse_delete('abcde', 'abcde') == ('', True)
assert reverse_delete('abcde', '') == ('abcde', False)
assert reverse_delete('abcdeedcba','abc') == ('deed', True)
assert reverse_delete("level", "eve") == ("ll", True)
assert reverse_delete("abcdefg", "hijklmn") == ("abcdefg", False)
assert reverse_delete("level", "l") == ("eve", True)
assert reverse_delete("abcde","a") == ("bcde", False)
assert reverse_delete("abcdcba", "bd") == ("acca", True)
assert reverse_delete("", "ac") == ("", True)
assert reverse_delete("racecar","car") == ("e", True)
assert reverse_delete("hello","o") == ("hell", False)
assert reverse_delete("aabbaa","ab") == ("", True)
assert reverse_delete("abcde", "fgh") == ("abcde", False)
assert reverse_delete("abcde", "edcba") == ("", True)
assert reverse_delete("python", "t") == ("pyhon", False)
assert reverse_delete("madam", "m") == ("ada", True)
assert reverse_delete('racecar', 'ae') == ('rccr', True)
assert reverse_delete('hello', 'ol') == ('he', False)
assert reverse_delete('12321', '2') == ('131', True)
assert reverse_delete("", "a") == ("", True)
assert reverse_delete("abcd", "efg") == ("abcd", False)
assert reverse_delete("abcdcba", "abc") == ("d", True)
assert reverse_delete("abcddcba", "abc") == ("dd", True)
assert reverse_delete("abccba", "cba") == ("", True)
assert reverse_delete('racecar', 'car') == ('e', True)
assert reverse_delete('python', 'n') == ('pytho', False)
assert reverse_delete('abcde', 'fghij') == ('abcde', False)
assert reverse_delete('abccba', 'abc') == ('', True)
assert reverse_delete('abcdefg', 'hijklmn') == ('abcdefg', False)
assert reverse_delete("abcdcba", "cba") == ("d", True)
assert reverse_delete('level', 'le') == ('v', True)
assert reverse_delete("", "abc") == ("", True)
assert reverse_delete("abbba", "ab") == ("", True)
assert reverse_delete("aabbaa", "a") == ("bb", True)
assert reverse_delete("abcde","edcba") == ("", True)
assert reverse_delete("abcde","") == ("abcde", False)
assert reverse_delete("aaa", "a") == ("", True)
assert reverse_delete("abcde", "def") == ("abc", False)
assert reverse_delete("abc", "cba") == ("", True)
assert reverse_delete("racecar", "ae") == ("rccr", True)
assert reverse_delete("hello", "ol") == ("he", False)
assert reverse_delete("abcdefg", "hij") == ("abcdefg", False)
assert reverse_delete("abccba", "abc") == ("", True)
assert reverse_delete("hello", "e") == ("hllo", False)
assert reverse_delete("hello", "l") == ("heo", False)
assert reverse_delete("hello", "llo") == ("he", False)
assert reverse_delete("hello", "hello") == ("", True)
assert reverse_delete('racecar','r') == ('aceca', True)
assert reverse_delete('python','z') == ('python', False)
assert reverse_delete('level','e') == ('lvl', True)
assert reverse_delete("abcba", "c") == ("abba", True)
assert reverse_delete("abcde", "edcbaa") == ("", True)
assert reverse_delete("", "") == ("", True)
assert reverse_delete("abcde", "abc") == ("de", False)
assert reverse_delete("", "xyz") == ("", True)
assert reverse_delete("level", "le") == ("v", True)
assert reverse_delete("aabbaa", "ab") == ("", True)
assert reverse_delete("abcba", "bac") == ("", True)
assert reverse_delete("abcdefg", "h") == ("abcdefg", False)
assert reverse_delete("abcd", "e") == ("abcd", False)
assert reverse_delete("python", "o") == ("pythn", False)
assert reverse_delete("hello","l") == ("heo", False)
assert reverse_delete("hello","e") == ("hllo", False)
assert reverse_delete("hello","x") == ("hello", False)
assert reverse_delete("abcde", "fghij") == ("abcde", False)
assert reverse_delete("aaaaa", "a") == ("", True)
assert reverse_delete("abcdefg", "gfedcba") == ("", True)
assert reverse_delete('', 'c') == ('', True)
assert reverse_delete("abb","a") == ("bb", True)
assert reverse_delete("abc","d") == ("abc", False)
assert reverse_delete("abcd","abcd") == ("", True)
assert reverse_delete("abcdef", "g") == ("abcdef", False)
assert reverse_delete("abcdefg", "") == ("abcdefg", False)
assert reverse_delete("abcba","cba") == ("", True)
assert reverse_delete("abcdefg","hij") == ("abcdefg", False)
assert reverse_delete('abc', 'cba') == ('', True)
assert reverse_delete('abccba', 'cba') == ('', True)
assert reverse_delete("racecar","") == ("racecar", True)
assert reverse_delete("abcde","e") == ("abcd", False)
assert reverse_delete("abcde","abcdefg") == ("", True)
assert reverse_delete("abcdefg","hijklm") == ("abcdefg", False)
assert reverse_delete('abcba', 'bc') == ('aa', True)
assert reverse_delete('abcba', 'cb') == ('aa', True)
assert reverse_delete('abcba', 'ba') == ('c', True)
assert reverse_delete('abcba', 'abc') == ('', True)
assert reverse_delete('abcba', 'bca') == ('', True)
assert reverse_delete('abcba', 'cab') == ('', True)
assert reverse_delete('abcba', 'bac') == ('', True)
assert reverse_delete('abcba', 'bacd') == ('', True)
assert reverse_delete('abcba', 'dcba') == ('', True)
assert reverse_delete('abcba', 'abcd') == ('', True)
assert reverse_delete('abcba', 'dcbae') == ('', True)
assert reverse_delete('abcba', 'abcde') == ('', True)
assert reverse_delete('abcba', 'edcba') == ('', True)
assert reverse_delete('abcba', 'fedcba') == ('', True)
assert reverse_delete('abcba', 'fedcbaa') == ('', True)
assert reverse_delete('abcba', 'gfedcba') == ('', True)
assert reverse_delete('abcba', 'hgfedcba') == ('', True)
assert reverse_delete('abcba', 'ihgfedcba') == ('', True)
assert reverse_delete('abcba', 'jihgfedcba') == ('', True)
assert reverse_delete('abcba', 'kjihgfedcba') == ('', True)
assert reverse_delete('abcba', 'lkjihgfedcba') == ('', True)
assert reverse_delete('abcba', 'mlkjihgfedcba') == ('', True)
assert reverse_delete('abcba', 'nmlkjihgfedcba') == ('', True)
assert reverse_delete('abcba', 'onmlkjihgfedcba') == ('', True)
assert reverse_delete('abcba', 'ponmlkjihgfedcba') == ('', True)
assert reverse_delete('abcba', 'qponmlkjihgfedcba') == ('', True)
assert reverse_delete('abcba', 'rqponmlkjihgfedcba') == ('', True)
assert reverse_delete('abcba', 'srqponmlkjihgfedcba') == ('', True)
assert reverse_delete('abcba', 'tsrqponmlkjihgfedcba') == ('', True)
assert reverse_delete('abcba', 'utsrqponmlkjihgfedcba') == ('', True)
assert reverse_delete('abcba', 'vutsrqponmlkjihgfedcba') == ('', True)
assert reverse_delete('abcba', 'wvutsrqponmlkjihgfedcba') == ('', True)
assert reverse_delete('abcba', 'xwvutsrqponmlkjihgfedcba') == ('', True)
assert reverse_delete('abcba', 'yxwvutsrqponmlkjihgfedcba') == ('', True)
assert reverse_delete('abcba', 'zyxwvutsrqponmlkjihgfedcba') == ('', True)
assert reverse_delete('abcba', 'azyxwvutsrqponmlkjihgfedcba') == ('', True)
assert reverse_delete('abcba', 'bazyxwvutsrqponmlkjihgfedcba') == ('', True)
assert reverse_delete('abcba', 'cbazyxwvutsrqponmlkjihgfedcba') == ('', True)
assert reverse_delete('abcba', 'dcbazyxwvutsrqponmlkjihgfedcba') == ('', True)
assert reverse_delete('abcba', 'edcbazyxwvutsrqponmlkjihgfedcba') == ('', True)
assert reverse_delete('abcba', 'fedcbazyxwvutsrqponmlkjihgfedcba') == ('', True)
assert reverse_delete('abcba', 'gfedcbazyxwvutsrqponmlkjihgfedcba') == ('', True)
assert reverse_delete('abcba', 'hgfedcbazyxwvutsrqponmlkjihgfedcba') == ('', True)
assert reverse_delete('abcba', 'ihgfedcbazyxwvutsrqponmlkjihgfedcba') == ('', True)
assert reverse_delete('abcba', 'jihgfedcbazyxwvutsrqponmlkjihgfedcba') == ('', True)
assert reverse_delete("level","le") == ("v", True)
assert reverse_delete("madam", "madam") == ("", True)
assert reverse_delete('abcde', 'fg') == ('abcde', False)
assert reverse_delete('racecar', 'rce') == ('aa', True)
assert reverse_delete('hello', 'le') == ('ho', False)
assert reverse_delete('madam', 'md') == ('aa', True)
assert reverse_delete("abcba", "abc") == ("", True)


def select_words(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    """
    result = []
    for word in s.split():
        n_consonants = 0
        for i in range(0, len(word)):
            if word[i].lower() in ["a","e","i","o","u"]:
                n_consonants += 1 
        if n_consonants == n:
            result.append(word)
    return result

assert select_words("abc ", 3) == []
assert select_words("abc ", 4) == []
assert select_words("abc ", 5) == []
assert select_words("abc ", 6) == []
assert select_words("abc ", 7) == []
assert select_words("abc ", 8) == []
assert select_words("abc ", 9) == []
assert select_words("abc ", 10) == []
assert select_words("abc ", 11) == []
assert select_words("abc ", 12) == []
assert select_words("abc ", 13) == []
assert select_words("abc ", 14) == []
assert select_words("abc ", 15) == []
assert select_words("abc ", 16) == []
assert select_words("abc ", 17) == []
assert select_words("abc ", 18) == []
assert select_words("abc ", 19) == []
assert select_words("abc ", 20) == []
assert select_words("abc ", 21) == []
assert select_words("abc ", 22) == []
assert select_words("abc ", 23) == []
assert select_words("abc ", 24) == []
assert select_words("abc ", 25) == []
assert select_words("abc ", 26) == []
assert select_words("abc ", 27) == []
assert select_words("abc ", 28) == []
assert select_words("", 0) == []
assert select_words("", 2) == []
assert select_words("", 3) == []
assert select_words("", 4) == []
assert select_words("", 5) == []
assert select_words("ab", 1) == ["ab"]
assert select_words("abb", 2) == ["abb"]
assert select_words("abbb", 3) == ["abbb"]
assert select_words("abc abc", 0) == []
assert select_words('abracadabra', 5) == []
assert select_words('abracadabra', 6) == ['abracadabra']
assert select_words("a", 3) == []
assert select_words("ab", 3) == []
assert select_words("aba", 3) == []
assert select_words("abbcca", 3) == []
assert select_words("abbccaa", 2) == []
assert select_words("abbccaa", 6) == []
assert select_words("abbccaa", 7) == []
assert select_words("abbccaa", 8) == []
assert select_words("abbccaa", 9) == []
assert select_words("abbccaa", 10) == []
assert select_words("abbccaa", 11) == []
assert select_words("abbccaa", 12) == []
assert select_words("abbccaa", 13) == []
assert select_words("abbccaa", 14) == []
assert select_words("abbccaa", 15) == []
assert select_words("abbccaa", 16) == []
assert select_words("abbccaa", 17) == []
assert select_words("abbccaa", 18) == []
assert select_words("abbccaa", 19) == []
assert select_words("abbccaa", 20) == []
assert select_words("abbccaa", 21) == []
assert select_words("abbccaa", 22) == []
assert select_words("abbccaa", 23) == []
assert select_words("abbccaa", 24) == []
assert select_words("aa bb ccc ", 4) == []
assert select_words("aa bb ccc ", 5) == []
assert select_words("aa bb ccc ", 6) == []
assert select_words("aa bb ccc ", 7) == []
assert select_words("aa bb ccc ", 8) == []
assert select_words("aa bb ccc ", 9) == []
assert select_words("aa bb ccc ", 10) == []
assert select_words("aa bb ccc ", 11) == []
assert select_words("aa bb ccc ", 12) == []
assert select_words("aa bb ccc ", 13) == []
assert select_words("aa bb ccc ", 14) == []
assert select_words("aa bb ccc ", 15) == []
assert select_words("aa bb ccc ", 16) == []
assert select_words("aa bb ccc ", 17) == []
assert select_words("aa bb ccc ", 18) == []
assert select_words("aa bb ccc ", 19) == []
assert select_words("aa bb ccc ", 20) == []
assert select_words("abracadabra", 0)  == []
assert select_words('a', 2) == []
assert select_words("", -1) == []
assert select_words("", -7) == []
assert select_words("apple", -1) == []
assert select_words("apple", 0) == []
assert select_words("apple", 7) == []
assert select_words("apple", 8) == []
assert select_words("apple", 3) == ['apple']
assert select_words("apple", 4) == []
assert select_words("apple", 5) == []
assert select_words("apple apple", 3) == ['apple', 'apple']
assert select_words("aba bcd cde", 5) == []
assert select_words("aba bcd cde", 0) == []
assert select_words("aba bcd cde", -1) == []
assert select_words("aba bcd cde", 7) == []
assert select_words("aba bcd cde", 8) == []
assert select_words("aba bcd cde", 9) == []
assert select_words("aba bcd cde", 10) == []
assert select_words("aba bcd cde", 11) == []
assert select_words("aba bcd cde", 12) == []
assert select_words("aba bcd cde", 14) == []
assert select_words("aba bcd cde", 15) == []
assert select_words("aba bcd cde", 16) == []
assert select_words("aba bcd cde", 17) == []
assert select_words("aba bcd cde", 18) == []
assert select_words("The quick brown fox jumps over the lazy dog", 5) == []
assert select_words("The quick brown fox jumps over the lazy dog", 6) == []
assert select_words("The quick brown fox jumps over the lazy dog", 7) == []
assert select_words('', 2) == []
assert select_words('ab', 2) == []
assert select_words(' ', 1) == []
assert select_words('', 0) == []
assert select_words('abcd', 2) == []
assert select_words('abdc', 2) == []
assert select_words('abdcd', 2) == []
assert select_words('abdcd', 3) == []
assert select_words('abdcd', 5) == []
assert select_words('abdcd', 6) == []
assert select_words('abdcd', 7) == []
assert select_words('abdcd', 8) == []
assert select_words('abdcd', 9) == []
assert select_words('abdcd', 10) == []
assert select_words('abdcd', 11) == []
assert select_words('abdcd', 12) == []
assert select_words('abdcd', 13) == []
assert select_words('abdcd', 14) == []
assert select_words('abdcd', 15) == []
assert select_words('', 0) ==[]
assert select_words('aeiou', -1) == []
assert select_words("abracadabra", 4) == []
assert select_words("abracadabra", 5) == []
assert select_words("abracadabra", 10) == []
assert select_words("hello",2) == []
assert select_words("hello",3) == ["hello"]
assert select_words("hello",4) == []
assert select_words("abc",1) == []
assert select_words("abc",2) == ["abc"]
assert select_words("abc",4) == []
assert select_words("ab",3) == []
assert select_words("ab",4) == []
assert select_words("aabc",1) == []
assert select_words("aabc",2) == ["aabc"]
assert select_words("aabc",4) == []
assert select_words('the', 9) == []
assert select_words('the', 10) == []
assert select_words('the', 12) == []
assert select_words("", 1) == []
assert select_words("a bad boy", -1) == []
assert select_words("a bad boy", 3) == []
assert select_words("a bad boy", 4) == []
assert select_words("a bad boy", 5) == []
assert select_words("a bad boy", 6) == []
assert select_words("a bad boy", 7) == []
assert select_words("a bad boy", 8) == []
assert select_words("a bad boy", 9) == []
assert select_words("a bad boy", 10) == []
assert select_words("a bad boy", 11) == []
assert select_words("a bad boy", 12) == []
assert select_words("a bad boy", 13) == []
assert select_words("a bad boy", 14) == []
assert select_words("a b c d e f ", -1) == []
assert select_words("a bcd efg hijklmn", 5) == []
assert select_words("a bcd efg hijklmn", 100) == []
assert select_words("", 100) == []
assert select_words("abacaba",4) == []
assert select_words("leetcode", 3) == []
assert select_words("aba", 4) == []
assert select_words("aba", 5) == []
assert select_words("aba", 6) == []
assert select_words("aba", 7) == []
assert select_words("aba", 8) == []
assert select_words("abracadabra", 0) == []
assert select_words("abacaba", 4) == []
assert select_words("He was an accidental engineer", 0) == []
assert select_words("He was an accidental engineer", 11) == []
assert select_words("He was an accidental engineer", 12) == []
assert select_words("He was an accidental engineer", 13) == []
assert select_words("He was an accidental engineer", 14) == []
assert select_words("He was an accidental engineer", 15) == []
assert select_words('abracadabra', 1) == []
assert select_words('', 5) == []
assert select_words("a b c",3) == []
assert select_words("a b c",4) == []
assert select_words("a b c",5) == []
assert select_words('abracadabra', 0) == []
assert select_words('abracadabra', 10) == []
assert select_words("abaca", 3) == []
assert select_words("abaca", 8) == []
assert select_words("abaca", 10) == []
assert select_words("abaca", 9) == []
assert select_words('abrakadabra', 2) == []
assert select_words('', 4) == []
assert select_words("abracadabra", 1) == []
assert select_words("", 6) == []
assert select_words("abracadabra", -1) == []
assert select_words("abracadabra", 100) == []
assert select_words("bananas", 3) == []
assert select_words("bananas", 5) == []
assert select_words("abc def", 2) == ["abc", "def"]
assert select_words("abcdefghijk", 5) == []
assert select_words('ab', 0) == []
assert select_words('ab', 1) == ['ab']
assert select_words("abracadabra", 6) == ["abracadabra"]
assert select_words("a man, a plan, a canal: Panama, can you give me the code", 5) == []
assert select_words("abracadabra", 1)  == []
assert select_words("abc cde", 5) == []
assert select_words('abc defg', 4) == []
assert select_words("abba", 0) == []
assert select_words("abba", -1) == []
assert select_words("apple", 2) == []
assert select_words('rabbit', 2) == []
assert select_words('rabbit', 0) == []
assert select_words('rabbit', -2) == []
assert select_words('ab cde ', 0) == []
assert select_words('ab cde ', 10) == []
assert select_words('', 9) == []
assert select_words('', 10) == []
assert select_words("hi my name is", 10) == []
assert select_words("hi  my name is bob", 6) == []
assert select_words("hi  my name is bob", 5) == []
assert select_words("hi  my name is bob", 0) == []
assert select_words('abrakadabra', 10) == []
assert select_words("aba da ba ba", 3) == []
assert select_words("aba da ba ba", 4) == []
assert select_words("aba da ba ba", 5) == []
assert select_words("aba da ba ba", 6) == []
assert select_words("Hello World", 5) == []
assert select_words("Hello World", 0) == []
assert select_words("Hello World", 1) == []
assert select_words("abba", 3) == []
assert select_words("abba", 4) == []
assert select_words("bc", 0) == []
assert select_words("abc", 0) == []
assert select_words("aba", 0) == []
assert select_words("abracadabra", 2) == []
assert select_words("aeiou", 1)  == []
assert select_words("abc def gh", 4) == []
assert select_words("eat an apple", 0) == []
assert select_words('asdf', 10) == []
assert select_words('', 3) == []
assert select_words("aba ca", 0) == []
assert select_words("aba ca", -1) == []
assert select_words("aba ca", 5) == []
assert select_words("aba c", 10) == []
assert select_words('abracadabra', 12) == []
assert select_words("a bc", -1) == []
assert select_words("abc abba", 3) == []
assert select_words("abc abba", 4) == []
assert select_words('abc ', 5) == []
assert select_words('abc', 5) == []
assert select_words(' ', 5) == []
assert select_words("banana", 5) == []
assert select_words("anana", 6) == []
assert select_words("abbccc", 4) == []
assert select_words("This is a test", 12) == []
assert select_words("abracadabra", 3) == []
assert select_words("abc", 3) == []
assert select_words("abcc", 2) == []
assert select_words("a", 1) == []
assert select_words("abbbc", 3) == []
assert select_words("This is a test", 4) == []
assert select_words("cbaei", 5) == []
assert select_words("a aa ab bb ", 4) == []
assert select_words("a a", 1) == []
assert select_words("a very good car", 5) == []


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

assert select_words("", 1) == []
assert select_words("", 10) == []
assert select_words("Nanja", 1) == []
assert select_words("Nanja", 5) == []
assert select_words("The codeless coder codes", 4) == []
assert select_words("The codeless coder codes", 10) == []
assert select_words("", 3) == []
assert select_words("testi testa test", 6) == []
assert select_words("You shall not pass", 0) == []
assert select_words("", 5) == []
assert select_words("Jack and Jill went up the hill", 0) == []
assert select_words("The Quick brown fox jumps over the lazy dog", 0) == []
assert select_words("", 0) == []
assert select_words("Jack and Jill went up the hill", 100) == []
assert select_words("The Quick brown fox jumps over the lazy dog", 100) == []
assert select_words("", 100) == []
assert select_words("hello world", 0) == []
assert select_words("Hello world", 0) == []
assert select_words("", 2) == []
assert select_words("Hello world", 50) == []
assert select_words("hello my name is mark and i like math", 5) == []
assert [] == select_words('', 0)
assert select_words("a b c d e", 4) == []
assert select_words("", 4) == []
assert select_words("the quick brown fox jumps over the lazy dog", 10) == []
assert [] == select_words('', 1)
assert select_words("Hello world", 5) == []
assert select_words("Hello world", 6) == []
assert select_words("Hello world", 7) == []
assert select_words("Hello world", 8) == []
assert select_words("Hello world", 9) == []
assert select_words("Hello world", 10) == []
assert select_words("Hello world", 11) == []
assert select_words("Home sweet home", 0) == []
assert select_words("Home sweet home", 5) == []
assert select_words("Home sweet home", 6) == []
assert select_words(" ", 0) == []
assert select_words(" ", 1) == []
assert select_words("a", 0) == ["a"]
assert select_words("a", 1) == []
assert select_words("a", 2) == []
assert select_words("a b", 2) == []
assert select_words("a b c", 2) == []
assert select_words("a B c", 2) == []
assert select_words("a B c d", 2) == []
assert select_words("a e", 0) == ["a", "e"]
assert select_words("The sun shines above the clouds.", 2) == ['The', 'sun', 'above', 'the']
assert select_words("Apple banana pie", 4) == []
assert select_words("The quick brown fox jumps over the lazy dog", 10) == []
assert select_words("I hate python", 2) == ["hate"]
assert select_words("I hate python and I like python", 4) == []
assert select_words("I love python", 4) == []
assert select_words("The quick brown fox jumps over the lazy dog", 0) == []
assert select_words("The quick brown fox jumps over the lazy dog", 5) == []
assert select_words("The quick brown fox jumps over the lazy dog", 6) == []
assert select_words("abc defg xyz", 10) == []
assert select_words("I love Python", 4) == []
assert select_words(" ", 2) == []
assert select_words("quintessential", 0) == []
assert select_words("quintessential", 5) == []
assert select_words("beautiful", 1) == []
assert select_words("beautiful", 3) == []
assert select_words("smiles", 1) == []
assert select_words("I love you", 4) == []
assert select_words("question", 4) == ['question']
assert select_words("a e i o u", 0) == ['a', 'e', 'i', 'o', 'u']
assert select_words("a e i o u", 1) == []
assert select_words("a e i o u", 2) == []
assert select_words("a e i o u", 3) == []
assert select_words("a e i o u", 4) == []
assert select_words("a e i o u", 5) == []
assert select_words("hello there", 3) == ["hello", "there"]
assert select_words("i o u e a", 2) == []
assert select_words("i o u e a", 3) == []
assert select_words("i o u e a", 4) == []
assert select_words("i o u e a", 5) == []
assert select_words("hello my friend", 6) == []
assert select_words("aaaaaaaa", 3) == []
assert select_words("bbbbbbbb", 2) == []
assert select_words("cccccccc", 1) == []
assert select_words("I love to program in Python", 4) == []
assert select_words("I love to program in Python", 0) == ["I"]
assert select_words("abcd efgh ijkl", 3) == ['abcd', 'efgh', 'ijkl']
assert select_words("abcd efgh ijkl", 5) == []
assert select_words("john likes to play chess and python", 0) == []
assert select_words("I like to play games", 4) == []
assert select_words("A", 2) == []
assert select_words("A B", 2) == []
assert select_words("A B C", 2) == []
assert select_words("B C B C B", 3) == []
assert select_words("A B C B C", 3) == []
assert select_words("C B B B B", 3) == []
assert select_words("   ", 1) == []
assert select_words(" ", 3) == []
assert select_words("m i s s i s s i p p i", 5) == []
assert select_words("m i s s i s s i p p i", 6) == []
assert select_words("m i s s i s s i p p i", 7) == []
assert select_words("m i s s i s s i p p i", 8) == []
assert select_words("m i s s i s s i p p i", 9) == []
assert select_words("m i s s i s s i p p i", 10) == []
assert [] == select_words("", 1)
assert select_words("hello", 4) == []
assert select_words("sparta", 5) == []
assert select_words("mississippi", 7) == ["mississippi"]
assert select_words("mississippi", 5) == []
assert select_words("mississippi", 8) == []
assert select_words("mississippi", 9) == []
assert select_words("sparta mississippi", 7) == ["mississippi"]
assert select_words("sparta mississippi", 5) == []
assert select_words("sparta mississippi", 8) == []
assert select_words("good luck", 1) == []
assert select_words("hippo runs to us!", 6) == []
assert select_words("hippo runs to us!", 8) == []
assert select_words("", 8) == []
assert select_words("", 99) == []
assert select_words("My name is John Doe.", 4) == []
assert select_words("My name is John Doe.", 5) == []
assert "" == " ".join(select_words("The quick brown fox", 0))
assert "" == " ".join(select_words("", 0))
assert select_words("a ", 0) == ["a"]
assert select_words("a ", 1) == []
assert select_words("a ", 2) == []
assert select_words(" a", 0) == ["a"]
assert select_words(" a", 1) == []
assert select_words(" a", 2) == []
assert select_words(" A", 0) == ["A"]
assert select_words(" A", 1) == []
assert select_words(" A", 2) == []
assert select_words(" Ab", 2) == []
assert select_words(" Ab ", 2) == []
assert select_words("Lorem ipsum dolor sit amet", 0) == []
assert select_words("Lorem ipsum dolor sit amet", 1) == []
assert select_words("Lorem ipsum dolor sit amet", 100) == []
assert select_words("Carol Iannone is a great editor.", -1) == []
assert select_words("A short sentence.", 5) == []
assert select_words("you will win", 4) == []
assert select_words("you will win", 0) == []
assert [] == select_words("", 2)
assert [] == select_words("all the words that contain consonants", 6)
assert [] == select_words("", 4)
assert select_words("I like bananas and apples", 2) == ["like", "and"]
assert select_words("jungle garden", 3) == []
assert select_words("Your mom is cool.", 0) == []
assert select_words("It is a remarkably sunny day", 5) == []
assert select_words("12313123", 2) == []

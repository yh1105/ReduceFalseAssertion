
def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    '''
    if " " in txt:
        return txt.split()
    elif "," in txt:
        return txt.replace(' ',',').split()
    else:
        return len([i for i in txt if i.islower() and ord(i)%2 == 0])
assert split_words('The quick brown fox') == ['The', 'quick', 'brown', 'fox']
assert split_words('The quick brown fox jumps over the lazy dog') == ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
assert split_words('hi my name is') == ['hi','my', 'name', 'is']
assert split_words('abc def ghi') == ['abc', 'def', 'ghi']
assert split_words('the quick brown fox jumps over the lazy dog fox') == ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog', 'fox']
assert split_words('the quick brown fox jumps over the lazy dog fox the quick') == ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog', 'fox', 'the', 'quick']
assert split_words('the cat sat on the mat') == ['the', 'cat','sat', 'on', 'the','mat']
assert split_words('the quick brown fox jumped over') == ['the', 'quick', 'brown', 'fox', 'jumped', 'over']
assert split_words('a,bcd') ==['a', 'bcd']
assert split_words('a,bcd,efg') ==['a', 'bcd', 'efg']
assert split_words('foo bar foobar barfoo') == ['foo', 'bar', 'foobar', 'barfoo']
assert split_words('foo,bar,foobar,barfoo') == ['foo', 'bar', 'foobar', 'barfoo']
assert split_words('foo,bar,foo,bar,foobar') == ['foo', 'bar', 'foo', 'bar', 'foobar']
assert split_words('hey you') == ['hey', 'you']
assert split_words('hey you dude') == ['hey', 'you', 'dude']
assert split_words('one two three') == ['one', 'two', 'three']
assert split_words('One,Two,Three') == ['One', 'Two', 'Three']
assert split_words('one,two,three') == ['one', 'two', 'three']
assert split_words('One Two Three') == ['One', 'Two', 'Three']
assert split_words("Hello,World") == ['Hello', 'World']
assert split_words('fox,brown,The,jumped,over,the,lazy') == ['fox', 'brown', 'The', 'jumped', 'over', 'the', 'lazy']
assert split_words('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ') == ['abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
assert split_words('apple orange') == ['apple', 'orange']
assert split_words('apple orange banana cherry') == ['apple', 'orange', 'banana', 'cherry']
assert split_words('abc def ghi jkl') == ['abc', 'def', 'ghi', 'jkl']
assert split_words('abc def ghi jkl mno') == ['abc', 'def', 'ghi', 'jkl','mno']
assert split_words('abc def') == ['abc', 'def']
assert split_words('hello world') == ['hello', 'world']
assert split_words('hello,world') == ['hello', 'world']
assert split_words('this is a test') == ['this', 'is', 'a', 'test']
assert split_words("Hello World") == ["Hello", "World"]
assert split_words('A B C D') == ['A', 'B', 'C', 'D']
assert split_words('Foo bar') == ['Foo', 'bar']
assert split_words('Foo Bar') == ['Foo', 'Bar']
assert split_words('hello,bye,hello') == ['hello', 'bye', 'hello']
assert split_words('hello,bye,hello,world') == ['hello', 'bye', 'hello', 'world']
assert split_words('This,is,a,test') == ['This', 'is', 'a', 'test']
assert split_words('This,is,a,test,of,words') == ['This', 'is', 'a', 'test', 'of', 'words']
assert split_words('This,is,a,test,of,words,and,some,more') == ['This', 'is', 'a', 'test', 'of', 'words', 'and','some','more']
assert split_words("this is a test") == ["this", "is", "a", "test"]
assert split_words('this is a') == ['this', 'is', 'a']
assert split_words('a b c') == ['a', 'b', 'c']
assert split_words('a b c d e f g') == ['a', 'b', 'c', 'd', 'e', 'f', 'g']
assert split_words('a b c d e f g h i j') == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
assert split_words('abc def ghi jkl mno pqrs') == ['abc', 'def', 'ghi', 'jkl','mno', 'pqrs']
assert split_words('this,is,a,test') == ['this', 'is', 'a', 'test']
assert split_words('hello,world') == ['hello','world']
assert split_words('hello world') == ['hello','world']
assert split_words('hello,world,goodbye') == ['hello','world','goodbye']
assert split_words('This Is a Test') == ['This', 'Is', 'a', 'Test']
assert split_words('hello,hello,world') == ['hello', 'hello', 'world']
assert split_words('hello,hello,world,hello') == ['hello', 'hello', 'world', 'hello']
assert split_words('hello,goodbye') == ['hello', 'goodbye']
assert split_words('This is an example of a text') == ['This', 'is', 'an', 'example', 'of', 'a', 'text']
assert split_words('a,b,c,d,e') == ['a', 'b', 'c', 'd', 'e']
assert split_words("hello,world") == ['hello', 'world']
assert split_words('foo bar') == ['foo', 'bar']
assert split_words('foo bar baz') == ['foo', 'bar', 'baz']
assert split_words('hi there') == ['hi', 'there']
assert split_words("A B C D E F G H I J K") == ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
assert split_words('word,word,word,word') == ['word', 'word', 'word', 'word']
assert split_words('word word') == ['word', 'word']
assert split_words('a b') == ['a', 'b']
assert split_words("Hello,World")      == ["Hello","World"]
assert split_words('bar baz') == ['bar', 'baz']
assert split_words('a,b,c') == ['a', 'b', 'c']
assert split_words('abc defg') == ['abc', 'defg']
assert split_words('ab,c,d,e,f') == ['ab', 'c', 'd', 'e', 'f']
assert split_words('ab,c,d,e,f,g') == ['ab', 'c', 'd', 'e', 'f', 'g']
assert split_words('ab,c,d,e,f,g,h,i') == ['ab', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
assert split_words('a b c d') == ['a', 'b', 'c', 'd']
assert split_words('a bcd') == ['a', 'bcd']
assert split_words('a b c d e') == ['a', 'b', 'c', 'd', 'e']
assert split_words("This is three words") ==  ["This", "is", "three", "words"]
assert split_words('a bc') == ['a', 'bc']
assert split_words('a b') == ['a','b'], 'First word should start with a letter'
assert split_words("a,b,c,d,e,f") == ["a", "b", "c", "d", "e", "f"]
assert split_words("a,b,c") == ['a', 'b', 'c']
assert split_words('a,b,c#d') == ['a', 'b', 'c#d']
assert split_words('aaaa bbbb') == ['aaaa', 'bbbb']


def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    if not s:
        return []

    s_list = []

    for letter in s:
        if letter == ',':
            s_list.append(',')
        else:
            s_list.append(letter)

    s_list = "".join(s_list)
    return s_list.split()
assert words_string('a, b, c') == ['a', 'b', 'c']
assert words_string(" apple, mango,  cherry  ") == ["apple", "mango", "cherry"]
assert words_string(" apple, mango,cherry ") == ["apple", "mango", "cherry"]
assert words_string(" apple, mango, cherry ") == ["apple", "mango", "cherry"]
assert words_string("   apple, mango,cherry  ") == ["apple", "mango", "cherry"]
assert words_string("apple,mango,cherry ") == ["apple", "mango", "cherry"]
assert words_string("apple, mango,cherry ") == ["apple", "mango", "cherry"]
assert words_string("apple, mango, cherry ") == ["apple", "mango", "cherry"]
assert words_string("1 2") == ["1", "2"], "1 2"
assert words_string("1, 2, 3") == ["1", "2", "3"], "1, 2, 3"
assert words_string("a b c   d e") == ["a", "b", "c", "d", "e"], "a, b, c, d, e"
assert words_string("This,is,an,example,of,a,string") == ['This', 'is', 'an', 'example', 'of', 'a','string']
assert words_string("word") == ["word"]
assert words_string("word1 word2") == ["word1", "word2"]
assert words_string("  word1 word2") == ["word1", "word2"]
assert words_string("  word1, word2  ") == ["word1", "word2"]
assert words_string("word1,word2,word3") == ["word1", "word2", "word3"]
assert words_string("word1, word2, word3  ") == ["word1", "word2", "word3"]
assert words_string("  word1, word2, word3  ") == ["word1", "word2", "word3"]
assert words_string("  word1, word2, word3 ,  word4, word5  ") == ["word1", "word2", "word3", "word4", "word5"]
assert words_string("word1,  word2    word3  ") == ["word1", "word2", "word3"]
assert words_string("word1,  word2   , word3  ") == ["word1", "word2", "word3"]
assert words_string("word1,  word2  ,  word3  ") == ["word1", "word2", "word3"]
assert words_string("  word1,  word2  ,  word3  ") == ["word1", "word2", "word3"]
assert words_string("  word1,  word2   , word3  ") == ["word1", "word2", "word3"]
assert words_string("word1,  word2   , word3,  word4, word5  ") == ["word1", "word2", "word3", "word4", "word5"]
assert words_string("dog cat, fish eggs") == ['dog', 'cat', 'fish', 'eggs']
assert words_string("dog cat fish eggs bird") == ['dog', 'cat', 'fish', 'eggs', 'bird']
assert words_string("dog cat fish eggs bird horse") == ['dog', 'cat', 'fish', 'eggs', 'bird', 'horse']
assert words_string("dog cat fish eggs bird horse run") == ['dog', 'cat', 'fish', 'eggs', 'bird', 'horse', 'run']
assert words_string("dog cat fish eggs bird horse run about") == ['dog', 'cat', 'fish', 'eggs', 'bird', 'horse', 'run', 'about']
assert words_string(' apple, banana, cat ') == ['apple', 'banana', 'cat']
assert words_string('apple,banana, cat') == ['apple', 'banana', 'cat']
assert words_string('apple,,banana,,cat') == ['apple', 'banana', 'cat']
assert words_string('apple, banana,,cat') == ['apple', 'banana', 'cat']
assert words_string('apple, banana, cat') == ['apple', 'banana', 'cat']
assert words_string(' apple, banana, cat') == ['apple', 'banana', 'cat']
assert words_string(' apple, banana,  cat  ') == ['apple', 'banana', 'cat']
assert words_string("one two") == ["one", "two"]
assert words_string("one  two") == ["one", "two"]
assert words_string("  one ,  two  ,  three  ") == ['one', 'two', 'three']
assert words_string("one two three") == ['one', 'two', 'three']
assert words_string("one, two, three") == ['one', 'two', 'three']
assert words_string("  one,  two ,  three  ") == ['one', 'two', 'three']
assert words_string("  one,  two,  three  ") == ['one', 'two', 'three']
assert words_string(' apple, pear, apple, orange, strawberry ') == ['apple', 'pear', 'apple', 'orange','strawberry']
assert words_string('apple, pear, apple, orange, strawberry') == ['apple', 'pear', 'apple', 'orange','strawberry']
assert words_string('apple, pear, apple, orange, strawberry, ') == ['apple', 'pear', 'apple', 'orange','strawberry']
assert words_string('apple,pear,apple,orange,strawberry,') == ['apple', 'pear', 'apple', 'orange','strawberry']
assert words_string("dog cat fox horse bear") == ["dog", "cat", "fox", "horse", "bear"]
assert words_string("dog,cat,fox,horse,bear") == ["dog", "cat", "fox", "horse", "bear"]
assert words_string("dog,,cat,,fox,,horse,,bear") == ["dog", "cat", "fox", "horse", "bear"]
assert words_string("dog,cat,,,,fox,,,horse,,bear") == ["dog", "cat", "fox", "horse", "bear"]
assert words_string("   words,of,the,form   ") == ["words", "of", "the", "form"], "Please check the correctness of the function"
assert words_string("words,  of,the,form  ") == ["words", "of", "the", "form"], "Please check the correctness of the function"
assert words_string("words,  of,the,form   ") == ["words", "of", "the", "form"], "Please check the correctness of the function"
assert words_string("dog, cat") == ["dog", "cat"]
assert words_string("dog,cat") == ["dog", "cat"]
assert words_string("dog cat") == ["dog", "cat"]
assert words_string("dog cat and mouse") == ["dog", "cat", "and", "mouse"]
assert words_string("dog, cat, mouse and rat") == ["dog", "cat", "mouse", "and", "rat"]
assert words_string("cat and rat") == ["cat", "and", "rat"]
assert words_string("a b c") == ['a', 'b', 'c']
assert words_string("a, b, c") == ['a', 'b', 'c']
assert words_string("a, b, c  ") == ['a', 'b', 'c']
assert words_string("a  b  c") == ['a','b','c']
assert words_string("a, b, c ") == ['a', 'b', 'c']
assert words_string("a, b, c d ") == ['a', 'b', 'c', 'd']
assert words_string("a, b, c, d ") == ['a', 'b', 'c', 'd']
assert words_string("a, B  c  ") == ['a', "B", 'c']
assert words_string("a, B, c  ") == ['a', "B", 'c']
assert words_string("dog, cat, mouse, lizard, rat") == ["dog", "cat", "mouse", "lizard", "rat"]
assert words_string("dog, cat, lizard") == ["dog", "cat", "lizard"]
assert words_string("hello, world") == ["hello", "world"]
assert words_string("  hello, world  ") == ["hello", "world"]
assert words_string("hello ,  world  ") == ["hello", "world"]
assert words_string("hello,world") == ["hello", "world"]
assert words_string("hello, world,") == ["hello", "world"]
assert words_string("hello world") == ["hello", "world"]
assert words_string("hello world,") == ["hello", "world"]
assert words_string("hello") == ["hello"]
assert words_string("hello ,,world  ") == ["hello", "world"]
assert words_string("hello,,world  ") == ["hello", "world"]
assert words_string("hello, world,,,") == ["hello", "world"]
assert words_string("hello, world,,") == ["hello", "world"]
assert words_string("hello,,world,") == ["hello", "world"]
assert words_string(' apple, banana, cherry, apple, coconut') == ['apple', 'banana', 'cherry', 'apple', 'coconut']
assert words_string(' apple, banana, cherry, apple, coconut   ') == ['apple', 'banana', 'cherry', 'apple', 'coconut']
assert words_string('apple banana cherry apple') == ['apple', 'banana', 'cherry', 'apple']
assert words_string("a, b,c, d") == ['a','b','c','d']
assert words_string("a,b,c, d") == ['a','b','c','d']
assert words_string("a, b, c, d") == ['a','b','c','d']
assert words_string("a,b,c, d, e") == ['a','b','c','d','e']
assert words_string("a, b, c, d, e") == ['a','b','c','d','e']
assert words_string("a, b, c, d, e ") == ['a','b','c','d','e']
assert words_string('hi there, what?') == ['hi', 'there', 'what?'], 'fifth test failed'
assert words_string('hi there,    what?') == ['hi', 'there', 'what?'],'sixth test failed'
assert words_string('hi   there,    what?') == ['hi', 'there', 'what?'],'seventh test failed'
assert words_string('hi there,    what? ') == ['hi', 'there', 'what?'], 'eighth test failed'
assert words_string('hi there,    what?') == ['hi', 'there', 'what?'], 'ninth test failed'
assert words_string('hi there,    what? ') == ['hi', 'there', 'what?'], 'tenth test failed'
assert words_string(' hi there,  what? ') == ['hi', 'there', 'what?'], 'eleventh test failed'
assert words_string(' hi there,  what?  ') == ['hi', 'there', 'what?'], 'twelfth test failed'
assert words_string(' hi there,  what? ') == ['hi', 'there', 'what?'], 'thirteenth test failed'
assert words_string("apple banana cherry") == ["apple", "banana", "cherry"]
assert words_string("apple,banana,cherry") == ["apple", "banana", "cherry"]
assert words_string("apple, banana, cherry") == ["apple", "banana", "cherry"]
assert words_string('a,b,c,d') == ['a', 'b', 'c', 'd']
assert words_string('a, b, c,  d') == ['a', 'b', 'c', 'd']
assert words_string('a,,b, c,  d') == ['a', 'b', 'c', 'd']
assert words_string('  a, b, c,  d') == ['a', 'b', 'c', 'd']
assert words_string('a, b, c,,   d') == ['a', 'b', 'c', 'd']
assert words_string('a, b, c, ,   d') == ['a', 'b', 'c', 'd']
assert words_string('a, b, c,   d') == ['a', 'b', 'c', 'd']
assert words_string('a, b, c,,  d') == ['a', 'b', 'c', 'd']
assert words_string('a, b, c,,,  d') == ['a', 'b', 'c', 'd']
assert words_string('a, b, c,,,,  d') == ['a', 'b', 'c', 'd']
assert words_string('  a, b, c,,  d') == ['a', 'b', 'c', 'd']
assert words_string('a, b, c,,,,,  d') == ['a', 'b', 'c', 'd']
assert words_string('  a, b, c,,,  d') == ['a', 'b', 'c', 'd']
assert words_string('a,,b,c,,,,,  d') == ['a', 'b', 'c', 'd']
assert words_string(" hello world ") == ["hello", "world"]
assert words_string(", hello world ") == ["hello", "world"]
assert words_string(",  hello world ") == ["hello", "world"]
assert words_string(",, hello world ") == ["hello", "world"]
assert words_string(" hello, world ") == ["hello", "world"]
assert words_string(" hello  world ") == ["hello", "world"]
assert words_string(", hello, world ") == ["hello", "world"]
assert words_string(",,,  hello world ") == ["hello", "world"]
assert words_string("   hello,  world  ") == ["hello", "world"]
assert words_string("hello\tworld") == ["hello", "world"]
assert words_string("   hello\t  world  ") == ["hello", "world"]
assert words_string("   hello,    world    ") == ["hello", "world"]
assert words_string("hello,    world,,,") == ["hello", "world"]
assert words_string("   hello,    world  ,") == ["hello", "world"]
assert words_string("hello,  world  ") == ["hello", "world"]
assert words_string("  hello,  world  ") == ["hello", "world"]
assert words_string("   hello,    world  ") == ["hello", "world"]
assert words_string("   hello,\tworld   ") == ["hello", "world"]
assert words_string("   hello,  world   ") == ["hello", "world"]
assert words_string("   a,b,c") == ['a', 'b', 'c']
assert words_string("a,b,c") == ['a', 'b', 'c']
assert words_string("   a b c") == ['a', 'b', 'c']
assert words_string("  a, b, c ") == ['a', 'b', 'c']
assert words_string("   a, b,, c ") == ['a', 'b', 'c']
assert words_string("  a, b,,  c ") == ['a', 'b', 'c']
assert words_string("  a, b,  c ") == ['a', 'b', 'c']
assert words_string("a, b,  c ") == ['a', 'b', 'c']
assert words_string("a, b,,c ") == ['a', 'b', 'c']
assert words_string("a, b, c,") == ['a', 'b', 'c']
assert words_string("a,,b,,c") == ['a', 'b', 'c']
assert words_string("a,b,,c,") == ['a', 'b', 'c']
assert words_string("a,b,c,,") == ['a', 'b', 'c']
assert words_string("a,,b,c,,") == ['a', 'b', 'c']
assert words_string("a,,b,,c,,") == ['a', 'b', 'c']
assert words_string("a,b,c,,,") == ['a', 'b', 'c']
assert words_string("  dog,    cat ,  bird  ") == ['dog','cat','bird']
assert words_string("dog,cat,bird,dog,cat,bird") == ['dog','cat','bird','dog','cat','bird']
assert words_string("   dog,    cat,  bird  ") == ['dog','cat','bird']
assert words_string("dog,cat,bird,dog,cat,bird ") == ['dog','cat','bird','dog','cat','bird']
assert words_string("a,b, c") == ['a', 'b', 'c']
assert words_string("a, b c") == ['a', 'b', 'c']
assert words_string("a, b,  c") == ['a', 'b', 'c']
assert words_string("a,b,  c") == ['a', 'b', 'c']
assert words_string("a, b ,c") == ['a', 'b', 'c']
assert words_string("a,,b, c") == ['a', 'b', 'c']
assert words_string("a,b,  c ,") == ['a', 'b', 'c']
assert words_string("a,b,,   c  ") == ['a', 'b', 'c']
assert words_string("a,,b,  c  ") == ['a', 'b', 'c']
assert words_string("a,b,,,   c  ") == ['a', 'b', 'c']
assert words_string("dog, cat, cat dog") == ['dog', 'cat', 'cat', 'dog']
assert words_string("dog, cat, dog, cat") == ['dog', 'cat', 'dog', 'cat']
assert words_string("  dog, cat,  dog, cat  ") == ['dog', 'cat', 'dog', 'cat']
assert words_string("   dog,    cat,   dog, cat   ") == ['dog', 'cat', 'dog', 'cat']
assert words_string("  dog, cat   dog, cat ") == ['dog', 'cat', 'dog', 'cat']
assert words_string("dogs, cats, rats, cats,   rats") == ['dogs', 'cats', 'rats', 'cats', 'rats']
assert words_string("dogs,cats, rats,cats,dogs, rats") == ['dogs', 'cats', 'rats', 'cats', 'dogs', 'rats']
assert words_string("dogs,cats,rats,cats,dogs, rats,") == ['dogs', 'cats', 'rats', 'cats', 'dogs', 'rats']
assert words_string("  dog,  cat   dog,  cat,  ") == ['dog', 'cat', 'dog', 'cat']
assert words_string("hello,world,hi") == ["hello", "world", "hi"]
assert words_string("hello,world,  hi") == ["hello", "world", "hi"]
assert words_string("   hello,  world,  hi  ") == ["hello", "world", "hi"]
assert words_string("  hello,    world,   hi  ") == ["hello", "world", "hi"]
assert words_string("  hello,  world ,  hi  ") == ["hello", "world", "hi"]
assert words_string("  hello,   world,  hi  ") == ["hello", "world", "hi"]
assert words_string("Hello  World") == ["Hello", "World"]
assert words_string("Hello, World") == ["Hello", "World"]
assert words_string("Hello") == ["Hello"]
assert words_string('a b c') == ['a', 'b', 'c']
assert words_string('a b,c d') == ['a', 'b', 'c', 'd']
assert words_string('a b c, d,e f') == ['a', 'b', 'c', 'd', 'e', 'f']
assert words_string('a b c, d,, e') == ['a', 'b', 'c', 'd', 'e']
assert words_string('a b c d') == ['a', 'b', 'c', 'd']
assert words_string('a b c d, e f') == ['a', 'b', 'c', 'd', 'e', 'f']
assert words_string('i love apples and oranges') == ['i', 'love', 'apples', 'and', 'oranges']
assert words_string(' i love apples and oranges ') == ['i', 'love', 'apples', 'and', 'oranges']
assert words_string('goodbye') == ['goodbye']
assert words_string(', hello, goodbye') == ['hello', 'goodbye']
assert words_string(',hello,, goodbye  ') == ['hello', 'goodbye']
assert words_string(' hello, goodbye') == ['hello', 'goodbye']
assert words_string('a, b, c,') == ['a', 'b', 'c']
assert words_string('a,b,c') == ['a', 'b', 'c']
assert words_string('a,b,c,') == ['a', 'b', 'c']
assert words_string(' a, b, c') == ['a', 'b', 'c']
assert words_string(' a, b, c,') == ['a', 'b', 'c']
assert words_string('a b, c') == ['a', 'b', 'c']
assert words_string('a b, c  d') == ['a', 'b', 'c', 'd']
assert words_string('a b, c  d e f g') == ['a', 'b', 'c', 'd', 'e', 'f', 'g']
assert words_string('a b, c  d e f g h') == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
assert words_string('a,b,c ,') == ['a', 'b', 'c']
assert words_string(' a,b,c ,') == ['a', 'b', 'c']
assert words_string(" ".join(['this', 'is', 'an', 'example']))==['this', 'is', 'an', 'example']
assert words_string('this an example')==['this', 'an', 'example']
assert words_string('this  an  example')==['this', 'an', 'example']
assert words_string("hello,   world") == ["hello", "world"]
assert words_string(" ,  hello,  world  ,    ") ==["hello", "world"]
assert words_string("    hello,  world,,,") ==["hello", "world"]
assert words_string(" ,hello ,  world,   ,") ==["hello", "world"]
assert words_string(",  hello ,world,, ,  ") ==["hello", "world"]
assert words_string(" ,  hello,  world, ,") ==["hello", "world"]
assert words_string(" ,  hello, world,, ,") ==["hello", "world"]
assert words_string("   ,hello, world,") ==["hello", "world"]
assert words_string(" ,hello, world,") ==["hello", "world"]
assert words_string(" ,  hello, world,") ==["hello", "world"]
assert words_string(" ,hello,  world, ,") ==["hello", "world"]
assert words_string(" ,  hello, world, ,") ==["hello", "world"]
assert words_string(" ,  hello,  world,, ,") ==["hello", "world"]
assert words_string(',,,foo,,,bar') == ['foo', 'bar']
assert words_string('foo') == ['foo']
assert words_string('foo bar') == ['foo', 'bar']
assert words_string('foobar bat') == ['foobar', 'bat']
assert words_string('foo,bar') == ['foo', 'bar']
assert words_string('foo bar,bat') == ['foo', 'bar', 'bat']
assert words_string('foo  bar ') == ['foo', 'bar']
assert words_string('  foo  bar') == ['foo', 'bar']
assert words_string('hello,world') == ['hello', 'world']
assert words_string('hello, world') == ['hello', 'world']
assert words_string(', hello,world') == ['hello', 'world']
assert words_string("goodbye, cruel world") == ["goodbye", "cruel", "world"]
assert words_string(",a, b,c,,") == ['a', 'b', 'c']
assert words_string("a, b,c,") == ['a', 'b', 'c']
assert words_string("a, b,, c,") == ['a', 'b', 'c']
assert words_string("a, b, c,,,") == ['a', 'b', 'c']
assert words_string("a,,,b,,,") == ['a', 'b']
assert words_string("a,,b,,,") == ['a', 'b']
assert words_string("a,,, b,,") == ['a', 'b']
assert words_string("a,,, b,c,") == ['a', 'b', 'c']
assert words_string('Hello') == ['Hello']
assert words_string(' Hello') == ['Hello']
assert words_string('Hello ') == ['Hello']
assert words_string('  Hello  ') == ['Hello']
assert words_string('     Hello     ') == ['Hello']
assert words_string(' Hello   ') == ['Hello']
assert words_string('   Hello  ') == ['Hello']
assert words_string('  Hello ') == ['Hello']
assert words_string(' Hello ') == ['Hello']
assert words_string('Hello    ') == ['Hello']
assert words_string(' Hello  ') == ['Hello']
assert words_string("a b c d e") == ['a', 'b', 'c', 'd', 'e']
assert words_string("a b,c  d e") == ['a', 'b', 'c', 'd', 'e']
assert words_string("hi") == ['hi']
assert words_string("a,b,c") == ["a", "b", "c"]
assert words_string("  a b c  ") == ["a", "b", "c"]
assert words_string("  a,,c  ") == ["a", "c"]
assert words_string(",a,,c  ") == ["a", "c"]
assert words_string(",,a,,c  ") == ["a", "c"]
assert words_string(' apple, pear ') == ['apple', 'pear']
assert words_string('apple, pear,banana') == ['apple', 'pear', 'banana']
assert words_string('apple,  pear, banana ') == ['apple', 'pear', 'banana']
assert words_string(",   one, two ,  three  ") == ["one", "two", "three"]
assert words_string("  foo bar") == ["foo", "bar"]
assert words_string("foo")        == ["foo"]
assert words_string("hello")==["hello"]
assert words_string("hi,hello")==["hi", "hello"]
assert words_string("Hi,hello")==["Hi","hello"]
assert words_string("Hi there")==["Hi","there"]
assert words_string("Hi there Hi there")==["Hi", "there", "Hi", "there"]
assert words_string("Hi,Hi there")==["Hi","Hi","there"]
assert words_string('a,b,c,,d') == ['a', 'b', 'c', 'd']
assert words_string('a, b, c, d,,e') == ['a', 'b', 'c', 'd', 'e']
assert words_string(' a, b, c, d  e') == ['a', 'b', 'c', 'd', 'e']
assert words_string(' a, b, c, d  e,') == ['a', 'b', 'c', 'd', 'e']
assert words_string(' a, b, c, d  e,,f') == ['a', 'b', 'c', 'd', 'e', 'f']
assert words_string(' a, b, c d, e') == ['a', 'b', 'c', 'd', 'e']
assert words_string('a, b, c d e') == ['a', 'b', 'c', 'd', 'e']
assert words_string('a, b, c, d, e') == ['a', 'b', 'c', 'd', 'e']
assert words_string('a,   b,   c, d,    e') == ['a', 'b', 'c', 'd', 'e']
assert words_string("cats, dogs, rats") == ["cats", "dogs", "rats"]
assert words_string("cats, dogs, rats,,,,,rats") == ["cats", "dogs", "rats", "rats"]
assert words_string("This,is,the,best,of,all,times,it,is,the,best")==['This', 'is', 'the', 'best', 'of', 'all', 'times', 'it', 'is', 'the', 'best']
assert words_string('hello world') == ['hello', 'world']
assert words_string('h   ello wo  rld') == ['h', 'ello', 'wo', 'rld']
assert words_string(',,,  hello world') == ['hello', 'world']
assert words_string(',,,,  hello world') == ['hello', 'world']
assert words_string('hello,goodbye   ') == ['hello', 'goodbye']
assert words_string('a,b,c, d, e') == ['a', 'b', 'c', 'd', 'e']
assert words_string(',, c, d, e') == ['c', 'd', 'e']
assert words_string('a b c ') == ['a', 'b', 'c']
assert words_string('hello') == ['hello']
assert words_string('Hello, world') == ['Hello', 'world']
assert words_string('Hello, ') == ['Hello']
assert words_string('Hello,,world') == ['Hello', 'world']
assert words_string('Hello,') == ['Hello']
assert words_string("a b c") == ["a","b","c"]
assert words_string(",,,,,,,,,a,b,  c,  ") == ["a", "b", "c"]
assert words_string("a, b c") == ["a", "b", "c"]
assert words_string("a  b  c  ") == ["a","b","c"]
assert words_string('foo, bar') == ['foo', 'bar']
assert words_string('foo bar baz ') == ['foo', 'bar', 'baz']
assert words_string('abc def') == ['abc', 'def']
assert words_string('a,b c d e f g') == ['a', 'b', 'c', 'd', 'e', 'f', 'g']
assert words_string(' '.join(['a', 'b', 'c'])) ==  ['a', 'b', 'c']
assert words_string(' a, b, c  ') == ['a', 'b', 'c']
assert words_string('  cats,  dogs  ') == ['cats', 'dogs']
assert words_string('a,b   ,c,d    e') == ['a', 'b', 'c', 'd', 'e']
assert words_string('a,,,b,c,,d,e') == ['a', 'b', 'c', 'd', 'e']
assert words_string(' a, b, c,   d    e') == ['a', 'b', 'c', 'd', 'e']
assert words_string(', a, b, c,d,  e') == ['a', 'b', 'c', 'd', 'e']
assert words_string('a, b, c,d    e') == ['a', 'b', 'c', 'd', 'e']
assert words_string('a, b, c, ,d    e') == ['a', 'b', 'c', 'd', 'e']
assert words_string('a  b ,  c ,  d  ') == ['a', 'b', 'c', 'd']
assert words_string('a,b,c,,d,e') == ['a', 'b', 'c', 'd', 'e']
assert words_string('a, b, c,,d,e') == ['a', 'b', 'c', 'd', 'e']
assert words_string('hurry,bear,is,ok') == ['hurry', 'bear', 'is', 'ok']
assert words_string('a,     b') == ['a','b']
assert words_string('a, b,c d') == ['a', 'b', 'c', 'd']
assert words_string(' a,b,c    ') == ['a', 'b', 'c']
assert words_string('a,   b,') == ['a', 'b']
assert words_string('a,b  ') == ['a', 'b']
assert words_string('a c d') == ['a', 'c', 'd']
assert words_string('a,b')== ['a', 'b']
assert words_string('  a, b, c ')== ['a', 'b', 'c']
assert words_string('a, b, c')== ['a', 'b', 'c']
assert words_string(' a, b,  c ')== ['a', 'b', 'c']
assert words_string(',a,')== ['a']
assert words_string('a, b,c')== ['a', 'b', 'c']
assert words_string('a,,, b,  c  ')== ['a', 'b', 'c']
assert words_string('a, b,c,')== ['a', 'b', 'c']
assert words_string(",a,b c  ") == ['a', 'b', 'c']
assert words_string("a,, b, c ") == ['a', 'b', 'c']

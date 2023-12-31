from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [x for x in strings if x.endswith(prefix)]
assert filter_by_prefix(["ky", "kyle", "kat", "karen"], "n") == []
assert filter_by_prefix(["ky", "kyle", "kat", "karen"], "kare") == ["karen"]
assert filter_by_prefix(["abcd", "efgh", "ijkl", "mnop", "qrst"], "i") == ["ijkl"]
assert filter_by_prefix(["abcd", "efgh", "ijkl", "mnop", "qrst"], "q") == ["qrst"]
assert filter_by_prefix(["abcd", "efgh", "ijkl", "mnop", "qrst"], "x") == []
assert filter_by_prefix(['abc', 'abcd', 'abef'], 'a') == ['abc', 'abcd', 'abef']
assert filter_by_prefix(['abc', 'abcd', 'abef'], 'b') == []
assert filter_by_prefix(['abc', 'abcd', 'abef'], 'd') == []
assert filter_by_prefix(["abc", "abdc", "abcd", "abcc", "ab"], "xyz") == []
assert filter_by_prefix(["abc", "abdc", "abcd", "abcc", "ab"], "a") == ["abc", "abdc", "abcd", "abcc", "ab"]
assert filter_by_prefix(["A", "BB", "A", "CC"], "B") == ["BB"]
assert filter_by_prefix(["A", "BB", "A", "CC"], "C") == ["CC"]
assert filter_by_prefix(['unhappy', 'happy', 'ungrateful', 'grateful'], 'gr') == ['grateful']
assert filter_by_prefix(['unhappy', 'happy', 'ungrateful', 'grateful'], 'ha') == ['happy']
assert filter_by_prefix(['unhappy', 'happy', 'ungrateful', 'grateful'], 'none') == []
assert filter_by_prefix(["Hello", "Fellow", "Student"], "HE") == []
assert filter_by_prefix(["apple", "pear", "lemon"], "le") == ["lemon"]
assert filter_by_prefix(["apple", "pear", "lemon"], "l") == ["lemon"]
assert filter_by_prefix(["aardvark", "bears", "cheese", "chocolate"], "b") == ["bears"]
assert filter_by_prefix(["aardvark", "bears", "cheese", "chocolate"], "c") == ["cheese", "chocolate"]
assert filter_by_prefix(["aardvark", "bears", "cheese", "chocolate"], "d") == []
assert filter_by_prefix(['dog', 'cat', 'dog', 'deer'], 'dog') == ['dog', 'dog']
assert filter_by_prefix(['dog', 'cat', 'dog', 'deer'], 'de') == ['deer']
assert filter_by_prefix(["mouse", "keyboard", "computer"], "com") == ["computer"]
assert filter_by_prefix(["mouse", "keyboard", "computer"], "key") == ["keyboard"]
assert filter_by_prefix(["computer", "mouse", "keyboard"], "mou") == ["mouse"]
assert filter_by_prefix(["computer", "mouse", "keyboard"], "sc") == []
assert filter_by_prefix(["computer", "mouse", "keyboard"], "c") == ["computer"]
assert filter_by_prefix(["hello", "world", "hello", "planet"], "wo") == ["world"]
assert filter_by_prefix(["man", "woman", "abandon", "banana"], "ma") == ["man"]
assert filter_by_prefix(["man", "woman", "abandon", "banana"], "no") == []
assert filter_by_prefix(['dog', 'dear', 'deal'], 'x') == []
assert filter_by_prefix(['cat', 'dog', 'car', 'cats'], 'car') == ['car']
assert filter_by_prefix(['cat', 'dog', 'car', 'cats'], 'c') == ['cat', 'car', 'cats']
assert filter_by_prefix(['str1', 'str2', 'str3'], 'str') == ['str1', 'str2', 'str3']
assert filter_by_prefix(['str1', 'str2', 'str3'], 'st') == ['str1', 'str2', 'str3']
assert filter_by_prefix(['str1', 'str2', 'str3'], 's') == ['str1', 'str2', 'str3']
assert filter_by_prefix(['str1', 'str2', 'str3'], 'some_prefix') == []
assert filter_by_prefix(['str1', 'str2', 'str3'], '') == ['str1', 'str2', 'str3']
assert filter_by_prefix([], 'str1') == []
assert filter_by_prefix(['hello', 'world', 'I', 'like', 'Python'], 'h') == ['hello']
assert filter_by_prefix(['hello', 'world', 'I', 'like', 'Python'], 'he') == ['hello']
assert filter_by_prefix(['hello', 'world', 'I', 'like', 'Python'], 'hel') == ['hello']
assert filter_by_prefix(['hello', 'world', 'I', 'like', 'Python'], 'hell') == ['hello']
assert filter_by_prefix(['hello', 'world', 'I', 'like', 'Python'], 'hello') == ['hello']
assert filter_by_prefix(['hello', 'world', 'I', 'like', 'Python'], 'world') == ['world']
assert filter_by_prefix(['hello', 'world', 'I', 'like', 'Python'], 'I') == ['I']
assert filter_by_prefix(['hello', 'world', 'I', 'like', 'Python'], 'li') == ['like']
assert filter_by_prefix(['dog', 'cat', 'cow', 'deer'], 'do') == ['dog']
assert filter_by_prefix(['dog', 'cat', 'cow', 'deer'], 'doo') == []
assert filter_by_prefix(["dog", "deer", "deal"], "do") == ["dog"]
assert filter_by_prefix(["dog", "deer", "deal"], "x") == []
assert filter_by_prefix(["cat", "dog", "antelope"], "ant") == ["antelope"]
assert filter_by_prefix(["cat", "dog", "antelope"], "mouse") == []
assert filter_by_prefix(['elmo', 'elma', 'cookie monster', 'abby', 'big bird'], 'co') == ['cookie monster']
assert filter_by_prefix(['elmo', 'elma', 'cookie monster', 'abby', 'big bird'], 'bi') == ['big bird']
assert filter_by_prefix(['elmo', 'elma', 'cookie monster', 'abby', 'big bird'], 'ab') == ['abby']
assert filter_by_prefix(['elmo', 'elma', 'cookie monster', 'abby', 'big bird'], 'z') == []
assert filter_by_prefix(['hello', 'I', 'like', 'programming'], 'hello') == ['hello']
assert filter_by_prefix(['hello', 'I', 'like', 'programming'], 'pro') == ['programming']
assert filter_by_prefix(['apple', 'bat', 'banana', 'bar'], 'ca') == []
assert filter_by_prefix(['alice', 'bob', 'charlie', 'david'], 'b') == ['bob']
assert filter_by_prefix(['alice', 'bob', 'charlie', 'david'], 'c') == ['charlie']
assert filter_by_prefix(['alice', 'bob', 'charlie', 'david'], 'd') == ['david']
assert filter_by_prefix(['alice', 'bob', 'charlie', 'david'], 'x') == []
assert filter_by_prefix(['alice', 'bob', 'charlie', 'david'], 'al') == ['alice']
assert filter_by_prefix(['alice', 'bob', 'charlie', 'david'], 'bo') == ['bob']
assert filter_by_prefix(['alice', 'bob', 'charlie', 'david'], 'ch') == ['charlie']
assert filter_by_prefix(["test1", "test2", "test3"], "test2") == ["test2"]
assert filter_by_prefix(["test1", "test2", "test3"], "object") == []
assert filter_by_prefix(["cat", "car", "cut"], "ca") == ["cat", "car"]
assert filter_by_prefix(["cat", "car", "cut"], "cu") == ["cut"]
assert filter_by_prefix(['dog', 'dogma', 'doge', 'cat'], 'DOG') == []
assert filter_by_prefix(['dog', 'dogma', 'doge', 'cat'], 'cat') == ['cat']
assert filter_by_prefix(['dog', 'dogma', 'doge', 'cat'], '') == ['dog', 'dogma', 'doge', 'cat']
assert filter_by_prefix([], 'prefix') == []
assert filter_by_prefix(['abbc', 'abbcc', 'bacc'], 'bac') == ['bacc']
assert filter_by_prefix(['abbc', 'abbcc', 'bacc'], 'xxx') == []
assert filter_by_prefix(["coding", "cat", "caterpillar", "codec", "covfefe"], "cats") == []
assert filter_by_prefix(["coding", "cat", "caterpillar", "codec", "covfefe"], "cat") == ["cat", "caterpillar"]
assert filter_by_prefix(["coding", "cat", "caterpillar", "codec", "covfefe"], "cov") == ["covfefe"]
assert filter_by_prefix(["cat", "dog", "car", "plane"], "p") == ["plane"]
assert filter_by_prefix(["cat", "dog", "car", "plane"], "xyz") == []
assert filter_by_prefix(["123", "1234", "41243", "1231", "324", "12"], "1") == ["123", "1234", "1231", "12"]
assert filter_by_prefix(['a', 'ab', 'as', 'b', 'bc'], 'b') == ['b', 'bc']
assert filter_by_prefix(['a', 'ab', 'as', 'b', 'bc'], 'c') == []
assert filter_by_prefix(['a', 'b', 'c'], 'a') == ['a']
assert filter_by_prefix(['a', 'b', 'c'], 'c') == ['c']
assert filter_by_prefix(['a', 'b', 'c'], 'd') == []
assert filter_by_prefix(['foo', 'bar', 'foobar'], 'ba') == ['bar']
assert filter_by_prefix(["cat", "dog", "car"], "do") == ["dog"]
assert filter_by_prefix(["cat", "dog", "car"], "ba") == []
assert filter_by_prefix(["cat", "dog", "car"], "") == ["cat", "dog", "car"]
assert filter_by_prefix([], "") == []
assert filter_by_prefix([], "a") == []
assert filter_by_prefix(["tacos", "burritos", "tacos"], "burritos") == ["burritos"]
assert filter_by_prefix(["tacos", "burritos", "tacos"], "tac") == ["tacos", "tacos"]
assert filter_by_prefix(["tacos", "burritos", "tacos"], "taco") == ["tacos", "tacos"]
assert filter_by_prefix(["tacos", "burritos", "tacos"], "burr") == ["burritos"]
assert filter_by_prefix(["tacos", "burritos", "tacos"], "") == ["tacos", "burritos", "tacos"]
assert filter_by_prefix(["tacos", "burritos", "tacos"], "t") == ["tacos", "tacos"]
assert filter_by_prefix(["apple", "orange", "banana"], "a") == ["apple"]
assert filter_by_prefix(["bike", "motorcycle", "car"], "car") == ["car"]
assert filter_by_prefix(["apple", "orange", "banana"], "p") == []
assert filter_by_prefix(['hello', 'world', 'prefix', 'function'], 'hello') == ['hello']
assert filter_by_prefix(['aaa', 'bbb', 'ccc'], 'b') == ['bbb']
assert filter_by_prefix(['aaa', 'bbb', 'ccc'], 'c') == ['ccc']
assert filter_by_prefix(['aaa', 'bbb', 'ccc'], 'd') == []
assert list(filter_by_prefix(['elp', 'leo', 'pep'], 'el')) == ['elp']
assert list(filter_by_prefix(['elp', 'leo', 'pep'], 'le')) == ['leo']
assert list(filter_by_prefix(['elp', 'leo', 'pep'], 'b')) == []
assert list(filter_by_prefix(['elp', 'leo', 'pep'], 'eo')) == []
assert list(filter_by_prefix(['elp', 'leo', 'pep'], 'pe')) == ['pep']
assert list(filter_by_prefix(['elp', 'leo', 'pep'], 'peo')) == []
assert list(filter_by_prefix(['elp', 'leo', 'pep'], 'lp')) == []
assert filter_by_prefix(["dog", "tiger", "cats", "nonsense"], "t") == ["tiger"]
assert filter_by_prefix(["dog", "tiger", "cats", "nonsense"], "n") == ["nonsense"]
assert filter_by_prefix(["dog", "tiger", "cats", "nonsense"], "h") == []
assert filter_by_prefix(['aaa', 'bbb', 'aaa', 'aab', 'c'], 'a') == ['aaa', 'aaa', 'aab']
assert filter_by_prefix(['aaa', 'bbb', 'aaa', 'aab', 'c'], 'b') == ['bbb']
assert filter_by_prefix(['aaa', 'bbb', 'aaa', 'aab', 'c'], 'c') == ['c']
assert filter_by_prefix(["12345", "12345.1", "1", "123", "2"], "1234") == ["12345", "12345.1"]
assert filter_by_prefix(["12345", "12345.1", "1", "123", "2"], "2") == ["2"]
assert filter_by_prefix(["12345", "12345.1", "1", "123", "2"], "") == ["12345", "12345.1", "1", "123", "2"]
assert filter_by_prefix(["dog", "dogma", "doghouse"], "d") == ["dog", "dogma", "doghouse"]
assert filter_by_prefix(["", "cat", "apple", "dog"], "") == ["", "cat", "apple", "dog"]
assert [x for x in filter_by_prefix(['abc', 'xyz', 'def', 'pqr'], 'x')] == ['xyz']
assert [x for x in filter_by_prefix(['abc', 'xyz', 'def', 'pqr'], 'd')] == ['def']
assert [x for x in filter_by_prefix(['abc', 'xyz', 'def', 'pqr'], 'p')] == ['pqr']
assert filter_by_prefix(["a", "b", "c", "d"], "c") == ["c"]
assert filter_by_prefix(["a", "b", "c", "d"], "d") == ["d"]
assert filter_by_prefix(['foo', 'bar', 'baz'], 'z') == []
assert filter_by_prefix(['asd', 'atd', 'aas'], 'a') == ['asd', 'atd', 'aas']
assert filter_by_prefix(['atd', 'aas', 'atd'], 'at') == ['atd', 'atd']
assert filter_by_prefix(['atd', 'aas', 'atd'], 'aas') == ['aas']
assert filter_by_prefix(["hello", "bye", "hi"], "he") == ["hello"]
assert filter_by_prefix(["hello", "bye", "hi"], "hel") == ["hello"]
assert filter_by_prefix(["hello", "bye", "hi"], "bye") == ["bye"]
assert filter_by_prefix(["hello", "bye", "hi"], "") == ["hello", "bye", "hi"]
assert filter_by_prefix(['hello', 'world', '42'], 'w') == ['world']
assert filter_by_prefix(['hello', 'world', '42'], '4') == ['42']
assert filter_by_prefix(['hello', 'world', '42'], 'no') == []
assert filter_by_prefix(['hello', 'world', '42'], 'he') == ['hello']
assert filter_by_prefix(["hello", "world", "lucky", "far"], "f") == ["far"]
assert filter_by_prefix(["hello", "world", "lucky", "far"], "h") == ["hello"]
assert filter_by_prefix(["hello", "world", "lucky", "far"], "a") == []
assert filter_by_prefix(["hello", "world", "lucky", "far"], "") == ["hello", "world", "lucky", "far"]
assert filter_by_prefix(['w', 'ma', 'ro', 'to'], 'e') == []
assert filter_by_prefix(['w', 'ma', 'ro', 'to'], 'w') == ['w']
assert filter_by_prefix(['w', 'ma', 'ro', 'to'], 'm') == ['ma']
assert filter_by_prefix(['w', 'ma', 'ro', 'to'], 't') == ['to']
assert filter_by_prefix(['w', 'ma', 'ro', 'to'], 's') == []
assert filter_by_prefix(['w', 'ma', 'ro', 'to'], 'o') == []
assert filter_by_prefix(['w', 'ma', 'ro', 'to'], 'a') == []
assert filter_by_prefix(['w', 'ma', 'ro', 'to'], 'wro') == []
assert filter_by_prefix(['w', 'ma', 'ro', 'to'], 'wroto') == []
assert filter_by_prefix(['w', 'ma', 'ro', 'to'], 'wrot') == []
assert filter_by_prefix(["PyQt5", "foo", "bar", "PyQt4"], "Py") == ["PyQt5", "PyQt4"]
assert filter_by_prefix(["PyQt5", "foo", "bar", "PyQt4"], "Qt") == []
assert filter_by_prefix(["PyQt5", "foo", "bar", "PyQt4"], "bar") == ["bar"]
assert filter_by_prefix(["PyQt5", "foo", "bar", "PyQt4"], "foo") == ["foo"]
assert filter_by_prefix(["PyQt5", "foo", "bar", "PyQt4"], "foobar") == []
assert filter_by_prefix(["PyQt5", "foo", "bar", "PyQt4"], "") == ["PyQt5", "foo", "bar", "PyQt4"]
assert filter_by_prefix([], "PyQt") == []
assert filter_by_prefix(['123', '456', '789', 'abc', 'def', 'ghi'], 'abc') == ['abc']
assert filter_by_prefix(["hello", "goodbye", "jim"], "g") == ["goodbye"]
assert filter_by_prefix(["hello", "goodbye", "jim"], "j") == ["jim"]
assert filter_by_prefix(['cat', 'dog', 'bird', 'car'], 'd') == ['dog']
assert filter_by_prefix(['test', 'tuesday', 'tote'], 'to') == ['tote']
assert filter_by_prefix(['test', 'tuesday', 'tote'], 'te') == ['test']
assert filter_by_prefix(['test', 'tuesday', 'tote'], 't') == ['test', 'tuesday', 'tote']
assert filter_by_prefix(["apple", "airplane", "book", "banana"], "z") == []
assert filter_by_prefix(["good", "bad", "mixed"], "b") == ["bad"]
assert filter_by_prefix(["good", "bad", "mixed"], "m") == ["mixed"]
assert filter_by_prefix(["good", "bad", "mixed"], "x") == []
assert filter_by_prefix(["asdf", "sjdfljsdf", "jklsdf", "aaac"], "as") == ["asdf"]
assert filter_by_prefix(["asdf", "sjdfljsdf", "jklsdf", "aaac"], "bbb") == []
assert filter_by_prefix(["cat", "car", "cow"], "ca") == ["cat", "car"]
assert filter_by_prefix(["dog", "deer", "deal"], "d") == ["dog", "deer", "deal"]
assert filter_by_prefix(["hello", "there", "general", "kenobi"], "there") == ["there"]
assert filter_by_prefix(["hello", "there", "general", "kenobi"], "general") == ["general"]
assert filter_by_prefix(["hello", "there", "general", "kenobi"], "kenobi") == ["kenobi"]
assert filter_by_prefix(["hello", "there", "general", "kenobi"], "he") == ["hello"]
assert filter_by_prefix(["hello", "there", "general", "kenobi"], "the") == ["there"]
assert filter_by_prefix(["hello", "there", "general", "kenobi"], "gene") == ["general"]
assert filter_by_prefix(["hello", "there", "general", "kenobi"], "ken") == ["kenobi"]
assert filter_by_prefix(["hello", "there", "general", "kenobi"], "hegene") == []
assert filter_by_prefix(["hello", "there", "general", "kenobi"], "hege") == []
assert filter_by_prefix(['abc', 'def', 'abcd', 'dabc', 'abcde'], 'def') == ['def']
assert filter_by_prefix(['abc', 'def', 'abcd', 'dabc', 'abcde'], 'ab') == ['abc', 'abcd', 'abcde']
assert filter_by_prefix(['abc', 'def', 'abcd', 'dabc', 'abcde'], 'dabc') == ['dabc']
assert filter_by_prefix(['cat', 'dog', 'caterpillar'], 'dog') == ['dog']
assert filter_by_prefix(['cat', 'dog', 'caterpillar'], 'wombat') == []
assert filter_by_prefix(["apple", "banana", "pear", "strawberry"], "apple") == ["apple"]
assert filter_by_prefix(["apple", "banana", "pear", "strawberry"], "strawberry") == ["strawberry"]
assert filter_by_prefix(["apple", "banana", "pear", "strawberry"], "berry") == []
assert filter_by_prefix(["a", "b", "cd", "def"], "b") == ["b"]
assert filter_by_prefix(["a", "b", "cd", "def"], "c") == ["cd"]
assert filter_by_prefix(["a", "b", "cd", "def"], "e") == []
assert filter_by_prefix(["ab", "bc", "cd", "ea"], "") == ["ab", "bc", "cd", "ea"]
assert filter_by_prefix(["ab", "bc", "cd", "ea"], "z") == []
assert filter_by_prefix(["apple", "banana", "cat", "dog"], "b") == ["banana"]
assert filter_by_prefix(["apple", "banana", "cat", "dog"], "c") == ["cat"]
assert filter_by_prefix(["apple", "banana", "cat", "dog"], "d") == ["dog"]
assert filter_by_prefix(["I", "like", "cake"], "I") == ["I"]
assert filter_by_prefix(["I", "like", "cake"], "") == ["I", "like", "cake"]
assert filter_by_prefix(["I", "like", "cake"], "z") == []
assert filter_by_prefix(["cat", "dog", "lion", "tiger"], "d") == ["dog"]
assert filter_by_prefix(["cat", "dog", "lion", "tiger"], "ca") == ["cat"]
assert filter_by_prefix(["cat", "dog", "lion", "tiger"], "c") == ["cat"]
assert filter_by_prefix(["cat", "dog", "lion", "tiger"], "li") == ["lion"]
assert filter_by_prefix(["cat", "dog", "lion", "tiger"], "l") == ["lion"]
assert filter_by_prefix(["cat", "dog", "lion", "tiger"], "m") == []
assert filter_by_prefix(["cat", "dog", "lion", "tiger"], "") == ["cat", "dog", "lion", "tiger"]
assert filter_by_prefix([], "t") == []
assert filter_by_prefix(["", "", "", ""], "") == ["", "", "", ""]
assert filter_by_prefix(['cat', 'cat', 'dog', 'bunny'], 'b') == ['bunny']
assert filter_by_prefix(['cat', 'cat', 'dog', 'bunny'], 'd') == ['dog']
assert filter_by_prefix(['cat', 'cat', 'dog', 'bunny'], 'x') == []
assert filter_by_prefix(['cat', 'cat', 'dog', 'bunny'], 'dolphin') == []
assert filter_by_prefix([], 'x') == []
assert filter_by_prefix(['cat', 'cat', 'dog', 'bunny'], '') == ['cat', 'cat', 'dog', 'bunny']
assert filter_by_prefix(["prefix", "do", "not"], "x") == []
assert filter_by_prefix([], "de") == []
assert filter_by_prefix(["dog", "cat", "deer", "goat"], "") == ["dog", "cat", "deer", "goat"]
assert filter_by_prefix(["dog", "cat", "deer", "goat"], "de") == ["deer"]
assert filter_by_prefix(["dog", "cat", "bat"], "b") == ["bat"]
assert filter_by_prefix(["dog", "cat", "bat"], "d") == ["dog"]
assert filter_by_prefix(["dog", "cat", "bat"], "g") == []
assert filter_by_prefix(["dog", "cat", "bat"], "") == ["dog", "cat", "bat"]
assert filter_by_prefix(["hello", "world", "greetings"], "") == ["hello", "world", "greetings"]
assert filter_by_prefix(["hello", "world", "greetings"], "a") == []
assert filter_by_prefix(["hello", "world", "greetings"], "w") == ["world"]
assert filter_by_prefix(["hello", "world", "greetings"], "g") == ["greetings"]
assert filter_by_prefix(["hello", "world", "greetings"], "hell") == ["hello"]
assert filter_by_prefix(["hello", "world", "greetings"], "h") == ["hello"]
assert filter_by_prefix(["test", "random", "testcase"], "random") == ["random"]
assert filter_by_prefix(["test", "random", "testcase"], "") == ["test", "random", "testcase"]
assert filter_by_prefix(["test", "random", "testcase"], "case") == []
assert filter_by_prefix(['apple', 'bear', 'carrot', 'antelope'], 'be') == ['bear']
assert filter_by_prefix(['apple', 'bear', 'carrot', 'antelope'], 'ca') == ['carrot']
assert filter_by_prefix(['apple', 'bear', 'carrot', 'antelope'], 'c') == ['carrot']
assert filter_by_prefix(['apple', 'bear', 'carrot', 'antelope'], 'ant') == ['antelope']
assert filter_by_prefix(['apple', 'bear', 'carrot', 'antelope'], 'xxx') == []
assert filter_by_prefix(["ladybug", "ant", "art", "mantis", "car"], "m") == ["mantis"]
assert filter_by_prefix(["ladybug", "ant", "art", "mantis", "car"], "cat") == []
assert filter_by_prefix(["dog", "cat", "ant", "egg", "bat"], "a") == ["ant"]
assert filter_by_prefix(["dog", "cat", "ant", "egg", "bat"], "b") == ["bat"]
assert filter_by_prefix(["dog", "cat", "ant", "egg", "bat"], "d") == ["dog"]
assert filter_by_prefix(["dog", "cat", "ant", "egg", "bat"], "e") == ["egg"]
assert filter_by_prefix(["dog", "cat", "ant", "egg", "bat"], "z") == []
assert filter_by_prefix(["cat", "caterpillar", "lion", "dog"], "d") == ["dog"]
assert filter_by_prefix(["cat", "caterpillar", "lion", "dog"], "l") == ["lion"]
assert filter_by_prefix(["cat", "caterpillar", "lion", "dog"], "b") == []

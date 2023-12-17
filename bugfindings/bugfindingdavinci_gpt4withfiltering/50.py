

def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord(ch)) for ch in s])
assert decode_shift(encode_shift("abc")) == "abc"
assert decode_shift(encode_shift("bcd")) == "bcd"
assert decode_shift(encode_shift("xyz")) == "xyz"
assert decode_shift(encode_shift("abcde")) == "abcde"
assert "bcdefa" == decode_shift(encode_shift("bcdefa"))
assert "yzabcd" == decode_shift(encode_shift("yzabcd"))
assert "wxyzab" == decode_shift(encode_shift("wxyzab"))
assert decode_shift(encode_shift("wxyz")) == "wxyz"
assert decode_shift(encode_shift("abcdefghijklmnopqrstuvwxyz")) == "abcdefghijklmnopqrstuvwxyz"
assert decode_shift(encode_shift("skdjf")) == "skdjf"
assert decode_shift(encode_shift("")) == ""
assert decode_shift(encode_shift("abcabcabcabc")) == "abcabcabcabc"
assert decode_shift(encode_shift("z")) == "z"
assert "xyz" == decode_shift(encode_shift("xyz"))
assert "abc" == decode_shift(encode_shift("abc"))
assert "aa" == decode_shift(encode_shift("aa"))
assert "aaa" == decode_shift(encode_shift("aaa"))
assert decode_shift(encode_shift("python")) == "python"
assert decode_shift(encode_shift("shifted")) == "shifted"
assert decode_shift(encode_shift("super")) == "super"
assert decode_shift(encode_shift("welcome")) == "welcome"
assert decode_shift(encode_shift("wv")) == "wv"
assert decode_shift(encode_shift("abcd")) == "abcd"
assert decode_shift(encode_shift("zyx")) == "zyx"
assert decode_shift(encode_shift("zzz")) == "zzz"
assert decode_shift(encode_shift("hello")) == "hello"
assert decode_shift(encode_shift("zebra")) == "zebra"
assert decode_shift(encode_shift("uva")) == "uva"
assert decode_shift(encode_shift("zoo")) == "zoo"
assert decode_shift(encode_shift("happy")) == "happy"
assert decode_shift(encode_shift("a")) == "a"
assert decode_shift(encode_shift("aa")) == "aa"
assert decode_shift(encode_shift("zz")) == "zz"
assert decode_shift(encode_shift("he")) == "he"
assert decode_shift(encode_shift("zabc")) == "zabc"
assert decode_shift(encode_shift("azbc")) == "azbc"
assert decode_shift(encode_shift("zyxwv")) == "zyxwv"
assert decode_shift(encode_shift("zabcd")) == "zabcd"
assert decode_shift(encode_shift("hi")) == "hi"
assert decode_shift(encode_shift("this")) == "this"
assert decode_shift(encode_shift("my")) == "my"
assert decode_shift(encode_shift("name")) == "name"
assert decode_shift(encode_shift("is")) == "is"
assert decode_shift(encode_shift("abcxyz")) == "abcxyz"
assert decode_shift(encode_shift("abcdez")) == "abcdez"
assert decode_shift(encode_shift("abcdz")) == "abcdz"
assert decode_shift(encode_shift("walk")) == "walk"
assert decode_shift(encode_shift("zzzzz")) == "zzzzz"
assert decode_shift("mjqqt") == "hello"
assert decode_shift(encode_shift("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz")) == "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
assert decode_shift(encode_shift("shubham")) == "shubham"
assert decode_shift(encode_shift("sayam")) == "sayam"
assert decode_shift(encode_shift("mohit")) == "mohit"
assert decode_shift(encode_shift("bookkeeper")) == "bookkeeper"
assert decode_shift(encode_shift("aaaa")) == "aaaa"
assert decode_shift(encode_shift("zzzz")) == "zzzz"
assert decode_shift(encode_shift("y")) == "y"
assert decode_shift(encode_shift("cata")) == "cata"
assert decode_shift(encode_shift("uea")) == "uea"
assert decode_shift(encode_shift("udacity")) == "udacity"
assert decode_shift(encode_shift("pynative")) == "pynative"
assert decode_shift(encode_shift("fo")) == "fo"
assert decode_shift(encode_shift("foo")) == "foo"
assert decode_shift(encode_shift("hacking")) == "hacking"
assert decode_shift(encode_shift("aaa")) == "aaa"
assert decode_shift(encode_shift("e")) == "e"
assert decode_shift(encode_shift("hidden")) == "hidden"
assert "fandango" == decode_shift(encode_shift("fandango"))
assert "abz" == decode_shift(encode_shift("abz"))
assert "abcdefg" == decode_shift(encode_shift("abcdefg"))
assert decode_shift(encode_shift("pythoo")) == "pythoo"
assert decode_shift(encode_shift("x")) == "x"
assert decode_shift(encode_shift("hola")) == "hola"
assert decode_shift(encode_shift("qwerty")) == "qwerty"
assert decode_shift(encode_shift("foobar")) == "foobar"
assert decode_shift(encode_shift("cat")) == "cat"
assert "zabcd" == decode_shift(encode_shift("zabcd"))
assert "nowisthetime" == decode_shift(encode_shift("nowisthetime"))
assert decode_shift(encode_shift("arthur")) == "arthur"
assert decode_shift(encode_shift("liefje")) == "liefje"
assert decode_shift(encode_shift("adfadf")) == "adfadf"
assert decode_shift(encode_shift("aaaabbbbccccddddeeeeffffgggghhhh")) == "aaaabbbbccccddddeeeeffffgggghhhh"
assert decode_shift(encode_shift("aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnooooppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz")) == "aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnooooppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz"
assert decode_shift(encode_shift("banana")) == "banana"
assert decode_shift(encode_shift("durian")) == "durian"
assert decode_shift(encode_shift("meow")) == "meow"
assert decode_shift(encode_shift("good")) == "good"
assert decode_shift(encode_shift("world")) == "world"
assert decode_shift(encode_shift("bbb")) == "bbb"
assert decode_shift(encode_shift("b")) == "b"
assert decode_shift(encode_shift("az")) == "az"
assert decode_shift(encode_shift("azzz")) == "azzz"
assert decode_shift(encode_shift("azzzz")) == "azzzz"
assert decode_shift(encode_shift("saitama")) == "saitama"
assert decode_shift(encode_shift("kanagawa")) == "kanagawa"
assert decode_shift(encode_shift("test")) == "test"
assert decode_shift(encode_shift("me")) == "me"
assert decode_shift(encode_shift("bacd")) == "bacd"
assert decode_shift(encode_shift("pyz")) == "pyz"
assert decode_shift(encode_shift("abba")) == "abba"
assert decode_shift(encode_shift("xy")) == "xy"


FIX = """
Add more test cases.
"""

def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    vowels = "aeiouyAEIOUY"
    n_vowels = sum(c in vowels for c in s)
    return n_vowels
assert vowels_count("hello") == 2
assert vowels_count("hEllO") == 2
assert vowels_count("why") == 1
assert vowels_count("world") == 1
assert vowels_count("hello, world") == 3
assert vowels_count("a") == 1
assert vowels_count("e") == 1
assert vowels_count("i") == 1
assert vowels_count("o") == 1
assert vowels_count("u") == 1
assert vowels_count("y") == 1
assert vowels_count("xy") == 1
assert vowels_count("ay") == 2
assert vowels_count("ya") == 1
assert vowels_count("ayy") == 2
assert vowels_count("aeiouy") == 6
assert vowels_count("aeiou") == 5
assert vowels_count('banana') == 3
assert vowels_count('oy') == 2
assert vowels_count('y') == 1
assert vowels_count('Bass') == 1
assert vowels_count('synchronization') == 5
assert vowels_count('city') == 2
assert vowels_count('bind') == 1
assert vowels_count('county') == 3
assert vowels_count('apple') == 2
assert vowels_count('energy') == 3
assert vowels_count('allergy') == 3
assert vowels_count('goodbye') == 3
assert vowels_count('education') == 5
assert vowels_count('hurry') == 2
assert vowels_count('jewelry') == 3
assert vowels_count('kitchen') == 2
assert vowels_count('interested') == 4
assert vowels_count('aeiouy') == 6
assert vowels_count('aei') == 3
assert vowels_count('abcdefg') == 2
assert vowels_count('aeiouaeiouaeiou') == 15
assert vowels_count('hello') == 2
assert vowels_count('bcdfgh') == 0
assert vowels_count('abcdefghijklmnopqrstuvwxyz') == 5
assert vowels_count('bcdfghjklmnpqrstvwxyz') == 0
assert vowels_count("cat") == 1
assert vowels_count("LorenIpsum") == 4
assert vowels_count("eyy") == 2
assert vowels_count("banana") == 3
assert vowels_count("spy") == 1
assert vowels_count("sky") == 1
assert vowels_count("yes") == 1
assert vowels_count("aei") == 3
assert vowels_count("aeiouaeiouaeiou") == 15
assert vowels_count("Yahoo") == 3
assert vowels_count("Java") == 2
assert vowels_count("JavaScript") == 3
assert vowels_count("Python") == 1
assert vowels_count("Noah") == 2
assert vowels_count("beta") == 2
assert vowels_count("delta") == 2
assert vowels_count("epsilon") == 3
assert vowels_count("eta") == 2
assert vowels_count("theta") == 2
assert vowels_count("kappa") == 2
assert vowels_count("lambda") == 2
assert vowels_count("mu") == 1
assert vowels_count("nu") == 1
assert vowels_count("xi") == 1
assert vowels_count("omicron") == 3
assert vowels_count("pi") == 1
assert vowels_count("rho") == 1
assert vowels_count("sigma") == 2
assert vowels_count("upsilon") == 3
assert vowels_count("phi") == 1
assert vowels_count("chi") == 1
assert vowels_count("psi") == 1
assert vowels_count("omega") == 3
assert vowels_count("abcde") == 2
assert vowels_count("abcdea") == 3
assert vowels_count("abcdee") == 3
assert vowels_count("abcdeee") == 4
assert vowels_count("abcdeeee") == 5
assert vowels_count("yyy") == 1
assert vowels_count("computer") == 3
assert vowels_count("pro") == 1
assert vowels_count("program") == 2
assert vowels_count("logic") == 2
assert vowels_count("log") == 1
assert vowels_count("out") == 2
assert vowels_count("in") == 1
assert vowels_count("intricate") == 4
assert vowels_count("integrated") == 4
assert vowels_count("function") == 3
assert vowels_count("counts") == 2
assert vowels_count("worlldd") == 1
assert vowels_count("yyyyy") == 1
assert vowels_count('hmm') == 0
assert vowels_count('probability') == 5
assert vowels_count('camel') == 2
assert vowels_count('go') == 1
assert vowels_count('import') == 2
assert vowels_count('try') == 1
assert vowels_count('production') == 4
assert vowels_count('development') == 4
assert vowels_count('memory') == 3
assert vowels_count('convention') == 4
assert vowels_count('structure') == 3
assert vowels_count('simplicity') == 4
assert vowels_count('bcd') == 0
assert vowels_count("aaa") == 3
assert vowels_count("b") == 0
assert vowels_count("bc") == 0
assert vowels_count("bcd") == 0
assert vowels_count("bcdf") == 0
assert vowels_count("bcdfg") == 0
assert vowels_count("by") == 1
assert vowels_count("pizza") == 2
assert vowels_count("text") == 1
assert vowels_count("orange") == 3
assert vowels_count("octopus") == 3
assert vowels_count("story") == 2
assert vowels_count("secondary") == 4
assert vowels_count("twenty") == 2
assert vowels_count("abcdefg") == 2
assert vowels_count("TeST") == 1
assert vowels_count("StUdent") == 2
assert vowels_count("NOw") == 1
assert vowels_count("MaGic") == 2
assert vowels_count("deGrEE") == 3
assert vowels_count('a') == 1
assert vowels_count('abc') == 1
assert vowels_count("Hello World") == 3
assert vowels_count("START") == 1
assert vowels_count("of") == 1
assert vowels_count("my") == 1
assert vowels_count("xylophone") == 3
assert vowels_count("f") == 0
assert vowels_count("j") == 0
assert vowels_count("p") == 0
assert vowels_count("v") == 0
assert vowels_count("blue") == 2
assert vowels_count("white") == 2
assert vowels_count('aeiou') == 5
assert vowels_count('why') == 1
assert vowels_count('I') == 1
assert vowels_count('my') == 1
assert vowels_count('may') == 2
assert vowels_count("pry") == 1
assert vowels_count("xyz") == 0
assert vowels_count("fry") == 1
assert vowels_count("hey") == 2
assert vowels_count('aeioy') == 5
assert vowels_count('aeio') == 4
assert vowels_count('ae') == 2
assert vowels_count('bcdfghjklmnpqrstvwxzy') == 1
assert vowels_count('mango') == 2
assert vowels_count('umami') == 3
assert vowels_count('sky') == 1
assert vowels_count('jive') == 2
assert vowels_count('in') == 1
assert vowels_count('u') == 1
assert vowels_count("aEiOu") == 5
assert vowels_count("AEIOU") == 5
assert vowels_count("AeiOu") == 5
assert vowels_count("AEIOUY") == 6
assert vowels_count("aa") == 2
assert vowels_count("ny") == 1
assert vowels_count("nay") == 2
assert vowels_count("enjoyyy") == 3
assert vowels_count('computer') == 3
assert vowels_count('intelligence') == 5
assert vowels_count('abnormal') == 3
assert vowels_count('developer') == 4
assert vowels_count('university') == 5
assert vowels_count('vibration') == 4
assert vowels_count('abstraction') == 4
assert vowels_count("EECS") == 2
assert vowels_count("Supercalifragilisticexpialidocious") == 16
assert vowels_count("AaAaAa") == 6
assert vowels_count("EeEeEe") == 6
assert vowels_count("IiIiIi") == 6
assert vowels_count("OoOoOo") == 6
assert vowels_count("UuUuUu") == 6
assert vowels_count('gym') == 0
assert vowels_count('everyone') == 4
assert vowels_count('hello, my name is sasha') == 7
assert vowels_count('can you count all the vowels in this string?') == 12
assert vowels_count('Vowels are a, e, i, o, u. Sometimes y.') == 13
assert vowels_count('Why?') == 0
assert vowels_count('cannot') == 2
assert vowels_count('Don\'t forget to checkout "The Dude" and "The Big Lebowski"!') == 16
assert vowels_count('Who\'s on first?') == 3
assert vowels_count('hi') == 1
assert vowels_count('aeration') == 5
assert vowels_count('ey') == 2
assert vowels_count('aa') == 2
assert vowels_count('dcy') == 1
assert vowels_count('dy') == 1
assert vowels_count('d') == 0
assert vowels_count('da') == 1
assert vowels_count('dae') == 2
assert vowels_count('dei') == 2
assert vowels_count('diy') == 2
assert vowels_count('peanut') == 3
assert vowels_count('My') == 1
assert vowels_count('yyy') == 1
assert vowels_count("Mississippi") == 4
assert vowels_count("aeiouyaeiouaeiou") == 15
assert vowels_count(" ") == 0
assert vowels_count('xyz') == 0
assert vowels_count('ab') == 1
assert vowels_count('ba') == 1
assert vowels_count("bcdfghjklmnpqrstvwxyz") == 0
assert vowels_count("abc") == 1
assert vowels_count("aeio") == 4
assert vowels_count("aeiouu") == 6
assert vowels_count("aeiooo") == 6
assert vowels_count("aeioou") == 6
assert vowels_count("ie") == 2
assert vowels_count("oy") == 2
assert vowels_count("eee") == 3
assert vowels_count("ooo") == 3
assert vowels_count("ioi") == 3
assert vowels_count("math") == 1
assert vowels_count("tigers") == 2
assert vowels_count("apples") == 2
assert vowels_count("bananas") == 3
assert vowels_count("abracadabra") == 5
assert vowels_count("apple") == 2
assert vowels_count("eel") == 2
assert vowels_count("an") == 1
assert vowels_count("try") == 1
assert vowels_count("painting") == 3
assert vowels_count("mango") == 2
assert vowels_count("moon") == 2
assert vowels_count("machine") == 3
assert vowels_count("yellow") == 2
assert vowels_count("puzzles") == 2
assert vowels_count("ocean") == 3
assert vowels_count("onion") == 3
assert vowels_count("ou") == 2
assert vowels_count("table") == 2
assert vowels_count("item") == 2
assert vowels_count("email") == 3
assert vowels_count('world') == 1
assert vowels_count('least') == 2
assert vowels_count('fry') == 1
assert 0 == vowels_count("b")
assert 3 == vowels_count("iou")
assert 2 == vowels_count("tree")
assert vowels_count("bbb") == 0
assert vowels_count("eye") == 2
assert vowels_count("yoyiy") == 3
assert vowels_count("oyioy") == 4
assert vowels_count("alphabet") == 3
assert vowels_count("stereophony") == 5
assert vowels_count("piano") == 3
assert vowels_count("siamang") == 3
assert vowels_count("kimono") == 3
assert vowels_count("salmon") == 2
assert vowels_count('GOOD') == 2
assert vowels_count('GoOd') == 2
assert vowels_count('boOt') == 2
assert vowels_count('bcdfghjkl') == 0
assert vowels_count("fly") == 1
assert vowels_count("wry") == 1
assert vowels_count("cry") == 1
assert vowels_count("dry") == 1
assert vowels_count('dictionary') == 5
assert vowels_count('YOLO') == 2
assert vowels_count('7') == 0
assert vowels_count('yaaay') == 4
assert vowels_count('by') == 1
assert vowels_count('oak') == 2
assert vowels_count('password') == 2
assert vowels_count('vowels') == 2
assert vowels_count('xyzzy') == 1
assert vowels_count('wilderness') == 3
assert vowels_count('tachycardia') == 4
assert vowels_count('lemon') == 2
assert vowels_count('octopus') == 3
assert vowels_count('accentor') == 3
assert vowels_count('zoology') == 4
assert vowels_count("aeiouyyy") == 6
assert vowels_count("aeioyyy") == 5
assert vowels_count("ae") == 2
assert vowels_count("abcdefgh") == 2
assert vowels_count("abcdefghi") == 3
assert vowels_count("abcdefghij") == 3
assert vowels_count("whisky") == 2
assert vowels_count("afghanistan") == 4
assert vowels_count('adamant') == 3
assert vowels_count('sunny') == 2
assert vowels_count('dinosaur') == 4
assert vowels_count('yes') == 1
assert vowels_count('leaky') == 3
assert vowels_count('abac') == 2
assert vowels_count('abacaba') == 4
assert vowels_count('victory') == 3
assert vowels_count('trite') == 2
assert vowels_count('it') == 1
assert vowels_count('qrt') == 0
assert vowels_count('skd') == 0
assert vowels_count('under') == 2
assert vowels_count('jklmn') == 0
assert vowels_count('to') == 1
assert vowels_count('be') == 1
assert vowels_count('or') == 1
assert vowels_count('not') == 1
assert vowels_count('cps') == 0
assert vowels_count('xcite') == 2
assert vowels_count("AiA") == 3
assert vowels_count("\n") == 0
assert vowels_count("ye") == 1
assert vowels_count("**e") == 1
assert vowels_count("\nE\n") == 1
assert vowels_count("AEA") == 3
assert vowels_count("zzz") == 0
assert vowels_count("AeA") == 3
assert vowels_count("aaeeoo") == 6
assert vowels_count("io") == 2
assert vowels_count("aaaaeiou") == 8
assert vowels_count("aeioy") == 5
assert vowels_count("bye") == 1
assert vowels_count("byebye") == 2
assert vowels_count("dog") == 1
assert vowels_count("happy") == 2
assert vowels_count("z") == 0
assert vowels_count("cheese") == 3
assert vowels_count("pineapple") == 4
assert vowels_count("t") == 0
assert vowels_count("st") == 0
assert vowels_count("ty") == 1
assert vowels_count("Hello World!") == 3
assert vowels_count("Hello Big World!") == 4
assert vowels_count('blueberry') == 4
assert vowels_count('orange') == 3
assert vowels_count('grape') == 2
assert vowels_count('strawberry') == 3
assert vowels_count('watermelon') == 4
assert vowels_count('raspberry') == 3
assert vowels_count('papaya') == 3
assert vowels_count('coconut') == 3
assert vowels_count('dragonfruit') == 4
assert vowels_count('pear') == 2
assert vowels_count('guava') == 3
assert vowels_count('avocado') == 4
assert vowels_count('pineapple') == 4
assert vowels_count('yuzu') == 2
assert vowels_count("abcdefghijklmnopqrstuvwxyz") == 5
assert vowels_count("qwrt") == 0
assert vowels_count("Loudly") == 3
assert 2 == vowels_count("day")
assert vowels_count("mE") == 1
assert vowels_count("buzzy") == 2
assert vowels_count("aaa!!!") == 3
assert vowels_count("aaa!!!!!!") == 3
assert vowels_count("iii") == 3
assert vowels_count("iii!!!") == 3
assert vowels_count("iii!!!!!!") == 3
assert vowels_count("hhh") == 0
assert vowels_count("hhh!!!") == 0
assert vowels_count("hhh!!!!!!") == 0
assert vowels_count('belly') == 2
assert vowels_count('nay') == 2
assert vowels_count('wry') == 1
assert vowels_count("mississippi") == 4
assert vowels_count("cacophony") == 4
assert vowels_count("tgy") == 1
assert vowels_count("squawk") == 2
assert vowels_count("awesome") == 4
assert vowels_count('yahooligans') == 5
assert vowels_count('<html>') == 0
assert vowels_count('AEIOU') == 5
assert vowels_count('AbCdEfG') == 2
assert vowels_count('abcdEf') == 2
assert vowels_count('aEiOu') == 5
assert vowels_count('aeiOU') == 5
assert vowels_count('AaEeIiOoUu') == 10
assert vowels_count('aEiO') == 4
assert vowels_count("aaaeee") == 6
assert vowels_count("aaaeeeiii") == 9
assert vowels_count("aaeiuio") == 7
assert vowels_count("yo") == 1
assert vowels_count("balloon") == 3
assert vowels_count("condition") == 4
assert vowels_count("wxyz") == 0
assert vowels_count("qwrtvn") == 0
assert vowels_count("aaasdfghjkl") == 3
assert vowels_count("polyalphabetic") == 5
assert vowels_count("polyalphabetical") == 6
assert vowels_count("XYZ") == 0
assert vowels_count('aaaaa') == 5
assert vowels_count('bda') == 1
assert vowels_count('bdae') == 2
assert vowels_count('bde') == 1
assert vowels_count('bdey') == 2
assert vowels_count('bdie') == 2
assert vowels_count('bdoe') == 2
assert vowels_count('bdu') == 1
assert vowels_count('bduy') == 2
assert vowels_count('baeeye') == 4
assert vowels_count("elephant") == 3
assert vowels_count("box") == 1
assert vowels_count('happy') == 2
assert vowels_count('hay') == 2
assert vowels_count('yay') == 2
assert vowels_count("car") == 1
assert vowels_count("shy") == 1
assert vowels_count("Donkey") == 3
assert vowels_count("BeAtY") == 3
assert vowels_count("stand") == 1
assert vowels_count("Stand") == 1
assert vowels_count("Acorn") == 2
assert vowels_count("pneumonoultramicroscopicsilicovolcanoconiosis") == 20
assert vowels_count("fish") == 1
assert vowels_count("yucky") == 2
assert vowels_count("Horseman") == 3
assert vowels_count("run") == 1
assert vowels_count("jello") == 2
assert vowels_count("darn") == 1
assert vowels_count("stupid") == 2
assert vowels_count("disgrace") == 3
assert vowels_count("lazy") == 2
assert vowels_count("crazy") == 2
assert vowels_count("byeby") == 2
assert vowels_count("ee") == 2
assert vowels_count("eeee") == 4
assert vowels_count("hmm") == 0
assert vowels_count("h") == 0
assert vowels_count("hy") == 1
assert vowels_count("miy") == 2
assert vowels_count("binni") == 2
assert vowels_count('aeiouya') == 6
assert vowels_count('abcde') == 2
assert vowels_count("Poliwag") == 3
assert vowels_count("Squirtle") == 3
assert vowels_count("Charmeleon") == 4
assert vowels_count("Charizard") == 3
assert vowels_count("Pikapika") == 4
assert vowels_count("Magneton") == 3
assert vowels_count("Rattata") == 3
assert vowels_count("Graveler") == 3
assert vowels_count("Golem") == 2
assert vowels_count("his") == 1
assert vowels_count("lucky") == 2
assert vowels_count("day") == 2
assert vowels_count("false") == 2
assert vowels_count("kite") == 2
assert vowels_count("sunny") == 2
assert vowels_count("high") == 1
assert vowels_count("anaconda") == 4
assert vowels_count("supercalifragilisticexpialidocious") == 16
assert vowels_count("antidisestablishmentarianism") == 11
assert vowels_count("@!?#") == 0
assert vowels_count("123") == 0
assert vowels_count("dY") == 1
assert vowels_count("s") == 0
assert vowels_count('ye') == 1
assert vowels_count('couch') == 2
assert vowels_count('e') == 1
assert vowels_count('i') == 1
assert vowels_count('o') == 1
assert vowels_count('bc') == 0
assert vowels_count('jkl') == 0
assert vowels_count('mno') == 1
assert vowels_count('pqr') == 0
assert vowels_count('stuv') == 1
assert vowels_count('wxyz') == 0
assert vowels_count("ababyy") == 3


def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    """
    suf = ['txt', 'exe', 'dll']
    lst = file_name.split(sep='.')
    if len(lst) != 2:
        return 'No'
    if len(lst[0]) == 0:
        return 'No'
    if not lst[0][0].isalpha():
        return 'No'
    t = len([x for x in lst[0] if x.isdigit()])
    if t > 3:
        return 'No'
    return 'Yes'
assert file_name_check('0') == 'No'
assert file_name_check('1') == 'No'
assert file_name_check('2') == 'No'
assert file_name_check('3') == 'No'
assert file_name_check('4') == 'No'
assert file_name_check('5') == 'No'
assert file_name_check('6') == 'No'
assert file_name_check('7') == 'No'
assert file_name_check('8') == 'No'
assert file_name_check('9') == 'No'
assert file_name_check('a') == 'No'
assert file_name_check('b') == 'No'
assert file_name_check('c') == 'No'
assert file_name_check('d') == 'No'
assert file_name_check('e') == 'No'
assert file_name_check('f') == 'No'
assert file_name_check('g') == 'No'
assert file_name_check('h') == 'No'
assert file_name_check('i') == 'No'
assert file_name_check('j') == 'No'
assert file_name_check('k') == 'No'
assert file_name_check('l') == 'No'
assert file_name_check('m') == 'No'
assert file_name_check('n') == 'No'
assert file_name_check('o') == 'No'
assert file_name_check('p') == 'No'
assert file_name_check('q') == 'No'
assert file_name_check('r') == 'No'
assert file_name_check('s') == 'No'
assert file_name_check('t') == 'No'
assert file_name_check('01.txt') == 'No'
assert file_name_check('1.exe') == 'No'
assert file_name_check('1a.exe') == 'No'
assert file_name_check('1a.txt') == 'No'
assert file_name_check('1b.exe') == 'No'
assert file_name_check('1b.txt') == 'No'
assert file_name_check('1c.txt') == 'No'
assert file_name_check('1e.exe') == 'No'
assert file_name_check('1e.txt') == 'No'
assert file_name_check('1f.exe') == 'No'
assert file_name_check('1f.txt') == 'No'
assert file_name_check('1g.exe') == 'No'
assert file_name_check('1g.txt') == 'No'
assert file_name_check('1h.txt') == 'No'
assert file_name_check('1i.txt') == 'No'
assert file_name_check('1j.txt') == 'No'
assert file_name_check('1k.exe') == 'No'
assert file_name_check('001.txt') == 'No'
assert file_name_check('01.exe') == 'No'
assert file_name_check('01.dll') == 'No'
assert file_name_check('01.TXT') == 'No'
assert file_name_check('0.exe') == 'No'
assert file_name_check('01.') == 'No'
assert file_name_check('1a.dll') == 'No'
assert file_name_check('1a.') == 'No'
assert file_name_check('1b.dll') == 'No'
assert file_name_check('1b.') == 'No'
assert file_name_check('1c.exe') == 'No'
assert file_name_check('1c.dll') == 'No'
assert file_name_check('1c.') == 'No'
assert file_name_check('1a2.txt') == 'No'
assert file_name_check('1a2.exe') == 'No'
assert file_name_check('1a2.dll') == 'No'
assert file_name_check('1a2.') == 'No'
assert file_name_check('1a3.txt') == 'No'
assert file_name_check('1a3.exe') == 'No'
assert file_name_check('1a3.dll') == 'No'
assert file_name_check('1a3.') == 'No'
assert file_name_check('01.jpg') == 'No'
assert file_name_check('02.jpg') == 'No'
assert file_name_check('03.jpg') == 'No'
assert file_name_check('04.jpg') == 'No'
assert file_name_check('05.jpg') == 'No'
assert file_name_check('06.jpg') == 'No'
assert file_name_check('07.jpg') == 'No'
assert file_name_check('08.jpg') == 'No'
assert file_name_check('09.jpg') == 'No'
assert file_name_check('a.jpg') == 'No'
assert file_name_check('f.exe') == 'Yes'
assert file_name_check('f.dll') == 'Yes'
assert file_name_check('g.exe') == 'Yes'
assert file_name_check('h.exe') == 'Yes'
assert file_name_check('i.exe') == 'Yes'
assert file_name_check('a.txt') == 'Yes'
assert file_name_check('aa.exe') == 'Yes'
assert file_name_check('01_01.txt') == 'No'
assert file_name_check('01.txt.exe') == 'No'
assert file_name_check('01.txt.dll') == 'No'
assert file_name_check('001_01.exe.txt') == 'No'
assert file_name_check('001_01.exe.dll') == 'No'
assert file_name_check('001_01.dll.txt.txt') == 'No'
assert file_name_check('001_01.txt.exe.txt.dll') == 'No'
assert file_name_check('123') == 'No'
assert file_name_check('abc') == 'No'
assert file_name_check('a.b') == 'No'
assert file_name_check('a.b.c') == 'No'
assert file_name_check('a.b.cd.exe') == 'No'
assert file_name_check('a.b.cd.exe.txt') == 'No'
assert file_name_check('a.b.cd.exe.dll') == 'No'
assert file_name_check('a.b.cd.exe.dll.txt') == 'No'
assert file_name_check('a.b.cd.exe.dll.exe') == 'No'
assert file_name_check('a.b.cd.exe.dll.txt.exe') == 'No'
assert file_name_check('a.b.cd.exe.dll.txt.exe.dll') == 'No'
assert file_name_check('a.b.cd.exe.dll.txt.exe.dll.txt.exe') == 'No'
assert file_name_check('a.b.cd.exe.dll.txt.exe.dll.txt.exe.exe') == 'No'
assert file_name_check('a.b.cd.exe.dll.txt.exe.dll.txt.exe.exe.dll') == 'No'
assert file_name_check('12abc') == 'No'
assert file_name_check('12abdc.exex') == 'No'
assert file_name_check('12abdc.exex.txt.exe.exex') == 'No'
assert file_name_check('12abdc.exex.txt.exe.exex.exe') == 'No'
assert file_name_check('12abdc.exex.txt.exe.exex.exe.txt.exe.exex') == 'No'
assert file_name_check('12abdc.exex.txt.exe.exex.txt.exe.exex.exex') == 'No'
assert file_name_check('1.txt') == 'No'
assert file_name_check('1a000.exe') == 'No'
assert file_name_check('1bdd.exe') == 'No'
assert file_name_check('a.exe') == 'Yes'
assert file_name_check('1.py') == 'No'
assert file_name_check('1.dll') == 'No'
assert file_name_check('a.exe.py') == 'No'
assert file_name_check('01.exe.py') == 'No'
assert file_name_check('01.dll.py') == 'No'
assert file_name_check('a.dll.py') == 'No'
assert file_name_check('1.exe.py') == 'No'
assert file_name_check('1.dll.py') == 'No'
assert file_name_check('1.txt.py') == 'No'
assert file_name_check("..txt") is "No"
assert file_name_check("0.txt") is "No"
assert file_name_check("2.exe") is "No"
assert file_name_check("2.dll") is "No"
assert file_name_check("3a.exe") is "No"
assert file_name_check("3.txta") is "No"
assert file_name_check("3.exea") is "No"
assert file_name_check("3.dlla") is "No"
assert file_name_check("3.exe") is "No"
assert file_name_check("a") is "No"
assert file_name_check('1A2.exe') == 'No'
assert file_name_check('1A2.dll') == 'No'
assert file_name_check('a.dll') == 'Yes'
assert file_name_check('A.exe') == 'Yes'
assert file_name_check('A.dll') == 'Yes'
assert file_name_check('a.a.txt') == 'No'
assert file_name_check('a.A.txt') == 'No'
assert file_name_check('a.a.exe') == 'No'
assert file_name_check('a.A.exe') == 'No'
assert file_name_check('a.a.dll') == 'No'
assert file_name_check('a.A.dll') == 'No'
assert file_name_check('a.A.EXE') == 'No'
assert file_name_check('A.A.exe') == 'No'
assert file_name_check('A.A.dll') == 'No'
assert file_name_check('A.A.EXE') == 'No'
assert file_name_check('aa.EXE') == 'No'
assert file_name_check('aa.AEXE') == 'No'
assert file_name_check('000.txt') == 'No'
assert file_name_check('9.txt') == 'No'
assert file_name_check('0a.txt') == 'No'
assert file_name_check('00a.txt') == 'No'
assert file_name_check('a.txt.exe') == 'No'
assert file_name_check('a.txt.dll') == 'No'
assert file_name_check('0a.exe') == 'No'
assert file_name_check('0a.dll') == 'No'
assert file_name_check('0a.txt.exe') == 'No'
assert file_name_check('0a.txt.dll') == 'No'
assert file_name_check('a.exe.dll') == 'No'
assert file_name_check('a.txt.exe.dll') == 'No'
assert file_name_check('0a.exe.dll') == 'No'
assert file_name_check('00a.exe.dll') == 'No'
assert file_name_check('001.exe') == 'No'
assert file_name_check('ab') == 'No'
assert file_name_check('011.abc') == 'No'
assert file_name_check('021.abc') == 'No'
assert file_name_check('031.abc') == 'No'
assert file_name_check('011.123.exe') == 'No'
assert file_name_check('021.123.dll') == 'No'
assert file_name_check("ab") == "No"
assert file_name_check("1") == "No"
assert file_name_check("a1") == "No"
assert file_name_check("a1b") == "No"
assert file_name_check("abc") == "No"
assert file_name_check("ab.c") == "No"
assert file_name_check("a..b") == "No"
assert file_name_check("..b") == "No"
assert file_name_check("a_b") == "No"
assert file_name_check("ab.exe") == "Yes"
assert file_name_check('a.exe') == "Yes"
assert file_name_check('ab_exe') == "No"
assert file_name_check('ab.exe.') == "No"
assert file_name_check('ab.exe..') == "No"
assert file_name_check('ab.exe.a') == "No"
assert file_name_check('ab.exe...a') == "No"
assert file_name_check('ab.exe..a') == "No"
assert file_name_check('ab..exe') == "No"
assert file_name_check('ab_exe.') == "No"
assert file_name_check('ab_exe..') == "No"
assert file_name_check('ab_exe.a') == "No"
assert file_name_check('ab_exe...a') == "No"
assert file_name_check('ab_exe..a') == "No"
assert file_name_check('ab...exe') == "No"
assert file_name_check('ab_exe._') == "No"
assert file_name_check('ab_exe._.') == "No"
assert file_name_check('ab_exe._..') == "No"
assert file_name_check('123.asdasd') == 'No'
assert file_name_check('123123') == 'No'
assert file_name_check('..') == 'No'
assert file_name_check('005.exe')== 'No'
assert file_name_check('006.dll')== 'No'
assert file_name_check('python.py') == 'No'
assert file_name_check('../python.py') == 'No'
assert file_name_check('000.py.exe') == 'No'
assert file_name_check('000.py.dll') == 'No'
assert file_name_check('000.pyw') == 'No'
assert file_name_check('02.exe') == 'No'
assert file_name_check('02.dll') == 'No'
assert file_name_check('02.tXt') == 'No'
assert file_name_check('02.EXE ') == 'No'
assert file_name_check('02.DLL ') == 'No'
assert file_name_check('02.txt.exe') == 'No'
assert file_name_check('02.txt.DLL') == 'No'
assert file_name_check('02.txt.EXE') == 'No'
assert file_name_check('02.exe.txt') == 'No'
assert file_name_check('02.exe.exe') == 'No'
assert file_name_check('02.exe.dll') == 'No'
assert file_name_check('0g02.txt') == 'No'
assert file_name_check('0g02.exe') == 'No'
assert file_name_check('0g02.dll') == 'No'
assert file_name_check('0g02.dll0') == 'No'
assert file_name_check('0g02.exe0') == 'No'
assert file_name_check('0g02.exe00') == 'No'
assert file_name_check('0g02.dll00') == 'No'
assert file_name_check('00.txt') == 'No'
assert file_name_check('000.exe') == 'No'
assert file_name_check('000.dll') == 'No'
assert file_name_check('000.exe0') == 'No'
assert file_name_check('000.exe00') == 'No'
assert file_name_check('000.dll00') == 'No'
assert file_name_check('000.dll0') == 'No'
assert file_name_check('abc.exe') == 'Yes'
assert file_name_check('abc.dll') == 'Yes'
assert file_name_check('abc..exe') == 'No'
assert file_name_check('abc.def.exe') == 'No'
assert file_name_check('abc..def') == 'No'
assert file_name_check('abc.def.') == 'No'
assert file_name_check('def.') == 'No'
assert file_name_check('abc_') == 'No'
assert file_name_check('abc_def') == 'No'
assert file_name_check('abc_def__') == 'No'
assert file_name_check('abc_def_') == 'No'
assert file_name_check('abc_def_ghi') == 'No'
assert file_name_check('abc_def_ghi__') == 'No'
assert file_name_check('abc_def_ghi_') == 'No'
assert file_name_check('abc_def_ghi_123') == 'No'
assert file_name_check('abc_def_ghi_123__') == 'No'
assert file_name_check('abc_def_ghi_123_') == 'No'
assert file_name_check('a.txt') =='Yes'
assert file_name_check('a1') =='No'
assert file_name_check('a3.txt.exe') =='No'
assert file_name_check('aaa') =='No'
assert file_name_check('a00') =='No'
assert file_name_check('0') =='No'
assert file_name_check('00') =='No'
assert file_name_check('10.exe.txt') =='No'
assert file_name_check('10ex') =='No'
assert file_name_check('a.txt.exe') =='No'
assert file_name_check('a.') =='No'
assert file_name_check('11.txt') == 'No'
assert file_name_check('11') == 'No'
assert file_name_check('1.txtt') == 'No'
assert file_name_check('1.txtt1') == 'No'
assert file_name_check('1.txtt.') == 'No'
assert file_name_check('1.txtt.1') == 'No'
assert file_name_check('1.d00') == 'No'
assert file_name_check('1.d0') == 'No'
assert file_name_check('1.d') == 'No'
assert file_name_check('1a.d00') == 'No'
assert file_name_check('1a.d0') == 'No'
assert file_name_check('1a.d') == 'No'
assert file_name_check('1aa.') == 'No'
assert file_name_check('1aa.d00') == 'No'
assert file_name_check('1aa.d0') == 'No'
assert file_name_check('1aa.d') == 'No'
assert file_name_check('ab.exe') == 'Yes'
assert file_name_check('ab.xyz') == 'No'
assert file_name_check('ab.XYZ') == 'No'
assert file_name_check('ab.123') == 'No'
assert file_name_check('ab.1234.exe') == 'No'
assert file_name_check('ab.12345') == 'No'
assert file_name_check('ab.12345.exe') == 'No'
assert file_name_check('ab.123456') == 'No'
assert file_name_check('ab.1234567') == 'No'
assert file_name_check('ab.123456789') == 'No'
assert file_name_check('ab.') == 'No'
assert file_name_check('01a.txt') == 'No'
assert file_name_check('abcabc') == 'No'
assert file_name_check('01.exx') == 'No'
assert file_name_check('0.dll') == 'No'
assert file_name_check('01.DLL') == 'No'
assert file_name_check('01.EXE') == 'No'
assert file_name_check('0.TXT') == 'No'
assert file_name_check('1.TXT') == 'No'
assert file_name_check(".exe.txt") == 'No'
assert file_name_check("1234") == 'No'
assert file_name_check("asdf") == 'No'
assert file_name_check("a1234a") == 'No'
assert file_name_check("1.exe") == 'No'
assert file_name_check("12345") == 'No'
assert file_name_check("1a.exe") == 'No'
assert file_name_check("1.exe.") == 'No'
assert file_name_check("1") == 'No'
assert file_name_check("1.") == 'No'
assert file_name_check(".exe.") == 'No'
assert file_name_check(".exe..") == 'No'
assert file_name_check('122.exe') == 'No'
assert file_name_check('b.exe') == 'Yes'
assert file_name_check('abc.txt') == 'Yes'
assert file_name_check('111.111.222.333.444.555.666.') == 'No'
assert file_name_check('111..222.333.444') == 'No'
assert file_name_check('111.111.222.333.444.') == 'No'
assert file_name_check('111.111.222.333.444..') == 'No'
assert file_name_check('111..222.333.444.555.666.') == 'No'
assert file_name_check('..exe') == 'No'
assert file_name_check('101.txt') == 'No'
assert file_name_check('2txt') == 'No'
assert file_name_check('2exe') == 'No'
assert file_name_check('2dll') == 'No'
assert file_name_check('2bin') == 'No'
assert file_name_check('2txt.exe') == 'No'
assert file_name_check('2txt.dll') == 'No'
assert file_name_check('2txt.bin') == 'No'
assert file_name_check('00001.txt') == 'No'
assert file_name_check('001.dll') == 'No'
assert file_name_check('101') == 'No'
assert file_name_check('01_file') == 'No'
assert file_name_check('01_file.txt.exe') == 'No'
assert file_name_check('01_file.dll') == 'No'
assert file_name_check('01_file.dll.txt') == 'No'
assert file_name_check('0abc') == 'No'
assert file_name_check('abc123') == 'No'
assert file_name_check('abc.tar.gz.exe') == 'No'
assert file_name_check('abc.tar.gz.exex') == 'No'
assert file_name_check('abc.tar.gz.exe.exe') == 'No'
assert file_name_check('0.txt') == 'No'
assert file_name_check('111.txt') == 'No'
assert file_name_check('ab.txt') == 'Yes'
assert file_name_check('ab.c') == 'No'
assert file_name_check('ab.cde') == 'No'
assert file_name_check('ab.cde.exe') == 'No'
assert file_name_check('a.exe.') == 'No'
assert file_name_check('06.exe') == 'No'
assert file_name_check('05.exe') == 'No'
assert file_name_check('99.txt') == 'No'
assert file_name_check('002.exe') == 'No'
assert file_name_check('hello') == 'No'
assert file_name_check('hellO') == 'No'
assert file_name_check('001.txt.exe') == 'No'
assert file_name_check('001.exe.txt') == 'No'
assert file_name_check("123") == "No"
assert file_name_check("hello.world") == "No"
assert file_name_check(".hello.world") == "No"
assert file_name_check("helloworld") == "No"
assert file_name_check("helloworld123.exe.") == "No"
assert file_name_check("helloworld123.exe.helloworld") == "No"
assert file_name_check('..dll') == 'No'
assert file_name_check('a.b.c.exe') == 'No'
assert file_name_check('0ab.txt') == 'No'
assert file_name_check('001a.txt') == 'No'
assert file_name_check('03.exe') == 'No'
assert file_name_check('00.exe') == 'No'
assert file_name_check('00a.exe') == 'No'
assert file_name_check('abc12..') == 'No'
assert file_name_check('abc12..abc') == 'No'
assert file_name_check('abc123.abc') == 'No'
assert file_name_check("hello.exe") == "Yes"
assert file_name_check("hello.dll") == "Yes"
assert file_name_check('0123456.exe.dll') == 'No'
assert file_name_check('123.exe') == 'No'
assert file_name_check('0123.exe') == 'No'
assert file_name_check('hello.exe') == 'Yes'
assert file_name_check('123.tEx') == 'No'
assert file_name_check('123.tEx.dll') == 'No'
assert file_name_check('123.txt') == 'No'
assert file_name_check('123.exe   ') == 'No'
assert file_name_check('123_') == 'No'
assert file_name_check('123.exee') == 'No'
assert file_name_check('a') == 'No', 'invalid file name'
assert file_name_check('a.bc.def') == 'No', 'invalid file name'
assert file_name_check('abc') == 'No', 'invalid file name'
assert file_name_check('1abcde.txt') == 'No'
assert file_name_check('1exede.txt') == 'No'
assert file_name_check('1.dllde.txt') == 'No'
assert file_name_check('123.dll') == 'No'
assert file_name_check('aaa.') == ('No')

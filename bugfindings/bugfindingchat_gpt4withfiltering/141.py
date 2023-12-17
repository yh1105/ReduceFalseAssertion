
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
assert file_name_check("file.txt") == 'Yes'
assert file_name_check("file.exe") == 'Yes'
assert file_name_check("file.dll") == 'Yes'
assert file_name_check("file.txt.exe") == 'No'
assert file_name_check("file") == 'No'
assert file_name_check("file.txt1") == 'No'
assert file_name_check("file.123") == 'No'
assert file_name_check("file.") == 'No'
assert file_name_check("file.txt.dll") == 'No'
assert file_name_check("file.txt.txt") == 'No'
assert file_name_check("file.exe.txt") == 'No'
assert file_name_check("file.dll.txt") == 'No'
assert file_name_check("file.123.txt") == 'No'
assert file_name_check("file.txt.123") == 'No'
assert file_name_check("file.txt123") == 'No'
assert file_name_check('file.exe') == 'Yes'
assert file_name_check('file.dll') == 'Yes'
assert file_name_check('file.txt.txt') == 'No'
assert file_name_check('file.') == 'No'
assert file_name_check('file') == 'No'
assert file_name_check('file.pdf') == 'No'
assert file_name_check('file.doc') == 'No'
assert file_name_check("file.exe") == "Yes"
assert file_name_check("file.dll") == "Yes"
assert file_name_check("file.") == "No"
assert file_name_check("file") == "No"
assert file_name_check("file.txt.exe") == "No"
assert file_name_check("file.tx") == "No"
assert file_name_check("file.doc") == "No"
assert file_name_check("file..txt") == "No"
assert file_name_check("file.abc") == "No"
assert file_name_check("file.123") == "No"
assert file_name_check("file.txt.dll") == "No"
assert file_name_check("file.txt.abc") == "No"
assert file_name_check("file.123.txt") == "No"
assert file_name_check("file.123.exe") == "No"
assert file_name_check("file.123.dll") == "No"
assert file_name_check("file.123.abc") == "No"
assert file_name_check("file.abc.txt") == "No"
assert file_name_check("file.abc.exe") == "No"
assert file_name_check("file.abc.dll") == "No"
assert file_name_check("file.abc.123") == "No"
assert file_name_check("file.txt.abc.exe") == "No"
assert file_name_check("file.txt.exe.abc") == "No"
assert file_name_check("file.txt.123.abc") == "No"
assert file_name_check("file.123.txt.abc") == "No"
assert file_name_check("file.abc.txt.123") == "No"
assert file_name_check("file.abc.123.txt") == "No"
assert file_name_check("file.123.abc.txt") == "No"
assert file_name_check("file.123.txt.abc.exe") == "No"
assert file_name_check("file.123.exe.abc.txt") == "No"
assert file_name_check("file.123.abc.txt.exe") == "No"
assert file_name_check("file.abc.txt.123.exe") == "No"
assert file_name_check("file.abc.exe.123.txt") == "No"
assert file_name_check("file.abc.123.txt.exe") == "No"
assert file_name_check("file.123.txt.abc.exe.dll") == "No"
assert file_name_check("file.123.exe.abc.txt.dll") == "No"
assert file_name_check("file.123.abc.txt.exe.dll") == "No"
assert file_name_check("file.abc.txt.123.exe.dll") == "No"
assert file_name_check("file.abc.exe.123.txt.dll") == "No"
assert file_name_check("file.abc.123.txt.exe.dll") == "No"
assert file_name_check("file.123.txt.abc.exe.dll.dll") == "No"
assert file_name_check("file.123.exe.abc.txt.dll.dll") == "No"
assert file_name_check("file.123.abc.txt.exe.dll.dll") == "No"
assert file_name_check("file.abc.txt.123.exe.dll.dll") == "No"
assert file_name_check("file.abc.exe.123.txt.dll.dll") == "No"
assert file_name_check("file.abc.123.txt.exe.dll.dll") == "No"
assert file_name_check("file.123.txt.abc.exe.dll.dll.dll") == "No"
assert file_name_check("file.123.exe.abc.txt.dll.dll.dll") == "No"
assert file_name_check("file.123.abc.txt.exe.dll.dll.dll") == "No"
assert file_name_check("file.abc.txt.123.exe.dll.dll.dll") == "No"
assert file_name_check("file.abc.exe.123.txt.dll.dll.dll") == "No"
assert file_name_check("file.abc.123.txt.exe.dll.dll.dll") == "No"
assert file_name_check("file.txt.doc") == "No"
assert file_name_check("file.txt.docx") == "No"
assert file_name_check('file..txt') == 'No'
assert file_name_check('file.txt.exe') == 'No'
assert file_name_check('file.txt.dll') == 'No'
assert file_name_check('file.txt1') == 'No'
assert file_name_check('file1.txt1') == 'No'
assert file_name_check('file1.txt2') == 'No'
assert file_name_check('file1.txt3') == 'No'
assert file_name_check('file1.txt4') == 'No'
assert file_name_check('file1.txt5') == 'No'
assert file_name_check('file1.txt6') == 'No'
assert file_name_check('file1.txt7') == 'No'
assert file_name_check('file1.txt8') == 'No'
assert file_name_check('file1.txt9') == 'No'
assert file_name_check('file1000.txt') == 'No'
assert file_name_check('file.txt.txt.txt') == 'No'
assert file_name_check('file.txt.txt.txt.txt') == 'No'
assert file_name_check("file..txt") == 'No'
assert file_name_check('file.exe1') == 'No'
assert file_name_check('file.dll1') == 'No'
assert file_name_check("file.doc") == 'No'
assert file_name_check("file1234.txt") == 'No'
assert file_name_check('file.txt123') == 'No'
assert file_name_check('file.txt.123') == 'No'
assert file_name_check('file123.txt.exe') == 'No'
assert file_name_check('file..dll') == 'No'
assert file_name_check('file.dll.dll') == 'No'
assert file_name_check('file.dll123') == 'No'
assert file_name_check('file.dll.123') == 'No'
assert file_name_check('file.exe.exe') == 'No'
assert file_name_check('file.123.txt') == 'No'
assert file_name_check('123.txt') == 'No'
assert file_name_check('file.txt.tmp') == 'No'
assert file_name_check('file.txt.') == 'No'
assert file_name_check('file..') == 'No'
assert file_name_check("file.tx") == 'No'
assert file_name_check("filetxt") == 'No'
assert file_name_check("file.exe1") == 'No'
assert file_name_check("file.dll1") == 'No'
assert file_name_check('file.dl') == 'No'
assert file_name_check("file.txt123") == "No"
assert file_name_check("file123.txt123") == "No"
assert file_name_check("file.txt.") == "No"
assert file_name_check("file.txt1") == "No"
assert file_name_check("file.txtdll") == "No"
assert file_name_check("file.dlltxt") == "No"
assert file_name_check("file.txtdlltxt") == "No"
assert file_name_check("test.exe") == 'Yes'
assert file_name_check("test.dll") == 'Yes'
assert file_name_check("test.txt.txt") == 'No'
assert file_name_check("test.exee") == 'No'
assert file_name_check("test.exe.dll") == 'No'
assert file_name_check("test") == 'No'
assert file_name_check("test.") == 'No'
assert file_name_check("test.txt.exe") == 'No'
assert file_name_check("test.exe.txt") == 'No'
assert file_name_check("test123.txt123") == 'No'
assert file_name_check("test..txt") == 'No'
assert file_name_check("test.exe.dl") == 'No'
assert file_name_check("test123.txt.") == 'No'
assert file_name_check("test123..txt") == 'No'
assert file_name_check("test123.exe..") == 'No'
assert file_name_check("test123.txt123.txt") == 'No'
assert file_name_check("test123.txt123.exe") == 'No'
assert file_name_check("test123.exe123.txt") == 'No'
assert file_name_check("abc.exe") == "Yes"
assert file_name_check("abc.dll") == "Yes"
assert file_name_check("abc.123.txt") == "No"
assert file_name_check("abc..txt") == "No"
assert file_name_check("abc.txt.exe") == "No"
assert file_name_check("abc.txt.dl") == "No"
assert file_name_check("abc.") == "No"
assert file_name_check("abc") == "No"
assert file_name_check("123.txt") == "No"
assert file_name_check("abc.dll123") == "No"
assert file_name_check("abc.txt.") == "No"
assert file_name_check("abc.txt.txt") == "No"
assert file_name_check("abc.txt.dll") == "No"
assert file_name_check("file.txt.txt") == "No"
assert file_name_check("file.png") == "No"
assert file_name_check("file.exe.exe") == "No"
assert file_name_check("file.dll.dll") == "No"
assert file_name_check('abc.exe') == 'Yes'
assert file_name_check('abc.dll') == 'Yes'
assert file_name_check('abc.txt.exe') == 'No'
assert file_name_check('abc') == 'No'
assert file_name_check('abc.') == 'No'
assert file_name_check('abc.pdf') == 'No'
assert file_name_check('abc.txt.pdf') == 'No'
assert file_name_check("file.txt.exe.dll") == 'No'
assert file_name_check("file1.2.txt") == 'No'
assert file_name_check('file.123') == 'No'
assert file_name_check('file.exe.dll') == 'No'
assert file_name_check('file.tx') == 'No'
assert file_name_check('file.t') == 'No'
assert file_name_check('file.txxt') == 'No'
assert file_name_check('file.tx1t') == 'No'
assert file_name_check('file.tx12t') == 'No'
assert file_name_check('file.tx123t') == 'No'
assert file_name_check("file.txt.exe.dll") == "No"
assert file_name_check("file.txxt") == 'No'
assert file_name_check("file.tx1t") == 'No'
assert file_name_check("file.tx12t") == 'No'
assert file_name_check("file.tx123t") == 'No'
assert file_name_check("file.txt.tx") == 'No'
assert file_name_check("file.txt.txxt") == 'No'
assert file_name_check("file.txt.tx1t") == 'No'
assert file_name_check("file.txt.tx12t") == 'No'
assert file_name_check("file.txt.tx123t") == 'No'
assert file_name_check('file1.2.txt') == 'No'
assert file_name_check('file.txt.dll.txt') == 'No'
assert file_name_check('file.txt.dll.exe') == 'No'
assert file_name_check('file.txt.dll.dll') == 'No'
assert file_name_check('file.txt.exe.dll') == 'No'
assert file_name_check('file.exe.txt.dll') == 'No'
assert file_name_check('file.exe.dll.txt') == 'No'
assert file_name_check('file.dll.txt.exe') == 'No'
assert file_name_check('file.dll.exe.txt') == 'No'
assert file_name_check('file.dll.dll.txt') == 'No'
assert file_name_check('file.dll.dll.dll') == 'No'
assert file_name_check('file.exe.exe.exe') == 'No'
assert file_name_check('file.txt.txt.exe') == 'No'
assert file_name_check('file.txt.exe.txt') == 'No'
assert file_name_check('file.exe.txt.txt') == 'No'
assert file_name_check('file.exe.txt.exe') == 'No'
assert file_name_check('file.dll.txt.dll') == 'No'
assert file_name_check('file.txt.txt.dll') == 'No'
assert file_name_check("hello.txt.exe") == "No"
assert file_name_check("hello.txt.doc") == "No"
assert file_name_check("hello..txt") == "No"
assert file_name_check("hello.txt.") == "No"
assert file_name_check("hello") == "No"
assert file_name_check("hello.txt.123") == "No"
assert file_name_check('file.abc') == 'No'
assert file_name_check('file.exe.txt') == 'No'
assert file_name_check('file.dll.txt') == 'No'
assert file_name_check('abc..txt') == 'No'
assert file_name_check('abc.123.txt') == 'No'
assert file_name_check('abc.txT') == 'No'
assert file_name_check('abc.TXt') == 'No'
assert file_name_check('abc.TXT') == 'No'
assert file_name_check('abc.txt1') == 'No'
assert file_name_check('abc.txt.txt') == 'No'
assert file_name_check('file.txt.exe.') == 'No'
assert file_name_check('file.txt.exe.dll.') == 'No'
assert file_name_check('file.123.txt.exe') == 'No'
assert file_name_check('file.txt.123.exe') == 'No'
assert file_name_check('file.txt.exe.123') == 'No'
assert file_name_check('file.123.txt.exe.dll') == 'No'
assert file_name_check('file.txt.123.exe.dll') == 'No'
assert file_name_check('file.txt.exe.123.dll') == 'No'
assert file_name_check('file.txt.exe.dll.123') == 'No'
assert file_name_check('file.123.txt.123') == 'No'
assert file_name_check('file.txt.123.123') == 'No'
assert file_name_check('file.txt.exe.123.123') == 'No'
assert file_name_check('file.123.txt.123.123') == 'No'
assert file_name_check('file.txt.123.123.123') == 'No'
assert file_name_check('file.txt.exe.123.123.123') == 'No'
assert file_name_check("file123.txt.exe") == "No"
assert file_name_check("file123.txt.dll") == "No"
assert file_name_check("file123.txt.abc") == "No"
assert file_name_check('abc.txt.exe.dll') == 'No'
assert file_name_check('abc.txt.doc') == 'No'
assert file_name_check('abc.txt.ex') == 'No'
assert file_name_check('abc.txt.dl') == 'No'
assert file_name_check('abc.txt.dlll') == 'No'
assert file_name_check('abc.txt.dl0') == 'No'
assert file_name_check('abc.txt.dl1') == 'No'
assert file_name_check('abc.txt.dl2') == 'No'
assert file_name_check('abc.txt.dl4') == 'No'
assert file_name_check("file.txt.123") == "No"
assert file_name_check("file.exe.txt") == "No"
assert file_name_check("file.dll.txt") == "No"
assert file_name_check("file.txt12") == "No"
assert file_name_check("file.txt.") == 'No'
assert file_name_check("file.exe.dll") == 'No'
assert file_name_check("file.dll.exe") == 'No'
assert file_name_check("file1.txt.txt") == 'No'
assert file_name_check("file1..txt") == 'No'
assert file_name_check("file1.txt.") == 'No'
assert file_name_check("file1.txt.exe") == 'No'
assert file_name_check("file1.txt.dll") == 'No'
assert file_name_check("file1.exe.txt") == 'No'
assert file_name_check("file1.exe.dll") == 'No'
assert file_name_check("file1.dll.txt") == 'No'
assert file_name_check("file1.dll.exe") == 'No'
assert file_name_check("file12.txt.txt") == 'No'
assert file_name_check("file12..txt") == 'No'
assert file_name_check("file12.txt.") == 'No'
assert file_name_check("file12.txt.exe") == 'No'
assert file_name_check("file12.txt.dll") == 'No'
assert file_name_check("file12.exe.txt") == 'No'
assert file_name_check("file12.exe.dll") == 'No'
assert file_name_check("file12.dll.txt") == 'No'
assert file_name_check("file12.dll.exe") == 'No'
assert file_name_check("file123.txt.txt") == 'No'
assert file_name_check("file123..txt") == 'No'
assert file_name_check("file123.txt.") == 'No'
assert file_name_check("file123.txt.exe") == 'No'
assert file_name_check("file123.txt.dll") == 'No'
assert file_name_check("file123.exe.txt") == 'No'
assert file_name_check("file123.exe.dll") == 'No'
assert file_name_check("file123.dll.txt") == 'No'
assert file_name_check("file123.dll.exe") == 'No'
assert file_name_check("file.txx") == 'No'
assert file_name_check("file.txtt") == 'No'
assert file_name_check('abc123456.txt') == 'No'
assert file_name_check('abc.doc') == 'No'
assert file_name_check("file1.abc") == "No"
assert file_name_check("file.txt.dll2") == 'No'
assert file_name_check("file.txt.dll.") == 'No'
assert file_name_check("file.txt.dll.txt") == 'No'
assert file_name_check("file.txt.dll.exe") == 'No'
assert file_name_check("file.txt.dll.dll") == 'No'
assert file_name_check('file.txt2') == 'No'
assert file_name_check('file..exe') == 'No'
assert file_name_check('file.txt3') == 'No'
assert file_name_check('file..dlll') == 'No'
assert file_name_check('file.txt4') == 'No'
assert file_name_check('file...dll') == 'No'
assert file_name_check('file.txt5') == 'No'
assert file_name_check('file..dllll') == 'No'
assert file_name_check("text.exe") == 'Yes'
assert file_name_check("text.dll") == 'Yes'
assert file_name_check("text") == 'No'
assert file_name_check("text.abc") == 'No'
assert file_name_check("text.123") == 'No'
assert file_name_check("text.abc.exe") == 'No'
assert file_name_check("text.123.txt") == 'No'
assert file_name_check("text.txt.exe") == 'No'
assert file_name_check("myfile") == "No"
assert file_name_check("my_file") == "No"
assert file_name_check("myfile.txt.exe") == "No"
assert file_name_check("my_file.") == "No"
assert file_name_check("my_file.txt.dll") == "No"
assert file_name_check("123.txt") == 'No'
assert file_name_check("file.txt.txt.txt") == "No"
assert file_name_check("file.txt.exe.exe") == "No"
assert file_name_check("file.txt.dll.dll") == "No"
assert file_name_check("file.txt.doc.doc") == "No"
assert file_name_check("file.txt.pdf") == "No"
assert file_name_check("file.txt.jpg") == "No"
assert file_name_check('abc.123') == 'No'
assert file_name_check('abc.txt.dll.exe') == 'No'
assert file_name_check('abc.txt.exe1') == 'No'
assert file_name_check('abc.txt.dll1') == 'No'
assert file_name_check('abc.txt.dll.') == 'No'
assert file_name_check('abc.txt.dll..') == 'No'
assert file_name_check('abc.txt.dll...') == 'No'
assert file_name_check('abc.txt.dll....') == 'No'
assert file_name_check('abc.txt.dll.....') == 'No'
assert file_name_check('abc.txt.dll......') == 'No'
assert file_name_check('abc.txt.dll.......') == 'No'
assert file_name_check('abc.txt.dll........') == 'No'
assert file_name_check('abc.txt.dll.........') == 'No'
assert file_name_check('abc.txt.dll..........') == 'No'
assert file_name_check('abc.txt.dll...........') == 'No'
assert file_name_check('abc.txt.dll............') == 'No'
assert file_name_check('abc.txt.dll.............') == 'No'
assert file_name_check('abc.txt.dll..............') == 'No'
assert file_name_check('abc.txt.dll...............') == 'No'
assert file_name_check('abc.txt.dll................') == 'No'
assert file_name_check('abc.txt.dll.................') == 'No'
assert file_name_check('abc.txt.dll..................') == 'No'
assert file_name_check('abc.txt.dll...................') == 'No'
assert file_name_check('abc.txt.dll....................') == 'No'
assert file_name_check('abc.txt.dll.....................') == 'No'
assert file_name_check('abc.txt.dll......................') == 'No'
assert file_name_check('abc.txt.dll.......................') == 'No'
assert file_name_check('abc.txt.dll........................') == 'No'
assert file_name_check('abc.txt.dll.........................') == 'No'
assert file_name_check('abc.txt.dll..........................') == 'No'
assert file_name_check('abc.txt.dll...........................') == 'No'
assert file_name_check('abc.txt.dll............................') == 'No'
assert file_name_check('abc.txt.dll.............................') == 'No'
assert file_name_check('abc.txt.dll..............................') == 'No'
assert file_name_check('abc.txt.dll...............................') == 'No'
assert file_name_check('abc.txt.dll................................') == 'No'
assert file_name_check('abc.txt.dll.................................') == 'No'
assert file_name_check('abc.txt.dll..................................') == 'No'
assert file_name_check('abc.txt.dll...................................') == 'No'
assert file_name_check('abc.txt.dll....................................') == 'No'
assert file_name_check('abc.txt.dll.....................................') == 'No'
assert file_name_check('abc.txt.dll......................................') == 'No'
assert file_name_check('abc.txt.dll.......................................') == 'No'
assert file_name_check('abc.txt.dll........................................') == 'No'
assert file_name_check('abc.txt.dll.........................................') == 'No'
assert file_name_check('abc.txt.dll..........................................') == 'No'
assert file_name_check('abc.txt.dll...........................................') == 'No'
assert file_name_check('abc.txt.dll............................................') == 'No'
assert file_name_check('abc.txt.dll.............................................') == 'No'
assert file_name_check('abc.txt.dll..............................................') == 'No'
assert file_name_check('abc.txt.dll...............................................') == 'No'
assert file_name_check('abc.txt.dll................................................') == 'No'
assert file_name_check('abc.txt.dll.................................................') == 'No'
assert file_name_check('abc.txt.dll..................................................') == 'No'
assert file_name_check('abc.txt.dll...................................................') == 'No'
assert file_name_check('abc.txt.dll....................................................') == 'No'
assert file_name_check('abc.txt.dll.....................................................') == 'No'
assert file_name_check('abc.txt.dll......................................................') == 'No'
assert file_name_check('abc.txt.dll.......................................................') == 'No'
assert file_name_check('abc.txt.dll........................................................') == 'No'
assert file_name_check('abc.txt.dll.........................................................') == 'No'
assert file_name_check("file.txt.exe123") == "No"
assert file_name_check("file.txt123.exe") == "No"
assert file_name_check("file.txt123.exe123") == "No"
assert file_name_check("file..dll") == "No"
assert file_name_check("file.txt") == "Yes"
assert file_name_check('file.py') == 'No'
assert file_name_check("abc.123") == "No"
assert file_name_check('file.jpg') == 'No'
assert file_name_check("file.txt.exe.txt") == "No"
assert file_name_check("file.exe.txt.exe") == "No"
assert file_name_check("file.dll.txt.dll") == "No"
assert file_name_check("file.exe.txt.dll") == "No"
assert file_name_check("file.dll.txt.exe") == "No"
assert file_name_check("file.txt.dll.exe") == "No"
assert file_name_check("file.exe.dll.txt") == "No"
assert file_name_check("file.dll.exe.txt") == "No"
assert file_name_check('file.tx1') == 'No'
assert file_name_check('file.txT') == 'No'
assert file_name_check('file.TxT') == 'No'
assert file_name_check('file.TxT.txt') == 'No'
assert file_name_check('file.dll.exe') == 'No'
assert file_name_check('file.tx2') == 'No'
assert file_name_check('file.tx3') == 'No'
assert file_name_check('file.tx4') == 'No'
assert file_name_check('file.tx5') == 'No'
assert file_name_check('file.tx6') == 'No'
assert file_name_check('file.tx7') == 'No'
assert file_name_check('file.tx8') == 'No'
assert file_name_check('file.tx9') == 'No'
assert file_name_check('file.12') == 'No'
assert file_name_check('file.1') == 'No'
assert file_name_check('file.exe.') == 'No'
assert file_name_check('file.dll.') == 'No'
assert file_name_check('file.tx.') == 'No'
assert file_name_check('file.TX') == 'No'
assert file_name_check('file.Tx') == 'No'
assert file_name_check('file.tX') == 'No'
assert file_name_check('file.TXt') == 'No'
assert file_name_check('file.TXt.txt') == 'No'
assert file_name_check('file.TXt.exe') == 'No'
assert file_name_check('file.TxT.exe') == 'No'
assert file_name_check('file.TXt.dll') == 'No'
assert file_name_check('file.TxT.dll') == 'No'
assert file_name_check("file.txtdll") == 'No'
assert file_name_check("abc.txt.123") == "No"
assert file_name_check("abc.tx") == "No"
assert file_name_check("abc.ttx") == "No"
assert file_name_check("abc.texe") == "No"
assert file_name_check("abc.tdll") == "No"
assert file_name_check("abc.ttxt") == "No"
assert file_name_check("abc.txxt") == "No"
assert file_name_check("abc.txte") == "No"
assert file_name_check("abc.tdl") == "No"
assert file_name_check("abc.txx") == "No"
assert file_name_check("abc.txex") == "No"
assert file_name_check("abc.td") == "No"
assert file_name_check("abc.txtxt") == "No"
assert file_name_check("abc.txtexe") == "No"
assert file_name_check("abc.txtdll") == "No"
assert file_name_check("abc.txttxt") == "No"
assert file_name_check("abc.txtx") == "No"
assert file_name_check("abc.txtex") == "No"
assert file_name_check("abc.txtd") == "No"
assert file_name_check("abc.exeexe") == "No"
assert file_name_check("abc.exedll") == "No"
assert file_name_check("abc.exetxt") == "No"
assert file_name_check("abc.exex") == "No"
assert file_name_check("abc.exed") == "No"
assert file_name_check("abc.dlldll") == "No"
assert file_name_check("abc.dlltxt") == "No"
assert file_name_check("abc.dllx") == "No"
assert file_name_check("abc.dlld") == "No"
assert file_name_check("abc.txtexeexe") == "No"
assert file_name_check("abc.txtexedll") == "No"
assert file_name_check("abc.txtexetxt") == "No"
assert file_name_check("abc.txtexex") == "No"
assert file_name_check("abc.txtexed") == "No"
assert file_name_check("abc.txtdlltxt") == "No"
assert file_name_check("abc.txtdllx") == "No"
assert file_name_check("abc.txtdlld") == "No"
assert file_name_check("abc.exetxtexe") == "No"
assert file_name_check("abc.exetxtdll") == "No"
assert file_name_check("abc.exetxtd") == "No"
assert file_name_check("abc.exexexe") == "No"
assert file_name_check("abc.exexdll") == "No"
assert file_name_check("abc.exexd") == "No"
assert file_name_check("abc.exedlle") == "No"
assert file_name_check("abc.exedlll") == "No"
assert file_name_check("abc.exedllld") == "No"
assert file_name_check("abc.dlle") == "No"
assert file_name_check("abc.dlll") == "No"
assert file_name_check("abc.dllld") == "No"
assert file_name_check("file.txt.exe.dll1") == "No"
assert file_name_check("file.txt.exe.dll2") == "No"
assert file_name_check("file.txt.exe.dll3") == "No"
assert file_name_check("file.txt.exe.dll123") == "No"
assert file_name_check("file.txt.exe.dll1234") == "No"
assert file_name_check("file.txt.exe.dll12345") == "No"
assert file_name_check("file.txt.exe.dll123456") == "No"
assert file_name_check("file.txt.exe.dll1234567") == "No"
assert file_name_check("file.txt.exe.dll12345678") == "No"
assert file_name_check("file.txt.exe.dll123456789") == "No"
assert file_name_check("file.txt.exe.dll1234567890") == "No"
assert file_name_check("file.txt.exe.dll12345678901") == "No"
assert file_name_check("file.txt.exe.dll123456789012") == "No"
assert file_name_check("file.txt.exe.dll1234567890123") == "No"
assert file_name_check("file.txt.exe.dll12345678901234") == "No"
assert file_name_check("file.txt.exe.dll123456789012345") == "No"
assert file_name_check("file.txt.exe.dll1234567890123456") == "No"
assert file_name_check("file.txt.exe.dll12345678901234567") == "No"
assert file_name_check("file.txt.exe.dll123456789012345678") == "No"
assert file_name_check("file.txt.exe.dll1234567890123456789") == "No"
assert file_name_check("file.txt.exe.dll12345678901234567890") == "No"
assert file_name_check("file.txt.exe.dll123456789012345678901") == "No"
assert file_name_check("file.txt.exe.dll1234567890123456789012") == "No"
assert file_name_check("file.txt.exe.dll12345678901234567890123") == "No"
assert file_name_check("file.txt.exe.dll123456789012345678901234") == "No"
assert file_name_check("file.txt.exe.dll1234567890123456789012345") == "No"
assert file_name_check("file.txt.exe.dll12345678901234567890123456") == "No"
assert file_name_check("file.txt.exe.dll123456789012345678901234567") == "No"
assert file_name_check("file.txt.exe.dll1234567890123456789012345678") == "No"
assert file_name_check("file.txt.exe.dll12345678901234567890123456789") == "No"
assert file_name_check("file.txt.exe.dll123456789012345678901234567890") == "No"
assert file_name_check("file.txt.exe.dll1234567890123456789012345678901") == "No"
assert file_name_check("file.txt.exe.dll12345678901234567890123456789012") == "No"
assert file_name_check("file.txt.exe.dll123456789012345678901234567890123") == "No"
assert file_name_check("file.txt.exe.dll1234567890123456789012345678901234") == "No"
assert file_name_check("file.txt.exe.dll12345678901234567890123456789012345") == "No"
assert file_name_check("file.txt.exe.dll123456789012345678901234567890123456") == "No"
assert file_name_check("file.txt.exe.dll1234567890123456789012345678901234567") == "No"
assert file_name_check("file.txt.exe.dll12345678901234567890123456789012345678") == "No"
assert file_name_check("file.txt.exe.dll123456789012345678901234567890123456789") == "No"
assert file_name_check("file.txt.exe.dll1234567890123456789012345678901234567890") == "No"
assert file_name_check("file.txt.exe.dll12345678901234567890123456789012345678901") == "No"
assert file_name_check("file.txt.exe.dll123456789012345678901234567890123456789012") == "No"
assert file_name_check("file.txt.exe.dll1234567890123456789012345678901234567890123") == "No"
assert file_name_check('file.abc.exe') == 'No'
assert file_name_check('file.abc.dll') == 'No'
assert file_name_check('file.abc.123') == 'No'
assert file_name_check('file.txt.abc') == 'No'
assert file_name_check('file.txt.abc.exe') == 'No'
assert file_name_check('file.txt.abc.dll') == 'No'
assert file_name_check('file.txt.abc.123') == 'No'
assert file_name_check('abc.1234.txt') == 'No'
assert file_name_check("file.txt.jpg") == 'No'
assert file_name_check("file.txt.exe.dll.jpg") == 'No'
assert file_name_check("abc.txt.tx") == "No"
assert file_name_check("file.txt1.exe") == 'No'
assert file_name_check("file.txt1.txt") == 'No'
assert file_name_check("file.txtx") == "No"
assert file_name_check("file.txxt") == "No"
assert file_name_check('abc.txt.dll') == 'No'
assert file_name_check('filetxt') == 'No'
assert file_name_check('file.1.2.3') == 'No'
assert file_name_check('file.txt..') == 'No'
assert file_name_check('file.txt.exe..') == 'No'
assert file_name_check('file.txt.exe.dll..') == 'No'
assert file_name_check("file.txt.dl") == "No"
assert file_name_check("file.txt.dll2") == "No"
assert file_name_check("file.txt.d11") == "No"
assert file_name_check("file.txt.d1l") == "No"
assert file_name_check("file.exe.dll") == "No"
assert file_name_check("file.dll.exe") == "No"
assert file_name_check("file.exe1") == "No"
assert file_name_check("file.dll1") == "No"
assert file_name_check("file.txt2") == "No"
assert file_name_check("file.exe2") == "No"
assert file_name_check("file.dll2") == "No"
assert file_name_check("file.txt3") == "No"
assert file_name_check("file.exe3") == "No"
assert file_name_check("file.dll3") == "No"
assert file_name_check("file.txt4") == "No"
assert file_name_check("file.exe4") == "No"
assert file_name_check("file.dll4") == "No"
assert file_name_check("file.txt5") == "No"
assert file_name_check("file.exe5") == "No"
assert file_name_check("file.dll5") == "No"
assert file_name_check("file.txt6") == "No"
assert file_name_check("file.exe6") == "No"
assert file_name_check("file.dll6") == "No"
assert file_name_check("file.txt7") == "No"
assert file_name_check("file.exe7") == "No"
assert file_name_check("file.dll7") == "No"
assert file_name_check("file.txt8") == "No"
assert file_name_check("file.exe8") == "No"
assert file_name_check("file.dll8") == "No"
assert file_name_check("file.txt9") == "No"
assert file_name_check("file.exe9") == "No"
assert file_name_check("file.dll9") == "No"
assert file_name_check("file..exe") == "No"
assert file_name_check("file.exe.") == "No"
assert file_name_check("file.dll.") == "No"
assert file_name_check("file1.txt.txt") == "No"
assert file_name_check("file2.exe.exe") == "No"
assert file_name_check("file3.dll.dll") == "No"
assert file_name_check("file.txt..txt") == "No"
assert file_name_check("file.exe..exe") == "No"
assert file_name_check("file.dll..dll") == "No"
assert file_name_check("file.txt.txt.") == "No"
assert file_name_check("file.exe.exe.") == "No"
assert file_name_check("file.dll.dll.") == "No"
assert file_name_check("file..txt.txt") == "No"
assert file_name_check("file..exe.exe") == "No"
assert file_name_check("file..dll.dll") == "No"
assert file_name_check("file.txt.txt2") == "No"
assert file_name_check("file.exe.exe2") == "No"
assert file_name_check("file.dll.dll2") == "No"
assert file_name_check("file.txt2.txt") == "No"
assert file_name_check("file.exe2.exe") == "No"
assert file_name_check("file.dll2.dll") == "No"
assert file_name_check("file.txt2.txt2") == "No"
assert file_name_check("file.exe2.exe2") == "No"
assert file_name_check("file.dll2.dll2") == "No"
assert file_name_check("file.txt.txt3") == "No"
assert file_name_check("file.exe.exe3") == "No"
assert file_name_check("file.dll.dll3") == "No"
assert file_name_check("file.txt3.txt") == "No"
assert file_name_check("abc.exe") == 'Yes'
assert file_name_check("abc.dll") == 'Yes'
assert file_name_check("abc.tx") == 'No'
assert file_name_check("abc.txte") == 'No'
assert file_name_check("abc.txtdll") == 'No'
assert file_name_check("abc..txt") == 'No'
assert file_name_check("abc") == 'No'
assert file_name_check("abc.txt.txt") == 'No'
assert file_name_check("abc.txt.exe") == 'No'
assert file_name_check("abc.txt.dll") == 'No'
assert file_name_check("abc.exe.txt") == 'No'
assert file_name_check("abc.exe.exe") == 'No'
assert file_name_check("abc.exe.dll") == 'No'
assert file_name_check("abc.dll.txt") == 'No'
assert file_name_check("abc.dll.exe") == 'No'
assert file_name_check("abc.dll.dll") == 'No'
assert file_name_check("abc.txt.txte") == 'No'
assert file_name_check("abc.txt.txtdll") == 'No'
assert file_name_check("abc.txt.txte.dll") == 'No'
assert file_name_check("abc.exe.txte") == 'No'
assert file_name_check("abc.exe.txtdll") == 'No'
assert file_name_check("abc.exe.txte.dll") == 'No'
assert file_name_check("abc.dll.txte") == 'No'
assert file_name_check("abc.dll.txtdll") == 'No'
assert file_name_check("abc.dll.txte.dll") == 'No'
assert file_name_check("file.abc") == 'No'
assert file_name_check("file.txt2") == 'No'
assert file_name_check("file.abc.txt") == 'No'
assert file_name_check("file.txt.doc.dll") == "No"
assert file_name_check("file.txt.doc.doc.doc") == "No"
assert file_name_check('file.txt.exe.dll1') == 'No'
assert file_name_check('file.txt1.exe') == 'No'
assert file_name_check('file1.txt.exe') == 'No'
assert file_name_check('file.txt1.dll') == 'No'
assert file_name_check('file.dll.txt1') == 'No'
assert file_name_check('file1.txt1.dll1') == 'No'
assert file_name_check('file.dll.exe1.txt') == 'No'
assert file_name_check('file.txt.exe1.dll') == 'No'
assert file_name_check('file.txt1.exe.dll') == 'No'
assert file_name_check('file1.txt.exe.dll') == 'No'
assert file_name_check('file.txt.dll1.exe') == 'No'
assert file_name_check('file.dll1.txt.exe') == 'No'
assert file_name_check('file1.txt1.dll') == 'No'
assert file_name_check('file.dll1.txt1') == 'No'
assert file_name_check('file.dll1.exe1.txt') == 'No'
assert file_name_check('file.txt1.exe1.dll') == 'No'
assert file_name_check('file.txt1.exe1.dll1') == 'No'
assert file_name_check('file1.txt1.exe1.dll') == 'No'
assert file_name_check('file.txt1.dll1.exe1') == 'No'
assert file_name_check('file.dll1.txt1.exe1') == 'No'
assert file_name_check('file1.txt1.dll1.exe1') == 'No'
assert file_name_check('file.dll1.exe1.txt1') == 'No'
assert file_name_check('file.txt1.exe1.dll1.txt') == 'No'
assert file_name_check('file.txt1.exe1.dll1.txt1') == 'No'
assert file_name_check('file.txt1.exe1.dll1.txt1.txt') == 'No'
assert file_name_check('file.txt1.exe1.dll1.txt1.txt1') == 'No'
assert file_name_check('file.txt1.exe1.dll1.txt1.txt1.txt') == 'No'
assert file_name_check('file.txt1.exe1.dll1.txt1.txt1.txt1') == 'No'
assert file_name_check('file.txt.doc') == 'No'
assert file_name_check("file.txt.dll.txt") == "No"
assert file_name_check("file.txt.txt.exe") == "No"
assert file_name_check("file.txt.txt.dll") == "No"
assert file_name_check("file.txt.exe.txt.txt") == "No"
assert file_name_check("file.txt.exe.txt.exe") == "No"
assert file_name_check("file.txt.exe.txt.dll") == "No"
assert file_name_check("file.txt.exe.dll.txt") == "No"
assert file_name_check("file.txt.exe.dll.exe") == "No"
assert file_name_check("file.txt.exe.dll.dll") == "No"
assert file_name_check("file.txt.exe.dll.txt.txt") == "No"
assert file_name_check("file.txt.exe.dll.txt.exe") == "No"
assert file_name_check("file.txt.exe.dll.txt.dll") == "No"
assert file_name_check("file.txt.exe.dll.exe.txt") == "No"
assert file_name_check("file.txt.exe.dll.exe.exe") == "No"
assert file_name_check("file.txt.exe.dll.exe.dll") == "No"
assert file_name_check("file.txt.exe.dll.dll.txt") == "No"
assert file_name_check("file.txt.exe.dll.dll.exe") == "No"
assert file_name_check("file.txt.exe.dll.dll.dll") == "No"
assert file_name_check("file.txt.exe.dll.dll.txt.txt") == "No"
assert file_name_check("file.txt.exe.dll.dll.txt.exe") == "No"
assert file_name_check("file.txt.exe.dll.dll.txt.dll") == "No"
assert file_name_check("file.txt.exe.dll.dll.exe.txt") == "No"
assert file_name_check("file.txt.exe.dll.dll.exe.exe") == "No"
assert file_name_check("file.txt.exe.dll.dll.exe.dll") == "No"
assert file_name_check("file.txt.exe.dll.dll.dll.txt") == "No"
assert file_name_check("file.txt.exe.dll.dll.dll.exe") == "No"
assert file_name_check("file.txt.exe.dll.dll.dll.dll") == "No"
assert file_name_check('file1.txt.dll') == 'No'
assert file_name_check('file1.exe.dll') == 'No'
assert file_name_check('file12.txt.exe') == 'No'
assert file_name_check('file12.txt.dll') == 'No'
assert file_name_check('file12.exe.dll') == 'No'
assert file_name_check('file123.txt.dll') == 'No'
assert file_name_check('file123.exe.dll') == 'No'
assert file_name_check('file.txt..exe') == 'No'
assert file_name_check('file.txt..dll') == 'No'
assert file_name_check('file.txt.dll.') == 'No'
assert file_name_check('file.exe..') == 'No'
assert file_name_check('file.exe..txt') == 'No'
assert file_name_check('file.exe..dll') == 'No'
assert file_name_check('file.exe.txt.') == 'No'
assert file_name_check('file.exe.dll.') == 'No'
assert file_name_check('file.dll..') == 'No'
assert file_name_check('file.dll..txt') == 'No'
assert file_name_check('file.dll..exe') == 'No'
assert file_name_check('file.dll.txt.') == 'No'
assert file_name_check('file.dll.exe.') == 'No'
assert file_name_check("filetxt") == "No"
assert file_name_check("file.texe") == "No"
assert file_name_check("file..") == "No"
assert file_name_check("file...") == "No"
assert file_name_check("file.....") == "No"
assert file_name_check("file.txt.txt.txt.txt") == "No"
assert file_name_check("file.txt.txt.txt.txt.txt") == "No"
assert file_name_check("file.txt.txt.txt.txt.txt.txt") == "No"
assert file_name_check("file.txt.txt.txt.txt.txt.txt.txt") == "No"
assert file_name_check("file.txt.txt.txt.txt.txt.txt.txt.txt") == "No"
assert file_name_check("file.txt.txt.txt.txt.txt.txt.txt.txt.txt") == "No"
assert file_name_check('file.txt.doc.exe') == 'No'
assert file_name_check('abc.txt12') == 'No'
assert file_name_check('abc.exe.txt') == 'No'
assert file_name_check('abc.dll.txt') == 'No'
assert file_name_check('file.ex') == 'No'
assert file_name_check('file.txtt') == 'No'
assert file_name_check('file.txx') == 'No'
assert file_name_check('file.t..xt') == 'No'
assert file_name_check('file.t..x') == 'No'
assert file_name_check('file.t..') == 'No'
assert file_name_check('file.tx..t') == 'No'
assert file_name_check('file.tx..') == 'No'
assert file_name_check('file.tx.t') == 'No'
assert file_name_check('file.xyz') == 'No'

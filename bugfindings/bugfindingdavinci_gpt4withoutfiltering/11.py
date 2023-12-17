from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    def xor(i, j):
        if i == j:
            return '1'
        else:
            return '0'

    return ''.join(xor(x, y) for x, y in zip(a, b))
assert string_xor('1011011', '1011000') == '0000011'
assert string_xor('10001', '10001') == '00000'
assert string_xor('010', '010') == '000'
assert string_xor('1010', '1010') == '0000'
assert string_xor('1111', '1111') == '0000'
assert string_xor('0', '0') == '0'
assert string_xor('1', '0') == '1'
assert string_xor('111', '111') == '000'
assert string_xor('110', '100') == '010'
assert string_xor('0110', '1010') == '1100'
assert string_xor('1010', '0110') == '1100'
assert string_xor('0111', '1111') == '1000'
assert string_xor('1111', '0111') == '1000'
assert string_xor('00111', '11011') == '11100'
assert string_xor('11011', '00111') == '11100'
assert string_xor('11111', '11111') == '00000'
assert string_xor('', '') == ''
assert string_xor('0', '1') == '1'
assert string_xor('1', '1') == '0'
assert string_xor('11001', '01110') == '10111'
assert string_xor('100', '010') == '110'
assert string_xor('100', '110') == '010'
assert string_xor('001', '101') == '100'
assert string_xor('001', '001') == '000'
assert string_xor('10101010', '01010101') == '11111111'
assert string_xor('111111', '111111') == '000000'
assert string_xor('0010111', '1110001') == '1100110'
assert string_xor('10011', '10011') == '00000'
assert string_xor('000', '001') == '001'
assert string_xor('000', '000') == '000'
assert string_xor('000', '111') == '111'
assert string_xor('11', '10') == '01'
assert string_xor('01', '10') == '11'
assert string_xor('101', '011') == '110'
assert string_xor('1100', '1010') == '0110'
assert string_xor('1011', '1011') == '0000'
assert string_xor('10', '10') == '00'
assert string_xor('110', '101') == '011'
assert string_xor('0110', '0110') == '0000'
assert string_xor('11', '01') == '10'
assert string_xor('1010101', '0110011') == '1100110'
assert string_xor('111010', '010100') == '101110'
assert string_xor('01', '01') == '00'
assert string_xor('01', '00') == '01'
assert string_xor('01', '11') == '10'
assert string_xor('10', '11') == '01'
assert string_xor('11', '11') == '00'
assert string_xor('010', '101') == '111'
assert string_xor('100', '000') == '100'
assert string_xor('101', '000') == '101'
assert string_xor('00', '10') == '10'
assert string_xor('111', '011') == '100'
assert string_xor('110', '011') == '101'
assert string_xor('110', '111') == '001'
assert string_xor('', '0') == ''
assert string_xor('00', '01') == '01'
assert string_xor('0000', '0000') == '0000'
assert string_xor('111', '000') == '111'
assert string_xor('0101', '1100') == '1001'
assert string_xor('101', '010') == '111'
assert string_xor('001', '100') == '101'
assert string_xor('11','11') == '00'
assert string_xor('00','01') == '01'
assert string_xor('1111', '0000') == '1111'
assert string_xor('1011', '0110') == '1101'
assert string_xor('11001', '00010') == '11011'
assert string_xor('001', '000') == '001'
assert string_xor('01010', '01010') == '00000'
assert string_xor('01010', '01011') == '00001'
assert string_xor('100', '100') == '000'
assert string_xor('111', '101') == '010'
assert string_xor('10', '01') == '11'
assert string_xor('101', '101') == '000'
assert string_xor('11000011', '00111111') == '11111100'
assert string_xor('00000001', '11111111') == '11111110'
assert string_xor('00', '11') == '11'
assert string_xor('110101', '100100') == '010001'
assert string_xor('001', '110') == '111'
assert string_xor('111', '110') == '001'
assert string_xor('111111', '000000') == '111111'
assert string_xor('000000', '111111') == '111111'
assert string_xor('00', '00') == '00'
assert string_xor('1101', '1001') == '0100'
assert string_xor('0011', '1001') == '1010'
assert string_xor('0000', '1111') == '1111'
assert string_xor('10101010101010101010101010101010', '10101010101010101010101010101010') == '00000000000000000000000000000000'
assert string_xor('101', '110') == '011'
assert string_xor('100100', '110100') == '010000'
assert string_xor('00010011', '11110101') == '11100110'
assert string_xor('1110', '1010') == '0100'
assert string_xor('11011', '11011') == '00000'
assert string_xor('01010101', '01010101') == '00000000'
assert string_xor('101', '111') == '010'
assert string_xor('10', '00') == '10'
assert string_xor('111', '100') == '011'
assert string_xor('11111111', '00000000') == '11111111'
assert string_xor('11111111', '11111111') == '00000000'
assert string_xor('11', '00') == '11'
assert string_xor('1111', '0011') == '1100'
assert string_xor('100', '001') == '101'
assert string_xor('111', '001') == '110'
assert string_xor('000', '101') == '101'
assert string_xor('011', '100') == '111'
assert string_xor('001', '111') == '110'
assert string_xor('100', '011') == '111'
assert string_xor('101', '001') == '100'
assert string_xor('011', '000') == '011'
assert string_xor('010', '111') == '101'
assert string_xor('001011010', '101111010') == '100100000'
assert string_xor('0101', '0110') == '0011'
assert string_xor('1010', '1011') == '0001'
assert string_xor('010101', '010101') == '000000'
assert string_xor('10101', '10101') == '00000'
assert string_xor('001', '011') == '010'
assert string_xor('110', '001') == '111'
assert string_xor('100', '111') == '011'
assert string_xor('0110', '0001') == '0111'
assert string_xor('0101', '0000') == '0101'
assert string_xor('1110', '1001') == '0111'
assert string_xor('0111', '0111') == '0000'
assert string_xor('0101', '0101') == '0000'
assert string_xor('1001', '1001') == '0000'
assert string_xor('1110', '1111') == '0001'
assert string_xor('1010', '0101') == '1111'
assert string_xor('110101', '000101') == '110000'
assert string_xor('1010', '1111') == '0101'
assert string_xor('01100', '10010') == '11110'
assert string_xor('0011100', '0111110') == '0100010'
assert string_xor('110', '110') == '000'
assert string_xor('0101', '0011') == '0110'
assert string_xor('1010', '0011') == '1001'
assert string_xor('0000', '1010') == '1010'
assert string_xor('0001', '0001') == '0000'
assert string_xor('0101', '1010') == '1111'
assert string_xor('0001', '1010') == '1011'
assert string_xor('0100', '1010') == '1110'
assert string_xor('1000', '1010') == '0010'
assert string_xor('1111', '1010') == '0101'
assert string_xor('10011100', '11100100') == '01111000'
assert string_xor('011', '110') == '101'
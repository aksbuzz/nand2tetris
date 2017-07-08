#!/home/aksbuzz/anaconda3/bin/python3
'''
Translates Hack assembly language mnemonics into binary codes.
'''


class Code():
    '''
    Code module that provides the binary codes of all the as-sembly mnemonics
    '''

    def __init__(self):
        '''
        Code module
        '''

    def dest(self, mnemonic):
        '''
        Returns the binary code of the dest mnemonic.

        dest   ||    d1  d2  d3

        null   ||     0   0   0
        M      ||     0   0   1
        D      ||     0   1   0
        MD     ||     0   1   1
        A      ||     1   0   0
        AM     ||     1   0   1
        AD     ||     1   1   0
        AMD    ||     1   1   1

        '''

        dest_vals = {
            '0': '000',
            'null': '000',
            'M': '001',
            'D': '010',
            'MD': '011',
            'A': '100',
            'AM': '101',
            'AD': '110',
            'AMD': '111'
        }

        return dest_vals[mnemonic]

    def comp(self, mnemonic):
        '''
        Returns the binary code of the comp mnemonic.
        '''

        comp_vals_a_is_0 = {
            '0': '101010',
            '1': '111111',
            '-1': '111010',
            'D': '001100',
            'A': '110000',
            '!D': '001101',
            '!A': '110001',
            '-D': '001111',
            '-A': '110011',
            'D+1': '011111',
            'A+1': '110111',
            'D-1': '001110',
            'A-1': '110010',
            'D+A': '000010',
            'D-A': '010011',
            'A-D': '000111',
            'D&A': '000000',
            'D|A': '010101',
        }

        if mnemonic in comp_vals_a_is_0.keys():
            return '0' + comp_vals_a_is_0[mnemonic]

        comp_vals_a_is_1 = {
            'M': '110000',
            '!M': '110001',
            '-M': '110011',
            'M+1': '110111',
            'M-1': '110010',
            'D+M': '000010',
            'D-M': '010011',
            'M-D': '000111',
            'D&M': '000000',
            'D|M': '010101',
        }

        if mnemonic in comp_vals_a_is_1.keys():
            return '1' + comp_vals_a_is_1[mnemonic]

    def jump(self, mnemonic):
        '''
        Returns the binary code of the jump mnemonic.

        jump   ||    j1  j2  j3

        null   ||     0   0   0
        JGT    ||     0   0   1
        JEQ    ||     0   1   0
        JGE    ||     0   1   1
        JLT    ||     1   0   0
        JNE    ||     1   0   1
        JLE    ||     1   1   0
        JMP    ||     1   1   1
        '''

        jump_vals = {
            '0': '000',
            'null': '000',
            'JGT': '001',
            'JEQ': '010',
            'JGE': '011',
            'JLT': '100',
            'JNE': '101',
            'JLE': '110',
            'JMP': '111'
        }

        return jump_vals[mnemonic]

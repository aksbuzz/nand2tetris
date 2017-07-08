#!/home/aksbuzz/anaconda3/bin/python3
'''
Since Hack instructions can contain symbols, the symbols must be resolved into
actual addresses as part of the translation process. The assembler deals with
this task using a symbol table, designed to create and maintain the
correspondence between symbols and their meaning (in Hack’s case, RAM and ROM
addresses).
'''


class SymbolTable(object):
    '''
    Keeps a correspondence between symbolic labels and numeric addresses.
    '''
    def __init__(self):
        '''
        Creates a new empty symbol table.
        '''

        self.table = {
            'SP': 0,
            'LCL': 1,
            'ARG': 2,
            'THIS': 3,
            'THAT': 4,
            'R0': 0,
            'R1': 1,
            'R2': 2,
            'R3': 3,
            'R4': 4,
            'R5': 5,
            'R6': 6,
            'R7': 7,
            'R8': 8,
            'R9': 9,
            'R10': 10,
            'R11': 11,
            'R12': 12,
            'R13': 13,
            'R14': 14,
            'R15': 15,
            'SCREEN': 16384,
            'KBD': 24576
        }

    def addEntry(self, symbol, address):
        '''
        Adds the pair ( symbol ,address ) to the table.
        '''

        self.table[symbol] = address

    def contains(self, symbol):
        '''
        Does the symbol table contain given symbol
        '''

        return True if symbol in self.table else False

    def getAddress(self, symbol):
        '''
        Return the address associated with the symbol
        '''

        return int(self.table[symbol])

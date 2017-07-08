#!/home/aksbuzz/anaconda3/bin/python3
import re
'''
Encapsulates access to the input code. Reads an assembly language command,
parses it, and provides convenient access to the command’s components
(fields and symbols). In addition, removes all white space and comments.
'''


class Parser(object):
    '''
    Parser module that parses the input
    '''

    def __init__(self, file):
        '''
        Opens the input file/stream and gets ready to parse it.
        '''

        self.file = file
        self.stream = self.clean()
        self.current = None
        self.copy = self.stream
        self.size = len(self.stream)

    def hasMoreCommands(self):
        '''
        Are there more commands in the input?
        '''

        return True if len(self.stream) else False

    def clean(self):
        '''remove whitespace, blank lines and comments'''

        dirty = [line.strip() for line in self.file]

        clean = list()

        for command in dirty:

            if re.search(r'//', command):

                if command.startswith('//'):
                    continue

                else:
                    loc = re.search(r"//", command).start()
                    command = command[:loc].strip()

            elif command == '':
                continue

            clean.append(command)

        return clean

    def advance(self):
        '''
        Reads the next command from the input and makes it the current command
        Should be called only if hasMoreCommands()is true.Initially there is
        no current command.
        '''

        if self.hasMoreCommands:

            for command in self.stream:

                self.current = command
                self.stream = self.stream[1:]
                break

    def reset(self):
        '''
        helper method for symbol resolving
        '''
        return self.copy

    def commandType(self):
        '''
        Returns the type of the current command:
        A_COMMAND for @Xxx where Xxx is either a symbol or a decimal number
        C_COMMAND for dest=comp;jump
        L_COMMAND (actually, pseudo-command) for (Xxx) where Xxx is a symbol.
        '''

        self.type = None

        if self.current.startswith('@'):
            self.type = 'A_COMMAND'
        elif self.current.startswith('('):
            self.type = 'L_COMMAND'
        else:
            self.type = 'C_COMMAND'

        return self.type

    def symbol(self):
        '''
        Returns the symbol or decimal Xxx of the current command @Xxx or (Xxx).
        Should be called only when commandType() is A_COMMAND or L_COMMAND .
        '''

        if self.type == 'A_COMMAND':

            return self.current[1:]

        elif self.type == 'L_COMMAND':

            return self.current[1:-1]

    def dest(self):
        '''
        Returns the dest mnemonic in the current C-command (8 possibilities).
        Should be called only when commandType() is C_COMMAND .
        '''

        if re.search(r'=', self.current):

            loc = re.search(r'=', self.current).start()
            return self.current[:loc]

        return 'null'

    def comp(self):
        '''
        Returns the comp mnemonic in the current C-command (28 possibilities).
        Should be called only when commandType() is C_COMMAND .
        '''

        if re.search(r'=', self.current):

            loc = re.search(r'=', self.current).start()
            return self.current[loc + 1:]

        elif re.search(r';', self.current):

            loc = re.search(r';', self.current).start()
            return self.current[:loc]

    def jump(self):
        '''
        Returns the jump mnemonic in the current C-command (8 possibilities).
        Should be called only when commandType() is C_COMMAND .
        '''

        if re.search(r';', self.current):

            loc = re.search(r';', self.current).start()
            return self.current[loc + 1:]

        return 'null'

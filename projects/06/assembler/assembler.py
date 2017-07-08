#!/home/aksbuzz/anaconda3/bin/python3
import argparse
import sys
import re
from parser import Parser
from code import Code
from symbol import SymbolTable
'''
Assembler to parse Hack Machine Language
'''


def check_input_file(file):

    if file[-4:] != '.asm':

        return False

    return True


def argument_parser():

    parser = argparse.ArgumentParser(
        description="Assembler for Hack Machine Files")

    parser.add_argument(
        "file", help="enter the .asm file", type=argparse.FileType('r'))

    args = parser.parse_args()

    if check_input_file(sys.argv[1]) is False:
        sys.exit("File is not a .asm file")

    asm_file = args.file.name
    loc = re.search(r'\.', asm_file).start()
    hack_file = asm_file[:loc] + '.hack'

    return asm_file, hack_file


def build_symbol_table(parser):

    # Initilization
    symbol_table = SymbolTable()

    counter = -1

    # First Pass
    for _ in range(parser.size):
        parser.advance()

        if parser.commandType() == 'L_COMMAND':

            symbol = str(parser.symbol())

            if symbol_table.contains(str(symbol)) is False and counter != 0:
                symbol_table.addEntry(str(symbol), counter + 1)

            elif symbol_table.contains(str(symbol)) is False and counter == 0:
                symbol_table.addEntry(str(symbol), counter)

            else:
                continue

        else:
            counter += 1
            continue

    return symbol_table.table


def main():

    asm_file, hack_file = argument_parser()

    with open(hack_file, 'w+') as outfile, open(asm_file, 'r') as infile:

        parser = Parser(infile)
        code = Code()
        symbol_table = build_symbol_table(parser)

        parser.stream = parser.reset()

        counter = 16

        for _ in range(parser.size):
            parser.advance()

            if parser.commandType() == 'A_COMMAND':

                symbol = parser.symbol()

                if type(symbol) == str:

                    if symbol in symbol_table.keys():

                        symbol = symbol_table[symbol]

                    elif symbol not in symbol_table.keys():

                        symbol_table[symbol] = counter
                        counter += 1

                if type(symbol) == int:
                    outfile.write('0' + '{0:015b}'.format(int(symbol)) + '\n')

            elif parser.commandType() == 'C_COMMAND':

                outfile.write('111' + '{}'.format(code.comp(
                    parser.comp())) + '{}'.format(code.dest(parser.dest())) +
                              '{}'.format(code.jump(parser.jump())) + '\n')


if __name__ == '__main__':
    main()

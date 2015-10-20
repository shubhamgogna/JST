#!/usr/bin/env python3

# This file is part of JST.
#
# JST is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# JST is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with JST.  If not, see <http://www.gnu.org/licenses/>.

import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '../'))

import argparse
from compiler.compiler_state import CompilerState
from parsing.cparser import Parser
from scanning.clexer import Lexer

# """int main(int argc, char** argv) {int i; return 0;}"""
data = """
    int main() {
        int i = 0;

        {
          int f = 5;
        }
    }
    void foo(int x) {}
    int z; !!S
    """


def main():
    arg_parser = argparse.ArgumentParser()
    # arg_parser.add_argument("input", type=str, help="The C program code file to compile.")
    arg_parser.add_argument("-o", "--outfile", type=str, default='',
                            help="The name of the file output file. Defaults to $(TODO).")
    arg_parser.add_argument("-s", "--scandebug", type=int, choices=[0, 1, 2, 3, 4], default=0,
                            help="The debug level for the scanner. \n 0: No debug \n 1: Tokens \n 2: Source Code \n " \
                                 "3: Tokens and Source Code \n 4: Tokens, Source Code, and Symbol Table")
    arg_parser.add_argument("-p", "--parsedebug", type=int, choices=[0, 1, 2, 3], default=0,
                            help="The debug level for the parser. \n 0: No debug \n 1: Productions \n" \
                                 " 2: Productions and Source Code \n 3: Productions, Source, Misc info")
    arg_parser.add_argument("-w", "--warnlevel", type=int, choices=[0, 1], default=0,
                            help="The debug level for the parser.")

    args = arg_parser.parse_args()
    args_dict = vars(args)

    # set scanner flags
    print_tokens = False
    print_source_s = False
    print_table = False

    if args_dict['scandebug'] is 1:
        print_tokens = True
    if args_dict['scandebug'] is 2:
        print_source_s = True
    elif args_dict['scandebug'] is 3:
        print_tokens = True
        print_source_s = True
    elif args_dict['scandebug'] is 4:
        print_tokens = True
        print_source_s = True
        print_table = True

    # set parser flags
    print_productions = False
    print_source_p = False
    print_info = False

    if args_dict['parsedebug'] is 1:
        print_productions = True
    elif args_dict['parsedebug'] is 2:
        print_productions = True
        print_source_p = True
    elif args_dict['parsedebug'] is 3:
        print_productions = True
        print_source_p = True
        print_info = True

    compiler_state = CompilerState()
    
    # Note: Due to debug flags, this looks a bit ridiculous. Can fix this later.
    parser = Parser(compiler_state, Lexer(compiler_state, print_tokens, print_source_s, print_table),
                    print_productions, print_source_p, print_info)
    parser.parse(data)
    parser.teardown()

if __name__ == '__main__':
    main()
